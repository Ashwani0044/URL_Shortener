## Full-Stack Containerized URL Shortener

A production-ready, full-stack URL Shortener built with **FastAPI**, **React (Vite)**, **MySQL 8.0**, and **Nginx**, orchestrated with **Docker Compose** and automated via **GitHub Actions CI/CD**.

---

## System Architecture

```text
                        ┌───────────────────────────────────────┐
                        │           Nginx Reverse Proxy         │
                        │              (Port 80)                │
                        └───────┬───────────────────────┬───────┘
                                │                       │
            Static React Assets │                       │ /api/* & /{short_code}
                                ▼                       ▼
                  ┌─────────────────────────┐   ┌───────────────────────────┐
                  │   React + Vite Bundle   │   │      FastAPI Backend      │
                  │    (/usr/share/nginx)   │   │        (Port 8000)        │
                  └─────────────────────────┘   └─────────────┬─────────────┘
                                                              │
                                                              │ SQLAlchemy + PyMySQL
                                                              ▼
                                                ┌───────────────────────────┐
                                                │      MySQL 8.0 Database   │
                                                │        (Port 3306)        │
                                                └───────────────────────────┘