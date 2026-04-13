# DriveAgain MVP Implementation Plan

## Goal
Build and launch a trustworthy used-vehicle marketplace MVP with three surfaces:
- Buyer website
- Seller portal
- Admin verification dashboard

## Delivery Target
- MVP ready for internal demo in 4 weeks
- Production hardening in week 5

## Working Model
- Branch base: `develop`
- No direct push to `main`
- Every change through Pull Request
- At least 1 approval before merge

## Phase 0: Scope Freeze (Day 1)

### Tasks
- Freeze MVP feature list for Buyer, Seller, and Admin.
- Define non-goals for MVP (what is explicitly out of scope).
- Finalize acceptance criteria per module.

### Owners
- Backend Lead: final technical sign-off
- Frontend 1 and Frontend 2: UI scope sign-off
- Backend 2 and Backend 3: API and moderation scope sign-off

### Checkpoint
- Single signed document in docs with MVP scope and non-goals.

### Rollback Trigger
- If any team member requests a feature not in the freeze list, it moves to post-MVP backlog unless critical.

## Phase 1: Architecture Freeze (Day 1-2)

### Tasks
- Finalize database entity list (users, vehicles, media, verification, messages, views).
- Finalize API contract v1 (OpenAPI draft).
- Finalize route map for frontend pages.
- Finalize role-based permission matrix.

### Checkpoint
- Architecture review meeting completed.
- Approval notes added to docs.

### Rollback Trigger
- If schema changes impact more than 20% of API contract, branch is paused and architecture is re-approved before coding resumes.

## Phase 2: Environment and Repo Hardening (Day 2)

### Tasks
- Confirm local setup guide works on a fresh machine.
- Add CI checks for frontend build and lint.
- Define env variable template files for frontend and backend.
- Confirm no duplicate package managers or lockfiles outside intended folders.

### Checkpoint
- CI passes on `develop`.
- At least one teammate reproduces setup from zero.

### Rollback Trigger
- If setup fails for any teammate, stop feature work and fix environment first.

## Phase 3: First Coding Slice (Day 3-5)

### Vertical Slice Scope (Read Flow First)
- Buyer can open home page and see vehicle cards from API.
- Seller and Admin pages remain simple role placeholders.
- Basic API health endpoint and vehicle list endpoint live.

### Team Assignment
- Frontend 1: Buyer list page UI and loading/error states.
- Frontend 2: Shared UI components and form scaffold for Seller page.
- Backend Lead: DB schema v1 migration strategy and review gate.
- Backend 2: Vehicle list API and media URL contract.
- Backend 3: Admin queue data shape and verification status model.

### Checkpoint
- End-to-end demo: browser request to API and data visible in Buyer page.
- PRs merged into `develop` only after review.

### Rollback Trigger
- If API contract breaks frontend integration, revert to previous tagged contract and open a hotfix PR.

## Phase 4: Trust and Verification Core (Week 2)

### Scope
- KYC document upload pipeline (metadata only first).
- Admin approve/reject action with audit log.
- Seller status reflected in dashboard.

### Checkpoint
- Verification flow tested with approved and rejected scenarios.

## Phase 5: Search and Marketplace Quality (Week 3)

### Scope
- Filters: mileage, fuel type, price range, city.
- Pagination and sorting.
- View-count tracking for seller analytics.

### Checkpoint
- Query performance baseline captured and documented.

## Phase 6: Stabilization and Release Readiness (Week 4)

### Scope
- Bug fixes and performance pass.
- Security checks for auth and upload endpoints.
- Deployment checklist for Vercel and Koyeb.

### Checkpoint
- Staging sign-off and go/no-go decision.

## Quality Gates (Apply Every Week)
- No merge without review.
- No feature merge without acceptance criteria met.
- No release if critical security or auth bug is open.

## Risk Register (Initial)
- KYC compliance complexity
- Image upload/storage consistency
- Geo-search query performance
- Role permission mistakes

## First Step to Execute Today
1. Create a branch: `planning/implementation-v1`.
2. Add architecture docs: `docs/db-schema-v1.md`, `docs/api-contract-v1.md`, `docs/permissions-matrix.md`.
3. Open one planning PR to `develop` titled: `docs: freeze MVP architecture v1`.
4. Hold a 30-minute sign-off meeting and merge only after all 5 team members approve scope.
