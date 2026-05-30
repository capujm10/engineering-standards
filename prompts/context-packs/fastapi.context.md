# FastAPI Async Service Context Pack

This context pack governs FastAPI backend services, REST APIs, and database migrations.

---

## 🛠️ Stack Summary & Architecture Patterns
* **Target Runtime**: Python 3.10 / 3.11 / 3.12
* **Framework Core**: FastAPI v0.100+ utilizing Pydantic v2 schemas.
* **Database Layer**: SQLAlchemy Async Engine mapped via Alembic migrations.
* **Routing Standard**: Modular API routers separated by domain boundaries.

---

## ⚙️ Repository Expectations & Constraints
* **Directories**:
  * `src/api/`: Endpoint controllers and routing bindings.
  * `src/models/`: Declarative SQLAlchemy classes and Pydantic schemas.
  * `src/services/`: Pure business logic processing.
* **Async Concurrency**: Database calls and external networking actions must utilize async/await pathways. Never mix blocking calls (e.g. `requests`) inside async controllers; use `httpx` instead.

---

## 📊 Telemetry Conventions
* **Log Standard**: Structured JSON logs serializing request details (`method`, `path`, `status_code`, `duration_ms`).
* **Trace Context Injection**: Automatically inject trace IDs into standard HTTP header keys.

---

## ⚖️ Governance Rules & Validations
* **Validation Command**: Run backend structural validations:
  ```bash
  python validation/bin/validate-repo.py --target ./ --audit --observability
  ```
* **No Database Drift**: All schema changes must be declared inside Alembic migration scripts. Direct SQL mutations are strictly prohibited.
