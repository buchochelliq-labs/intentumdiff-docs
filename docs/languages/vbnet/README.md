# VB.NET

[All languages](../gallery.md)

These real terminal captures use a historical development build. They are not current release certification; independent output review and current installed-wheel scenario checks remain pending.

## Overview

This worked example compares `Code.vb`. Advertised filename extensions: `.vb`.

## What changes

Rewrite greeting using string interpolation and append exclamation mark; add integer Multiply function; leave Add unchanged.

## Before

````text
Module HelloWorld
    Sub Greet(name As String)
        Console.WriteLine("Hello, " & name)
    End Sub

    Function Add(a As Integer, b As Integer) As Integer
        Return a + b
    End Function
End Module
````

## After

````text
Module HelloWorld
    Sub Greet(name As String)
        Console.WriteLine($"Hello, {name}!")
    End Sub

    Function Add(a As Integer, b As Integer) As Integer
        Return a + b
    End Function

    Function Multiply(a As Integer, b As Integer) As Integer
        Return a * b
    End Function
End Module
````

## Things to know

- String interpolation requires a supporting VB language version.

## Recorded output

![Actual VB.NET terminal capture](meaningful-change.svg)

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
intentumdiff file before/Code.vb after/Code.vb
```

The installed Python wheel includes its parser components. The native CLI requires a component directory. Compare the result with the source change described above; agreement between APIs alone is not proof of correctness.
