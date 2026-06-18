<div align="center">

<br/>

```
 ███████╗██╗  ██╗ ██████╗ ██╗  ██╗ ██████╗ ██████╗ ███████╗
 ██╔════╝██║  ██║██╔═══██╗██║  ██║██╔═══██╗██╔══██╗██╔════╝
 ███████╗███████║██║   ██║███████║██║   ██║██████╔╝█████╗  
 ╚════██║██╔══██║██║   ██║██╔══██║██║   ██║██╔══██╗██╔══╝  
 ███████║██║  ██║╚██████╔╝██║  ██║╚██████╔╝██║  ██║███████╗
 ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                             
 ██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗
 ██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║
 ██║ █╗ ██║███████║   ██║   ██║     ███████║
 ██║███╗██║██╔══██║   ██║   ██║     ██╔══██║
 ╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║
  ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
```

### 🚨 Urban Emergency Response & Monitoring API

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-red?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://django-rest-framework-simplejwt.readthedocs.io/)
[![Swagger](https://img.shields.io/badge/Swagger-UI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](https://swagger.io/)

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg?style=flat-square)](https://github.com/Tanbir-Hasan-247)
[![API-First](https://img.shields.io/badge/Architecture-API--First-blueviolet?style=flat-square)](https://github.com/Tanbir-Hasan-247)

<br/>

[**Swagger Docs**](http://127.0.0.1:8000/api/schema/swagger-ui/) · [**ReDoc**](http://127.0.0.1:8000/api/schema/redoc/) · [**Report a Bug**](https://github.com/Tanbir-Hasan-247/ShohoreWatch/issues) · [**Request a Feature**](https://github.com/Tanbir-Hasan-247/ShohoreWatch/issues)

<br/>

</div>

---

## 📖 Table of Contents

- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Alert State Machine](#-alert-state-machine)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Documentation](#-api-documentation)
- [Core API Endpoints](#-core-api-endpoints)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🌟 About The Project

**ShohoreWatch** is a robust, API-first smart city backend system built with **Django REST Framework (DRF)**. It unifies citizens, city officials, and emergency responders into a single centralized platform — enabling real-time incident reporting, zone-based management, and structured emergency resolution workflows.

From a waterlogging report by a citizen to a fire dispatch assigned to a responder, ShohoreWatch handles the full lifecycle of an urban emergency — with role-aware access control, state-machine-driven alert tracking, and interactive API documentation out of the box.

> 💡 **Why ShohoreWatch?**  
> Urban emergencies suffer from poor coordination and delayed response. ShohoreWatch solves this by creating a structured, API-first backbone that any smart city frontend — web, mobile, or IoT — can plug into immediately.

---

## ✨ Key Features

<details>
<summary><b>🔐 Role-Based Access Control (RBAC)</b></summary>
<br/>

Four distinct user roles, each with tailored permissions and profile data:

| Role | Icon | Capabilities |
|---|:---:|---|
| **Citizen** | 🧑‍🤝‍🧑 | Report incidents, upload images, track personal alert status |
| **Official (Zone Controller)** | 👮 | Manage city zones, verify incidents, assign responders |
| **Responder** | 🚒 | Receive assignments, update real-time field status, resolve alerts |
| **Admin** | 👨‍💻 | Full system control, user management, analytics overview |

</details>

<details>
<summary><b>🚦 Smart Incident Workflow (State Machine)</b></summary>
<br/>

Every alert follows a structured, linear state machine to ensure accountability at every stage:

```
Pending ──► Active ──► Acknowledged ──► Responding ──► Resolved
                                                    └──► False Alarm
```

No alert can skip a step — every transition is logged with the responsible user and timestamp.

</details>

<details>
<summary><b>🔍 Advanced Filtering & Search</b></summary>
<br/>

| Filter | Options |
|---|---|
| Zone | Filter alerts by city zone |
| Category | Incident type (Fire, Accident, Crime, Waterlogging, etc.) |
| Severity | Low / Medium / High / Critical |
| Date Range | From–To date window for historical queries |
| Status | Current workflow state of the alert |
| Keyword | Free-text search across incident title and description |

Powered by `django-filter` with full pagination support.

</details>

<details>
<summary><b>📚 Interactive API Documentation</b></summary>
<br/>

Auto-generated, always up-to-date API docs powered by `drf-spectacular`:

| Interface | URL | Description |
|---|---|---|
| **Swagger UI** | `/api/schema/swagger-ui/` | Interactive, try-it-now API explorer |
| **ReDoc** | `/api/schema/redoc/` | Clean, readable reference documentation |

</details>

<details>
<summary><b>🗃️ Automated Data Population</b></summary>
<br/>

A custom Python seeding script generates a fully realistic dataset instantly:

- 🗺️ Multiple **City Zones** with names and boundaries
- 📂 Multiple **Incident Categories** (Fire, Flood, Crime, Accident, etc.)
- 👥 **10 Users** spread across all 4 roles with complete profiles
- 🚨 **30 Alerts** across various zones, categories, and severity levels

> All generated users share the default password: `password123`

</details>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|:---:|:---:|
| **Language** | Python 3.10+ |
| **Framework** | Django 4.2+ |
| **API Layer** | Django REST Framework (DRF) |
| **Authentication** | JWT via `djangorestframework-simplejwt` |
| **Database (Dev)** | SQLite |
| **Database (Prod)** | PostgreSQL |
| **API Documentation** | Swagger UI + ReDoc via `drf-spectacular` |
| **Filtering** | `django-filter` |
| **Config Management** | `python-decouple` |

</div>

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                         ShohoreWatch API                         │
│                                                                  │
│  ┌──────────┐  ┌────────────┐  ┌────────────┐  ┌─────────────┐  │
│  │ Citizen  │  │  Official  │  │  Responder │  │    Admin    │  │
│  └────┬─────┘  └─────┬──────┘  └─────┬──────┘  └──────┬──────┘  │
│       │              │               │                 │          │
│  ┌────▼──────────────▼───────────────▼─────────────────▼───────┐ │
│  │         JWT Authentication  +  RBAC Permission Layer        │ │
│  └───────────────────────────────┬──────────────────────────────┘ │
│                                  │                                │
│  ┌───────────────────────────────▼──────────────────────────────┐ │
│  │                  Django REST Framework Views                 │ │
│  │         (Alerts / Zones / Users / Categories / Auth)        │ │
│  └─────────┬─────────────────────┬────────────────┬────────────┘ │
│            │                     │                │              │
│  ┌─────────▼──────┐  ┌───────────▼──────┐  ┌─────▼──────────┐  │
│  │  Alert State   │  │   Django ORM     │  │  drf-spectacu- │  │
│  │  Machine       │  │ SQLite/PostgreSQL │  │  lar (Swagger) │  │
│  └────────────────┘  └──────────────────┘  └────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🚦 Alert State Machine

Every incident in ShohoreWatch follows a strictly enforced lifecycle:

```
                    ┌─────────┐
       [Citizen]    │ PENDING │   (Newly reported, awaiting review)
    Reports Alert──►└────┬────┘
                         │ Official Verifies
                    ┌────▼────┐
                    │ ACTIVE  │   (Confirmed as real incident)
                    └────┬────┘
                         │ Responder Assigned
                ┌────────▼────────┐
                │  ACKNOWLEDGED   │   (Responder confirms receipt)
                └────────┬────────┘
                         │ En Route
                  ┌──────▼──────┐
                  │  RESPONDING │   (Team is on the ground)
                  └──────┬──────┘
                         │
              ┌──────────┴──────────┐
         ┌────▼────┐           ┌────▼────────┐
         │RESOLVED │           │ FALSE ALARM │
         └─────────┘           └─────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- **Python** `>= 3.10` — [Download](https://python.org/downloads)
- **Git** — [Download](https://git-scm.com/)
- Optionally: **PostgreSQL** for production-like setup

---

### Installation

**Step 1 — Clone the repository**

```bash
git clone https://github.com/Tanbir-Hasan-247/ShohoreWatch.git
cd ShohoreWatch
```

**Step 2 — Create and activate a virtual environment**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

> ⚠️ Avoid naming your virtual environment `.env` — it will conflict with your environment variables file.

**Step 3 — Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4 — Apply database migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 5 — (Optional) Populate with realistic dummy data**

```bash
python populate_db.py
```

> This generates Zones, Categories, 10 role-specific Users, and 30 Alerts.  
> Default password for all generated users: **`password123`**

**Step 6 — Create a superuser (Admin)**

```bash
python manage.py createsuperuser
```

**Step 7 — Start the development server**

```bash
python manage.py runserver
```

🎉 Server is live at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📚 API Documentation

Once the server is running, explore all endpoints interactively:

<div align="center">

| Interface | URL | Description |
|:---:|:---:|:---:|
| **Swagger UI** | [`/api/schema/swagger-ui/`](http://127.0.0.1:8000/api/schema/swagger-ui/) | Try-it-now interactive explorer |
| **ReDoc** | [`/api/schema/redoc/`](http://127.0.0.1:8000/api/schema/redoc/) | Clean, readable reference docs |

</div>

> All protected endpoints require a **Bearer JWT token** in the `Authorization` header.  
> Obtain your token via `POST /api/auth/login/` and include it as: `Authorization: Bearer <your_access_token>`

---

## 📌 Core API Endpoints

<div align="center">

| Module | Method | Endpoint | Description | Auth Required |
|:---:|:---:|---|---|:---:|
| **Auth** | `POST` | `/api/v1/auth/users/` | Register a new user | ❌ |
| **Auth** | `POST` | `/api/auth/v1/jwt/create/` | Obtain JWT Access & Refresh tokens | ❌ |
| **Auth** | `POST` | `/api/auth/v1/token/refresh/` | Refresh an expired access token | ❌ |
| **Alerts** | `GET` | `/api/v1/alerts/` | List all alerts (filter & paginate) | ✅ |
| **Alerts** | `POST` | `/api/v1/alerts/` | Report a new incident | ✅ Citizen |
| **Alerts** | `GET` | `/api/v1/alerts/{id}/` | Retrieve a single alert's details | ✅ |
| **Alerts** | `PATCH` | `/api/v1/alerts/{id}/status/` | Update alert status | ✅ Official / Responder |
| **Zones** | `GET` | `/api/v1/zones/` | List all city zones | ✅ |
| **Zones** | `POST` | `/api/v1/zones/` | Create a new zone | ✅ Admin |
| **Categories** | `GET` | `/api/v1/categories/` | List all incident categories | ✅ |
| **Users** | `GET` | `/api/v1/users/` | List all users | ✅ Admin |
| **Users** | `GET` | `/api/v1/users/{id}/` | View a specific user profile | ✅ |

</div>

> 📖 See **Swagger UI** for full request bodies, response schemas, query parameters, and error codes.

---

## 🗺️ Roadmap

- [x] ✅ Four-role RBAC system (Citizen, Official, Responder, Admin)
- [x] ✅ JWT-based authentication with token refresh
- [x] ✅ Full alert CRUD with state machine workflow
- [x] ✅ Zone and category management
- [x] ✅ Advanced filtering & search via `django-filter`
- [x] ✅ Auto-generated Swagger UI & ReDoc documentation
- [x] ✅ Database seeding script with realistic dummy data
- [ ] 🔔 **Real-Time WebSockets** — Django Channels + Redis for live alert broadcasting
- [ ] 📍 **Live Location Tracking** — WebSocket consumers for responder GPS coordinates
- [ ] 📧 **Email / SMS Notifications** — Signal-triggered alerts for critical incidents
- [ ] 📊 **Analytics & SLA API** — Average response times and resolution metrics per zone
- [ ] 🗺️ **Map Integration** — Geo-tagged incident pinning on an interactive city map
- [ ] 🧪 **Automated Tests** — Full unit and integration test suite with `pytest-django`

---

## 🤝 Contributing

Contributions, issues, and feature requests are always welcome!

1. **Fork** the repository
2. **Create** a feature branch → `git checkout -b feature/AmazingFeature`
3. **Commit** your changes → `git commit -m 'Add AmazingFeature'`
4. **Push** to the branch → `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

Please ensure your API changes are reflected in the Swagger schema and include appropriate comments.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## 👨‍💻 Author

<div align="center">

### Tanbir Hasan

*Aspiring Software Developer & Competitive Programmer*

<br/>

[![Email](https://img.shields.io/badge/Email-tanbirhasan569%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tanbirhasan569@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Tanbir--Hasan--247-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Tanbir-Hasan-247)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/tanbir-hasan-638075345/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-3b82f6?style=for-the-badge&logo=safari&logoColor=white)](https://tanbir-hasan-247.github.io/Tanbir-Hasan/)

<br/>

*If this project was useful to you, please consider giving it a ⭐ — it really helps!*

</div>

---

<div align="center">

Made with ❤️ and ☕ by **Tanbir Hasan**

<br/>

*ShohoreWatch — Because every second counts in an emergency.*

</div>