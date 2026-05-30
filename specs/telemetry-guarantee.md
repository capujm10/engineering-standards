# SpecDD: Telemetry Guarantee Specification

This specification governs the runtime observability contracts. It guarantees that any service running inside our ecosystem emits standardized, parseable, and trace-correlated logs, metrics, and spans.

---

## 📊 1. Structured Logging Schema
All software packages emitting log streams to stdout must serialize messages into a standardized single-line JSON envelope:

```json
{
  "timestamp": "2026-05-24T00:30:00Z",
  "level": "INFO",
  "service": "target-service-name",
  "message": "Action completed successfully.",
  "duration_ms": 42,
  "context": {
    "module": "database/core",
    "trace_id": "8e3b320d3f..."
  }
}
```

---

## 📈 2. Standard Metric Formats
Applications requiring metrics monitoring must expose endpoints in Prometheus exposition format or hook directly into an OpenTelemetry exporter:
* **Latency Histogram**: `<service>_request_duration_seconds` (split by route and status code).
* **Load Counter**: `<service>_requests_total` (tracks overall query volume).
* **Crash Counter**: `<service>_errors_total` (tracks raw unhandled exceptions count).

---

## 🕵️ 3. Tracing Context Propagation
To preserve cross-service correlation:
* **Traceparent Format**: Outbound HTTP requests and backend script calls must inject W3C standard trace correlation headers:
  ```
  traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
  ```
* **Logging Integration**: Current trace spans must be parsed and injected directly into structured JSON log files to ensure logs and spans align.
