# 🏎️ DriveAgain - Core Repository

Welcome to the official repository for **DriveAgain**, the dedicated, high-trust marketplace for second-hand vehicles. 

This repository is structured as a **Monorepo**, containing both the Next.js public-facing applications and the Python API infrastructure.

---

## 🏗️ Architecture & Tech Stack

* **Frontend:** Next.js + Tailwind CSS
* **Backend:** Python (FastAPI)
* **Database:** PostgreSQL (Neon.tech)
* **Media Storage:** Cloudflare R2
* **Hosting:** Vercel (Frontend) & Koyeb (Backend)

---

## 📁 Repository Structure

```text
DriveAgain/
├── frontend/               # Next.js UI (Buyer, Seller, Admin portals)
├── backend/                # FastAPI backend (buyer/seller/admin APIs)
├── scripts/                # Local setup/start helpers
├── README.md               # You are here
└── .gitignore              # Global git ignore rules
```

---

## Team Onboarding

For step-by-step clone, setup, and run instructions, read:

- [docs/start-guide.md](docs/start-guide.md)