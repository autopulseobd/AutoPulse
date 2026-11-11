# Public engineering brief — AutoPulse

This repository publishes the AutoPulse overview and engineering backlog. Application implementation remains in the private owning repository, with its current contracts and release gates. Current coordination is in [PLANS.md](PLANS.md).

Before a commit, run `git diff --check`, `bash -n create_github_issues.sh`, Python syntax validation, and `python3 create_github_issues.py --repo autopulseobd/AutoPulse` (dry run). Enable the supplied gate once per clone with `git config core.hooksPath tool/hooks`.

- Keep product claims consistent with the released artifact and recorded evidence. Do not claim universal adapter support or infer hardware acceptance from replay checks.
- Work on one scoped issue with an exact source revision, one writer per checkout, and a named verification oracle.
- Preserve session state identity, command ordering, timing, callbacks, recovery, and shutdown semantics. An unfamiliar branch requires investigation before replacement.
- For a fix, preserve a failing example and a healthy neighbouring example. Do not alter expected results to make an implementation pass.
- Verify the actual mobile entry point. A component test or successful build does not establish that the UI invokes the new path.
- Keep credentials, account tokens, raw vehicle logs, and private audit records out of public exports. Preserve required attribution, licenses, and provenance.
- Create no release, deployment, paid model run, or external message without task authority.
- Do not modify application code from this overview package. Consult the owning repository and current work allocation first.
