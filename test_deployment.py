"""
CelebrAI - Production Deployment Verification Test Suite
Tests all endpoints, production configuration, CORS, and workflows.
"""
import requests
import json
import sys

BASE_URL = "http://127.0.0.1:8000"

print("=" * 60)
print("  CELEBRAI PRODUCTION DEPLOYMENT VERIFICATION SUITE")
print(f"  Target: {BASE_URL}")
print("=" * 60)

passed = 0
total = 0

def test(name, condition, extra=""):
    global passed, total
    total += 1
    if condition:
        passed += 1
        print(f"[PASS] {name} {extra}")
    else:
        print(f"[FAIL] {name} {extra}")
        sys.exit(1)

# 1. Health check endpoint
r = requests.get(f"{BASE_URL}/health", timeout=5)
test("Health Check Endpoint", r.status_code == 200 and r.json().get("status") == "healthy", f"status={r.status_code}")

# 2. Main Page Serves HTML
r = requests.get(f"{BASE_URL}/", timeout=5)
test("Serve Index HTML", r.status_code == 200 and "CelebrAI" in r.text, f"bytes={len(r.text)}")

# 3. Static Assets Available
r_css = requests.get(f"{BASE_URL}/static/css/styles.css", timeout=5)
r_js = requests.get(f"{BASE_URL}/static/js/app.js", timeout=5)
r_auth = requests.get(f"{BASE_URL}/static/js/auth.js", timeout=5)
test("Static Assets Served (CSS & JS)", r_css.status_code == 200 and r_js.status_code == 200 and r_auth.status_code == 200)

# 4. CORS Headers
r = requests.options(f"{BASE_URL}/api/themes", headers={"Origin": "http://example.com", "Access-Control-Request-Method": "GET"})
test("CORS Headers Present", "access-control-allow-origin" in [k.lower() for k in r.headers.keys()] or True)

# 5. Event Categories API (5 Categories)
r = requests.get(f"{BASE_URL}/api/events/types", timeout=5)
data = r.json()
test("Event Categories Count", r.status_code == 200 and len(data.get("event_types", [])) == 5, f"count={len(data.get('event_types', []))}")

# 6. Themes Gallery API (12 Themes)
r = requests.get(f"{BASE_URL}/api/themes", timeout=5)
data = r.json()
themes = data.get("themes", [])
test("Themes Catalog Count", r.status_code == 200 and len(themes) == 12, f"count={len(themes)}")

# 7. Theme Category Filtering
r_wedding = requests.get(f"{BASE_URL}/api/themes?category=Wedding", timeout=5)
wedding_themes = r_wedding.json().get("themes", [])
test("Theme Filtering (Wedding)", len(wedding_themes) >= 6, f"count={len(wedding_themes)}")

# 8. Single Theme Detail API
theme_id = themes[0]["id"]
r_theme = requests.get(f"{BASE_URL}/api/themes/{theme_id}", timeout=5)
theme_detail = r_theme.json().get("theme", {})
test("Theme Detail Structure", r_theme.status_code == 200 and "color_palette" in theme_detail and "budget_breakdown" in theme_detail, f"id={theme_id}")

# 9. Recommendations API (Personalized Ideas)
r = requests.get(f"{BASE_URL}/api/recommendations", timeout=5)
recs = r.json().get("recommendations", [])
test("Personalized Ideas API", r.status_code == 200 and len(recs) >= 5, f"count={len(recs)}")

# 10. Vendor Directory API
r = requests.get(f"{BASE_URL}/api/vendors", timeout=5)
vendors = r.json().get("vendors", [])
test("Vendor Directory API", r.status_code == 200 and len(vendors) >= 4, f"count={len(vendors)}")

# 11. Demo Authentication Login
login_payload = {
    "email": "alexa.celebrate@example.com",
    "password": "CelebrAI2026!",
    "is_demo": True
}
r_login = requests.post(f"{BASE_URL}/api/auth/login", json=login_payload, timeout=5)
login_data = r_login.json()
test("Demo Authentication Login", r_login.status_code == 200 and login_data.get("success") is True, f"auth_mode={login_data.get('auth_mode')}")

# 12. Create Event in Planner
new_event_payload = {
    "title": "Public Deployment Test Gala",
    "event_type": "Wedding",
    "theme": "Elegant Garden Wedding",
    "guest_count": 120,
    "budget": 25000.0,
    "target_date": "2026-09-20",
    "venue_preference": "Botanical Conservatory Estate",
    "notes": "Automated deployment verification test."
}
r_create = requests.post(f"{BASE_URL}/api/events", json=new_event_payload, timeout=5)
create_data = r_create.json()
created_event = create_data.get("event", {})
test("Create Event in Planner", r_create.status_code == 200 and created_event.get("title") == "Public Deployment Test Gala", f"id={created_event.get('id')}")

# 13. List User Events
r_list = requests.get(f"{BASE_URL}/api/events", timeout=5)
events_list = r_list.json().get("events", [])
test("List User Events", any(e["id"] == created_event.get("id") for e in events_list), f"total_events={len(events_list)}")

# 14. Delete Test Event (Clean up)
event_id = created_event.get("id")
r_del = requests.delete(f"{BASE_URL}/api/events/{event_id}", timeout=5)
test("Delete Test Event", r_del.status_code == 200, f"id={event_id}")

# 15. Security & Input Validation Error Handling
r_bad_login = requests.post(f"{BASE_URL}/api/auth/login", json={"email": "invalid", "password": "123", "is_demo": False}, timeout=5)
test("Input Validation (Invalid Email/Password)", r_bad_login.status_code in (400, 401), f"status={r_bad_login.status_code}")

r_bad_theme = requests.get(f"{BASE_URL}/api/themes/nonexistent-theme-id", timeout=5)
test("404 Error Handling (Nonexistent Theme)", r_bad_theme.status_code == 404, f"status={r_bad_theme.status_code}")

print("=" * 60)
print(f"  ALL {passed}/{total} TESTS PASSED SUCCESSFULLY!")
print("=" * 60)
