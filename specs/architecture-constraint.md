# SpecDD: Architecture Constraint Specification

This specification defines core technical boundaries, security rules, and structural constraints that prevent system bloat, unauthorized database hooks, or runtime environment drift.

---

## 🔒 1. Security & Environment Isolation
* **Credentials Standard**: Never hardcode credentials, passwords, database connections, or API key strings directly inside source files.
* **Env Loading**: Configuration parameters must parse dynamically from system environment parameters using libraries like Pydantic Settings or dotenv.
* **File Separation**: Local development keys must remain isolated inside `.env.local` files, which are explicitly blocked from Git commits by `.gitignore`.

---

## 📡 2. Networking & Microservices
* **API Boundaries**: Subsystem interactions must utilize structured HTTP REST APIs, gRPC services, or isolated queue workers.
* **No Direct DB Hooking**: Downstream packages are strictly barred from connecting directly to database engines owned by separate services; all transactions must route via the owner's public API.

---

## 💾 3. State & Thread Management

* **Stateless Runtimes**: Wherever possible, web routes and script engines must remain entirely stateless, scaling up or down with no session caching.
* **Concurrency Workers**: For heavy background computation, tasks must offload to dedicated queues (e.g. Celery) or managed background thread pools (e.g. QThreadPool) to prevent blocking main routines.

---

## 🛡️ 4. AI Operations Workbench Sandboxing

To ensure safety and integrity when executing system commands:
* **Shell Isolation**: All CLI and shell execution tasks initiated by the workbench must run in sandboxed terminal environments with restricted user privileges.
* **Execution Guardrails**: Subprocess commands must enforce strict runtime timeouts (default `<60s`) and write standard audit trails tracing the initiating agent and the command run.
* **Memory & CPU Capping**: Sandbox executions must be throttled to prevent runaway process trees from consuming host system resources.

---

## 🏢 5. Hub-Based Product Decoupling

When organizing features into modular intelligence hubs:
* **Strict Interface Boundaries**: Modular hubs (e.g. `incident-intelligence-hub`, `knowledge-intelligence-hub`) must communicate exclusively through clean public API boundaries (e.g. gRPC interfaces, HTTP REST, or message queues).
* **Zero Circular Imports**: Sibling hubs are strictly prohibited from importing each other's internal modules or sharing internal databases. All shared models or data contracts must be extracted into a separate common library.

