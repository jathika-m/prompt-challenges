# CelebrAI — Your Personal AI Event Planner
### Google for Developers Prompt Wars Challenge 5 — Celebration & Event Planner

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**CelebrAI** is a modern, luxury web application engineered for planning **Weddings, Birthdays, Engagement Ceremonies, Anniversaries, and Community Events**. Designed with an editorial aesthetic, CelebrAI pairs sophisticated venue photography with intelligent budget estimation, curated blueprints, and seamless event management.

GitHub Repository: [https://github.com/jathika-m/prompt-challenges](https://github.com/jathika-m/prompt-challenges)

---

## 🌟 Key Application Features

### 1. Hero & Celebration Category Suite
- **Panoramic Evening Venue Hero**: High-contrast luxury venue photography with headline *"Every Celebration Begins with a Beautiful Plan"* and quick-start actions.
- **5-Column Event Selection Grid**: Single horizontal desktop row (`lg:grid-cols-5`) covering **Wedding**, **Birthday**, **Engagement**, **Anniversary**, and **Community Event** with one-click planner pre-filling.

### 2. Discover Themes & Inspiration Gallery (12 Curated Themes)
- **Responsive 4-Column Layout**: 4 per row on desktop, 2 on tablet, 1 on mobile (`grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6`).
- **Authentic Venue Photography**: Authentic venue styling featuring botanical conservatories, beachfront canopies, heritage palaces, and rooftop penthouses (*no stock cake imagery*).
- **Instant Category Filtering**: Real-time filtering (`All | Wedding | Birthday | Engagement | Anniversary | Community Event`) without page reload.
- **The 12 Curated Themes**:
  1. *Elegant Garden Wedding*
  2. *Minimalist Modern Wedding*
  3. *Royal Traditional Wedding*
  4. *Luxury Evening Wedding*
  5. *Beachside Wedding*
  6. *Rustic Countryside Wedding*
  7. *Pastel Birthday Celebration*
  8. *Luxury Evening Birthday*
  9. *Outdoor Garden Birthday*
  10. *Romantic Candlelight Engagement*
  11. *Golden Anniversary Celebration*
  12. *Eco-Friendly Community Festival*

### 3. Panoramic Theme Details Modal
- **Top Full-Width Venue Banner**: Atmospheric venue image with location styling caption.
- **Two-Column Planning Blueprint**:
  - **Left Column**: Atmosphere & Character, **Curated Color Palette** (circular swatches with click-to-copy hex functionality and zero I-beam caret bugs), Decoration Suggestions, Lighting & Illumination Concepts, Venue Recommendations.
  - **Right Column**: Theme Specifications (Guest Capacity, Estimated Budget Range), Invitation Style & Typography, Food & Catering Style, Illustrative Budget Allocation, Practical Planning Tips.
- **Prominent Champagne-Gold Action**: *"Use This Theme →"* pre-loads the theme into the event planner form with an active theme banner.

### 4. Personalized Editorial Ideas
- Horizontal cards featuring concept imagery, guest capacity, illustrative budget tiers, mini color swatches, and dual actions (**Explore Idea** moodboard and **Apply to Planner**).

### 5. Interactive Event Planner & Dynamic Budget Engine
- Configure event type, title, guest count, target date, venue preference, and custom budget.
- Automatic breakdown calculation across Venue (35%), Catering (30%), Decor (15%), Photo/Video (12%), and Entertainment/Staff (8%).
- Save events directly into the user's planner with persistent session tracking.

### 6. Vendor Directory & Demo Authentication
- Curated directory of florists, event stylists, caterers, and photographers with instant contact inquiry dialogs.
- Demo authentication sandbox with clear security notices, password toggle, client-side validation, and SHA-256 password hashing.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.9+, FastAPI, Pydantic, Starlette, Uvicorn (ASGI)
- **Frontend**: HTML5, Tailwind CSS (via CDN), Google Fonts (*Cinzel* & *Plus Jakarta Sans*), Lucide Icons, Modular Vanilla JavaScript (`app.js`, `auth.js`, `data.js`)
- **Deployment & Server**: Uvicorn, Procfile, Environment Variable Configuration

---

## 💻 Local Development Setup

### 1. Prerequisites
- Python 3.9 or higher installed on your machine.
- Git installed.

### 2. Clone the Repository
```bash
git clone https://github.com/jathika-m/prompt-challenges.git
cd prompt-challenges
```

### 3. Create and Activate a Virtual Environment
```bash
# On Linux / macOS:
python3 -m venv venv
source venv/bin/activate

# On Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Start the Application
Run using the designated entry point:
```bash
python run.py
```
Or directly with Uvicorn:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The application is now accessible at: **`http://localhost:8000`**

### Demo Login Credentials
- **Email**: `alexa.celebrate@example.com`
- **Password**: `CelebrAI2026!`
*(Or click the "One-Click Instant Demo Login" button on the login screen).*

---

## ⚙️ Environment Variables

The application can be configured via environment variables:

| Variable | Default | Description |
| :--- | :--- | :--- |
| `PORT` | `8000` | Port on which the web server listens (automatically injected by cloud hosts). |
| `HOST` | `0.0.0.0` | Host interface address. |
| `ENV` | `production` | Environment mode (`development` or `production`). |
| `ALLOWED_ORIGINS` | `*` | Comma-separated list of allowed CORS origins or `*` for all. |
| `RELOAD` | `false` | Enable/disable auto-reload (`true` for local development). |

---

## ☁️ Public Cloud Deployment Guide

This project is packaged and production-ready for deployment on **Render**, **Railway**, or any ASGI/Docker hosting provider.

### Recommended Platform: Render (Free Tier)
Render provides native Python web service support, free HTTPS, zero configuration, and continuous deployment directly from your public GitHub repository.

#### Step-by-Step Instructions:
1. **Push your code to GitHub**:
   Ensure all changes are pushed to your repository:
   ```bash
   git add .
   git commit -m "Prepare CelebrAI for public deployment"
   git push origin main
   ```
2. **Sign up / Log in to [Render](https://render.com/)**:
   Sign in using your GitHub account.
3. **Create a New Web Service**:
   - In the Render Dashboard, click **New +** and select **Web Service**.
   - Select **Build and deploy from a Git repository**.
   - Connect your GitHub repository: `jathika-m/prompt-challenges`.
4. **Configure Service Settings**:
   - **Name**: `celebr-ai` (or your preferred name)
   - **Region**: Choose the closest region (e.g., Oregon / Frankfurt / Singapore)
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python run.py` (or `uvicorn app.main:app --host 0.0.0.0 --port $PORT`)
   - **Instance Type**: Select **Free**
5. **Click "Create Web Service"**:
   - Render will build the container, install dependencies, and start CelebrAI.
   - Once deployed, your public URL will be visible at the top (e.g., `https://celebr-ai.onrender.com`).
6. **Verify Health**:
   Visit `https://<your-render-url>/health` to verify `{"status": "healthy"}`.

#### Free-Tier Characteristics & Limitations:
- **Spin-Down on Inactivity**: Free web services spin down after 15 minutes of inactivity. The first request after sleep may take 30–50 seconds to wake up the server.
- **In-Memory Storage**: The application uses an in-memory database for demo sandbox sessions and events. Any newly added events will reset to initial seed events when the server restarts.
- **Outbound Bandwidth**: Free tier includes 100 GB/month, which is generous for evaluation and demo submissions.

---

## 🧪 Testing & Verification

Run the automated test suites to verify functionality:

```bash
# 1. Run the Production Deployment Verification Suite (16 checks)
python test_deployment.py

# 2. Run the Themes Redesign Verification Suite (8 checks)
python test_themes_redesign.py
```

All 24 test assertions verify:
- Health check and static asset delivery
- 5 categories and 12 curated themes with 2-column detailed data
- Personalized editorial ideas and vendor directory
- Demo authentication and password hashing security
- Event creation, theme attachment, budget calculation, and deletion
- Error handling (400, 401, 404) and CORS compliance
