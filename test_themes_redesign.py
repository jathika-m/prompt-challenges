import requests
import sys

base = 'http://127.0.0.1:8000'

print("--- CELEBRAI THEMES REDESIGN TEST SUITE ---")

# 1. Test Index
r = requests.get(base + '/')
assert r.status_code == 200, f"Index failed: {r.status_code}"
assert "Discover Themes" in r.text, "Gallery heading missing"
assert "Find the perfect atmosphere for your next unforgettable celebration." in r.text, "Subtitle missing"
assert "gallery-filter-all" in r.text, "Category filter missing"
assert "planner-selected-theme-banner" in r.text, "Selected theme banner container missing"
print("[OK] Test 1: Index HTML contains redesigned gallery structure, subtitle, filters, and planner banner.")

# 2. Test All 12 Themes API
r = requests.get(base + '/api/themes')
assert r.status_code == 200
themes = r.json()['themes']
assert len(themes) >= 12, f"Expected at least 12 themes, found {len(themes)}"
print(f"[OK] Test 2: Successfully retrieved {len(themes)} themes from backend.")

# 3. Check for the exact 12 required themes
required_themes = [
    # Wedding
    "Elegant Garden Wedding",
    "Minimalist Modern Wedding",
    "Royal Traditional Wedding",
    "Luxury Evening Wedding",
    "Beachside Wedding",
    "Rustic Countryside Wedding",
    # Birthday
    "Pastel Birthday Celebration",
    "Luxury Evening Birthday",
    "Outdoor Garden Birthday",
    # Engagement and Anniversary
    "Romantic Candlelight Engagement",
    "Golden Anniversary Celebration",
    # Community Event
    "Eco-Friendly Community Festival"
]

found_names = [t['name'] for t in themes]
for name in required_themes:
    assert name in found_names, f"Missing required theme: '{name}'"
    print(f"   * Verified theme: {name}")
print("[OK] Test 3: All 12 required themes are present.")

# 4. Check category filtering for every category
categories = ["Wedding", "Birthday", "Engagement", "Anniversary", "Community Event"]
for cat in categories:
    r = requests.get(base + f'/api/themes?category={cat}')
    assert r.status_code == 200
    cat_themes = r.json()['themes']
    assert len(cat_themes) >= 1, f"No themes returned for category {cat}"
    print(f"[OK] Test 4: Category '{cat}' filter returned {len(cat_themes)} themes.")

# 5. Check detailed structure of theme models
test_theme_ids = [
    "elegant-garden-wedding",
    "beachside-wedding",
    "luxury-evening-birthday",
    "romantic-candlelight-engagement"
]

for tid in test_theme_ids:
    r = requests.get(base + f'/api/themes/{tid}')
    assert r.status_code == 200
    t = r.json()['theme']
    
    assert 'tagline' in t and len(t['tagline']) > 5, f"Tagline missing for {tid}"
    assert 'atmosphere_style' in t and len(t['atmosphere_style']) > 3, f"Atmosphere missing for {tid}"
    assert 'color_palette' in t and len(t['color_palette']) >= 3, f"Palette insufficient for {tid}"
    assert 'decoration_suggestions' in t and len(t['decoration_suggestions']) >= 3, f"Decor missing for {tid}"
    assert 'lighting_ideas' in t and len(t['lighting_ideas']) >= 3, f"Lighting missing for {tid}"
    assert 'venue_recommendations' in t and len(t['venue_recommendations']) >= 2, f"Venues missing for {tid}"
    assert 'invitation_style' in t and len(t['invitation_style']) > 10, f"Invitations missing for {tid}"
    assert 'catering_considerations' in t and len(t['catering_considerations']) >= 2, f"Catering missing for {tid}"
    assert 'budget_range' in t and "Illustrative" in t['budget_range'], f"Illustrative budget missing for {tid}"
    assert 'budget_breakdown' in t and len(t['budget_breakdown']) >= 4, f"Budget breakdown missing for {tid}"
    assert 'guest_count_range' in t, f"Guests missing for {tid}"
    assert 'planning_tips' in t and len(t['planning_tips']) >= 2, f"Tips missing for {tid}"
    assert 'image' in t and t['image'].startswith('http'), f"Image missing for {tid}"
    print(f"[OK] Test 5: Theme '{t['name']}' has complete 2-column detailed data structure.")

# 6. Test Personalized Recommendations
r = requests.get(base + '/api/recommendations')
assert r.status_code == 200
recs = r.json()['recommendations']
assert len(recs) >= 5
for rec in recs:
    assert 'theme_match' in rec, f"Theme match missing on {rec['title']}"
    assert 'color_palette' in rec, f"Color palette missing on {rec['title']}"
    assert 'budget_split' in rec, f"Budget split missing on {rec['title']}"
print(f"[OK] Test 6: Personalized Ideas contains {len(recs)} enriched concepts with theme matching.")

# 7. Test Creating an event with a selected theme
new_evt = {
    "title": "Katherine & Julian Garden Gala",
    "event_type": "Wedding",
    "theme": "Elegant Garden Wedding",
    "guest_count": 140,
    "budget": 32000,
    "target_date": "2026-09-18",
    "venue_preference": "Botanical Conservatory Estate",
    "notes": "Champagne lawn reception with wisteria canopy and harpist."
}
r = requests.post(base + '/api/events', json=new_evt)
assert r.status_code == 200, f"Event creation failed: {r.status_code}"
evt_data = r.json()['event']
evt_id = evt_data['id']
assert evt_data['theme'] == "Elegant Garden Wedding"
print(f"[OK] Test 7: Successfully created event with selected theme '{evt_data['theme']}'.")

# Clean up
r = requests.delete(base + f'/api/events/{evt_id}')
assert r.status_code == 200
print("[OK] Test 8: Successfully cleaned up test event.")

print("\nALL 8 TESTS PASSED SUCCESSFULLY! THEMES REDESIGN VERIFIED.")
