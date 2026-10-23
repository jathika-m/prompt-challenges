"""
CelebrAI - Event Planner Data Models and Seed Data
Comprehensive catalog including 12 curated themes, realistic venue photography, and personalized ideas.
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: str
    email: str
    name: str
    avatar: str
    role: str = "Event Host"
    is_demo: bool = True

class LoginRequest(BaseModel):
    email: str
    password: str
    is_demo: bool = False

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

class ForgotPasswordRequest(BaseModel):
    email: str

class EventPlan(BaseModel):
    id: Optional[str] = None
    title: str
    event_type: str
    theme: Optional[str] = None
    guest_count: int
    budget: float
    target_date: str
    venue_preference: str = "Indoor Ballroom"
    notes: Optional[str] = ""
    status: str = "Planning"
    created_at: Optional[str] = None

# Curated event categories
EVENT_TYPES = [
    {
        "id": "wedding",
        "title": "Wedding",
        "badge": "Grand Romance",
        "tagline": "Timeless Elegance & Sacred Moments",
        "description": "Bespoke vows, floral arches, enchanting dinners, and curated rituals tailored to your unique love story.",
        "image": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80",
        "popular_themes": [
            "Elegant Garden Wedding",
            "Minimalist Modern Wedding",
            "Royal Traditional Wedding",
            "Luxury Evening Wedding",
            "Beachside Wedding",
            "Rustic Countryside Wedding"
        ],
        "avg_guest_range": "100 - 350 guests",
        "icon": "heart"
    },
    {
        "id": "birthday",
        "title": "Birthday",
        "badge": "Milestone Cheer",
        "tagline": "Joyful Themes & Vibrant Gatherings",
        "description": "Sophisticated milestone gatherings, illuminated lounges, interactive culinary stations, and unforgettable nightlife.",
        "image": "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?auto=format&fit=crop&w=1200&q=80",
        "popular_themes": [
            "Pastel Birthday Celebration",
            "Luxury Evening Birthday",
            "Outdoor Garden Birthday"
        ],
        "avg_guest_range": "30 - 120 guests",
        "icon": "sparkles"
    },
    {
        "id": "engagement",
        "title": "Engagement",
        "badge": "Chapter One",
        "tagline": "Champagne Toasts & Golden Hours",
        "description": "Candlelit terraces, romantic string quartets, bespoke cocktail hours, and intimate celebrations with cherished ones.",
        "image": "https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?auto=format&fit=crop&w=1200&q=80",
        "popular_themes": [
            "Romantic Candlelight Engagement",
            "Elegant Garden Wedding",
            "Luxury Evening Wedding"
        ],
        "avg_guest_range": "40 - 150 guests",
        "icon": "gem"
    },
    {
        "id": "anniversary",
        "title": "Anniversary",
        "badge": "Enduring Love",
        "tagline": "Golden Milestones & Sweet Memories",
        "description": "Celebrate years of shared devotion with exquisite tablescapes, vintage wines, heartfelt speeches, and private live music.",
        "image": "https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=1200&q=80",
        "popular_themes": [
            "Golden Anniversary Celebration",
            "Luxury Evening Wedding",
            "Minimalist Modern Wedding"
        ],
        "avg_guest_range": "25 - 100 guests",
        "icon": "flame"
    },
    {
        "id": "community",
        "title": "Community Event",
        "badge": "Shared Spirit",
        "tagline": "Gatherings That Inspire & Connect",
        "description": "Fundraising galas, cultural festivals, eco-summits, and neighborhood reunions brought to life with communal harmony.",
        "image": "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=1200&q=80",
        "popular_themes": [
            "Eco-Friendly Community Festival",
            "Outdoor Garden Birthday",
            "Rustic Countryside Wedding"
        ],
        "avg_guest_range": "80 - 500+ guests",
        "icon": "users"
    }
]

# 12 Curated Themes Detailed Catalog
THEMES = [
    # ---------------- 1. Elegant Garden Wedding ----------------
    {
        "id": "elegant-garden-wedding",
        "name": "Elegant Garden Wedding",
        "category": "Wedding",
        "tagline": "Lush botanical romance enveloped in fragrant floral archways and golden afternoon sunlight.",
        "atmosphere_style": "Botanical Romance, Ethereal, Soft Naturalism",
        "suitable_events": ["Wedding", "Engagement", "Anniversary"],
        "image": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Botanical grandeur with cascading rose archways, natural linen tablescapes, and sunlit lawn terraces.",
        "overview": "The Elegant Garden Wedding theme captures the timeless allure of an English estate or Mediterranean botanical sanctuary. It emphasizes organic textures, lush seasonal florals, antique gold hardware, and fluid transitions between golden afternoon sunlight and enchanted twilight illuminations.",
        "color_palette": [
            {"name": "Sage Green", "hex": "#7A8F7A"},
            {"name": "Warm Ivory", "hex": "#FAF6EE"},
            {"name": "Blush Rose", "hex": "#E8B4B8"},
            {"name": "Champagne Gold", "hex": "#D4AF37"},
            {"name": "Soft Olive", "hex": "#556B2F"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Cascading English garden roses, blush ranunculus, eucalyptus, and wisteria garlands.",
            "Entrance: Curved wrought-iron archway draped in climbing greenery and white floral boughs.",
            "Table Styling: Raw washed-linen tablecloths with distressed oak crossback chairs and cut-crystal glassware.",
            "Stage & Focal Point: Circular open botanical gazebo framing ceremony vows with natural grass carpet.",
            "Backdrops & Props: Botanical press-flower signage, brass urns, and vintage French champagne carts."
        ],
        "lighting_ideas": [
            "Fairy Lights: Cascading warm 2400K micro-fairy canopies woven directly into mature weeping trees.",
            "Chandeliers: Antique brass crystal chandeliers suspended safely from sturdy oak tree branches.",
            "Lanterns: Patinated brass hurricane lanterns lining the ceremony aisle and stone walkways.",
            "Candlelight: Glass-enclosed pillar candles of staggered heights along dining table centerpieces.",
            "Ambient Lighting: Soft amber uplighting washing stone manor walls as dusk descends."
        ],
        "venue_recommendations": [
            "Private vineyard manor with panoramic lawn terraces.",
            "Historic botanical conservatory or glasshouse orangery.",
            "Secluded lakeside estate with mature gardens and weeping willows."
        ],
        "invitation_style": "Deckle-edge handmade cotton cardstock with pressed botanical florals, olive wax seal, blind letterpress calligraphy, and raw silk ribbon.",
        "catering_considerations": [
            "Menu Style: Seasonal farm-to-table grazing tables and four-course plated garden supper.",
            "Dietary Accommodations: Dedicated heirloom vegetable tasting courses alongside grass-fed lamb and seabass.",
            "Service Format: Butler-passed botanical hors d'oeuvres during cocktail hour followed by seated fine dining.",
            "Beverages: Craft gin mixology bar featuring elderflower, cucumber ribbons, and edible violas."
        ],
        "budget_range": "$18,000 – $38,000 (Illustrative estimate)",
        "budget_breakdown": {
            "Venue & Grounds": "34%",
            "Catering & Bar Service": "30%",
            "Florals & Garden Styling": "18%",
            "Photography & Cinematography": "10%",
            "Acoustic Music & Lighting": "8%"
        },
        "guest_count_range": "75 – 220 guests",
        "guest_capacity_notes": "Comfortable seating up to 220 guests with ample lawn clearances for tented weather backup and cocktail circulation.",
        "planning_tips": [
            "Always secure a high-quality clear-top marquee on standby for sudden rain or heavy sun.",
            "Provide complementary heel-protector caps in wicker baskets for guests walking on soft turf.",
            "Schedule portraits 45 minutes prior to golden hour for optimal natural illumination."
        ]
    },

    # ---------------- 2. Minimalist Modern Wedding ----------------
    {
        "id": "minimalist-modern-wedding",
        "name": "Minimalist Modern Wedding",
        "category": "Wedding",
        "tagline": "Architectural clean lines, monochromatic nuance, sculptured floral artistry, and understated luxury.",
        "atmosphere_style": "Contemporary Architectural, High-Contrast Monolith, Curated Space",
        "suitable_events": ["Wedding", "Engagement", "Anniversary"],
        "image": "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Clean architectural lines, monochromatic floral sculptures, smoked acrylic, and pure negative space.",
        "overview": "Curated for design-conscious couples who appreciate spatial luxury and architectural restraint. This theme trades conventional clutter for deliberate negative space, monochromatic contrast, bespoke modern typography, and high-impact singular floral sculptures.",
        "color_palette": [
            {"name": "Charcoal Black", "hex": "#1A1A1A"},
            {"name": "Alabaster White", "hex": "#F4F4F2"},
            {"name": "Brushed Nickel", "hex": "#A8A8A8"},
            {"name": "Soft Taupe", "hex": "#C4B5A5"},
            {"name": "Champagne Accent", "hex": "#E5D3B3"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Architectural singular calla lily stems in smoked glass cylinders and bleached monstera leaves.",
            "Entrance: Matte black monolithic portal with sharp recessed LED linear glow.",
            "Table Styling: Seamless black mirror runners paired with translucent acrylic ghost chairs and matte ceramic dinnerware.",
            "Stage & Focal Point: Clean white plinth altar with asymmetric sculptural white orchid arrangement.",
            "Backdrops & Props: Steel geometric photo backdrop with laser-etched blind typography."
        ],
        "lighting_ideas": [
            "Precision Pin-Spotting: Focused 3000K spots strictly highlighting dining tables and sculptural pieces.",
            "Ambient Light Bars: Recessed linear floor lighting washing concrete and plaster architectural walls.",
            "Linear Pendants: Suspended horizontal smoked-glass light tubes at staggered heights.",
            "Candlelight: Monochromatic black taper candles in weighted gunmetal candle holders."
        ],
        "venue_recommendations": [
            "Contemporary art museum or minimalist private gallery atrium.",
            "Restored industrial loft with polished concrete floors and exposed steel frames.",
            "Modernist cantilevered glass villa overlooking city horizons."
        ],
        "invitation_style": "Heavyweight 700gsm cotton black card with embossed blind minimalist typography, translucent vellum outer jacket, and magnetic closure.",
        "catering_considerations": [
            "Menu Style: Deconstructed 5-course chef's modern tasting menu with natural wine pairings.",
            "Dietary Accommodations: Individualized plant-forward modern gastronomic tasting options.",
            "Service Format: Synchronized silver service by coordinated culinary staff.",
            "Beverages: Monogrammed crystal-clear ice cube cocktails with smoked bourbon and clarified citrus."
        ],
        "budget_range": "$24,000 – $52,000 (Illustrative estimate)",
        "budget_breakdown": {
            "Venue Loft & Art Space": "35%",
            "Gastronomic Catering & Bar": "32%",
            "Sculptural Florals & Decor": "15%",
            "Architectural Lighting & Sound": "10%",
            "Editorial Photography": "8%"
        },
        "guest_count_range": "50 – 160 guests",
        "guest_capacity_notes": "Ideal for intimate to mid-size gatherings where spatial luxury and generous negative space are prioritized.",
        "planning_tips": [
            "In minimalism, visual flaws have nowhere to hide; ensure tablecloth steaming and table spacing alignment are exact.",
            "Invest budget into fewer, monumental floral art moments rather than dispersed minor centerpieces."
        ]
    },

    # ---------------- 3. Royal Traditional Wedding ----------------
    {
        "id": "royal-traditional-wedding",
        "name": "Royal Traditional Wedding",
        "category": "Wedding",
        "tagline": "Opulent brocades, hand-forged antique gold artifacts, fragrant floral mandaps, and majestic celebration.",
        "atmosphere_style": "Imperial Opulence, Regal Heritage, Ceremonial Splendor",
        "suitable_events": ["Wedding", "Anniversary", "Community Event"],
        "image": "https://images.unsplash.com/photo-1545232979-8bf68ee9b1af?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Heritage palace grandeur with crimson velvets, hand-carved gold jali screens, and crystal chandeliers.",
        "overview": "A lavish celebration honoring cultural heritage and timeless majesty. Envision rich velvet drapes, hand-forged antique gold artifacts, fragrant marigold and royal rose mandaps, and resonant instrumental music echoing through ornate banquet halls.",
        "color_palette": [
            {"name": "Imperial Crimson", "hex": "#8B0000"},
            {"name": "Majestic Gold", "hex": "#D4AF37"},
            {"name": "Deep Emerald", "hex": "#097969"},
            {"name": "Royal Ivory", "hex": "#FFFDD0"},
            {"name": "Midnight Sapphire", "hex": "#0F2537"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Over 3,000 deep crimson Dutch roses, cascading tuberoses, and gold-dusted magnolia leaves.",
            "Entrance: Grand ceremonial archway flanked by hand-beaten brass urli vessels with floating petals and diyas.",
            "Table Styling: Brocade and velvet table coverings, heavy gold-plated charger plates, and ornate candelabras.",
            "Stage & Focal Point: Hand-carved four-pillar ceremonial mandap adorned with floral chandeliers and royal thrones.",
            "Backdrops & Props: Gilded jali latticework screens, embroidered royal bolsters, and velvet divans."
        ],
        "lighting_ideas": [
            "Chandeliers: Multi-tiered Bohemian crystal chandeliers casting prismatic amber light across the ballroom.",
            "Lanterns: Handcrafted brass Moroccan and Indian filigree lanterns framing the royal procession walkway.",
            "Candlelight: Hundreds of flickering brass diyas and enclosed hurricane lamps on stairwells.",
            "Perimeter Uplighting: Deep amber and rich magenta architectural washes accentuating heritage arches."
        ],
        "venue_recommendations": [
            "Historic palace hotel or heritage fort courtyard.",
            "Grand hotel ballroom with double-height vaulted ceilings and gold moldings.",
            "Sprawling ceremonial royal banquet estate."
        ],
        "invitation_style": "Hardcover embroidered velvet presentation box containing laser-etched gold brass plaques, scented sandalwood mist, and artisanal dry fruits.",
        "catering_considerations": [
            "Menu Style: Multi-course royal ceremonial feast featuring authentic regional royal recipes.",
            "Dietary Accommodations: Dedicated pure vegetarian royal kitchen alongside gourmet non-vegetarian delicacies.",
            "Service Format: Royal thali presentation or interactive live tandoor and artisanal bread stations.",
            "Beverages: Saffron-infused milk sherbets, rose cordial mocktails, and royal spiced chai service."
        ],
        "budget_range": "$35,000 – $90,000 (Illustrative estimate)",
        "budget_breakdown": {
            "Grand Palace Venue": "32%",
            "Royal Banquet Catering": "33%",
            "Ceremonial Mandap & Florals": "20%",
            "Cinematography & Heirloom Photo": "8%",
            "Traditional Orchestra & Lighting": "7%"
        },
        "guest_count_range": "150 – 650 guests",
        "guest_capacity_notes": "Spacious ballroom configurations designed to comfortably host multi-generational ceremonies and large processions.",
        "planning_tips": [
            "Dedicate distinct hospitality teams for ceremonial arrival processions and ritual transitions.",
            "Arrange dedicated quiet luxury lounges for senior family members away from high-decibel entertainment zones."
        ]
    },

    # ---------------- 4. Luxury Evening Wedding ----------------
    {
        "id": "luxury-evening-wedding",
        "name": "Luxury Evening Wedding",
        "category": "Wedding",
        "tagline": "Black-tie glamour bathed in candlelight, reflective mirror tables, and high-gloss metropolitan drama.",
        "atmosphere_style": "Midnight Gala, Sophisticated Glamour, Metropolitan Chic",
        "suitable_events": ["Wedding", "Anniversary", "Engagement"],
        "image": "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Black-tie drama with high-sheen mirror tables, crystal candelabras, champagne towers, and dusk jazz.",
        "overview": "An intoxicating blend of moody glamour and metropolitan sophistication. Designed for landmark weddings where formal black-tie attire, crystal chandelier canopies, champagne towers, and candlelit mirror tables create an indelible atmosphere of prestige.",
        "color_palette": [
            {"name": "Midnight Charcoal", "hex": "#0F172A"},
            {"name": "Metallic Gold", "hex": "#D4AF37"},
            {"name": "Smoked Glass", "hex": "#4A4E69"},
            {"name": "Pure Alabaster", "hex": "#FFFFFF"},
            {"name": "Velvet Onyx", "hex": "#000000"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Towering 5-foot crystal candelabras overflowing with white phalaenopsis orchids and black callas.",
            "Entrance: Glossy black runway flanked by mirror plinths holding oversized frosted crystal urns.",
            "Table Styling: High-sheen black mirror dining tables reflecting hundreds of flickering candles without cloths.",
            "Stage & Focal Point: Curvilinear velvet banquettes and gold-piped risers framing an elevated live orchestra.",
            "Backdrops & Props: Bespoke dark smoked mirror photo wall with cold-spark fountains for milestone toasts."
        ],
        "lighting_ideas": [
            "Chandeliers: Linear clusters of cascading crystal pendants creating an illuminated celestial canopy.",
            "Pin-Spotting: Focused warm white pin-spots illuminating floral heads and table crystal.",
            "Candlelight: Black tapers in crystal hurricane tubes paired with floating glass votives.",
            "Ambient Wash: Moody indigo and warm champagne perimeter lighting setting an intimate evening tone."
        ],
        "venue_recommendations": [
            "Rooftop penthouse with panoramic illuminated city skyline vistas.",
            "Private historic yacht club or waterfront luxury pavilion at nightfall.",
            "Bespoke museum hall or members-only modern gala ballroom."
        ],
        "invitation_style": "Midnight black ultra-heavy matte paperboard with gold gilded beveled edges, gold hot-stamped foil, and personalized wax seal.",
        "catering_considerations": [
            "Menu Style: Five-course seated silver-service gourmet banquet with premier vintage wine pairings.",
            "Dietary Accommodations: High-end bespoke options including black truffle risotto and Chilean sea bass.",
            "Service Format: White-glove synchronized banquet service with sommelier wine pours.",
            "Beverages: Champagne tower pour on arrival and midnight live espresso martini bar."
        ],
        "budget_range": "$30,000 – $75,000 (Illustrative estimate)",
        "budget_breakdown": {
            "Rooftop/Ballroom Venue": "34%",
            "Premium Catering & Bar": "34%",
            "Crystal Decor & Orchids": "16%",
            "Orchestra & Cold-Spark Effects": "9%",
            "Editorial Photography": "7%"
        },
        "guest_count_range": "60 – 250 guests",
        "guest_capacity_notes": "Comfortable seating up to 250 guests with dedicated coat check, cocktail mezzanine, and generous dance floor.",
        "planning_tips": [
            "Specify 'Formal Black Tie Optional' clearly on invitations at least 8 weeks in advance.",
            "Include private valet parking and luxury coat check attendants to ensure frictionless arrivals."
        ]
    },

    # ---------------- 5. Beachside Wedding ----------------
    {
        "id": "beachside-wedding",
        "name": "Beachside Wedding",
        "category": "Wedding",
        "tagline": "Ocean breezes, coastal linen drapery, driftwood floral arches, and sunset shoreline celebrations.",
        "atmosphere_style": "Coastal Breeze, Organic Serenity, Barefoot Luxury",
        "suitable_events": ["Wedding", "Engagement", "Anniversary"],
        "image": "https://images.unsplash.com/photo-1544078751-58fee2d8a03b?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Coastal romance with driftwood arches, billowy linen drapery, and candlelit oceanside banquets.",
        "overview": "Embrace the effortless poetry of the sea. Featuring ocean breezes, organic driftwood floral arches, soft coastal linen drapery billowing in the wind, and barefoot luxury dining right on the sand as the sun melts into the Pacific.",
        "color_palette": [
            {"name": "Ocean Azure", "hex": "#4A7C9B"},
            {"name": "Sand Dune", "hex": "#E3D5C5"},
            {"name": "Crisp White", "hex": "#FFFFFF"},
            {"name": "Sea Salt Green", "hex": "#9BB8A8"},
            {"name": "Warm Coral", "hex": "#E88D72"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: White king proteas, beach roses, sea grasses, and dried palm fronds.",
            "Entrance: Natural timber pathway laid over sand flanked by weathered rope stanchions and pampas grass.",
            "Table Styling: Bleached teak banquet tables with airy seafoam cheesecloth runners and mother-of-pearl cutlery.",
            "Stage & Focal Point: Hand-hewn driftwood archway wrapped in sheer linen and coastal blooms framing open ocean.",
            "Backdrops & Props: Woven rattan lounge cabanas, coconut water welcome station, and surfboard guestbook."
        ],
        "lighting_ideas": [
            "Festoon Lights: Low-voltage warm globe strings anchored to natural bamboo poles across the sand.",
            "Lanterns: Oversized weathered timber and glass lanterns holding thick beeswax pillar candles.",
            "Tiki & Fire: Discreet perimeter bamboo tiki torches and central sunken beach firepit for twilight.",
            "Candlelight: Hurricane glass tubes shielding candle tapers from coastal sea breezes."
        ],
        "venue_recommendations": [
            "Private beachfront resort cove with exclusive beach permit.",
            "Cliffside coastal estate with gentle stone stair access to sandy shoreline.",
            "Waterfront luxury pavilion with panoramic ocean views and breeze windows."
        ],
        "invitation_style": "Textured handmade cotton deckle-edge paper with sea-glass watercolor wash, blind-debossed wave motifs, and raw twine tie.",
        "catering_considerations": [
            "Menu Style: Coastal seafood grill, fresh ceviche raw bar, and tropical wood-fired fare.",
            "Dietary Accommodations: Abundant plant-based tropical salads, grilled hearts of palm, and fresh citrus creations.",
            "Service Format: Passed beachside canapés followed by family-style seaside dining.",
            "Beverages: Fresh young coconut water bar, passionfruit mezcal palomas, and crisp chilled rosé."
        ],
        "budget_range": "$16,000 – $42,000 (Illustrative estimate)",
        "budget_breakdown": {
            "Beach Cove & Pavilion": "32%",
            "Seafood Catering & Tiki Bar": "33%",
            "Coastal Florals & Driftwood": "18%",
            "Shoreline Sound & Lighting": "9%",
            "Documentary Photography": "8%"
        },
        "guest_count_range": "40 – 180 guests",
        "guest_capacity_notes": "Ideal for 40 to 180 guests with solid timber flooring over sand to ensure effortless walking and dancing.",
        "planning_tips": [
            "Check tide tables rigorously during ceremony scheduling to ensure high tide doesn't encroach on seating.",
            "Provide guests with a 'Shoe Valet' station featuring custom flip-flops and towels for sandy feet."
        ]
    },

    # ---------------- 6. Rustic Countryside Wedding ----------------
    {
        "id": "rustic-countryside-wedding",
        "name": "Rustic Countryside Wedding",
        "category": "Wedding",
        "tagline": "Reclaimed barn timbers, wildflower bouquets, string lights, and heartwarming countryside hospitality.",
        "atmosphere_style": "Rustic Chic, Organic Farmstead, Timeless Whimsy",
        "suitable_events": ["Wedding", "Engagement", "Anniversary"],
        "image": "https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Restored heritage barn, exposed timber beams, wildflower runners, and live bluegrass warmth.",
        "overview": "Down-to-earth elegance with soulful country warmth. Set inside a historic restored barn or under sweeping farmstead oaks, featuring exposed timber trusses, handcrafted wooden tables, seasonal wildflower centerpieces, and cozy string lights.",
        "color_palette": [
            {"name": "Warm Cedar", "hex": "#8B5A2B"},
            {"name": "Sunflower Gold", "hex": "#DAA520"},
            {"name": "Wild Moss", "hex": "#556B2F"},
            {"name": "Linen Cream", "hex": "#F5F5DC"},
            {"name": "Dusty Terracotta", "hex": "#CC4E46"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Native sunflowers, baby's breath, field lavender, chamomile, and wheat sheaves.",
            "Entrance: Whiskey barrels topped with zinc flower buckets and hand-painted reclaimed wood directional signs.",
            "Table Styling: Solid oak harvest tables left bare with burlap runners, mason jar flower clusters, and tinware.",
            "Stage & Focal Point: Natural timber pergola backdrop surrounded by hay bale seating with plaid throw blankets.",
            "Backdrops & Props: Vintage pickup truck photo booth, rustic horse trough beverage cooler, and apple crate displays."
        ],
        "lighting_ideas": [
            "String Lights: Dense overhead canopy of Edison filament bulbs strung between exposed barn rafters.",
            "Barn Lanterns: Vintage blackened tin kerosene-style electric lanterns hung from cast-iron hooks.",
            "Fairy Garlands: Delicate copper-wire fairy strings twined around weathered wood support posts.",
            "Campfire: Central outdoor stone firepit with cast iron marshmallow roasting stations."
        ],
        "venue_recommendations": [
            "Historic working farmstead with restored timber bank barn.",
            "Vineyard estate with outdoor orchard grove and rolling hills.",
            "Rustic country ranch with open-air covered cedar pavilion."
        ],
        "invitation_style": "Heavy recycled kraft paper with hand-drawn botanical illustrations, woodgrain blind deboss, and raw burlap tie.",
        "catering_considerations": [
            "Menu Style: Slow-smoked artisanal barbecue, cast-iron cornbread, and wood-fired seasonal roasts.",
            "Dietary Accommodations: Hearty roasted heirloom squash, smoked portobello steaks, and farm-stand salads.",
            "Service Format: Interactive family-style carving boards or upscale rustic buffet service.",
            "Beverages: Craft beer tasting flight station, spiked iced cider, and blackberry bourbon lemonade."
        ],
        "budget_range": "$12,000 – $32,000 (Illustrative estimate)",
        "budget_breakdown": {
            "Barn Venue & Ranch Grounds": "30%",
            "Country Feast & Barrels": "34%",
            "Wildflowers & Rustic Decor": "16%",
            "Acoustic Band & Barn Lighting": "11%",
            "Heartfelt Photography": "9%"
        },
        "guest_count_range": "60 – 240 guests",
        "guest_capacity_notes": "Comfortably accommodates up to 240 guests across main barn dining floor and outdoor lawn games area.",
        "planning_tips": [
            "Ensure the barn venue is equipped with modern climate control or industrial directional fans for summer warmth.",
            "Confirm that restrooms and power generator capacities are sufficient for full catering and music production."
        ]
    },

    # ---------------- 7. Pastel Birthday Celebration ----------------
    {
        "id": "pastel-birthday-celebration",
        "name": "Pastel Birthday Celebration",
        "category": "Birthday",
        "tagline": "Dreamy confectionery hues, organic balloon art, whimsical pedestals, and chic celebratory joy.",
        "atmosphere_style": "Whimsical Sophistication, Modern Confection, Playful Luxury",
        "suitable_events": ["Birthday", "Engagement"],
        "image": "https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Joyful pastel palettes with organic balloon clouds, fluted pedestals, and customized neon backdrops.",
        "overview": "A joyful celebration bathed in dreamy sophistication. Ideal for milestone 21st, 30th, or sweet jubilees, combining French pastel hues, fluted cylindrical display pedestals, bespoke neon phrasing, and decadent confectionery tablescapes.",
        "color_palette": [
            {"name": "Dusty Rose", "hex": "#DCAE96"},
            {"name": "French Lilac", "hex": "#C8A2C8"},
            {"name": "Soft Buttercup", "hex": "#FDFD96"},
            {"name": "Mint Whisper", "hex": "#BFFCC6"},
            {"name": "Champagne Shimmer", "hex": "#F7E7CE"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Fluffy pastel carnations, blush peonies, candy hydrangeas, and sweet peas.",
            "Entrance: Curved pastel acrylic welcome board with personalized gold vinyl typography.",
            "Table Styling: Fluted pastel cylindrical display pedestals with glass cloches and candy-striped linen runners.",
            "Stage & Focal Point: Multi-layered organic balloon cloud sculpture framing a custom glowing cursive neon quote.",
            "Backdrops & Props: Pastel arched wooden backdrop panels in gradient hues with instant photo camera station."
        ],
        "lighting_ideas": [
            "Neon Signage: Custom cursive neon statement sign ('Forever Young' or name) in soft warm white.",
            "Globe Lanterns: Diffused Japanese paper globe lanterns suspended at staggered elevations.",
            "Fairy Curtains: Sheer white drapery with embedded warm micro-LED lights behind the main photo area.",
            "Color Wash: Soft pastel lavender and peach floor wash lights brightening room corners."
        ],
        "venue_recommendations": [
            "Sunlit designer loft studio with white brick walls and natural skylights.",
            "Boutique garden cafe terrace with manicured floral hedges.",
            "Private greenhouse lounge or poolside cabana deck."
        ],
        "invitation_style": "Wavy-edge pastel die-cut cards with holographic pink foil stamping and interactive animated digital RSVP countdown.",
        "catering_considerations": [
            "Menu Style: French macaron pyramids, gourmet mini sliders, and rainbow brioche sandwiches.",
            "Dietary Accommodations: Gluten-free confectionery treats and plant-based rainbow fruit skewers.",
            "Service Format: Passed gourmet cocktail canapés and open dessert tasting station.",
            "Beverages: Violet gin fizzes, cotton-candy champagne flutes, and butterfly pea flower mocktails."
        ],
        "budget_range": "$4,000 – $13,500 (Illustrative estimate)",
        "budget_breakdown": {
            "Studio Loft Venue": "32%",
            "Canapés & Dessert Bar": "32%",
            "Balloon Art & Custom Neon": "20%",
            "Photo Booth & Instant Favors": "9%",
            "DJ & Ambient Lights": "7%"
        },
        "guest_count_range": "25 – 85 guests",
        "guest_capacity_notes": "Intimate setting optimized for 25 to 85 guests with dedicated Instagrammable photo zones.",
        "planning_tips": [
            "Coordinate balloon artist setup at least 3 hours prior to guest arrival in temperature-controlled rooms.",
            "Provide take-home custom pastel gift boxes so guests can pack curated artisanal sweets."
        ]
    },

    # ---------------- 8. Luxury Evening Birthday ----------------
    {
        "id": "luxury-evening-birthday",
        "name": "Luxury Evening Birthday",
        "category": "Birthday",
        "tagline": "Rooftop skyline vistas, craft mixology, velvet banquette lounges, and electrifying nightlife energy.",
        "atmosphere_style": "High-Gloss Nightlife, Metropolitan Penthouse, VIP Prestige",
        "suitable_events": ["Birthday", "Anniversary"],
        "image": "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?auto=format&fit=crop&w=1200&q=80",
        "short_description": "High-energy skyline rooftop with illuminated VIP lounge cabanas, live DJ, and bespoke cocktail towers.",
        "overview": "Celebrate your milestone birthday in ultra-modern VIP fashion. Overlooking glittering metropolitan city lights from a high-altitude penthouse terrace, featuring curated DJ beats, custom craft cocktail towers, and velvet lounge booths.",
        "color_palette": [
            {"name": "Obsidian Black", "hex": "#0B0F19"},
            {"name": "Electric Gold", "hex": "#FFD700"},
            {"name": "Neon Amber", "hex": "#FF7E00"},
            {"name": "Platinum Silver", "hex": "#E5E4E2"},
            {"name": "Deep Plum", "hex": "#36013F"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Modern dark calla lilies, gold-sprayed monstera leaves, and deep black roses.",
            "Entrance: Velvet ropes and brass stanchions leading to an illuminated mirrored step-and-repeat backdrop.",
            "Table Styling: Backlit onyx cocktail tables with brushed brass cocktail stirrers and smoked crystal tumblers.",
            "Stage & Focal Point: Elevated DJ booth with integrated LED video panels displaying customized milestone visuals.",
            "Backdrops & Props: Giant illuminated marquee numbers indicating the birthday age with bottle-service sparklers."
        ],
        "lighting_ideas": [
            "Moving Heads: Club-grade intelligent moving head beam lights synchronized to the DJ set.",
            "LED Neon: Custom backlit acrylic monogram sign with dynamic RGB color shift capability.",
            "Architectural Uplight: Deep amber perimeter wash framing city skyscraper terrace railings.",
            "Glow Pods: Wireless rechargeable table lamps with warm amber dimming controls."
        ],
        "venue_recommendations": [
            "Downtown penthouse rooftop terrace with 360-degree skyline views.",
            "Members-only luxury nightlife lounge with private outdoor patio.",
            "Industrial converted glass penthouse with open-air terrace."
        ],
        "invitation_style": "Black metallic card with holographic gold foil lettering and private QR code digital pass for VIP security check-in.",
        "catering_considerations": [
            "Menu Style: High-end passed bites including wagyu sliders, tuna tartare cones, and truffle bao buns.",
            "Dietary Accommodations: Dedicated vegan sushi platters and gluten-free ceviche spoons.",
            "Service Format: Continuous circulating cocktail service and late-night artisan pizza bar.",
            "Beverages: Dedicated mixologist craft bar with smoked bourbon, tequila reposado, and champagne fountains."
        ],
        "budget_range": "$8,000 – $22,000 (Illustrative estimate)",
        "budget_breakdown": {
            "Rooftop Penthouse Venue": "36%",
            "Craft Bar & Gourmet Bites": "34%",
            "Live DJ, Sound & Club Lights": "16%",
            "VIP Decor & Marquee Numbers": "8%",
            "Event Videography": "6%"
        },
        "guest_count_range": "40 – 120 guests",
        "guest_capacity_notes": "Tailored for 40 to 120 guests with distinct zones for dancing, lounge seating, and skyline viewing.",
        "planning_tips": [
            "Ensure sound permits for rooftop venues allow amplified music up to the scheduled conclusion hour.",
            "Arrange dedicated coat check and valet parking to ensure frictionless arrivals for dressed-up guests."
        ]
    },

    # ---------------- 9. Outdoor Garden Birthday ----------------
    {
        "id": "outdoor-garden-birthday",
        "name": "Outdoor Garden Birthday",
        "category": "Birthday",
        "tagline": "Sun-drenched patio pergolas, acoustic melodies, fresh sangria bars, and relaxed lawn gatherings.",
        "atmosphere_style": "Alfresco Warmth, Garden Bistro, Relaxed Conviviality",
        "suitable_events": ["Birthday", "Engagement", "Community Event"],
        "image": "https://images.unsplash.com/photo-1527529482837-4698179dc6ce?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Sun-drenched garden patio with bistro seating, acoustic guitar jams, and artisan Mediterranean grazing.",
        "overview": "An effortless open-air gathering celebrating life under leafy pergolas and warm blue skies. Features long banquet tables, layered garden linens, acoustic live music, artisanal sangria carafes, and lawn lounge corners where conversations flow into twilight.",
        "color_palette": [
            {"name": "Citrus Yellow", "hex": "#F4C430"},
            {"name": "Olive Leaf", "hex": "#6B8E23"},
            {"name": "Terracotta", "hex": "#E2725B"},
            {"name": "Warm Linen", "hex": "#FAF0E6"},
            {"name": "Sky Blue", "hex": "#87CEEB"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Potted lavender, rosemary sprigs, wild chamomile, and fresh citrus branch centerpieces.",
            "Entrance: Chalkboard easel sign draped in olive branches with woven baskets of sun hats for guests.",
            "Table Styling: Long wooden farmhouse tables with terracotta potted herb runners and hand-spun linen napkins.",
            "Stage & Focal Point: Pergola framed in climbing jasmine with an acoustic guitar lounge rug.",
            "Backdrops & Props: Vintage bicycle with floral basket photo prop, bocce ball court, and croquet lawn set."
        ],
        "lighting_ideas": [
            "Festoon Lighting: Criss-crossing cafe bulb festoons suspended between wooden posts over dining tables.",
            "Mason Jar Lanterns: Solar-charged mason jar lanterns hung from tree branches with jute twine.",
            "Candlelight: Citronella and beeswax pillar candles inside recycled glass hurricane lanterns.",
            "Pathway Lights: Solar copper stake lights guiding guests along garden paths to amenities."
        ],
        "venue_recommendations": [
            "Historic orchard or private landscaped farmhouse garden.",
            "Boutique winery patio with shady wisteria pergola.",
            "Private country club lawn pavilion."
        ],
        "invitation_style": "Illustrated botanical postcard printed on recycled linen paper with playful hand-lettering and RSVP link.",
        "catering_considerations": [
            "Menu Style: Wood-fired sourdough pizzas, fresh burrata & heirloom tomato platters, and grilled skewers.",
            "Dietary Accommodations: Abundant garden salads with edible flowers and roasted Mediterranean vegetables.",
            "Service Format: Live interactive outdoor chef stations with self-serve sangria and spritz dispensers.",
            "Beverages: White peach sangria, strawberry mint lemonade, and artisanal regional craft ales."
        ],
        "budget_range": "$5,000 – $15,000 (Illustrative estimate)",
        "budget_breakdown": {
            "Garden Patio Grounds": "30%",
            "Wood-Fired Feast & Spritz": "35%",
            "Pergola Florals & Games": "16%",
            "Acoustic Duo & Festoon Setup": "10%",
            "Outdoor Photography": "9%"
        },
        "guest_count_range": "30 – 110 guests",
        "guest_capacity_notes": "Comfortably hosts up to 110 guests with shaded pergola dining and open lawn lounge pockets.",
        "planning_tips": [
            "Have discreet insect control measures (natural lemongrass diffusers and citronella) deployed 2 hours prior.",
            "Provide cozy fleece throw blankets in wicker baskets for evening temperature drops."
        ]
    },

    # ---------------- 10. Romantic Candlelight Engagement ----------------
    {
        "id": "romantic-candlelight-engagement",
        "name": "Romantic Candlelight Engagement",
        "category": "Engagement",
        "tagline": "Hundreds of flickering candles, intimate terrace dining, rose petal carpets, and heartfelt pledges.",
        "atmosphere_style": "Intimate Romance, Velvet Twilight, Candlelit Enchantment",
        "suitable_events": ["Engagement", "Anniversary", "Wedding"],
        "image": "https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Enchanting candlelit terrace with rose petal carpets, acoustic cello duets, and champagne toasts.",
        "overview": "An exquisitely romantic setting tailored for unforgettable engagement toasts and private vows. Set against a twilight terrace glowing with hundreds of glass-enclosed hurricane candles, velvet lounge seating, acoustic string melodies, and vintage champagne pairings.",
        "color_palette": [
            {"name": "Blush Velvet", "hex": "#D19CA4"},
            {"name": "Deep Burgundy", "hex": "#800020"},
            {"name": "Warm Gold", "hex": "#D4AF37"},
            {"name": "Ivory Silk", "hex": "#FFFFF0"},
            {"name": "Smoked Glass", "hex": "#5A5D64"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Lush arrangements of garden roses, burgundy dahlias, and cascading eucalyptus.",
            "Entrance: Rose petal pathway flanked by 100+ glass pillar candles leading to the terrace overlook.",
            "Table Styling: Intimate communal tables draped in champagne silk with crystal bud vases and gold flatware.",
            "Stage & Focal Point: Circular golden archway wrapped in blush blooms framing the panoramic twilight horizon.",
            "Backdrops & Props: Custom calligraphy vow keepsake book, vintage silver champagne bucket, and framed couple memories."
        ],
        "lighting_ideas": [
            "Candlelight: Over 250 glass hurricane cylinders with varied pillar candles creating a shimmering sea of light.",
            "String Canopies: Delicate warm-white micro-twinkle fairy curtains illuminating terrace glass railings.",
            "Chandelier: Singular antique crystal chandelier suspended from custom pergola overhead.",
            "Amber Glow: Hidden 2200K warm LED strips along terrace baseboards creating a floating illusion."
        ],
        "venue_recommendations": [
            "Private cliffside terrace with panoramic ocean or valley sunset views.",
            "Historic luxury villa courtyard with stone fountain and lemon trees.",
            "Boutique hotel rooftop conservatory with private buyout access."
        ],
        "invitation_style": "Soft blush handmade cotton paper with gold calligraphy, deckle edges, burgundy silk ribbon, and wax seal stamp.",
        "catering_considerations": [
            "Menu Style: Four-course plated gourmet tasting menu with live oyster shucking and artisanal pairings.",
            "Dietary Accommodations: Delicate vegetarian truffle pasta courses and customized seafood alternatives.",
            "Service Format: Discrete synchronized silver service designed for intimate conversation flow.",
            "Beverages: Vintage champagne pour for the milestone toast and custom His & Hers crafted cocktails."
        ],
        "budget_range": "$7,500 – $18,500 (Illustrative estimate)",
        "budget_breakdown": {
            "Terrace Overlook Venue": "35%",
            "Gourmet Dining & Vintage Wine": "35%",
            "Candlelight Production & Florals": "18%",
            "Acoustic String Duo": "7%",
            "Romance Cinematography": "5%"
        },
        "guest_count_range": "20 – 75 guests",
        "guest_capacity_notes": "Designed specifically for intimate guest counts between 20 and 75 to maintain warmth and personal connection.",
        "planning_tips": [
            "Time the grand toast precisely 15 minutes before official sunset to capture optimal golden-hour twilight photography.",
            "Ensure glass hurricane sleeves are tall enough to prevent light coastal breezes from extinguishing candle flames."
        ]
    },

    # ---------------- 11. Golden Anniversary Celebration ----------------
    {
        "id": "golden-anniversary-celebration",
        "name": "Golden Anniversary Celebration",
        "category": "Anniversary",
        "tagline": "Commemorating decades of devotion with gilded accents, vintage fine dining, and nostalgic memory galleries.",
        "atmosphere_style": "Golden Elegance, Timeless Devotion, Heirloom Prestige",
        "suitable_events": ["Anniversary", "Wedding", "Birthday"],
        "image": "https://images.unsplash.com/photo-1520854221256-17451cc331bf?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Gilded splendor with gold-rimmed crystal, nostalgic photo galleries, vintage champagne, and jazz.",
        "overview": "Honor decades of shared love and family legacy with unmatched refinement. Featuring gold-leaf gilded table accents, vintage crystal chandeliers, five-course nostalgic family dining, a curated archival photo walkway, and classical live swing jazz.",
        "color_palette": [
            {"name": "24K Gold", "hex": "#FFD700"},
            {"name": "Warm Champagne", "hex": "#F7E7CE"},
            {"name": "Noble Navy", "hex": "#000080"},
            {"name": "Pure Alabaster", "hex": "#FEFEFA"},
            {"name": "Antique Bronze", "hex": "#8C7853"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Golden roses, white calla lilies, and champagne orchids dusted with subtle gold shimmer.",
            "Entrance: 'Memory Lane' gallery walkway showcasing framed family photos across the decades with brass picture lights.",
            "Table Styling: Gold-embroidered damask linens, 24K gold-rimmed bone china, and cut-crystal vintage stemware.",
            "Stage & Focal Point: Gilded floral arch framing the renewal of vows ceremony and anniversary toast riser.",
            "Backdrops & Props: Audio guestbook phone booth for recording heartfelt family memories and leather-bound album."
        ],
        "lighting_ideas": [
            "Chandeliers: Dimmable gold brass and crystal chandeliers creating a radiant, nostalgic ballroom glow.",
            "Pin-Spotting: Delicate spots illuminating individual centerpieces and the archival photo walkway.",
            "Warm Candlelight: Heavy gold candelabras with ivory taper candles along banquet tables.",
            "Projection: High-definition subtle projector screen for a surprise retro family memory film reel."
        ],
        "venue_recommendations": [
            "Historic manor dining salon with hardwood wainscoting and stone fireplace.",
            "Private country estate banquet hall with sweeping lawn vistas.",
            "Luxury boutique hotel ballroom with intimate private salon."
        ],
        "invitation_style": "Heavyweight ivory cotton cardstock with embossed gold foil anniversary crest, gold gilded beveled edges, and wax seal.",
        "catering_considerations": [
            "Menu Style: Five-course gourmet banquet featuring modern reinterpretations of the couple's original wedding menu.",
            "Dietary Accommodations: Careful dietary tailoring for multi-generational guests from children to seniors.",
            "Service Format: Traditional white-glove silver service with dedicated table sommeliers.",
            "Beverages: Vintage reserves of the anniversary year, classic martinis, and artisanal digestifs."
        ],
        "budget_range": "$12,000 – $28,000 (Illustrative estimate)",
        "budget_breakdown": {
            "Historic Manor Salon": "32%",
            "Five-Course Gourmet Banquet": "36%",
            "Gold Florals & Table Settings": "16%",
            "Live Swing Jazz Ensemble": "9%",
            "Heirloom Photography & Album": "7%"
        },
        "guest_count_range": "35 – 130 guests",
        "guest_capacity_notes": "Comfortably seats up to 130 guests with spacious table distances facilitating comfortable movement for all generations.",
        "planning_tips": [
            "Curate a 7-minute family video tribute early and test audiovisual projection acoustics in advance.",
            "Provide accessible seating, ramps, and nearby parking for senior relatives attending the milestone."
        ]
    },

    # ---------------- 12. Eco-Friendly Community Festival ----------------
    {
        "id": "eco-friendly-community-festival",
        "name": "Eco-Friendly Community Festival",
        "category": "Community Event",
        "tagline": "Zero-waste sustainability, local farm harvests, solar-powered melodies, and vibrant communal spirit.",
        "atmosphere_style": "Sustainable Harmony, Community Spirit, Earthy Vitality",
        "suitable_events": ["Community Event", "Birthday", "Anniversary"],
        "image": "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=1200&q=80",
        "short_description": "Planet-positive festival with living herb centerpieces, solar-powered acoustic stage, and zero-waste dining.",
        "overview": "A heart-centered celebration prioritizing planet-positive ethics without compromising on aesthetic joy. Featuring potted living plant centerpieces that guests take home to plant, zero single-use plastics, compostable table settings, solar illuminations, and community engagement.",
        "color_palette": [
            {"name": "Forest Moss", "hex": "#2E5A36"},
            {"name": "Terracotta Earth", "hex": "#C86D51"},
            {"name": "Natural Linen", "hex": "#E3DAC9"},
            {"name": "Oatmeal Kraft", "hex": "#D1C7BD"},
            {"name": "Sky Blue Accent", "hex": "#7BA7BC"}
        ],
        "decoration_suggestions": [
            "Floral Arrangements: Living potted rosemary, lavender, and olive tree centerpieces in clay pots (take-home gifts).",
            "Entrance: Reclaimed timber arbor decorated with hanging macramé planters and chalkboard community map.",
            "Table Styling: Upcycled natural timber benches, reclaimed wood bars, and hand-spun unbleached linen runners.",
            "Stage & Focal Point: Pallet-wood amphitheater stage with living fern and ivy acoustic backdrop wall.",
            "Backdrops & Props: Seedling exchange booth, solar phone charging station, and interactive community mural canvas."
        ],
        "lighting_ideas": [
            "Solar Festoons: Solar-charged warm LED festoon strings along pavilions and tree trunks.",
            "Natural Candles: Natural soy and beeswax pillar candles inside recycled glass hurricane jars.",
            "Copper Garlands: Low-voltage copper-wire fairy lights illuminating community exhibition stalls.",
            "Lanterns: Recycled paper punched tin lanterns casting playful stars across park walkways."
        ],
        "venue_recommendations": [
            "Public botanical sanctuary or community heritage garden.",
            "Solar-powered urban community center or covered open-air park amphitheater.",
            "Organic community farm with open-sided timber barn."
        ],
        "invitation_style": "100% plantable seeded paper embedded with bee-friendly wildflower seeds, with digital QR code for event scheduling and maps.",
        "catering_considerations": [
            "Menu Style: Hyper-local farm-to-fork plant-forward buffet highlighting regional seasonal harvests.",
            "Dietary Accommodations: 100% vegetarian, vegan, and allergen-friendly options with zero single-use packaging.",
            "Service Format: Community self-serve harvest table with compostable palm-leaf plates and birch cutlery.",
            "Beverages: Glass hydration stations infused with garden mint, lemon verbena, and local cider barrels."
        ],
        "budget_range": "$4,500 – $15,000 (Illustrative estimate)",
        "budget_breakdown": {
            "Park Pavilion Permit & Power": "22%",
            "Local Farm Harvest Catering": "38%",
            "Living Centerpieces & Signage": "18%",
            "Solar Sound & Acoustic Stage": "14%",
            "Workshops & Seedling Favors": "8%"
        },
        "guest_count_range": "80 – 450 guests",
        "guest_capacity_notes": "Open-air park configuration accommodating large flow of up to 450 guests with clear pathways and recycling hubs.",
        "planning_tips": [
            "Partner with local municipal composting groups and clearly label waste stations with visual picture signage.",
            "Encourage guests to utilize public transit or organized group cycling with bike valet incentives."
        ]
    }
]

# Curated Personalized Recommendations ("Ideas You'll Love")
RECOMMENDATIONS = [
    {
        "id": "rec-1",
        "title": "Sunset Terrace Champagne Soirée",
        "tag": "Intimate Luxury",
        "event_type": "Engagement",
        "style": "Romantic Luxury",
        "theme_match": "Romantic Candlelight Engagement",
        "image": "https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?auto=format&fit=crop&w=1200&q=80",
        "summary": "An exquisite golden-hour engagement with candlelit terrace dining, acoustic cello, and vintage champagne pairings.",
        "guest_count": "40 - 75 guests",
        "guest_count_val": 50,
        "est_budget": "$9,000 – $16,500",
        "budget_val": 14000,
        "color_palette": [
            {"name": "Blush Velvet", "hex": "#D19CA4"},
            {"name": "Warm Gold", "hex": "#D4AF37"},
            {"name": "Ivory Silk", "hex": "#FFFFF0"}
        ],
        "highlights": [
            "Golden hour toast timing with sunset coordinates",
            "Bespoke oyster & vintage champagne tasting station",
            "Personalized calligraphy vows book & guestbook table",
            "Warm amber mood lighting & acoustic string duo"
        ],
        "decorations": [
            "200+ hurricane glass candles lining the terrace perimeter",
            "Blush and burgundy rose petal carpet",
            "Silk-draped circular golden backdrop arch"
        ],
        "venue_style": "Cliffside Panoramic Terrace",
        "budget_split": {
            "Terrace Overlook Venue": "35%",
            "Fine Dining & Champagne": "35%",
            "Candlelight & Florals": "18%",
            "Acoustic String Duo": "12%"
        }
    },
    {
        "id": "rec-2",
        "title": "Enchanted Botanical Conservatory Wedding",
        "tag": "Botanical Charm",
        "event_type": "Wedding",
        "style": "Modern Botanical",
        "theme_match": "Elegant Garden Wedding",
        "image": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80",
        "summary": "Surround your closest family and friends with exotic flora, botanical cocktails, and candlelit glass conservatory magic.",
        "guest_count": "60 - 120 guests",
        "guest_count_val": 100,
        "est_budget": "$18,000 – $32,000",
        "budget_val": 26000,
        "color_palette": [
            {"name": "Sage Green", "hex": "#7A8F7A"},
            {"name": "Warm Ivory", "hex": "#FAF6EE"},
            {"name": "Champagne Gold", "hex": "#D4AF37"}
        ],
        "highlights": [
            "Protected greenhouse setting with 360-degree glass views",
            "Long communal banquet table with hanging floral chandelier",
            "Artisan botanical gin & tonic cocktail bar",
            "Documentary-style editorial photography package"
        ],
        "decorations": [
            "Hanging wisteria and trailing jasmine canopy",
            "Oak crossback dining chairs with linen napkins",
            "Cut-crystal bud vases with heirloom roses"
        ],
        "venue_style": "Historic Glasshouse Conservatory",
        "budget_split": {
            "Glasshouse Venue": "32%",
            "Seasonal Plated Feast": "32%",
            "Floral Canopy & Styling": "20%",
            "Photography & Cinematography": "16%"
        }
    },
    {
        "id": "rec-3",
        "title": "Starlit Rooftop Milestone Celebration",
        "tag": "Metropolitan Chic",
        "event_type": "Birthday",
        "style": "Glam Evening",
        "theme_match": "Luxury Evening Birthday",
        "image": "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?auto=format&fit=crop&w=1200&q=80",
        "summary": "A breathtaking milestone birthday overlooking twinkling city lights with a live DJ, custom cocktail bar, and lounge cabanas.",
        "guest_count": "50 - 110 guests",
        "guest_count_val": 75,
        "est_budget": "$8,500 – $18,000",
        "budget_val": 15000,
        "color_palette": [
            {"name": "Obsidian Black", "hex": "#0B0F19"},
            {"name": "Electric Gold", "hex": "#FFD700"},
            {"name": "Neon Amber", "hex": "#FF7E00"}
        ],
        "highlights": [
            "Private penthouse terrace with skyline photo backdrops",
            "Signature craft mocktails and cocktail mixologist",
            "Custom illuminated monogram milestone installation",
            "Late-night gourmet slider and artisan taco station"
        ],
        "decorations": [
            "Giant illuminated marquee numbers",
            "Glossy mirror cocktail tables with amber lamps",
            "Velvet VIP lounge cabana pods"
        ],
        "venue_style": "Downtown High-Altitude Penthouse Terrace",
        "budget_split": {
            "Rooftop Venue Space": "36%",
            "Craft Bar & Gourmet Bites": "34%",
            "Live DJ & Intelligent Lights": "18%",
            "Marquee Decor & Photo Moment": "12%"
        }
    },
    {
        "id": "rec-4",
        "title": "Heritage Golden Jubilee Anniversary",
        "tag": "Timeless Romance",
        "event_type": "Anniversary",
        "style": "Classical Elegance",
        "theme_match": "Golden Anniversary Celebration",
        "image": "https://images.unsplash.com/photo-1520854221256-17451cc331bf?auto=format&fit=crop&w=1200&q=80",
        "summary": "Honoring decades of devotion with nostalgic photo galleries, a five-course gourmet dinner, and renewal of vows.",
        "guest_count": "50 - 120 guests",
        "guest_count_val": 80,
        "est_budget": "$12,000 – $26,000",
        "budget_val": 20000,
        "color_palette": [
            {"name": "24K Gold", "hex": "#FFD700"},
            {"name": "Noble Navy", "hex": "#000080"},
            {"name": "Pure Alabaster", "hex": "#FEFEFA"}
        ],
        "highlights": [
            "Curated 'Memory Lane' retro photo walkway",
            "Live swing and classical quartet during dinner",
            "Vintage champagne toast and multi-tiered anniversary cake",
            "Leather-bound guest memory audio recorder & book"
        ],
        "decorations": [
            "Gold-leaf candelabras with ivory taper candles",
            "24K gold-rimmed bone china and damask linens",
            "Framed archival family portrait walkway"
        ],
        "venue_style": "Historic Manor Grand Salon",
        "budget_split": {
            "Historic Dining Salon": "32%",
            "Gourmet Plated Banquet": "38%",
            "Gold Florals & Table Setup": "15%",
            "Live Swing Ensemble": "15%"
        }
    },
    {
        "id": "rec-5",
        "title": "Boutique Artisan Harvest Festival",
        "tag": "Community Spirit",
        "event_type": "Community Event",
        "style": "Eco-Chic Community",
        "theme_match": "Eco-Friendly Community Festival",
        "image": "https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&w=1200&q=80",
        "summary": "An uplifting open-air community gathering featuring local artisan market stalls, acoustic stage, and zero-waste harvest dining.",
        "guest_count": "100 - 350 guests",
        "guest_count_val": 200,
        "est_budget": "$5,000 – $14,000",
        "budget_val": 9500,
        "color_palette": [
            {"name": "Forest Moss", "hex": "#2E5A36"},
            {"name": "Terracotta Earth", "hex": "#C86D51"},
            {"name": "Natural Linen", "hex": "#E3DAC9"}
        ],
        "highlights": [
            "Zero single-use plastics with compostable stations",
            "Acoustic solar-powered community performance stage",
            "Local culinary food stalls and farm-fresh bakery",
            "Interactive pottery and floral wreath workshops"
        ],
        "decorations": [
            "Potted rosemary and lavender take-home centerpieces",
            "Solar-powered warm LED festoon lighting",
            "Reclaimed timber directional signage and benches"
        ],
        "venue_style": "Community Park Amphitheater & Pavilion",
        "budget_split": {
            "Park Pavilion Permit": "22%",
            "Community Harvest Buffet": "38%",
            "Solar Sound & Stage": "25%",
            "Workshops & Seedling Favors": "15%"
        }
    }
]

# Curated Vendors Directory
VENDORS = [
    {
        "id": "v-1",
        "name": "Lumière Floral & Botanicals",
        "category": "Floral Design & Decor",
        "rating": 4.9,
        "reviews": 84,
        "location": "Beverly Hills & Greater Area",
        "price_tier": "$$$$",
        "image": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80",
        "specialty": "Bespoke garden archways, exotic cascading orchids, and sustainable tablescapes.",
        "badge": "CelebrAI Preferred"
    },
    {
        "id": "v-2",
        "name": "Velvet Horizon Events",
        "category": "Full-Service Production",
        "rating": 5.0,
        "reviews": 112,
        "location": "Downtown & Coastal Venues",
        "price_tier": "$$$$",
        "image": "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=600&q=80",
        "specialty": "Architectural lighting, audio engineering, staging, and luxury event coordination.",
        "badge": "Top Rated"
    },
    {
        "id": "v-3",
        "name": "Artisan Harvest Table",
        "category": "Catering & Mixology",
        "rating": 4.8,
        "reviews": 67,
        "location": "Metro Area",
        "price_tier": "$$$",
        "image": "https://images.unsplash.com/photo-1555244162-803834f70033?auto=format&fit=crop&w=600&q=80",
        "specialty": "Farm-to-table seasonal feasts, zero-waste mixology bars, and interactive culinary stations.",
        "badge": "Sustainable Choice"
    },
    {
        "id": "v-4",
        "name": "Golden Hour Photography",
        "category": "Visual Storytelling",
        "rating": 4.9,
        "reviews": 95,
        "location": "Available Worldwide",
        "price_tier": "$$$",
        "image": "https://images.unsplash.com/photo-1537633552985-df8429e8048b?auto=format&fit=crop&w=600&q=80",
        "specialty": "Editorial wedding photography, drone cinematography, and heirloom physical albums.",
        "badge": "CelebrAI Featured"
    }
]
