# Kotlin

[All languages](../gallery.md)

These real terminal captures use a historical development build. They are not current release certification; independent output review and current installed-wheel scenario checks remain pending.

## Overview

This worked example compares `Code.kt`. Advertised filename extensions: `.kt`.

## What changes

Append ! via interpolation in greet; rename add parameters and use expression body; add multiply.

## Before

````text
fun greet(name: String) {
    println("Hello, " + name)
}

fun add(a: Int, b: Int): Int {
    return a + b
}
````

## After

````text
fun greet(name: String) {
    println("Hello, $name!")
}

fun add(x: Int, y: Int): Int = x + y

fun multiply(x: Int, y: Int): Int = x * y
````

## Things to know

- Renaming public parameters a/b to x/y can break named-argument call sites; this is not unconditionally a safe rename.

## Recorded output

![Actual Kotlin terminal capture](meaningful-change.svg)

Recorded from a real native CLI through rs-rich-record. A refactoring label does not prove equivalent behavior. [Build identities](../provenance.md).

## Scenario coverage

| Scenario | Status |
|---|---|
| Meaningful edit | Source example reviewed; output captured; independent result certification pending |
| Unchanged content | Not yet certified for this candidate |
| Populate / clear a file | Not yet certified for this candidate |
| Add / delete an entity | Not yet certified for this candidate |
| Rename a symbol | Not yet certified for this candidate |
| Move / reorder code | Not yet certified for this candidate |
| Formatting only | Not yet certified for this candidate |
| Git file rename / move | Not yet certified for this candidate |
| Mixed move and edit | Not yet certified for this candidate |
| Invalid syntax / actionable error | Not yet certified for this candidate |
| Guardrail review | Not yet certified for this candidate |

## Try it

Save the two source blocks as separate files with the shown extension, then compare them:

```bash
intentumdiff file before/Code.kt after/Code.kt
```

The installed Python wheel includes its parser components. The native CLI requires a component directory. Compare the result with the source change described above; agreement between APIs alone is not proof of correctness.
