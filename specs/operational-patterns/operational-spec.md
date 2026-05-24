# Operational Patterns & Workflows Standard

This specification governs branching conventions, project naming, and evaluation scoring models, keeping our portfolio repositories operationally unified and portable.

---

## 🌿 1. Git Branching & Workflow Model

We maintain a streamlined, lightweight branch model optimized for single-developer speed and automated CI validation checks:

* **`main`**: The stable branch representing production-grade code. Direct push is blocked if RML is `governed` or higher.
* **`develop`**: The integration branch for staging feature additions.
* **Feature Branches (`feature/<short-name>`)**: Isolated branches created off `develop` to build specific milestones.

### Pull Request & Integration Flow
1. Developer creates a branch off `develop`.
2. Developer commits changes and runs local schema validations:
   ```bash
   python validation/bin/validate-repo.py --target ./
   ```
3. Developer opens a Pull Request targeting `develop`.
4. GitHub Actions runs the centralized validator pipeline. 
5. Upon successful validation, the PR is merged.

---

## 🏷️ 2. Naming Conventions

Consistent nomenclature prevents confusion for automated tooling and AI agents scanning workspaces.

* **Repository Names**: lowercase, dash-separated (e.g., `ops-command-vault`, `opsmate-ai`).
* **Source Directories**:
  * Python: `src/` (root package) containing standard module components.
  * Node/TypeScript: `src/` (root module) or standard ESM files.
* **Config Files**: camelCase or snake_case matching schema boundaries.

---

## 📊 3. Operational Scorecard Matrix

To track portfolio maturity, we use a simple scoring matrix based on capability declarations:

| Metric | Score: 1 (Experimental) | Score: 2 (Governed) | Score: 3 (Observable) | Score: 4 (Portfolio-Grade) |
| :--- | :--- | :--- | :--- | :--- |
| **Telemetry** | Unstructured print loops | Structured JSON logs | Prometheus metrics | Full OTel tracing + local dashboards |
| **Governance** | No license or standard config | Standard license + `.cursorrules` | `governance.yml` matches schema | Continuous CI compliance checks |
| **Documentation** | Single paragraph | README + start scripts | Full nested `<details>` layout | Architecture narratives with themes |
| **Validation** | Manual testing only | Local pre-commit scripts | Automated schema validations | Centralized drift-prevention pipelines |
