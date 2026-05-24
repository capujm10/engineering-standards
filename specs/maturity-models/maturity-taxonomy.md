# Repository Maturity Taxonomy (RML)

This taxonomy defines the repository maturity classification tiers used to grade, validate, and align our portfolio repositories. 

By classifying repos, we determine the expected level of governance, telemetry, and verification rigor required.

---

## 📈 Maturity Tiers

```
┌────────────────────────────────────────────────────────┐
│             TIER 6: PRODUCTION-PATTERN                 │
│       (Gold standard reference, blueprint template)    │
├────────────────────────────────────────────────────────┤
│             TIER 5: PORTFOLIO-GRADE                    │
│      (Continuous CI validations, premium aesthetics)   │
├────────────────────────────────────────────────────────┤
│             TIER 4: GOVERNED-OBSERVABLE                │
│    (Active metadata schemas, full OpenTelemetry)       │
├────────────────────────────────────────────────────────┤
│             TIER 3: OBSERVABLE / GOVERNED               │
│       (Structured OTel logs OR schema validated)       │
├────────────────────────────────────────────────────────┤
│             TIER 2: OPERATIONAL                        │
│            (Runnable code, clean install instructions) │
├────────────────────────────────────────────────────────┤
│             TIER 1: EXPERIMENTAL                       │
│           (Draft script, simple CLI, no telemetry)     │
└────────────────────────────────────────────────────────┘
```

---

## 📋 Capability Matrix

| RML Level | Governance Rules | Telemetry Standard | Documentation | Validation Required |
| :--- | :--- | :--- | :--- | :--- |
| **experimental** | Minimal rules. | None. Standard print statements. | Simple single-line readme. | Local compilation only. |
| **operational** | Standard License + `.gitignore`. | Basic unstructured logs. | Basic start instructions. | Clean build verification. |
| **governed** | Root `governance.yml` matches schema. | Unstructured logs. | README + basic system layout. | `validate-repo.py` passes. |
| **observable** | Basic license. | OpenTelemetry metrics/logs. | Observability sections in README. | Telemetry ports configured. |
| **governed-observable** | Schema validated. | Unified JSON logs + OTel tracing. | Fully populated architecture specs. | Integrated telemetry validations. |
| **portfolio-grade** | Schema validated. | Unified JSON logs + metrics + traces. | Premium layout + nested Details. | Automated CI validator gates. |
| **production-pattern** | Gold-standard baseline. | Full observability + Dashboards. | Comprehensive architectural guides. | 100% test coverage + central CI. |
