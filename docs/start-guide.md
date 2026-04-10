# DriveAgain Team Start Guide

This guide explains exactly what every team member should do after joining the project.

## 1. Prerequisites (Install Once)

Install these tools before cloning:

- Git (latest stable)
- Node.js 20.9+ (LTS recommended)
- npm (comes with Node.js)
- Python 3.11+
- VS Code

Check versions:

```powershell
git --version
node -v
npm -v
python --version
```

## 2. Clone the Repository

Run these commands in your terminal:

```powershell
git clone https://github.com/dhanushrs1/DriveAgain.git
cd DriveAgain
```

If you already cloned an older remote URL, update origin:

```powershell
git remote set-url origin https://github.com/dhanushrs1/DriveAgain.git
git remote -v
```

## 3. Switch to the Team Branch

Never work directly on main.

```powershell
git fetch --all --prune
git checkout develop
git pull origin develop
```

## 4. Open the Project

```powershell
code .
```

## 5. Install Frontend + Backend Dependencies

Recommended setup command (run once from repository root):

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup.ps1
```

Manual setup (alternative):

```powershell
cd backend
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt

cd ..\frontend
npm install
```

## 6. Start Frontend + Backend Together

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\dev.ps1
```

This opens two terminals automatically.

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Backend docs: http://localhost:8000/docs

If port 3000 is already in use, Next.js will use the next available port.

## 7. Current Routes You Can Test

- Buyer website: http://localhost:3000/
- Seller portal: http://localhost:3000/seller
- Admin dashboard: http://localhost:3000/admin
- Buyer API: http://localhost:8000/api/buyer/ping
- Seller API: http://localhost:8000/api/seller/ping
- Admin API: http://localhost:8000/api/admin/ping

## 8. Stop the Servers

Close the two spawned terminals, or press Ctrl+C inside each server terminal.

## 9. Daily Team Workflow (Required)

At the start of each day:

```powershell
git checkout develop
git pull origin develop
```

Create a feature branch:

```powershell
git checkout -b feature/your-feature-name
```

After coding:

```powershell
git add .
git commit -m "feat: short clear message"
git push -u origin feature/your-feature-name
```

Then open a Pull Request:

- Base branch: develop
- Compare branch: feature/your-feature-name

## 10. Rules Everyone Must Follow

- Do not push directly to main.
- Create a feature branch from develop.
- Keep commits small and clear.
- Open PRs for review before merge.

## 11. Common Problems and Fixes

### Error: missing script dev

You are likely in the wrong folder. Run:

```powershell
cd frontend
npm run dev
```

### Python command not found

Install Python 3.11+ and restart terminal.

### Port already in use

Use the URL shown in terminal output.

### Hydration warning in dev

This is often caused by browser extensions. Test once in private/incognito mode.

## 12. Backend Status

Backend API starter is ready with buyer, seller, and admin modules.

## 13. Deployment Targets (Later)

- Frontend hosting: Vercel
- Backend hosting: Koyeb
- Database: Neon PostgreSQL
- Image/file storage: Cloudflare R2
