# Copilot / AI Agent Instructions for this repository  

Purpose
- Help AI agents be immediately productive in this repo: small notebook-based Spark/Delta examples under `Fabric_Test/`.

Big picture (what matters)
- This repo contains interactive PySpark/Delta notebooks (not a packaged app). Key files:
  - `blank_notebook.ipynb` — small Python example (filtering helper). Use for simple refactors & examples.
  - `Delta_Merge_Optimization.ipynb` — Delta Lake merge performance example using `delta.tables.DeltaTable` and partition-aware merge conditions.
- Typical workflow is exploratory: run in a Spark/Databricks environment or local PySpark with Delta support.

What to look for / preserve
- Do not commit large data or absolute local paths (the notebook uses placeholders like `/random/source/`). Replace with parameterized paths or test-only temp dirs.
- Partitioning convention: the notebooks use a `par` column and rely on `par`-based filtering to limit the merge scope. Preserve that pattern when changing merge logic.
- Merge condition pattern: notebooks build a `conditions_list` and join with `AND` to form the `condition` used in `DeltaTable.merge(...)`. Keep this compositional style.

Environment & how to run (discoverable from code)
- The code relies on PySpark + Delta packages. Minimal local setup examples:
  - pip: `pip install pyspark delta-spark`
  - Or run with spark submit including delta packages: `PYSPARK_SUBMIT_ARGS="--packages io.delta:delta-core_2.12:<version>,io.delta:delta-spark:<version> pyspark-shell"`
- Prefer running notebooks in Databricks or a configured local Spark session to get `display()`, `spark.*` and Delta behaviour.

Agent behavior & suggested prompts (concrete examples)
- Refactor example: "Extract the merge sequence in `Delta_Merge_Optimization.ipynb` into a testable function `apply_merge(delta_path, updates_df, partition_col)` that accepts a Spark DataFrame and returns the number of rows merged. Keep the `par`-filter optimization as optional parameter."  
- Fix example: "Replace hard-coded path `/random/source/` with a configurable variable and add a short example that writes to a temp dir using `tempfile.TemporaryDirectory()` for local tests."  
- Small improvement: "In `blank_notebook.ipynb`, move `filter_even_numbers` into a small module `fabric_test/utils.py` and add a tiny unit test that imports and asserts behaviour."

Testing & PR checklist
- Validate by running the modified notebook(s) in a Spark session (or unit tests for extracted functions).  
- Ensure no large binary outputs or datasets are committed. Notebooks should not contain secret keys.  
- Update README or add `requirements.txt` / `environment.yml` if you introduce new dependencies.

Files to inspect for patterns
- `Delta_Merge_Optimization.ipynb` — Delta merge patterns, partition-aware filtering, `DeltaTable.isDeltaTable` usage.  
- `blank_notebook.ipynb` — small Python example for refactoring into modules/tests.

If unclear or missing info
- Ask: Which Spark/Delta versions should be targeted? Do you prefer Databricks notebooks or runnable PySpark scripts for CI?  

Keep instructions concise; prefer small, testable changes that don't require large data or environment setup.  
