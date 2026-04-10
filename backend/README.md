# Backend API (FastAPI)

This backend powers all API domains for DriveAgain:

- Buyer API
- Seller API
- Admin API

## Structure

```text
backend/
├── main.py                    # FastAPI app entrypoint
├── requirements.txt           # Python dependencies
├── .env.example               # Neon + Cloudflare env template
└── api/
    ├── buyer/routes.py
    ├── seller/routes.py
    └── admin/routes.py
```

## Local Setup

```powershell
cd backend
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run Backend

```powershell
cd backend
.\venv\Scripts\python.exe -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Smoke Test URLs

- API root: http://localhost:8000/
- Health: http://localhost:8000/health
- Swagger docs: http://localhost:8000/docs
- Buyer ping: http://localhost:8000/api/buyer/ping
- Seller ping: http://localhost:8000/api/seller/ping
- Admin ping: http://localhost:8000/api/admin/ping
