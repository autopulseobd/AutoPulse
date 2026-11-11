# AutoPulse

AutoPulse is a Flutter application that helps drivers review vehicle diagnostic information and AI-assisted explanations using a compatible OBD2 adapter.

[iOS App Store](https://apps.apple.com/us/app/id6759092401) · [Website](https://autopulseobd.com)

## Release status

The iOS product is available on the App Store. The English release and Google Play launch are in preparation. Vehicle and adapter support varies; broader coverage is a development objective.

Engineering priorities are standard OBD2 connection and recovery, sensor polling, VIN and classic trouble-code reads, deterministic session shutdown, and report persistence. Manufacturer-specific diagnostics follow the first standard-OBD release.

We validate changes with automated checks and recorded communication. Host-side replay results are distinct from mobile integration and device acceptance. A sensor count or a compatibility claim requires evidence from the specific release, vehicle, and adapter.

## Repository access

The implementation repository is private. This public repository contains the product overview, engineering brief and issue-authoring materials; it does not expose the application implementation or grant a source-code license.

## Engineering tasks

See [DEVIN_BACKLOG.md](DEVIN_BACKLOG.md). Issue creation requires an explicit repository and defaults to a dry run:

```sh
bash create_github_issues.sh --repo autopulseobd/AutoPulse
bash create_github_issues.sh --repo autopulseobd/AutoPulse --apply
```

Run these commands from the root of the public repository. The second command creates missing issues and labels; repeating it preserves existing issues. Current coordination is recorded in [PLANS.md](PLANS.md).
