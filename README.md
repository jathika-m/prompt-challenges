# CelebrAI — Your Personal AI Event Planner
## Premium Themes Gallery & Interactive Theme Details Redesign

A luxury web application for planning **Weddings, Birthdays, Engagement Ceremonies, Anniversaries, and Community Events**, running live on `http://127.0.0.1:8000`.

---

## 🌟 Key Features & Redesign Highlights

### 1. Discover Themes & Inspiration Gallery (Redesigned)
- **Title**: *"Discover Themes & Inspiration"*
- **Subtitle**: *"Find the perfect atmosphere for your next unforgettable celebration."*
- **4-Column Responsive Layout**:
  - **Large Desktops**: 4 cards per row (`grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6`).
  - **Tablets**: 2 cards per row (`sm:grid-cols-2`).
  - **Mobile Phones**: 1 card per row (`grid-cols-1`).
  - Consistent card heights and aligned dual action buttons.
- **Realistic Event Venue Photography**:
  - High-resolution landscape photography (~16:10 ratio) featuring authentic venue locations: botanical gardens, grand banquet ballrooms, heritage palaces, oceanfront beach aisles, restored countryside barns, and rooftop penthouses (*no cake images*).
  - Subtle zoom on card hover (`group-hover:scale-105 transition-transform duration-500`).
  - Integrated JavaScript SVG fallback handler (`window.handleImageError`) preventing any broken image containers.
- **Instant Category Filter Pills**:
  - `All | Wedding | Birthday | Engagement | Anniversary | Community Event`
  - Updates cards immediately in real-time without reloading the page.

### 2. 12 Curated Luxury Themes
1. **Wedding**:
   - **Elegant Garden Wedding**: Cascading rose arches, washed linen tables, and sunlit lawn terraces.
   - **Minimalist Modern Wedding**: Clean architectural lines, monochromatic calla lilies, and pure negative space.
   - **Royal Traditional Wedding**: Heritage palace grandeur with crimson velvets, hand-carved gold jali screens, and crystal chandeliers.
   - **Luxury Evening Wedding**: Black-tie gala drama with high-sheen mirror tables, crystal candelabras, and champagne towers.
   - **Beachside Wedding**: Coastal romance with driftwood arches, billowy linen drapery, and oceanside banquets.
   - **Rustic Countryside Wedding**: Restored heritage barn, exposed timber beams, wildflower runners, and bluegrass warmth.
2. **Birthday**:
   - **Pastel Birthday Celebration**: Confectionery tones with organic balloon clouds, fluted pedestals, and cursive neon signs.
   - **Luxury Evening Birthday**: High-energy rooftop penthouse with illuminated VIP lounge cabanas, live DJ, and cocktail towers.
   - **Outdoor Garden Birthday**: Sun-drenched garden patio with bistro seating, acoustic guitar, and artisan Mediterranean grazing.
3. **Engagement & Anniversary**:
   - **Romantic Candlelight Engagement**: Enchanting terrace with 200+ hurricane candles, rose petal carpets, and acoustic cello.
   - **Golden Anniversary Celebration**: Gilded splendor with gold-rimmed crystal, nostalgic photo galleries, and swing jazz.
4. **Community Event**:
   - **Eco-Friendly Community Festival**: Planet-positive festival with living herb centerpieces, solar-powered acoustic stage, and zero-waste dining.

---

### 3. Redesigned Two-Column Interactive Theme Details Modal
Clicking either the venue photograph or **"View Details"** opens an editorial modal:
- **Sticky Header**: Theme name (editorial serif heading), event category badge, short theme tagline, and close button.
- **Left Column**:
  - Large landscape venue photograph with location caption.
  - Atmosphere & Style tags.
  - Comprehensive theme overview.
  - Financial & Guest Scope card (guest range, illustrative budget range).
  - Interactive Colour Palette card with color names, HEX codes, and visual swatches.
  - Guest capacity and comfort notes.
- **Right Column**:
  - **Decoration Suggestions**: Floral arrangements, entrance, table styling, stage/focal-point design, backdrops.
  - **Lighting Ideas**: Fairy lights, chandeliers, lanterns, candlelight, ambient lighting.
  - **Venue Recommendations**: Tailored venue types appropriate to the theme.
  - **Invitation Style**: Digital/print specifications, typography, color motifs.
  - **Food & Catering**: Menu styles, veg/non-veg selections, dietary accommodations, service format.
  - **Estimated Budget Breakdown**: Illustrative allocations for Venue (35%), Catering (30%), Decor (15%), Photo (12%), Entertainment (8%).
  - **Practical Planning Tips**: Weather contingencies, booking priorities, seasonal floral availability, accessibility.
- **Prominent Champagne-Gold Action**:
  - Wide **"Use This Theme →"** button at the sticky footer.
  - Carries theme name, category, and color palette into the planner.
  - Displays the active theme banner in the planner and updates budget forecasts.

---

### 4. Enhanced "Ideas You'll Love" Section
- Personalized inspiration cards featuring concept image, title, category, short description, illustrative budget, suggested guest count, color swatches.
- Dual action buttons:
  - **"Explore Idea"**: Opens a detailed moodboard modal with highlights, venue style, color palette, and illustrative budget split.
  - **"Apply to Planner"**: One-click application of the concept (title, event type, budget, guest count) directly into the planner.
- Honest labeling: *Curated Editorial Recommendations (GenAI Integration Ready)*.

---

## 🚀 Running the Application

The server is running on:
👉 **`http://127.0.0.1:8000`**

To launch manually:
```powershell
python run.py
```
Or with Uvicorn:
```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### Demo Credentials
- **Email**: `alexa.celebrate@example.com`
- **Password**: `CelebrAI2026!`
*(Or click the "One-Click Instant Demo Login" button on the login screen).*
