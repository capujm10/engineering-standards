# Repository Operational Architecture Canon

This document outlines the operational and architectural philosophy governing our entire engineering ecosystem. By establishing a unified, metadata-driven single source of truth (SSOT), we maintain consistency, eliminate administrative bureaucracy, and facilitate seamless developer and AI agent onboarding.

---

## 🏛️ Repository Governance Architecture

Rather than relying on manual approvals or enterprise committees, our governance operates as a **deterministic software layer** directly inside each codebase:

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#1e293b', 'primaryTextColor': '#f8fafc', 'primaryBorderColor': '#475569', 'lineColor': '#94a3b8', 'secondaryColor': '#0f172a', 'tertiaryColor': '#334155'}}}%%
graph LR
    Core["Standards Canon SSOT <br>(This Repository)"] -->|Inject Specs & Schema| Target["Target Repository <br>(e.g. OpsMate_AI)"]
    Target -->|Local Run| Audit["validate-repo.py Check"]
    Audit -->|Passes Gate| CI["Github Actions CI Gates"]
```

1. **Global Standards Anchor**: This repository represents the immutable SSOT. It publishes metadata schemas, visual templates, and context packs.
2. **Local Metadata Contract**: Target repositories (`OpsMate_AI`, `ops-command-vault`, etc.) maintain a lightweight `governance.yml` declaration anchor mapping their architectural stack, observability tools, and maturity level.
3. **Automated Verification Gates**: Pre-commit hooks and Github Actions CI workflows compile validations against the target metadata. If a developer deviates from declared capability parameters, the validation gate triggers an exit code `1` and blocks branch merging.

---

## 🤖 AI-Native Engineering Methodology

Our architecture is specifically optimized for **agentic co-development**. Large Language Models (LLMs) parse and generate code with high precision when grounded in highly structured, context-sparse standards:

* **Sparse Metadata Anchors**: A 40-line `governance.yml` allows an AI agent to instantly grasp a repository's full runtime environment, database framework, and logging conventions in ~300 tokens instead of wasting thousands of tokens scanning directories.
* **Collapsible Context Barriers**: README files utilize standard HTML `<details>` blocks to isolate complex deployment parameters, layout maps, and telemetry contracts. LLMs read the top-level summaries first, only expanding deep technical contexts when specifically working in those domains.
* **Context Packs**: Standardized, hyper-dense operational capsules (`.context.md` files) provide immediate platform-specific context injections, saving models from inventing novel code structures or redundant libraries.
* **Product Coherence & Guided Modes**: Systems enforce dual-operating modes:
  * *Guided Mode*: Confirms critical, destructive, or state-changing system operations with the user before execution (human-in-the-loop).
  * *Autonomous Mode*: Restricted to non-destructive analysis and sandboxed environments under strict runtime timeout limits.
* **Anti-Scope-Creep Controls**: Models are strictly bounded to the active task boundaries. Adding undeclared modules, redundant helpers, or third-party wrappers is blocked to maintain a clean codebase.

---

## 🏢 Architectural Paradigms: Workbench & Decoupled Hubs

Our portfolio standardizes on **AI Operations Workbench** systems driving **Decoupled Intelligence Hubs**:

* **Operations Workbench**: The core host plane coordinating sandboxed CLI tools, terminal executions, and user configuration. It isolates safety boundaries, logs telemetry, and hosts user interaction loops.
* **Decoupled Intelligence Hubs**: Specialized domains (e.g. `Incident Intelligence Hub`, `Knowledge Intelligence Hub`) operating as autonomous modules. Hubs must interact strictly via decoupled APIs (HTTP REST, gRPC, or message-driven queues), with absolutely zero circular dependencies.

---

## 📈 Operational Maturity Taxonomy (RML)

We grade codebase maturity using a unified 4-tier Repository Maturity Level (RML) system:
1. **Experimental (RML 1.0 - 1.9)**: Prototyping, zero OTel setup, print logging, high AI autonomy.
2. **Operational (RML 2.0 - 2.9)**: Workable builds, structured JSON logging, local script checks.
3. **Production (RML 3.0 - 3.9)**: OTel correlated spans + Prometheus metrics, automated CI Gates, protected staging branches.
4. **Strategic (RML 4.0)**: Locked main pipelines, 100% build tests, strict schema audits.

---

## 📡 Standards Propagation Strategy

When creating new repositories or upgrading existing codebases within our ecosystem:
* **Step 1**: Reference the central standards canon repo.
* **Step 2**: Copy the baseline `/governance/templates/governance.yml` to the target root.
* **Step 3**: Deploy standard editor rulesets by placing the standard `/prompts/.cursorrules` file in the target root.
* **Step 4**: Integrate the automated compliance validator in local pre-commit and remote CI pipelines:
  ```bash
  python validation/bin/validate-repo.py --target ./ --audit --observability
  ```
