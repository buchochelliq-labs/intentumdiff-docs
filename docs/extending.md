# Extending IntentumDiff

**Language support is a plugin, not a feature of the engine.**

Each of the 78 supported languages is an independent **WebAssembly component**, built against
a published SDK and loaded at runtime. Adding a language does not mean changing the engine,
waiting for an engine release, or persuading anyone to merge a grammar into a core codebase.

That is the whole design. A tool that supports "the languages we got round to" ages badly;
one where a language is a component anybody can build does not.

## What this means in practice

**A new language is a new repository.** It implements the parser interface, builds to
`wasm32-wasip2`, and is loaded like any other. The engine neither knows nor cares which
languages exist.

**Plugins are sandboxed.** WebAssembly components have no ambient access to your filesystem,
network or environment. A parser sees the source it was handed and returns a tree. This is why
third-party plugins can be loaded at all — the isolation is enforced by the runtime, not by
trusting the author.

**Plugins are pinned and checksummed.** The registry records a specific commit and a SHA-256
for every certified component, and provisioning resolves the **pinned** reference. You get the
same bytes we certified, not whatever the parser's default branch happens to be today.

**Analyzers are plugins too.** The same component model extends past parsing: a diff analyzer
is a transform over the final diff, so new classification behaviour can be added without
touching the engine either.

## Building one

The interface is defined as a WIT contract and the SDK generates the bindings:

- **[intentumdiff-plugin-sdk](https://github.com/buchochelliq-labs/intentumdiff-plugin-sdk)** —
  the SDK, the interface, and what a component must implement
- **[intentumdiff-registry](https://github.com/buchochelliq-labs/intentumdiff-registry)** —
  how a component becomes certified and pinned
- Any of the 78 `*-parser` repositories — a complete worked example

Most parsers wrap an existing [tree-sitter](https://tree-sitter.github.io/) grammar, so if a
grammar already exists for your language, the work is mapping its node types onto the
[canonical categories and roles](concepts.md) rather than writing a parser.

## Contributions are welcome

This is an open project and contributions are genuinely wanted — not merely tolerated.

Useful things to work on, roughly in order of how much they help:

- **A language you care about.** Either a parser that does not exist yet, or better category
  and role coverage in one that does
- **Bug reports with a reproduction.** A diff that gets classified wrongly is the most useful
  bug we receive, because it is a test case
- **Documentation.** If something here turned out not to be true, that is a bug worth
  reporting on its own — docs rot is why 0.0.1 had to be pulled
- **Anything in the issue trackers.** Issues are labelled and most carry enough context to
  start without asking

You do not need to ask permission to open a pull request, and you do not need to be confident
it is right. Each repository has a `CONTRIBUTING.md` with the setup steps and the branching
rule — the one thing worth knowing up front is that **pull requests target the release
candidate branch, never `main`**.

If you are unsure where something belongs, open an issue and ask. That is a perfectly good
first contribution.
