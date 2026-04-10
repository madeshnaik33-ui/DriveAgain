# 🏎️ DriveAgain - Core Repository

Welcome to the official repository for **DriveAgain**, the dedicated, high-trust marketplace for second-hand vehicles. 

This repository is structured as a **Monorepo**, containing both the Next.js public-facing applications and the Python API infrastructure.

---

## 🏗️ Architecture & Tech Stack

* **Frontend:** Next.js (React), Custom CSS Variables, Tailwind CSS
* **Backend:** Python (FastAPI/Django)
* **Database:** PostgreSQL (Neon.tech)
* **Media Storage:** Cloudflare R2
* **Hosting:** Vercel (Frontend) & Koyeb (Backend)

---

## 📁 Repository Structure

```text
DriveAgain/
├── frontend/               # The Next.js UI (Buyer Site & Seller Dashboard)
├── backend/                # The Python API & Core Logic
├── README.md               # You are here
└── .gitignore              # Global git ignore rules
```

---

## Team Onboarding

For step-by-step clone, setup, and run instructions, read:

- [docs/start-guide.md](docs/start-guide.md)