# How it works

## The problem with line diffs

A textual diff compares *characters*. It has no idea what a function is, so it cannot tell
you whether a change altered behaviour. Rename a variable across a file and a line diff
reports dozens of changes; move a function and it reports a large deletion and a large
addition that happen to be the same code.

Reviewers do this classification in their heads, on every review, at a cost in attention that
is rarely acknowledged.

## What IntentumDiff does instead

1. **Parse** both sides into a syntax tree, using a real grammar for the language
2. **Match** nodes between the two trees, so a moved function is recognised as the same
   function rather than a delete plus an add
3. **Classify** every surviving difference by what it does to the program

The output is a set of changes carrying a category, not a set of line ranges.

## Categories

| Category | Meaning | Where attention goes |
|---|---|---|
| **Meaningful** | Behaviour changed | This is the review |
| **Refactoring** | Structure changed, behaviour did not | Skim |
| **Moved** | Same code, different place | Confirm the destination |
| **Ignored style** | Formatting, whitespace | Ignore |

The practical effect: a 400-line reformat containing one behavioural change stops being a
wall of red and green and becomes one change worth reading.

## Facts

Alongside categories the engine derives **facts** about each change — structural properties
such as "a guard clause was added", "an early return was introduced", "a resource is now
acquired in a `with` block".

Facts are deliberately **counts, categories and flags**: no identifiers, no literals, no
source text. That is what makes them safe to send to a language model for explanation while
your code stays on your machine. See [Privacy](privacy.md).

## When it cannot parse

If a parser cannot load, or a file is not valid in its language, IntentumDiff degrades to a
token-level comparison rather than failing. You get a usable diff without semantic categories,
and the fallback is recorded in diagnostics rather than hidden.

## Where the work happens

The engine is a Rust core, with language support supplied as sandboxed WebAssembly components.
The Python package, the CLI and the VS Code extension are thin front ends over that one
implementation, so results do not depend on which one you use.
