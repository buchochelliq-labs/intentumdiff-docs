# IntentumDiff

**Semantic code review — see what a change *means*, not which lines moved.**

A textual diff shows you that 40 lines changed. It cannot tell you whether those 40 lines are
a rename, a function moved between files, a reformat, or a subtle change in behaviour hiding
among them. Reviewers spend most of their attention separating those cases by hand.

IntentumDiff parses both sides into a syntax tree, matches the trees against each other, and
classifies every change by what it *does*:

| Category | Meaning |
|---|---|
| **Meaningful** | Behaviour changed — this is what review time is for |
| **Refactoring** | Structure changed, behaviour did not |
| **Moved** | The same code, somewhere else |
| **Ignored style** | Formatting and whitespace |

A 400-line reformat with one behavioural change inside it stops being a wall of red and green,
and becomes one change worth reading.

## Start here

<div class="grid cards" markdown>

- :material-rocket-launch: **[Getting started](getting-started.md)** — one install, then a real diff
- :material-microsoft-visual-studio-code: **[VS Code extension](vscode.md)** — intent in the editor you already use
- :material-language-python: **[Python library and CLI](python.md)** — the API and command surface
- :material-lightbulb: **[How it works](concepts.md)** — why the results differ from a line diff

</div>

## What it supports

**78 languages** ship in the box, each an independent WebAssembly parser — Python, TypeScript, Go, Rust, Java,
C#, C++, SQL dialects, Terraform, and more. See the [full list](languages.md).

Language support is a **plugin, not a feature of the engine** — anyone can add a language
without changing the core, and [contributions are welcome](extending.md).

Beyond source code it also diffs structured data (JSON, YAML, TOML, XML), documentation
(Markdown, AsciiDoc, LaTeX) and images, using a perceptual comparison rather than a byte one.

## Privacy

IntentumDiff runs **entirely on your machine**. Parsing, matching and classification are local,
and nothing is sent anywhere by default.

The optional LLM explainer is bring-your-own-key and opt-in. When enabled it sends a
**privacy-safe fact sheet** — counts, categories and flags — never your source code,
identifiers or literals. See [Privacy](privacy.md) for exactly what leaves your machine.

!!! note "Status"

    IntentumDiff is early software and currently ships as a prerelease. Please
    [report anything that does not behave as documented](https://github.com/buchochelliq-labs/intentumdiff-python/issues)
    — including the docs themselves.
