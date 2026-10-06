# Languages

Choose a language or format to see its source examples, recorded output and known limitations.

[Browse language overviews and worked examples](languages/gallery.md)

## What is included

The 0.0.2 candidate catalogue has 74 language/format example entries, including aliases and generic text. This is not a count of independent parsers: components can serve multiple language names, and renderer/index components are not parsers.

First-party parser components are provisioned into the Python wheel. The native CLI needs its parser component directory. Rust owns parser selection and semantic comparison; Python supplies the public API and transport.

## Support boundaries

- PowerShell is explicitly unavailable on Windows ARM64. Other platform results do not remove this limitation.
- FreeBASIC is excluded from the enabled catalogue.
- Generic text comparison reports textual changes without promising language-specific semantics. Its cold native startup is currently slow; see [core #155](https://github.com/buchochelliq-labs/intentumdiff-core/issues/155).
- Unsupported source-only InterpretCst execution is rejected in 0.0.2. It does not silently return an empty successful review.
- Required Rust failures propagate. A successful empty diff means no reported changes, not that an engine failure was hidden.

## Reading the evidence

The worked examples are a **development draft**, not release certification. Each language page includes before/after source, source-review caveats, a real rs-rich-record terminal capture and a scenario coverage table. Missing scenarios and pending independent output review are explicit.

Captures are historical and have recorded build identities. These captures predate later fixes; they are not claims about the current candidate. Screenshots and Rust/Python parity alone do not establish correctness.

The intended scenario set includes meaningful edits, unchanged input, file population/clearing, entity addition/deletion, renames, code moves/reordering, formatting, Git file moves, mixed edits, invalid syntax and guardrails. Each is marked verified or pending rather than inferred from another language.

## Adding a language

Parsers are independent WebAssembly components built against the [plugin SDK](https://github.com/buchochelliq-labs/intentumdiff-plugin-sdk). Support depends on the execution contract and host capability; a new component is not automatically certified on every platform.
