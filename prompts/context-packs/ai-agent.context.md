# AI Agent & Orchestrator Context Pack

This context pack governs AI model integration, prompt caching, tool invocation loops, and deterministic formatting.

---

## 🛠️ Stack Summary & Architecture Patterns
* **Target Runtime**: Python 3.10+ / LangChain / Agnostic APIs.
* **System Prompt Design**: Highly modular YAML prompt templates designed to run with prompt compression algorithms.
* **Tool-Use Routing**: Declarative function calling returning strictly typed JSON schemas.

---

## ⚙️ Repository Expectations & Constraints
* **Recursion Cap**: All reasoning loops must enforce a hard execution count limit of `10` iterations to avoid runaway token costs.
* **Model Selection**: Multi-stage routing must allocate lighter models (e.g., Gemini 3.5 Flash) for parsing and heavy models for complex architectural decision logic.
* **Separation of Concerns**: Prompt instructions must be isolated under `prompts/` and never mixed inside application logic packages.

---

## 📊 Telemetry Conventions
* **Token Tracking**: Logs must record the prompt tokens, completion tokens, latency overhead, and API billing estimates.
* **Tracing Spans**: OTel spans must wrap all model routing and tool-use steps.

---

## ⚖️ Governance Rules & Validations
* **Validation Command**: Run reasoning verification checks:
  ```bash
  python validation/bin/validate-repo.py --target ./ --audit
  ```
* **No Prompt Drift**: System prompts must match validated configuration blocks in `prompts/system_prompts.yml`.
