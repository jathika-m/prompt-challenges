/**
 * CelebrAI - Frontend Data Store & Fallback Assets
 */

// Image Fallback Generator to ensure no broken images ever appear
window.getFallbackImage = function(title, category = "Event") {
  const encodedTitle = encodeURIComponent(title || "CelebrAI Event");
  const encodedCat = encodeURIComponent(category || "Celebration");
  // Clean SVG Data URI with luxury dark charcoal and gold accents
  return `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600">
    <defs>
      <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="%230F172A"/>
        <stop offset="100%" stop-color="%231E293B"/>
      </linearGradient>
      <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="%23F3E8B5"/>
        <stop offset="100%" stop-color="%23D4AF37"/>
      </linearGradient>
    </defs>
    <rect width="800" height="600" fill="url(%23bg)"/>
    <circle cx="400" cy="240" r="70" fill="none" stroke="url(%23gold)" stroke-width="2" opacity="0.6"/>
    <path d="M400 200 L408 228 L436 236 L408 244 L400 272 L392 244 L364 236 L392 228 Z" fill="url(%23gold)"/>
    <text x="400" y="360" font-family="'Cinzel', serif" font-size="28" font-weight="bold" fill="%23FFFFFF" text-anchor="middle">${encodedTitle}</text>
    <text x="400" y="400" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" fill="%23D4AF37" text-anchor="middle" letter-spacing="3">${encodedCat.toUpperCase()}</text>
    <text x="400" y="440" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" fill="%2394A3B8" text-anchor="middle">CelebrAI Curated Experience</text>
  </svg>`;
};

// Global image error handler
window.handleImageError = function(imgElement, title = "Celebration", category = "Event") {
  imgElement.onerror = null;
  imgElement.src = window.getFallbackImage(title, category);
};

// Currency formatter
window.formatCurrency = function(amount) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0
  }).format(amount);
};
