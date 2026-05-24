# Portfolio Engineering Standards Repository

This repository acts as the Single Source of Truth (SSOT) for architecture patterns, metadata schemas, validation engines, and context-engineering configurations across our repository portfolio.

## 🎯 Primary Objectives
1. **Reduce AI Token Consumption**: Consolidate repetitive descriptions into lightweight, context-sparse YAML configurations and markdown briefs.
2. **Eradicate Architectural Drift**: Maintain deterministic implementation models for logging, telemetry, security, and repository layouts.
3. **Establish Recruiter-Grade Aesthetics**: Keep repository presentation visually premium, responsive, and organized.

---

## 📂 Repository Directory Map

* **`/governance`**: Central validation schemas and global manifesto policies.
  * [governance-schema.json](governance/schemas/governance-schema.json): Schema contract mapping.
  * [governance.yml Base](governance/templates/governance.yml): The sparse metadata blueprint.
* **`/templates`**: Standardized project templates.
  * [README-template.md](templates/README-template.md): High-aesthetic, context-sparse README layout.
* **`/prompts`**: System instruction assets and custom `.cursorrules` rules.
* **`/validation`**: Automated verification engines.
  * [validate-repo.py](validation/bin/validate-repo.py): Compliancy validator CLI tool.

---

## ⚡ Quick Start: Standardizing a Target Repository

To align an existing repository to the portfolio operating model:

1. **Add the Metadata Anchor**: Copy `/governance/templates/governance.yml` into your project's root and customize its fields.
2. **Compress the README**: Replace your existing layout with the `/templates/README-template.md` structure, hiding technical details under `<details>` blocks to keep token cost low for agent reads.
3. **Activate Editor Controls**: Place `/prompts/.cursorrules` in your project's root to ensure coding assistants follow standard parameters.
4. **Validate Local Compliance**:
   ```bash
   python validation/bin/validate-repo.py --target /path/to/your/repo
   ```

---

## ⚖️ Governance & Licensing
All standard models and schema engines in this repository are licensed under the **MIT License**. For security alerts or policy adjustments, contact Portfolio Engineering.
