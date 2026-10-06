# Databricks

[All languages](../gallery.md)

Current installed-wheel output and media for this corrected notebook example remain pending.

## Overview

This worked example compares `notebook.py`. Advertised filename extensions: `.py`, `.sql`.

## What changes

Add a projection selecting `id` and `name` from active customers. Preserve the `customers` table and active-row filter. The output should report a meaningful code edit, not a formatting-only change.

These are notebook source inputs for comparison, not standalone scripts; executing them requires a Databricks Spark session.

## Before

```text
# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------
active = spark.table("customers").filter(F.col("active") == True)
```

## After

```text
# Databricks notebook source
from pyspark.sql import functions as F

# COMMAND ----------
active = spark.table("customers").filter(F.col("active") == True).select("id", "name")
```

## Things to know

- `notebook.py` currently routes through the Python parser. The Databricks header and cell separator are comments; this example does not certify notebook-cell semantics.
- Workflow configuration has its own [Databricks workflow example](../databricks-workflow/README.md).
- The earlier example incorrectly placed workflow YAML in `notebook.py`. Its historical capture has been withdrawn from this page because it does not depict the corrected source.

## Recorded output

A new installed-wheel capture of the corrected example is pending. No current release certification is claimed.

## Scenario coverage

| Scenario | Status |
|---|---|
| Meaningful edit | Corrected source example reviewed; installed-wheel output and capture pending |
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
intentumdiff file before/notebook.py after/notebook.py
```

The installed Python wheel includes its parser components. The native CLI requires a component directory. Compare the result with the source change described above; agreement between APIs alone is not proof of correctness.
