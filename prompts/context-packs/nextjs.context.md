# Next.js & React Frontend Context Pack

This context pack governs Next.js App Router frontends, React Server Components, and Tailwind CSS design styling.

---

## 🛠️ Stack Summary & Architecture Patterns
* **Target Runtime**: Node.js v20+ / Next.js v14+ utilizing App Router.
* **Component Layering**: React Server Components (RSC) for data fetching by default.
* **Client Boundary**: Explicitly isolate client interactions (modals, forms, state loops) via the `'use client'` directive at leaf components.
* **Styling core**: Tailwind CSS utilizing global theme variables declared in `tailwind.config.js`.

---

## ⚙️ Repository Expectations & Constraints
* **Directories**:
  * `app/`: Next.js page routers, layout engines, and API boundaries.
  * `components/`: Modular UI widgets split into core primitives (`components/ui/`) and dashboard panels.
* **TypeScript Rigidity**: Standard compiler settings must enforce strict type safety checks. Avoid bypassing using the `any` keyword.

---

## 📊 Telemetry Conventions
* **Browser Monitoring**: Performance telemetry captured using Next.js Web Vitals metrics.
* **API Logging**: Serverless API calls must serialize execution latency and error payloads.

---

## ⚖️ Governance Rules & Validations
* **Validation Command**: Run build and lint scripts:
  ```bash
  npm run lint && npm run build
  ```
* **No Styling Drift**: Visual elements must utilize standard theme colors and margins. Ad-hoc hardcoded pixel parameters are blocked in code edits.
