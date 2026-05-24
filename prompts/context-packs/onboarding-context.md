# AI-Native Onboarding Context Pack

This document acts as an ultra-compressed, context-sparse blueprint designed to hydrate any LLM session (Gemini, Codex, Claude, ChatGPT, or local models) with our entire engineering portfolio in under **600 tokens**. 

Paste this block into the system prompt or chat start when starting work on a new feature.

---

## ⚡ Compressed Portfolio Grounding Profile

```yaml
context_version: "1.0.0"
portfolio_domain: "Operational-Governance-Observability"
repos:
  - name: ops-command-vault            # Python, Typer, CLI auditing
  - name: OpsMate_AI                  # Python, LLM orchestration agent
  - name: OpsSight-Observability-Lab  # telemetry testing lab, jaeger
  - name: mini-tls-lab                # security, cryptographic testing
  - name: ResumeOps-Engine            # parsing CLI, automated resume builder
  - name: FacturaOps                  # invoice scanning pipelines
  - name: Technotopia                 # policy simulations
  - name: republica-transparente      # open government metadata parsing

engineering_manifesto:
  standards_repo: "engineering-standards"
  model: "Intent -> Contract -> Validation -> Telemetry -> Governance"
  telemetry: "OTel OTLP/gRPC on :4317, structured logs, Prom metrics"
  maturity_levels:
    - experimental
    - operational
    - governed
    - observable
    - governed-observable
    - portfolio-grade
    - production-pattern

ai_directives:
  1_read_metadata: "Locate and parse root governance.yml file first."
  2_enforce_cursorrules: "Always match code output to the local .cursorrules constraints."
  3_sparse_responses: "Use collapsed HTML <details> for complex file layouts or architecture."
```
