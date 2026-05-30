# SpecDD: AI Workflow Contract Specification

This specification governs the interactions between AI coding models, editor configurations, and prompt templates, establishing strict standards to optimize token budgets and maintain codebase consistency.

---

## 🤖 1. Assistant Grounding Rules
* **Metadata Context Injection**: Before proposing code changes, AI assistants must locate and parse the project's root `governance.yml`. This contract establishes the tech stack, library targets, and logging formats.
* **Context Preservation**: Assistants must avoid spitting out lengthy architectural narratives in chat windows unless requested. Explanations should be sparse and technical.

---

## ⚙️ 2. Reasoning Loop Cap & Operating Modes

* **Anti-Recursion Gate**: Autonomous AI agents executing commands or tool-use loops are capped at a maximum of `10` recursive actions.
* **Warning Sign**: If execution exceeds this limit without converging on the solution, the agent must halt, output the debug status, and prompt the developer for review.
* **Guided vs. Autonomous Execution Policy**:
  * *Guided Mode*: The AI must prompt the user for explicit confirmation before executing any system-altering, destructive, or state-changing action (e.g. deleting files, running arbitrary scripts, deploying builds, modifying live database schemas).
  * *Autonomous Mode*: Active only in isolated, sandboxed runtime environments with restricted shell paths and strict execution timeouts.

---

## 🛡️ 3. Anti-Scope-Creep Controls

To preserve codebase simplicity and maintain exact alignment with requested intents:
* **Active Boundary Restriction**: AI agents must restrict file modifications exclusively to the files and directories specified by the active task. Editing unrelated files or adding undocumented folders is strictly blocked.
* **Dependency & Library Lock**: Adding new third-party libraries, NPM packages, or Python dependencies is forbidden unless explicitly declared in the repository's root `governance.yml` and approved by the user.
* **Progress Auditing**: Agents must maintain a local `task.md` file during execution. Progress must be updated incrementally step-by-step to prevent reasoning drift.

---

## 📂 4. Prompt Curation & Location

* **Separation of Instructions**: Static system prompts or specific tool parameters must reside under the `prompts/` directory. They must never be hardcoded into python or typescript code packages.
* **Sparse Formats**: Prompt templates must rely on highly structured Markdown grids and YAML configuration maps, ensuring maximum token efficiency during model ingestion.

---

## 🚀 5. AI-Assisted Feature Delivery

* **Human-in-the-Loop Iterations**: Large feature rollouts must be broken down into small, digestible, and testable sub-milestones. Models must present clean diffs and prompt for feedback before proceeding to the next stage.
* **Aesthetic Superiority**: When generating user interfaces or visual components, assistants must implement custom harmonious HSL colors, modern typography, glassmorphism, and responsive CSS grids instead of generic browser defaults. Placeholders are strictly prohibited.

