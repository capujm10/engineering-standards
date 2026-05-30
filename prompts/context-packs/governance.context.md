# Codebase Governance & Compliance Context Pack

This context pack governs operational alignment, directory structures, branch rules, and compliance standards.

---

## 🛠️ Stack Summary & Architecture Patterns
* **Target Runtime**: Python 3.10+ (for validation cli engine).
* **Metadata Schema**: YAML parser verifying against JSON Schema Draft-07 contracts.
* **Checks Gate**: Deterministic local pre-commit hooks and Github Actions CI builders.

---

## ⚙️ Repository Expectations & Constraints
* **Root Anchors**: Must contain `governance.yml` (declaring capabilities) and standard `LICENSE` file.
* **Branch Policy**: Direct pushing to `main` branch is blocked for governed-level repositories. All changes must pass verification pipelines inside pull requests targeting `develop`.
* **Zero Overhead**: Never implement heavy DB checks or complex web setups inside verification workflows.

---

## 📊 Telemetry Conventions
* **Logs Format**: Auditor runs output results using standard terminal formats (success `[+]` or error `[-]`).
* **Compliance Grade**: Declared RML levels govern validation strictness (Experimental -> Portfolio-Grade).

---

## ⚖️ Governance Rules & Validations
* **Validation Command**: Run full compliance audit:
  ```bash
  python validation/bin/validate-repo.py --target ./ --schema governance/schemas/governance-schema.json --audit
  ```
* **No Drift Rules**: The validator blocks branch merges if properties are added to code structures without matching declarations in `governance.yml`.
