# OpsMate Desktop & CLI Stack Context Pack

This context pack anchors AI coding assistants operating on the `OpsMate` system. It enforces core framework boundaries, thread limits, and telemetry requirements.

---

## 🛠️ Stack Summary & Architecture Patterns
* **Target Runtime**: Python 3.10 / 3.11
* **UI Meta-Framework**: PySide6 (Qt for Python)
* **Design Core**: Model-View-Controller (MVC) with strict separation of backend daemon execution from GUI layouts.
* **Background Tasks**: Must utilize Qt Threading (`QThread`, `QRunnable`) combined with thread-safe signaling. Never execute blocking operations on the main GUI thread.

---

## ⚙️ Repository Expectations & Constraints
* **Directories**:
  * `src/gui/`: UI rendering components (never contain database logic or direct API requests).
  * `src/daemon/`: Persistent background tasks, shell scripting controllers, and hardware loop checks.
  * `src/core/`: Security configs and local config maps.
* **Operational Limits**: No global thread spawns. Active workers must utilize designated QThreadPools.

---

## 📊 Telemetry Conventions
* **Logs**: Serialized single-line JSON standard matching:
  ```json
  {"timestamp": "ISO", "level": "INFO", "component": "gui/daemon", "message": ""}
  ```
* **Event Dispatching**: Errors must trigger local Qt signals mapped to UI visual alert overlays.

---

## ⚖️ Governance Rules & Validations
* **Validation Command**: Run local structural sanity tests:
  ```bash
  python validation/bin/validate-repo.py --target ./ --audit
  ```
* **File Compliance**: Code edits must maintain `.cursorrules` parameters and ensure all new widgets inherit base style layers.
* **No Drift**: Adding external third-party GUI helper frameworks is strictly blocked unless declared in the root `governance.yml`.
