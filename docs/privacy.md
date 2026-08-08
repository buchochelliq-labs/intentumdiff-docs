# Privacy

**IntentumDiff runs entirely on your machine.** Parsing, matching and classification are local.
By default nothing leaves your computer, and there is no telemetry.

## The optional LLM explainer

IntentumDiff can ask a language model to explain a change in prose. It is **off by default**,
**opt-in**, and **bring-your-own-key**.

- We never bundle an API key and never run a paid proxy on your behalf
- Your key is stored in VS Code SecretStorage, never in `settings.json`
- A consent prompt precedes any send to a cloud endpoint

## What is actually sent

To a **cloud** endpoint, IntentumDiff sends a **privacy-safe fact sheet**: counts, categories
and boolean flags derived locally from the syntax tree.

| Sent | Never sent |
|---|---|
| Change categories | Your source code |
| Structural facts, e.g. "a guard clause was added" | Identifiers — names of functions, variables, files |
| Counts, e.g. "3 conditionals added" | Literals — strings, numbers, secrets |

The fact sheet is designed so that the original source cannot be reconstructed from it.

To a **local** endpoint — a model running on your own machine — verbatim source may be sent,
because it does not leave the machine.

## Token carriage

Where a fact could carry a source token, carriage is governed by an explicit policy that
**defaults to none and fails closed**. You choose, per category, how much the model may see —
from nothing at all up to full tokens. If the policy cannot be determined, nothing is carried.

## Tests do no network

The test suites perform **no** network calls, so running them cannot send your code anywhere.

## Reporting a concern

If you believe IntentumDiff sends something this page does not describe, please treat it as a
security issue and report it privately through the repository's security policy rather than a
public issue.
