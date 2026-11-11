# AutoPulse engineering backlog

Prepared November 11, 2026. The executable issue definitions are in [issues.json](issues.json).

The active implementation has separate UI and engine branches. Before editing, resolve the current source revision and writer ownership. Do not assume a directory exists on the default branch because it exists in an integration branch.

| Key | Work | Execution boundary |
| --- | --- | --- |
| AP-V1-SESSION | Connect Check-up and Drive to the selected standard-OBD engine | Integrate through the current writer; preserve saving and Stop |
| AP-V1-CLONE | Verify reset and protocol initialization on inexpensive adapters | Recorded failing and healthy inputs before a change |
| AP-V1-BLE | Verify fragmented BLE receive handling | Use received notifications; preserve order and reconnect ownership |
| AP-V1-PENDING | Verify ResponsePending handling | Recorded NRC 0x78 sequences and late completion/Stop negatives |
| AP-V1-COVERAGE | Measure standard sensor coverage and session endurance | Release/adapter-specific evidence; no fixed sensor guarantee |
| AP-EN-RELEASE | Complete English/Russian localization | Entire user journey and errors, not just platform dialogs |
| AP-ANDROID-RELEASE | Produce signed AAB and APK | Original upload key, clean frozen source, existing release gate |
| AP-OEM-AFTER-V1 | Audit existing OEM mobile integration | Deferred until standard-OBD V1 acceptance |

`devin-ready` means the investigation and acceptance contract are scoped. It does not authorize concurrent writes into an occupied checkout, claim a reproduced defect, or waive release approval. The deferred OEM issue receives `post-v1`, not `devin-ready`.

Excluded from this release slice: DTC clearing, new polling heuristics, unsupported fault-prediction claims, and guaranteed refresh rates or vehicle coverage. Further development follows measured evidence and the product owner's scope decisions.
