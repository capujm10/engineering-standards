# SpecDD: Repository Contract Specification

This specification governs the core codebase contract boundaries. It connects capability declarations directly to automated validation engines, ensuring all portfolio repositories remain unified.

---

## 🌿 1. Codebase Metadata Anchor
All projects must maintain a root-level `governance.yml` mapping out the following required blocks:
* **repository**: Identifies name, description, owner, and developer contact.
* **compliance**: Standardizes licensing constraints and dependency scan toggles.
* **architecture**: Dictates target runtime, framework layout, and database connectors.
* **observability**: Standardizes metrics endpoints and structured log collectors.

---

## 📦 2. Standard Taxonomy
Repositories must organize directories in accordance with standard taxonomy expectations:
* **`src/`**: Primary package implementation (never mix test files here).
* **`tests/`**: Unit, integration, and regression validations.
* **`docs/`**: Markdown system architecture constraints and telemetry briefs.
* **`validation/`**: Local pre-commit files or configuration scripts.

---

## 🛡️ 3. Branching & PR Controls
* **Branch Isolation**: Direct push to the `main` branch is prohibited.
* **Validation Check**: Every pull request targeting staging or master branches must run the automated cli validator:
  ```bash
  python validation/bin/validate-repo.py --target ./ --audit --observability
  ```
* **Drift Block**: Merge triggers will automatically fail and block execution if directory taxonomy conflicts with schema parameters.
