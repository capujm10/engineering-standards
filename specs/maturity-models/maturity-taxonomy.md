# Repository Maturity Level (RML) Taxonomy

This document establishes the unified Repository Maturity Level (RML) system. It dictates structural requirements, testing rigor, telemetry depth, and autonomous AI editing permissions across our entire software portfolio.

---

## 📈 The Six Maturity Tiers

```
┌────────────────────────────────────────────────────────┐
│               TIER 4: STRATEGIC                        │
│        (Immutable core patterns, high security audit)   │
├────────────────────────────────────────────────────────┤
│               TIER 3: PRODUCTION                       │
│      (Continuous CI validations, full OpenTelemetry)   │
├────────────────────────────────────────────────────────┤
│               TIER 2: OPERATIONAL                      │
│     (Workable system, clean build, metadata schema)    │
├────────────────────────────────────────────────────────┤
│               TIER 1: EXPERIMENTAL                     │
│      (Active research/prototyping, zero OTel)          │
└────────────────────────────────────────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────────────────┐
│               LIFECYCLE STATUSES                       │
│        (DEPRECATED / ARCHIVED)                         │
└────────────────────────────────────────────────────────┘
```

---

## 📋 Standardized Operational Matrix

| RML Level | Scoring Range | Governance Rules | Telemetry Expectation | Documentation | Validation Strictness | AI Automation Allowances |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **experimental** | `1.0` - `1.9` | None. Local prototyping. | Standard print loops (`stdout`). | Single-sentence README. | Compile and execute. | Unlimited. Can modify any file/structure. |
| **operational** | `2.0` - `2.9` | Root `governance.yml` + standard `LICENSE`. | Standard structured JSON logs. | Base README + CLI manuals. | passes `./validate-repo.py` locally. | High. Can write features; structural changes need review. |
| **production** | `3.0` - `3.9` | Schema verified. Block direct `main` push. | OTel trace spans + Prometheus metrics. | Premium README with `<details>` tags. | Automated CI validator gates on PR merges. | Moderate. Can fix bugs, add tests, write docs. |
| **strategic** | `4.0` | Strict schemas + lock files. | OTel + custom dashboards. | Full Specs + architectural blueprints. | 100% build checks + security scans. | Low. AI must request approval for any edit. |
| **deprecated** | N/A | Security updates only. | Basic log output. | Deprecation notice badge at root. | Vulnerability checks. | Restricted. Security patches and docs updates only. |
| **archived** | N/A | Read-Only. No active dev. | Idle / Turned Off. | Archival context note block. | None. Static preservation. | Blocked. No modifications allowed. |

---

## 📊 Scoring Guidance & Math

To determine a target repository's numeric RML rating, audit the codebase using four dimensions (Telemetry, Governance, Documentation, Validation), score each dimension from `1` (Experimental) to `4` (Strategic), and calculate the math average:

$$\text{RML Score} = \frac{\text{Telemetry} + \text{Governance} + \text{Documentation} + \text{Validation}}{4}$$

### Dimension Grids:
1. **Telemetry**:
   * *1 (Experimental)*: Print statement logging, zero metrics hooks.
   * *2 (Operational)*: Standard structured JSON console logging.
   * *3 (Production)*: OpenTelemetry trace correlation + custom span context.
   * *4 (Strategic)*: OTel + Prometheus metrics scraping + local dashboards.
2. **Governance**:
   * *1 (Experimental)*: No license or standards rules.
   * *2 (Operational)*: MIT License + root `governance.yml` with basic values.
   * *3 (Production)*: Validated metadata conforming to central schema + protected develop branch.
   * *4 (Strategic)*: Zero-drift enforcement + locked main branch + version audits.
3. **Documentation**:
   * *1 (Experimental)*: Single-line readme, missing installation guide.
   * *2 (Operational)*: Standard setup commands + CLI syntax rules.
   * *3 (Production)*: Premium README containing collapsible `<details>` blocks for AI token savings.
   * *4 (Strategic)*: Complete SpecDD specs folder + visual Mermaid architecture charts.
4. **Validation**:
   * *1 (Experimental)*: Manual unit testing.
   * *2 (Operational)*: Passes python CLI validator locally before commits.
   * *3 (Production)*: Automated CI validation gates fail builds on drift.
   * *4 (Strategic)*: 100% test coverage + dependency alerts + CVE scanning.
