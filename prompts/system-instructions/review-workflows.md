# AI Code & Architecture Review Workflows

This document establishes the standardized review prompts and QA checklists for AI coding assistants. These prompts are highly token-compressed, enabling deep architectural checks without expanding the model's context window.

---

## 🔍 1. Repository Schema Alignment Check
* **Goal**: Validate that all proposed directories, framework structures, and dependency changes align with the repository metadata contract.
* **Review Prompt**:
  ```markdown
  System Directive: Check the proposed code change against the repository's root `governance.yml` contract. 
  1. Does this introduction add new database paths, framework modules, or core APIs not declared in `architecture:` or `capabilities:`?
  2. If yes, reject the change and instruct the user to update `governance.yml` first.
  3. Ensure no hardcoded credentials or local paths are introduced.
  ```

---

## 📊 2. Observability & Telemetry Compliance Review
* **Goal**: Guarantee that trace spans, metric configurations, and structured log events comply with standard OTel patterns.
* **Review Prompt**:
  ```markdown
  System Directive: Analyze the code changes for telemetric logic.
  1. Are logs formatted in structured, single-line JSON with consistent tags (`timestamp`, `level`, `service`, `message`)?
  2. Are OpenTelemetry metrics named using `snake_case` and prefixed with the service name?
  3. Are traces propagating context through downstream functions?
  4. Ensure no custom, non-standard logger class is created. Use the standard package wrapper.
  ```

---

## ⚖️ 3. README & Documentation Audit
* **Goal**: Maintain recruiter-grade repository aesthetics while keeping context sizes minimal.
* **Review Prompt**:
  ```markdown
  System Directive: Review the project's README.md file.
  1. Is the visual hierarchy clean (# h1, ## h2, ### h3)?
  2. Are complex architectural directories or telemetry logs encapsulated under `<details>` tags to save token space?
  3. Are the standard dynamic shield badges configured (Standards RML level, License)?
  4. Keep narrative descriptions under 400 words. Focus on operational metrics and quick start steps.
  ```
