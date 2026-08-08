# Roadmap

What we are working on, and where each theme is tracked. Every item links to a live issue, so
status is never stale prose — if you want to know how far along something is, follow the link.

!!! note "How to read this"

    This is direction, not a schedule. Nothing here carries a date, and items move when they
    are ready. If something matters to you, say so on its issue — that is genuinely how
    priority gets decided.

## Language coverage

78 languages ship today, each an independent WebAssembly parser. Work continues in two
directions: **breadth** (languages with no parser yet) and **depth** (better category and role
coverage in the ones that exist — a coarse mapping still produces a diff, just a blunt one).

Because a parser is a plugin, neither needs a change to the engine. This is the easiest place
to contribute.

→ [Language coverage](https://github.com/buchochelliq-labs/intentumdiff-core/issues/8)
· [Extending guide](extending.md)

## A canonical AST

The vocabulary underneath intent classification: a small set of **categories** with orthogonal
**roles**, rather than an ever-growing list of node kinds. Roles are what let a guard clause
read as a guard clause instead of "a conditional containing a return".

This is the substrate for better intent facts, and it is where most current effort goes.

→ [Vocabulary](https://github.com/buchochelliq-labs/intentumdiff-ast/issues/1)
· [Roles](https://github.com/buchochelliq-labs/intentumdiff-ast/issues/2)
· [Query layer](https://github.com/buchochelliq-labs/intentumdiff-ast/issues/7)
· [Mappings as data](https://github.com/buchochelliq-labs/intentumdiff-ast/issues/8)
· [Engine integration](https://github.com/buchochelliq-labs/intentumdiff-ast/issues/9)

## More languages to call it from

All diffing, matching and classification live in the Rust core behind a stable C ABI. A
binding is a thin shell over that ABI doing **zero functional work**, so results cannot drift
between them. Python exists; Go and Java are next.

→ [Go binding](https://github.com/buchochelliq-labs/intentumdiff-go/issues/3)
· [Java binding](https://github.com/buchochelliq-labs/intentumdiff-java/issues/3)

## More editors

Semantic review should not be VS Code-only. A language server exposes intent to any
LSP-capable editor — Neovim, Helix, Emacs, JetBrains — without a bespoke extension for each.

→ [Editor support via LSP](https://github.com/buchochelliq-labs/intentumdiff-lsp/issues/4)

## An extension that needs nothing else

Today the VS Code extension requires the engine installed separately. Bundling the native
engine per platform makes the extension self-contained: install it, open a diff, done.

→ [Platform-specific VSIXs](https://github.com/buchochelliq-labs/intentumdiff-vscode/issues/21)

## Diffing without a repository

Comparing two loose files — a downloaded config against your own, a file before and after a
tool ran — is the case handled worst today: the editor integration expects a git-backed
workspace, so the engine is right there with no good way to drive it.

Three surfaces answer it: a local client that assumes no repository, an **online diff** you can
paste two files into, and a **playground in these docs** so you can try a real diff on the page
that explains it, without installing anything.

The online surfaces run **entirely in your browser**. The engine compiles to WebAssembly, so
nothing is uploaded and no server ever sees your code — the same guarantee as the local tool,
not a weaker one.

→ [Diffing without a repo](https://github.com/buchochelliq-labs/intentumdiff-core/issues/15)

## Semantic review in the terminal

Reviewing a diff in a terminal today means reading a scrolling dump — but semantic review is
inherently navigational: files, then change groups, then changes, then the intent behind them.
A flat printout is the one shape that cannot express that.

An interactive terminal UI built with [Ratatui](https://ratatui.rs/) would bring the structure
the editor already has to anyone working over SSH, in a container, or simply in the terminal —
fold a 400-line reformat to one line, jump to the next *meaningful* change, and read the
evidence behind a classification.

It lives in the Rust core rather than any one language's CLI, so every binding gets the same
one.

→ [Terminal review UI](https://github.com/buchochelliq-labs/intentumdiff-core/issues/10)
· [Navigable view](https://github.com/buchochelliq-labs/intentumdiff-core/issues/11)
· [Intent and evidence](https://github.com/buchochelliq-labs/intentumdiff-core/issues/12)
· [Guardrails view](https://github.com/buchochelliq-labs/intentumdiff-core/issues/13)

## Trustworthy releases

Less glamorous than the rest and more important than all of it. 0.0.1 shipped broken and was
pulled from three registries within a day, with every check green — because the checks proved
the code compiled, not that the artefact worked.

So: wheels tested on every platform we publish for, documented examples executed in CI against
a real installed wheel, and every link verified.

→ [Test every platform we publish for](https://github.com/buchochelliq-labs/intentumdiff-python/issues/9)
· [Vanilla-profile extension smoke test](https://github.com/buchochelliq-labs/intentumdiff-vscode/issues/19)
