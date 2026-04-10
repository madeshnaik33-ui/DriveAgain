# DriveAgain Team Start Guide

This guide explains exactly what every team member should do after joining the project.

## 1. Prerequisites (Install Once)

Install these tools before cloning:

- Git (latest stable)
- Node.js 20.9+ (LTS recommended)
- npm (comes with Node.js)
- VS Code

Check versions:

```bash
git --version
node -v
npm -v
```

## 2. Clone the Repository

Run these commands in your terminal:

```bash
git clone https://github.com/dhanushrs1/DriveAgain.git
cd DriveAgain
```

If you already cloned an older remote URL, update origin:

```bash
git remote set-url origin https://github.com/dhanushrs1/DriveAgain.git
git remote -v
```

## 3. Switch to the Team Branch

Never work directly on `main`.

```bash
git fetch --all --prune
git checkout develop
git pull origin develop
```

## 4. Open the Project

```bash
code .
```

## 5. Install Frontend Dependencies

From the repository root:

```bash
cd frontend
npm install
```

## 6. Start the Website (Frontend)

```bash
npm run dev
```

Open this in your browser:

- http://localhost:3000

If port 3000 is busy, Next.js will automatically use another port (for example, 3001).

## 7. Current Routes You Can Test

- Buyer site: http://localhost:3000/
- Seller portal: http://localhost:3000/seller
- Admin dashboard: http://localhost:3000/admin

## 8. Stop the Server

Press `Ctrl+C` in the terminal running `npm run dev`.

## 9. Daily Team Workflow (Required)

At the start of each day:

```bash
git checkout develop
git pull origin develop
```

Create a feature branch:

```bash
git checkout -b feature/your-feature-name
```

After coding:

```bash
git add .
git commit -m "feat: short clear message"
git push -u origin feature/your-feature-name
```

Then open a Pull Request:

- Base branch: `develop`
- Compare branch: `feature/your-feature-name`

## 10. Rules Everyone Must Follow

- Do not push directly to `main`.
- Create a feature branch from `develop`.
- Keep commits small and clear.
- Open PRs for review before merge.

## 11. Common Problems and Fixes

### Error: Missing script "dev"

You are likely in the wrong folder. Run:

```bash
cd frontend
npm run dev
```

### Port already in use

Next.js will choose the next free port automatically. Use the URL shown in terminal.

### Hydration warning in dev

This can be caused by browser extensions. Test once in private/incognito mode.

## 12. Backend Status

Backend API setup is planned next. For now, team members only need to run the frontend.
