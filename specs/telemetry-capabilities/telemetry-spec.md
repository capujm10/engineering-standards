# Telemetry & Observability Specifications

Our engineering operating model views observability as a fundamental property of running software. This document outlines the standard contracts for logs, metrics, and tracing, ensuring a unified telemetry landscape across all portfolio repositories.

---

## 📊 1. Structured Logging Standard

All projects emitting log statements to `stdout` must serialize logs in a standardized, single-line JSON format. This enables downstream collection (e.g., Fluentd, Loki, Datadog) without parsing overhead.

### Standard Log Schema
```json
{
  "timestamp": "2026-05-24T00:10:00Z",
  "level": "INFO",
  "service": "ops-command-vault",
  "message": "Vault CLI execution completed.",
  "duration_ms": 142,
  "context": {
    "user_id": "usr_9921",
    "command": "vault audit --type=jwt"
  }
}
```

---

## 📈 2. Metrics & Instrumentation

Applications exposing monitoring metrics must conform to OpenTelemetry metric protocols or export Prometheus-compatible scraping formats.

### Common Core Metrics
* **Request Count**: Counter metric indicating overall load.
  * *Name*: `<service_identifier>_requests_total`
* **Request Latency**: Histogram metric tracking performance.
  * *Name*: `<service_identifier>_request_duration_seconds`
* **Error Rate**: Counter tracking system failures.
  * *Name*: `<service_identifier>_errors_total`

---

## 🕵️ 3. Tracing Contracts (OTel)

For projects implementing full tracing, we use **OpenTelemetry standard API spans**:

* **Collector Sinks**: Sinks must map to local Jaeger collectors via port `4317` (gRPC) or port `4318` (HTTP).
* **Span Context Preservation**: Trace contexts must be propagated through downstream network layers or shell pipes to ensure end-to-end auditability.
