# VS Code capture evidence

These are real pre-publication captures from the clean-profile desktop acceptance run on
6 October 2026. They are retained in this documentation repository so viewing the guide does
not depend on a temporary CI artifact. They do not certify every language or capability.

## Candidate identity

| Component | Identity |
|---|---|
| Extension | `0.0.2-beta.1` |
| VS Code | `1.138.0` |
| Extension tested merge checkout | `810ad3da3dd6a64d826b9928a0086dff2628689a` |
| VSIX SHA-256 | `c6b66567bd7572fff9db7be10ef30ea9881f62d94d528b52c92e47bc0e272100` |
| Python tested merge checkout | `906502a5138166e640fbf2ef0668ecc955edcfa7` |
| Core commit | `cb497d91422d0ac15d50f2438653103b296e9584` |
| Wheel SHA-256 | `391e30bfb8a7e4a6e71c6f62af085461b6432c5789f97984b4a44c718a33586c` |
| Wheel artifact | `11394029774` |
| Capture artifact | `11396346196` |

[Desktop acceptance run](https://github.com/buchochelliq-labs/intentumdiff-vscode/actions/runs/37428332661)
passed with the corrected Python #95 wheel. The installed VSIX bytes were loaded by the
VS Code test host using an external real CLI. Capture checksums were verified against the
run’s manifest before visual inspection.

This runtime predates the shared rs-rich presentation changes in core #157 and Python #96.
It is evidence for this candidate, not a claim to have retested those later artifacts.

## Coverage

| Capability | Current visual evidence | Remaining evidence |
|---|---|---|
| Python behavioural edit | CodeLens, native diff, recovered review | More edit scenarios |
| Python and JavaScript incomplete edits | Explicit source fallback, parse-error count, f → g source change | More languages |
| Review toolbar | Controls visible at normal width | Stage/revert, navigation and Intent/Evidence tab interactions |
| Image review | Dark, light and high-contrast comparison | Each comparison mode in action |
| Narrow layout | Summary wraps without horizontal clipping | Lower image controls, hotspots and tooltip/accessibility interactions |
| Loading and recovery | Completed fallback and recovered result | Visible loading → ready transition |
| Peek and semantic-only diff | Dedicated current capture pending | Capture each capability |
| Intent, evidence, release notes, guardrails | Dedicated current captures pending | Capture each view with a meaningful scenario |
| Filters, grouping and dashboard | Dedicated current captures pending | Demonstrate each control |
| Diagnostics, empty/error states and runtime recovery | Dedicated current captures pending | Capture actionable failures and recovery |
| Language gallery | Python and JavaScript incomplete edits | Remaining languages and addition/deletion/refactor/move scenarios |
| Desktop video | [16-second CodeLens → native diff → review workflow](vscode/workflow/index.md); representative frames inspected | Broader capability and language recordings |
| Published extension | Not yet verified | Repeat acceptance after publication |

Screenshots alone do not establish keyboard accessibility or contrast compliance.
The existing CLI language illustrations are separate evidence and must not be counted as
VS Code captures.
