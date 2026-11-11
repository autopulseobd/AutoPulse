"""Create the reviewed issue manifest once per repository; dry run by default."""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys


def gh(*args):
    result = subprocess.run(
        ["gh", *args], check=True, text=True, capture_output=True
    )
    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="Explicit owner/repository")
    parser.add_argument("--apply", action="store_true", help="Create missing issues")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repo):
        parser.error("--repo must be owner/repository")
    issues = json.loads(Path(__file__).with_name("issues.json").read_text())
    keys = [item["key"] for item in issues]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate issue keys")
    for item in issues:
        if not re.fullmatch(r"AP-[A-Z0-9-]+", item["key"]):
            raise ValueError("Invalid issue key")
        if not item["title"] or not item["body"] or not item["labels"]:
            raise ValueError("Incomplete issue")
    if not args.apply:
        for item in issues:
            print(f"DRY RUN {args.repo}: {item['key']} {item['title']}")
        print("No GitHub requests made. Add --apply to create missing issues.")
        return

    # Use the repository from every command, never the caller's current checkout.
    repo = json.loads(gh("repo", "view", args.repo, "--json", "nameWithOwner,isPrivate"))
    if repo["nameWithOwner"].lower() != args.repo.lower():
        raise ValueError("Repository identity mismatch")
    print(f"Target: {repo['nameWithOwner']} (private={repo['isPrivate']})", flush=True)
    # Paginate REST directly; search indexing delay must not create duplicates on resume.
    existing = json.loads(gh(
        "api", "--paginate", "--slurp",
        f"repos/{args.repo}/issues?state=all&per_page=100",
    ))
    existing = [issue for page in existing for issue in page if "pull_request" not in issue]
    label_pages = json.loads(gh(
        "api", "--paginate", "--slurp", f"repos/{args.repo}/labels?per_page=100"
    ))
    labels = {label["name"] for page in label_pages for label in page}
    definitions = {
        "devin-ready": ("0E8A16", "Scoped investigation with acceptance criteria; respect writer ownership"),
        "post-v1": ("BFD4F2", "Deferred until standard-OBD V1 acceptance"),
    }
    for name in sorted({label for item in issues for label in item["labels"]}):
        if name not in labels:
            color, description = definitions[name]
            gh("label", "create", name, "--repo", args.repo,
               "--color", color, "--description", description)
            labels.add(name)
    for item in issues:
        marker = f"<!-- autopulse-grant:{item['key']} -->"
        matches = [issue for issue in existing
                   if marker in (issue.get("body") or "") or issue["title"] == item["title"]]
        if matches:
            print(f"EXISTS {item['key']}: {matches[0]['html_url']}", flush=True)
            continue
        body = marker + "\n\n" + item["body"]
        command = ["gh", "issue", "create", "--repo", args.repo,
                   "--title", item["title"], "--body-file", "-"]
        for label in item["labels"]:
            command.extend(["--label", label])
        result = subprocess.run(command, input=body, text=True, check=True,
                                capture_output=True)
        url = result.stdout.strip()
        existing.append({"title": item["title"], "body": body, "html_url": url})
        print(f"CREATED {item['key']}: {url}", flush=True)


if __name__ == "__main__":
    try:
        main()
    except (subprocess.CalledProcessError, ValueError, KeyError) as error:
        print(f"Stopped: {error}", file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError):
            print(error.stderr or "", file=sys.stderr)
        sys.exit(1)
