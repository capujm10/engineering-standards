# Telemetry & Observability Stack Context Pack

This context pack governs logging, metrics instrumentation, and distributed trace routing standards across all portfolio applications.

---

## 🛠️ Stack Summary & Architecture Patterns
* **Runtime Core**: OpenTelemetry (OTel) SDK bindings.
* **Ingestion Standard**: OTLP (OpenTelemetry Protocol) over gRPC (port `4317`) or HTTP (port `4318`).
* **Scraping Sinks**: Prometheus (port `9090`), Grafana Loki, and Jaeger tracing receivers.

---

## ⚙️ Repository Expectations & Constraints
* **Configurations**: Must maintain standard `otel-collector.yml` containing routing filters.
* **Trace Propagation**: Remote calls must implement W3C Trace Context propagation headers.
* **No Novel Logs**: Avoid generating raw text console outputs. All output streams must utilize structured JSON formats.

---

## 📊 Telemetry Conventions
* **Logs Format**: Strict single-line JSON structure:
  ```json
  {"timestamp": "ISO", "level": "INFO", "service": "name", "message": "msg", "duration_ms": 0}
  ```
* **Metrics Formats**:
  * `<service>_requests_total` (Counter tracking ingress traffic)
  * `<service>_request_duration_seconds` (Histogram tracking runtime)
  * `<service>_errors_total` (Counter tracking uncaught exception rates)

---

## ⚖️ Governance Rules & Validations
* **Validation Command**: Run full suite telemetry analysis:
  ```bash
  python validation/bin/validate-repo.py --target ./ --observability
  ```
* **Conformance checks**: Validator verifies that telemetry collectors are declared and that scrapers connect to standard port rules.
