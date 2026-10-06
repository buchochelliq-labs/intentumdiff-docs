# SQL

[All languages](../gallery.md)

These real terminal captures use a historical development build. They are not current release certification; independent output review and current installed-wheel scenario checks remain pending.

## Overview

This worked example compares `code.sql`. Advertised filename extensions: `.sql`, `.ddl`, `.dml`.

## What changes

Alias users as u; LEFT JOIN orders by user_id; add order total projection; qualify existing columns/filter; order results by user name.

## Before

````text
SELECT id, name, email
FROM users
WHERE active = 1;
````

## After

````text
SELECT
    u.id,
    u.name,
    u.email,
    o.total AS order_total
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE u.active = 1
ORDER BY u.name;
````

## Things to know

- A user can now produce multiple result rows when multiple orders match; unmatched users remain with null order_total.

## Recorded output

![Actual SQL terminal capture](meaningful-change.svg)

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
intentumdiff file before/code.sql after/code.sql
```

The installed Python wheel includes its parser components. The native CLI requires a component directory. Compare the result with the source change described above; agreement between APIs alone is not proof of correctness.
