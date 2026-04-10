# About DriveAgain 🏎️

## The Core Concept
**DriveAgain** is a "trust-first," dedicated digital marketplace exclusively for buying and selling second-hand vehicles. Unlike general classified sites, DriveAgain solves the biggest problems in the used-car market—scams and low-quality data—by enforcing strict identity verification (KYC) and offering advanced, car-specific search tools.

## 🏢 The Three-Sided Platform
The project is divided into three distinct applications that communicate with each other:

1. **The Buyer Front-End (Public Website):** A lightning-fast, SEO-optimized gallery where buyers can search for vehicles. Features advanced filters (mileage, fuel type), 360-degree image galleries, and secure "Contact Seller" buttons.
2. **The Publisher Dashboard (Seller Portal):** A private, professional portal for individual sellers and dealerships. Sellers can upload vehicle photos, track ad views, securely message buyers, and upload their KYC IDs.
3. **The Admin Control Panel:** The team's hidden "control room." Features a split-screen verification queue where moderators manually review uploaded IDs against vehicle listings to approve or reject them, keeping scammers off the platform.

## 🛠️ The Technical Stack
Designed to be incredibly fast, highly secure, and 100% free to host during the launch phase.

*   **Frontend (The Face):** Next.js + Tailwind CSS. Styled with a minimal-elastic design system using Sora/Inter typography and a distinct brick orange, black, and dark sky blue color palette.
*   **Backend API (The Brain):** Python (FastAPI or Django) to handle complex algorithms, database queries, and secure user authentication.
*   **Database (The Memory):** PostgreSQL (hosted on Neon.tech). Chosen to handle complex geographic searches (e.g., "Find cars within 15 km of me").
*   **Image Storage (The Vault):** Cloudflare R2. A dedicated bucket for high-resolution car photos and PDF documents.

## 🏗️ The Engineering Architecture
*   **The Codebase:** A Monorepo structure. Both the Next.js frontend and the Python backend live in a single GitHub repository (`DriveAgain`).
*   **The Hosting:** A decoupled architecture. The frontend is automatically deployed globally via Vercel, and the Python backend is hosted securely on Koyeb.

## 👥 The Development Team
A 5-person agile engineering team structured as follows:

*   **Frontend 1:** Focuses on the public Buyer Website and global CSS system.
*   **Frontend 2:** Focuses on complex dashboard forms and Seller/Admin Dashboards.
*   **Backend 1:** Focuses on database architecture, repository management, security, and code reviews.
*   **Backend 2:** Focuses on the core vehicle API, data creation, and Cloudflare image routing.
*   **Backend 3:** Focuses on Admin logic, verification algorithms, and geographic search filters.
