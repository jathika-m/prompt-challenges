/**
 * CelebrAI - Main Application Controller
 * Premium Themes Gallery, Two-Column Theme Details Modal, Planner Engine & GenAI-Ready Ideas
 */

const App = {
  currentTab: 'home',
  themes: [],
  eventTypes: [],
  recommendations: [],
  userEvents: [],
  vendors: [],
  selectedThemeForDetail: null,
  selectedIdeaForDetail: null,
  selectedPlannerTheme: null,
  currentGalleryFilter: 'all',
  currentCatalogFilter: 'all',

  async init() {
    this.bindEvents();
    await this.fetchInitialData();
    this.renderEventCards();
    this.renderThemeCards();
    this.renderRecommendations();
    this.renderUserEvents();
    this.renderVendors();
    this.setupPlannerCalculations();
    
    // Initialize icons
    if (window.lucide) lucide.createIcons();
  },

  bindEvents() {
    // Escape key closes modals
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.closeAllModals();
      }
    });

    // Close profile dropdown when clicking outside
    document.addEventListener('click', (e) => {
      const profileBtn = document.getElementById('profile-menu-button');
      const profileDropdown = document.getElementById('profile-dropdown');
      if (profileBtn && profileDropdown && !profileBtn.contains(e.target) && !profileDropdown.contains(e.target)) {
        profileDropdown.classList.add('hidden');
      }
    });

    // Modal backdrop clicks to close
    ['theme-detail-modal', 'idea-detail-modal'].forEach(modalId => {
      const modal = document.getElementById(modalId);
      if (modal) {
        modal.addEventListener('click', (e) => {
          if (e.target === modal) {
            this.closeAllModals();
          }
        });
      }
    });
  },

  toggleProfileDropdown() {
    const profileDropdown = document.getElementById('profile-dropdown');
    if (profileDropdown) {
      profileDropdown.classList.toggle('hidden');
    }
  },

  async fetchInitialData() {
    try {
      const [typesRes, themesRes, recsRes, eventsRes, vendorsRes] = await Promise.all([
        fetch('/api/events/types'),
        fetch('/api/themes'),
        fetch('/api/recommendations'),
        fetch('/api/events'),
        fetch('/api/vendors')
      ]);

      const typesData = await typesRes.json();
      const themesData = await themesRes.json();
      const recsData = await recsRes.json();
      const eventsData = await eventsRes.json();
      const vendorsData = await vendorsRes.json();

      this.eventTypes = typesData.event_types || [];
      this.themes = themesData.themes || [];
      this.recommendations = recsData.recommendations || [];
      this.userEvents = eventsData.events || [];
      this.vendors = vendorsData.vendors || [];

      this.updateEventsBadge();
    } catch (err) {
      console.error('Failed to load initial data:', err);
    }
  },

  async refreshData() {
    await this.fetchInitialData();
    this.renderEventCards();
    this.renderThemeCards();
    this.renderRecommendations();
    this.renderUserEvents();
    this.renderVendors();
    if (window.lucide) lucide.createIcons();
  },

  updateEventsBadge() {
    const badge = document.getElementById('my-events-badge');
    if (badge) {
      badge.textContent = this.userEvents.length;
      badge.classList.toggle('hidden', this.userEvents.length === 0);
    }
  },

  // ----------------- NAVIGATION -----------------
  switchTab(tabName) {
    this.currentTab = tabName;

    // Nav Link Highlights
    const navItems = ['home', 'planner', 'my-events', 'themes-catalog', 'vendors-tab'];
    navItems.forEach(tab => {
      const link = document.getElementById(`nav-link-${tab}`);
      const mobLink = document.getElementById(`mob-nav-link-${tab}`);
      
      const isActive = (tab === tabName);

      if (link) {
        if (isActive) {
          link.classList.add('text-amber-300', 'font-semibold');
          link.classList.remove('text-slate-300');
          link.innerHTML = `${link.getAttribute('data-title')} <span class="w-1.5 h-1.5 rounded-full bg-amber-400 inline-block ml-1 mb-0.5"></span>`;
        } else {
          link.classList.remove('text-amber-300', 'font-semibold');
          link.classList.add('text-slate-300');
          link.innerHTML = link.getAttribute('data-title');
        }
      }

      if (mobLink) {
        if (isActive) {
          mobLink.classList.add('text-amber-400', 'bg-slate-800/80');
          mobLink.classList.remove('text-slate-300');
        } else {
          mobLink.classList.remove('text-amber-400', 'bg-slate-800/80');
          mobLink.classList.add('text-slate-300');
        }
      }
    });

    // Close mobile drawer if open
    const mobMenu = document.getElementById('mobile-nav-drawer');
    if (mobMenu) mobMenu.classList.add('hidden');

    // View Switching
    const views = {
      'home': document.getElementById('view-home'),
      'planner': document.getElementById('view-planner'),
      'my-events': document.getElementById('view-my-events'),
      'themes-catalog': document.getElementById('view-themes-catalog'),
      'vendors-tab': document.getElementById('view-vendors')
    };

    Object.entries(views).forEach(([key, element]) => {
      if (element) {
        if (key === tabName) {
          element.classList.remove('hidden');
        } else {
          element.classList.add('hidden');
        }
      }
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
    if (window.lucide) lucide.createIcons();
  },

  toggleMobileMenu() {
    const mobMenu = document.getElementById('mobile-nav-drawer');
    if (mobMenu) {
      mobMenu.classList.toggle('hidden');
      if (window.lucide) lucide.createIcons();
    }
  },

  // ----------------- RENDER EVENT CARDS (Section 4 - Matching Reference 5-Column Grid) -----------------
  renderEventCards() {
    const container = document.getElementById('event-cards-grid');
    if (!container) return;

    container.innerHTML = this.eventTypes.map(ev => `
      <div class="card-hover-lift bg-white rounded-2xl overflow-hidden border border-slate-200/80 shadow-sm hover:shadow-md flex flex-col justify-between group">
        <div>
          <div class="relative aspect-16-10 overflow-hidden bg-slate-900 cursor-pointer" onclick="App.planEventPreselected('${ev.title}')">
            <img 
              src="${ev.image}" 
              alt="${ev.title} Venue Setup" 
              onerror="window.handleImageError(this, '${ev.title}', 'Event Venue')"
              class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/75 via-transparent to-transparent"></div>
            <span class="absolute top-2.5 left-2.5 bg-amber-400 text-slate-950 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full shadow-xs">
              ${ev.badge}
            </span>
          </div>

          <div class="p-4 sm:p-5">
            <h3 class="font-serif text-lg font-bold text-slate-900 group-hover:text-amber-700 transition-colors cursor-pointer line-clamp-1" onclick="App.planEventPreselected('${ev.title}')">
              ${ev.title}
            </h3>
            <p class="text-xs text-slate-500 mt-1 line-clamp-2 leading-relaxed">
              ${ev.description}
            </p>
          </div>
        </div>

        <div class="p-4 sm:p-5 pt-0">
          <button 
            type="button"
            onclick="App.planEventPreselected('${ev.title}')"
            class="w-full py-2.5 px-3 rounded-xl border border-slate-300 text-slate-800 hover:text-amber-900 hover:border-amber-400 hover:bg-amber-50/50 font-semibold text-xs transition-colors flex items-center justify-center gap-1.5 bg-slate-50 cursor-pointer">
            <span>Plan This Event</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </button>
        </div>
      </div>
    `).join('');

    if (window.lucide) lucide.createIcons();
  },

  planEventPreselected(eventType, themeName = null) {
    this.switchTab('planner');

    const typeSelect = document.getElementById('planner-event-type');
    const titleInput = document.getElementById('planner-title');
    const themeSelect = document.getElementById('planner-theme');

    if (typeSelect) {
      typeSelect.value = eventType;
      this.populateThemeDropdownForEvent(eventType);
    }

    if (themeName) {
      if (themeSelect) themeSelect.value = themeName;
      const themeObj = this.themes.find(t => t.name === themeName);
      if (themeObj) {
        this.selectedPlannerTheme = themeObj;
        this.renderPlannerSelectedThemeBanner(themeObj);
      }
    } else {
      // Find default popular theme for this event type
      const defaultTheme = this.themes.find(t => t.category === eventType || t.suitable_events.includes(eventType));
      if (defaultTheme && themeSelect) {
        themeSelect.value = defaultTheme.name;
        this.selectedPlannerTheme = defaultTheme;
        this.renderPlannerSelectedThemeBanner(defaultTheme);
      }
    }

    if (titleInput && (!titleInput.value || titleInput.value.includes('Celebration'))) {
      titleInput.value = `${eventType} Celebration`;
    }

    this.updatePlannerBudgetBreakdown();
    this.showToast(`Planner configured for: ${eventType}${themeName ? ' (' + themeName + ')' : ''}`, 'info');
  },

  populateThemeDropdownForEvent(eventType) {
    const themeSelect = document.getElementById('planner-theme');
    if (!themeSelect) return;

    themeSelect.innerHTML = `
      <option value="">-- Choose or keep open for inspiration --</option>
      ${this.themes.map(t => `
        <option value="${t.name}">${t.name} (${t.category})</option>
      `).join('')}
    `;

    // Listen to theme dropdown changes to update planner theme banner
    themeSelect.onchange = (e) => {
      const selectedName = e.target.value;
      const themeObj = this.themes.find(t => t.name === selectedName);
      if (themeObj) {
        this.selectedPlannerTheme = themeObj;
        this.renderPlannerSelectedThemeBanner(themeObj);
      } else {
        this.selectedPlannerTheme = null;
        this.renderPlannerSelectedThemeBanner(null);
      }
    };
  },

  // ----------------- RENDER THEMES GALLERY (Section 2 & 3) -----------------
  renderThemeCards(activeCategory = 'all') {
    this.currentGalleryFilter = activeCategory;
    const homeGrid = document.getElementById('themes-cards-grid');
    const catalogGrid = document.getElementById('catalog-themes-grid');

    const filtered = (activeCategory === 'all')
      ? this.themes
      : this.themes.filter(t => 
          t.category.toLowerCase() === activeCategory.toLowerCase() || 
          t.suitable_events.some(e => e.toLowerCase() === activeCategory.toLowerCase())
        );

    const html = filtered.map(th => {
      const displaySwatches = (th.color_palette || []).slice(0, 3);
      return `
        <div class="card-hover-lift bg-white rounded-2xl overflow-hidden border border-slate-200/90 shadow-sm hover:shadow-xl flex flex-col justify-between group transition-all">
          <div>
            <!-- Main Landscape Photography (approx 16:10) -->
            <div class="relative aspect-16-10 overflow-hidden bg-slate-900 cursor-pointer" onclick="App.openThemeModal('${th.id}')">
              <img 
                src="${th.image}" 
                alt="${th.name} Event Venue"
                onerror="window.handleImageError(this, '${th.name}', 'Venue')"
                class="w-full h-full object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                loading="lazy"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-black/25"></div>
              
              <!-- Category Badge -->
              <span class="absolute top-3 right-3 bg-slate-900/85 text-amber-300 text-[11px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full backdrop-blur-md border border-amber-500/30">
                ${th.category}
              </span>

              <!-- Bottom Budget Range Pill -->
              <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-xs">
                <span class="text-white/95 font-medium bg-black/60 px-2.5 py-0.5 rounded-md backdrop-blur-sm truncate max-w-[70%]">
                  ${th.budget_range.split('(')[0].trim()}
                </span>
                <span class="text-amber-200 text-[11px] font-semibold bg-black/60 px-2 py-0.5 rounded-md backdrop-blur-sm">
                  ${th.guest_count_range.split('guests')[0].trim()} guests
                </span>
              </div>
            </div>

            <!-- Card Body -->
            <div class="p-5 sm:p-6">
              <h4 
                class="font-serif text-lg sm:text-xl font-bold text-slate-900 group-hover:text-amber-700 transition-colors cursor-pointer line-clamp-1" 
                onclick="App.openThemeModal('${th.id}')"
                title="${th.name}">
                ${th.name}
              </h4>
              
              <p class="text-xs sm:text-sm text-slate-600 mt-2 line-clamp-2 leading-relaxed">
                ${th.short_description}
              </p>

              <!-- Color Palette Swatches -->
              <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between">
                <span class="text-[11px] text-slate-400 font-semibold uppercase tracking-wider">Palette</span>
                <div class="flex items-center gap-1.5">
                  ${displaySwatches.map(c => `
                    <div 
                      class="color-swatch-dot w-5 h-5 rounded-full border border-slate-300/80 shadow-xs cursor-pointer relative" 
                      style="background-color: ${c.hex};" 
                      title="${c.name} (${c.hex})">
                    </div>
                  `).join('')}
                </div>
              </div>
            </div>
          </div>

          <!-- Aligned Buttons Row -->
          <div class="p-5 sm:p-6 pt-0 flex items-center gap-2">
            <button 
              type="button"
              onclick="App.openThemeModal('${th.id}')"
              class="flex-1 py-2.5 px-3 rounded-xl border border-slate-300 text-slate-800 hover:text-amber-800 hover:border-amber-400 font-medium text-xs transition-colors flex items-center justify-center gap-1.5 bg-slate-50 hover:bg-amber-50/50 cursor-pointer">
              <i data-lucide="eye" class="w-3.5 h-3.5"></i>
              <span>View Details</span>
            </button>
            <button 
              type="button"
              onclick="App.useThemeInPlanner('${th.id}')"
              class="py-2.5 px-3.5 rounded-xl gold-gradient-bg text-slate-950 font-bold text-xs transition-all shadow-sm hover:shadow active:scale-95 flex items-center justify-center gap-1 cursor-pointer">
              <span>Use This Theme</span>
              <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>
      `;
    }).join('');

    if (homeGrid) homeGrid.innerHTML = html;
    if (catalogGrid) catalogGrid.innerHTML = html;
    if (window.lucide) lucide.createIcons();
  },

  filterGallery(category) {
    const filterTabs = ['all', 'Wedding', 'Birthday', 'Engagement', 'Anniversary', 'Community Event'];
    filterTabs.forEach(tab => {
      const btn = document.getElementById(`gallery-filter-${tab.replace(/\s+/g, '-').toLowerCase()}`);
      if (btn) {
        if (tab.toLowerCase() === category.toLowerCase()) {
          btn.classList.add('bg-amber-400', 'text-slate-950', 'font-bold');
          btn.classList.remove('bg-white', 'text-slate-700', 'border-slate-300');
        } else {
          btn.classList.remove('bg-amber-400', 'text-slate-950', 'font-bold');
          btn.classList.add('bg-white', 'text-slate-700', 'border-slate-300');
        }
      }
    });

    this.renderThemeCards(category);
  },

  filterCatalog(category) {
    const tabs = ['all', 'Wedding', 'Birthday', 'Engagement', 'Anniversary', 'Community Event'];
    tabs.forEach(tab => {
      const btn = document.getElementById(`filter-btn-${tab.replace(/\s+/g, '-').toLowerCase()}`);
      if (btn) {
        if (tab.toLowerCase() === category.toLowerCase()) {
          btn.classList.add('bg-amber-400', 'text-slate-950', 'font-bold');
          btn.classList.remove('bg-slate-800', 'text-slate-300');
        } else {
          btn.classList.remove('bg-amber-400', 'text-slate-950', 'font-bold');
          btn.classList.add('bg-slate-800', 'text-slate-300');
        }
      }
    });

    this.renderThemeCards(category);
  },

  // ----------------- THEME DETAILED MODAL (Section 4 & 5) -----------------
  openThemeModal(themeId) {
    const theme = this.themes.find(t => t.id === themeId);
    if (!theme) return;

    this.selectedThemeForDetail = theme;
    const modal = document.getElementById('theme-detail-modal');
    const container = document.getElementById('theme-detail-content');
    if (!modal || !container) return;

    container.innerHTML = `
      <!-- Modal Header (Matching Reference Design) -->
      <div class="sticky top-0 z-20 bg-white/95 backdrop-blur-md px-6 sm:px-8 py-4 border-b border-slate-200 flex items-center justify-between">
        <div class="flex items-center gap-2.5">
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-100 text-amber-900 text-xs font-bold uppercase tracking-wider">
            <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-600"></i>
            <span>Theme Details</span>
          </span>
          <span class="text-xs text-slate-300 font-medium hidden sm:inline">•</span>
          <span class="text-xs text-slate-600 font-bold uppercase tracking-wider hidden sm:inline">${theme.category}</span>
        </div>

        <button 
          type="button"
          onclick="App.closeThemeModal()"
          class="w-10 h-10 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 hover:text-slate-900 transition-colors flex items-center justify-center cursor-pointer ml-4 shrink-0 shadow-2xs"
          aria-label="Close theme modal">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <!-- Modal Body (Panoramic Banner on Top + Two-Column Layout Below) -->
      <div class="p-6 sm:p-8 lg:p-8 bg-[#FAF9F6] text-slate-900 overflow-y-auto light-scrollbar space-y-8">
        
        <!-- Top Full-Width Panoramic Luxury Venue Banner (Matching Reference Image) -->
        <div class="rounded-2xl overflow-hidden shadow-lg border border-slate-200/90 h-64 sm:h-72 lg:h-80 bg-slate-900 relative group">
          <img 
            src="${theme.image}" 
            alt="${theme.name} Venue"
            onerror="window.handleImageError(this, '${theme.name}', 'Venue')"
            class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950/85 via-slate-950/25 to-transparent"></div>
          <div class="absolute top-4 left-4">
            <span class="bg-amber-400 text-slate-950 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full shadow-md">
              ${theme.category}
            </span>
          </div>
          <div class="absolute bottom-4 left-4 right-4 sm:bottom-6 sm:left-6 sm:right-6 text-white flex flex-col sm:flex-row sm:items-end justify-between gap-3">
            <div>
              <span class="text-xs font-semibold tracking-wider text-amber-300 uppercase block mb-1">
                ${theme.atmosphere_style || 'Curated Aesthetic'}
              </span>
              <h2 class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold text-white leading-tight drop-shadow-md">
                ${theme.name}
              </h2>
            </div>
            <div class="text-xs text-slate-200 font-medium bg-black/40 backdrop-blur-md px-3.5 py-1.5 rounded-lg border border-white/10 w-fit shrink-0 flex items-center gap-1.5">
              <i data-lucide="map-pin" class="w-3.5 h-3.5 text-amber-400"></i>
              <span>Venue Atmosphere Styling</span>
            </div>
          </div>
        </div>

        <!-- Two-Column Structured Planning Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          <!-- LEFT COLUMN (lg:col-span-7): Overview, Circular Swatches, Decor & Atmosphere -->
          <div class="lg:col-span-7 space-y-6">
            
            <!-- Theme Overview Card -->
            <div class="planning-card">
              <h3 class="text-xs font-bold uppercase tracking-widest text-amber-800 mb-2 flex items-center gap-1.5">
                <i data-lucide="compass" class="w-4 h-4 text-amber-600"></i>
                <span>Theme Overview &amp; Character</span>
              </h3>
              <p class="text-slate-700 text-sm sm:text-base leading-relaxed">
                ${theme.overview}
              </p>
            </div>

            <!-- Curated Color Palette (Circular Swatches with Name & Hex Centered Underneath) -->
            <div class="planning-card select-none">
              <div class="flex items-center justify-between mb-4">
                <h3 class="text-xs font-bold uppercase tracking-widest text-amber-800 flex items-center gap-1.5">
                  <i data-lucide="palette" class="w-4 h-4 text-amber-600"></i>
                  <span>Curated Color Palette</span>
                </h3>
                <span class="text-[11px] text-slate-400 font-medium hidden sm:inline">Click color to copy hex</span>
              </div>
              
              <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3.5 select-none">
                ${theme.color_palette.map(c => `
                  <div 
                    onclick="App.copyColorHex('${c.hex}', '${c.name}', this)"
                    title="Click to copy ${c.name} (${c.hex})"
                    class="color-swatch-card group relative flex flex-col items-center p-3.5 bg-slate-50 hover:bg-amber-50/60 rounded-2xl border border-slate-200/80 hover:border-amber-400 hover:shadow-md transition-all cursor-pointer select-none active:scale-95">
                    
                    <div class="w-12 h-12 rounded-full shadow-md mb-2 shrink-0 transition-transform group-hover:scale-110 flex items-center justify-center relative cursor-pointer" style="background-color: ${c.hex}; border: 2px solid ${c.hex.toUpperCase() === '#FFFFFF' ? '#CBD5E1' : 'rgba(255,255,255,0.95)'};">
                      <i data-lucide="copy" class="w-4 h-4 ${c.hex.toUpperCase() === '#FFFFFF' ? 'text-slate-700' : 'text-white'} opacity-0 group-hover:opacity-85 transition-opacity drop-shadow"></i>
                    </div>
                    
                    <span class="text-xs font-bold text-slate-800 text-center leading-snug break-words max-w-full block group-hover:text-amber-900 cursor-pointer select-none">${c.name}</span>
                    <span class="text-[11px] text-slate-400 group-hover:text-amber-700 font-mono text-center block mt-1 cursor-pointer select-none font-medium">${c.hex}</span>
                    
                    <!-- Copy Confirmation Badge -->
                    <span class="copy-badge hidden absolute -top-2.5 bg-slate-900 text-amber-300 text-[10px] font-bold px-2 py-0.5 rounded-full shadow-lg border border-amber-400/40 z-10 select-none pointer-events-none">
                      Copied!
                    </span>
                  </div>
                `).join('')}
              </div>
            </div>

            <!-- Decoration Suggestions -->
            <div class="planning-card">
              <div class="flex items-center gap-2 text-slate-900 font-serif font-bold text-base sm:text-lg mb-3">
                <i data-lucide="flower-2" class="w-5 h-5 text-amber-600"></i>
                <h4>Decoration Suggestions</h4>
              </div>
              <ul class="space-y-2 text-sm text-slate-600">
                ${theme.decoration_suggestions.map(item => `
                  <li class="flex items-start gap-2.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-amber-500 mt-2 shrink-0"></span>
                    <span>${item}</span>
                  </li>
                `).join('')}
              </ul>
            </div>

            <!-- Lighting Ideas -->
            <div class="planning-card">
              <div class="flex items-center gap-2 text-slate-900 font-serif font-bold text-base sm:text-lg mb-3">
                <i data-lucide="sparkles" class="w-5 h-5 text-amber-600"></i>
                <h4>Lighting &amp; Illumination Concepts</h4>
              </div>
              <ul class="space-y-2 text-sm text-slate-600">
                ${theme.lighting_ideas.map(item => `
                  <li class="flex items-start gap-2.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-amber-500 mt-2 shrink-0"></span>
                    <span>${item}</span>
                  </li>
                `).join('')}
              </ul>
            </div>

            <!-- Venue Recommendations -->
            <div class="planning-card">
              <div class="flex items-center gap-2 text-slate-900 font-serif font-bold text-base sm:text-lg mb-3">
                <i data-lucide="building-2" class="w-5 h-5 text-amber-600"></i>
                <h4>Venue Recommendations</h4>
              </div>
              <ul class="space-y-2 text-sm text-slate-600">
                ${theme.venue_recommendations.map(item => `
                  <li class="flex items-start gap-2.5">
                    <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600 mt-0.5 shrink-0"></i>
                    <span>${item}</span>
                  </li>
                `).join('')}
              </ul>
            </div>

          </div>

          <!-- RIGHT COLUMN (lg:col-span-5): Specifications, Budget & Execution Tips -->
          <div class="lg:col-span-5 space-y-6">

            <!-- Scope & Key Specifications -->
            <div class="planning-card">
              <h3 class="text-xs font-bold uppercase tracking-widest text-amber-800 mb-3 flex items-center gap-1.5">
                <i data-lucide="sliders" class="w-4 h-4 text-amber-600"></i>
                <span>Theme Specifications</span>
              </h3>
              
              <div class="space-y-3 text-xs">
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200/80">
                  <span class="text-slate-400 block mb-0.5 font-medium">Suitable Celebrations</span>
                  <div class="flex flex-wrap gap-1.5 mt-1">
                    ${theme.suitable_events.map(ev => `
                      <span class="text-[11px] bg-amber-100/80 text-amber-900 px-2.5 py-0.5 rounded-full font-bold">
                        ${ev}
                      </span>
                    `).join('')}
                  </div>
                </div>

                <div class="grid grid-cols-2 gap-3">
                  <div class="p-3 bg-slate-50 rounded-xl border border-slate-200/80">
                    <span class="text-slate-400 block mb-0.5 font-medium">Guest Capacity</span>
                    <span class="text-sm font-bold text-slate-900">${theme.guest_count_range}</span>
                  </div>
                  <div class="p-3 bg-slate-50 rounded-xl border border-slate-200/80">
                    <span class="text-slate-400 block mb-0.5 font-medium">Estimated Budget</span>
                    <span class="text-sm font-bold text-amber-700">${theme.budget_range.split('(')[0].trim()}</span>
                  </div>
                </div>

                ${theme.guest_capacity_notes ? `
                  <p class="text-[11px] text-slate-500 italic bg-amber-50/50 p-2.5 rounded-lg border border-amber-100">
                    <i data-lucide="info" class="w-3.5 h-3.5 text-amber-600 inline mr-1"></i>
                    ${theme.guest_capacity_notes}
                  </p>
                ` : ''}
              </div>
            </div>

            <!-- Invitation Style -->
            <div class="planning-card">
              <div class="flex items-center gap-2 text-slate-900 font-serif font-bold text-base mb-2">
                <i data-lucide="mail" class="w-4 h-4 text-amber-600"></i>
                <h4>Invitation Style &amp; Typography</h4>
              </div>
              <div class="p-3 bg-amber-50/60 rounded-xl border border-amber-200/60 text-xs sm:text-sm text-amber-950 leading-relaxed">
                ${theme.invitation_style}
              </div>
            </div>

            <!-- Food & Catering Considerations -->
            <div class="planning-card">
              <div class="flex items-center gap-2 text-slate-900 font-serif font-bold text-base mb-3">
                <i data-lucide="utensils" class="w-4 h-4 text-amber-600"></i>
                <h4>Food &amp; Catering Style</h4>
              </div>
              <ul class="space-y-2 text-xs sm:text-sm text-slate-600">
                ${theme.catering_considerations.map(c => `
                  <li class="flex items-start gap-2">
                    <span class="text-amber-500 font-bold">•</span>
                    <span>${c}</span>
                  </li>
                `).join('')}
              </ul>
            </div>

            <!-- Illustrative Budget Breakdown -->
            <div class="planning-card bg-slate-900 text-white border-amber-500/30">
              <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2 text-amber-400 font-bold text-xs uppercase tracking-wider">
                  <i data-lucide="calculator" class="w-3.5 h-3.5"></i>
                  <span>Illustrative Budget Breakdown</span>
                </div>
                <span class="text-xs text-amber-300 font-bold">${theme.budget_range.split('(')[0].trim()}</span>
              </div>
              
              <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-center text-xs">
                ${Object.entries(theme.budget_breakdown || {}).map(([key, val]) => `
                  <div class="p-2 bg-slate-800/90 rounded-xl border border-slate-700/80">
                    <span class="text-amber-300 font-bold text-xs sm:text-sm block">${val}</span>
                    <span class="text-[10px] text-slate-400 block mt-0.5 truncate">${key}</span>
                  </div>
                `).join('')}
              </div>
              
              <p class="text-[10px] text-slate-400 mt-2.5 italic">
                *Illustrative guidance. Actual costs dynamically adapt to confirmed vendors.
              </p>
            </div>

            <!-- Practical Planning Tips -->
            <div class="planning-card">
              <div class="flex items-center gap-2 text-slate-900 font-serif font-bold text-base mb-3">
                <i data-lucide="lightbulb" class="w-4 h-4 text-amber-600"></i>
                <h4>Practical Planning Tips</h4>
              </div>
              <ul class="space-y-2 text-xs text-slate-600">
                ${theme.planning_tips.map(tip => `
                  <li class="flex items-start gap-2 bg-slate-50 p-2.5 rounded-lg border border-slate-100">
                    <i data-lucide="check" class="w-3.5 h-3.5 text-amber-600 mt-0.5 shrink-0"></i>
                    <span>${tip}</span>
                  </li>
                `).join('')}
              </ul>
            </div>

          </div>
        </div>
      </div>

      <!-- Modal Prominent Sticky Footer with "Use This Theme ->" Action (Matching Reference Image) -->
      <div class="sticky bottom-0 z-20 bg-slate-950 border-t border-amber-500/30 px-6 sm:px-8 py-4 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-2xl">
        <div class="text-xs text-slate-400 hidden sm:block">
          Ready to make <strong class="text-white">${theme.name}</strong> your celebration blueprint?
        </div>
        
        <button 
          type="button"
          onclick="App.useThemeInPlanner('${theme.id}')"
          class="w-full sm:w-auto py-3.5 px-10 rounded-xl font-bold text-sm gold-gradient-bg text-slate-950 shadow-xl shadow-amber-500/20 hover:shadow-amber-500/40 active:scale-95 transition-all flex items-center justify-center gap-2 cursor-pointer">
          <span>Use This Theme &rarr;</span>
        </button>
      </div>
    `;

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    if (window.lucide) lucide.createIcons();
  },

  closeThemeModal() {
    const modal = document.getElementById('theme-detail-modal');
    if (modal) modal.classList.add('hidden');
    document.body.style.overflow = 'auto';
  },

  copyColorHex(hex, name, el) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(hex).catch(() => {});
    }
    if (el) {
      const badge = el.querySelector('.copy-badge');
      if (badge) {
        badge.classList.remove('hidden');
        setTimeout(() => {
          badge.classList.add('hidden');
        }, 1400);
      }
    }
    this.showToast(`Copied ${name} (${hex}) to clipboard!`, 'info');
  },

  useThemeInPlanner(themeId) {
    const theme = this.themes.find(t => t.id === themeId);
    if (!theme) return;

    this.closeThemeModal();
    const targetEvent = theme.category || theme.suitable_events[0] || 'Wedding';
    this.planEventPreselected(targetEvent, theme.name);
  },

  renderPlannerSelectedThemeBanner(theme) {
    const bannerContainer = document.getElementById('planner-selected-theme-banner');
    if (!bannerContainer) return;

    if (!theme) {
      bannerContainer.innerHTML = '';
      bannerContainer.classList.add('hidden');
      return;
    }

    bannerContainer.classList.remove('hidden');
    bannerContainer.innerHTML = `
      <div class="p-4 sm:p-5 rounded-2xl bg-amber-50/80 border border-amber-200/80 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="flex items-center gap-3.5">
          <img 
            src="${theme.image}" 
            alt="${theme.name}" 
            onerror="window.handleImageError(this, '${theme.name}', 'Theme')"
            class="w-14 h-14 rounded-xl object-cover border border-amber-300 shadow-sm shrink-0" 
          />
          <div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] bg-amber-400 text-slate-950 font-bold uppercase tracking-wider px-2 py-0.5 rounded-full">
                Active Theme
              </span>
              <span class="text-xs text-slate-500 font-medium">${theme.category}</span>
            </div>
            <h4 class="font-serif text-base font-bold text-slate-900 mt-0.5">${theme.name}</h4>
            <div class="flex items-center gap-1.5 mt-1">
              ${(theme.color_palette || []).slice(0, 4).map(c => `
                <div class="w-3.5 h-3.5 rounded-full border border-slate-300" style="background-color: ${c.hex};" title="${c.name}"></div>
              `).join('')}
            </div>
          </div>
        </div>

        <button 
          type="button" 
          onclick="App.openThemeModal('${theme.id}')"
          class="text-xs font-semibold text-amber-800 hover:text-amber-950 flex items-center gap-1 bg-white px-3 py-2 rounded-lg border border-amber-200 shadow-2xs hover:bg-amber-100/50 cursor-pointer w-fit">
          <i data-lucide="eye" class="w-3.5 h-3.5 text-amber-600"></i>
          <span>View Full Blueprint</span>
        </button>
      </div>
    `;

    if (window.lucide) lucide.createIcons();
  },

  // ----------------- PERSONALISED IDEAS (Section 7) -----------------
  renderRecommendations(filterType = 'all') {
    const container = document.getElementById('recommendations-grid');
    if (!container) return;

    const filtered = (filterType === 'all')
      ? this.recommendations
      : this.recommendations.filter(r => r.event_type.toLowerCase() === filterType.toLowerCase());

    container.innerHTML = filtered.map(rec => {
      const swatches = (rec.color_palette || []).slice(0, 3);
      return `
        <div class="card-hover-lift bg-white rounded-2xl overflow-hidden border border-slate-200/90 shadow-sm flex flex-col sm:flex-row group">
          <!-- Left Thumbnail (Matching Reference Image) -->
          <div class="sm:w-2/5 relative min-h-[190px] sm:min-h-full overflow-hidden bg-slate-900 cursor-pointer shrink-0" onclick="App.openIdeaModal('${rec.id}')">
            <img 
              src="${rec.image}" 
              alt="${rec.title}"
              onerror="window.handleImageError(this, '${rec.title}', 'Idea')"
              class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 absolute inset-0"
              loading="lazy"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/85 via-transparent to-black/20"></div>
            
            <span class="absolute top-3 left-3 bg-slate-900/80 text-amber-300 text-[11px] font-semibold px-2.5 py-0.5 rounded-full backdrop-blur-md border border-amber-500/20">
              ${rec.tag}
            </span>
            <span class="absolute bottom-2.5 left-3 text-[11px] text-white/95 font-medium flex items-center gap-1">
              <i data-lucide="sparkles" class="w-3 h-3 text-amber-400"></i> ${rec.style}
            </span>
          </div>

          <!-- Right Details & Actions -->
          <div class="sm:w-3/5 p-5 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between text-xs text-slate-500 mb-1.5">
                <span class="font-bold text-amber-700 uppercase tracking-wider text-[11px]">${rec.event_type}</span>
                <span class="font-medium text-slate-700 bg-slate-100 px-2.5 py-0.5 rounded-full text-[11px]">${rec.guest_count}</span>
              </div>
              
              <h4 class="font-serif text-base sm:text-lg font-bold text-slate-900 group-hover:text-amber-700 transition-colors cursor-pointer leading-snug" onclick="App.openIdeaModal('${rec.id}')">
                ${rec.title}
              </h4>
              <p class="text-xs text-slate-600 mt-2 line-clamp-2 leading-relaxed">
                ${rec.summary}
              </p>

              <div class="mt-3.5 p-2.5 bg-amber-50/60 rounded-xl border border-amber-200/50 flex items-center justify-between">
                <div>
                  <span class="text-[10px] text-amber-900 font-semibold uppercase tracking-wider block">Est. Budget Range</span>
                  <span class="text-xs font-bold text-amber-800">${rec.est_budget}</span>
                </div>
                ${swatches.length > 0 ? `
                  <div class="flex items-center gap-1">
                    ${swatches.map(c => `
                      <div class="w-3.5 h-3.5 rounded-full border border-slate-300" style="background-color: ${c.hex};" title="${c.name}"></div>
                    `).join('')}
                  </div>
                ` : ''}
              </div>
            </div>

            <div class="mt-4 pt-3 border-t border-slate-100 flex items-center gap-2">
              <button 
                type="button"
                onclick="App.openIdeaModal('${rec.id}')"
                class="flex-1 py-2 px-2.5 rounded-lg border border-slate-300 text-slate-700 hover:text-amber-800 hover:border-amber-400 font-semibold text-xs transition-colors flex items-center justify-center gap-1 bg-white hover:bg-amber-50/40 cursor-pointer">
                <i data-lucide="compass" class="w-3.5 h-3.5"></i>
                <span>Explore Idea</span>
              </button>
              <button 
                type="button"
                onclick="App.applyIdeaToPlanner('${rec.id}')"
                class="py-2 px-3 rounded-lg gold-gradient-bg text-slate-950 font-bold text-xs transition-all shadow-xs hover:shadow flex items-center justify-center gap-1 cursor-pointer">
                <span>Apply to Planner</span>
                <i data-lucide="plus" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </div>
        </div>
      `;
    }).join('');

    if (window.lucide) lucide.createIcons();
  },

  filterIdeas(type) {
    const filters = ['all', 'Wedding', 'Birthday', 'Engagement', 'Anniversary', 'Community Event'];
    filters.forEach(f => {
      const btn = document.getElementById(`filter-idea-${f.replace(/\s+/g, '-').toLowerCase()}`);
      if (btn) {
        if (f.toLowerCase() === type.toLowerCase()) {
          btn.classList.add('bg-amber-400', 'text-slate-950', 'font-bold');
          btn.classList.remove('bg-slate-800', 'text-slate-300');
        } else {
          btn.classList.remove('bg-amber-400', 'text-slate-950', 'font-bold');
          btn.classList.add('bg-slate-800', 'text-slate-300');
        }
      }
    });

    this.renderRecommendations(type);
  },

  openIdeaModal(ideaId) {
    const idea = this.recommendations.find(r => r.id === ideaId);
    if (!idea) return;

    this.selectedIdeaForDetail = idea;
    const modal = document.getElementById('idea-detail-modal');
    const container = document.getElementById('idea-detail-content');
    if (!modal || !container) return;

    container.innerHTML = `
      <div class="relative aspect-16-10 sm:h-80 w-full bg-slate-950 overflow-hidden">
        <img 
          src="${idea.image}" 
          alt="${idea.title}"
          onerror="window.handleImageError(this, '${idea.title}', 'Idea')"
          class="w-full h-full object-cover"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/40 to-black/30"></div>
        <button 
          type="button"
          onclick="App.closeIdeaModal()"
          class="absolute top-4 right-4 bg-black/60 hover:bg-black/90 text-white rounded-full p-2.5 backdrop-blur-md transition-all cursor-pointer z-10">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>

        <div class="absolute bottom-6 left-6 right-6">
          <div class="flex items-center gap-2 mb-2">
            <span class="bg-amber-400 text-slate-950 text-xs font-bold uppercase tracking-wider px-3 py-1 rounded-full">
              ${idea.event_type}
            </span>
            <span class="bg-white/20 backdrop-blur-md text-white text-xs font-medium px-3 py-1 rounded-full">
              ${idea.style}
            </span>
          </div>
          <h2 class="font-serif text-2xl sm:text-3xl font-bold text-white drop-shadow-md">
            ${idea.title}
          </h2>
        </div>
      </div>

      <div class="p-6 sm:p-8 space-y-6 bg-white text-slate-900 overflow-y-auto light-scrollbar">
        <div>
          <h3 class="text-xs font-bold uppercase tracking-widest text-amber-700 mb-1">Concept Atmosphere</h3>
          <p class="text-slate-700 leading-relaxed text-sm sm:text-base">
            ${idea.summary}
          </p>
        </div>

        <!-- Curated Highlights -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-widest text-slate-400 mb-3">Key Experience Highlights</h4>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            ${idea.highlights.map(h => `
              <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs sm:text-sm text-slate-800 flex items-start gap-2.5">
                <i data-lucide="sparkles" class="w-4 h-4 text-amber-500 mt-0.5 shrink-0"></i>
                <span>${h}</span>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Decor & Venue Style -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
            <span class="text-xs font-bold uppercase tracking-wider text-amber-800 block mb-1">Venue Style</span>
            <span class="text-sm font-semibold text-slate-900">${idea.venue_style || 'Curated Location'}</span>
          </div>
          <div class="p-4 bg-slate-50 rounded-xl border border-slate-200">
            <span class="text-xs font-bold uppercase tracking-wider text-amber-800 block mb-1">Color Palette</span>
            <div class="flex items-center gap-2 mt-1">
              ${(idea.color_palette || []).map(c => `
                <div class="w-6 h-6 rounded-full border border-slate-300" style="background-color: ${c.hex};" title="${c.name}"></div>
              `).join('')}
            </div>
          </div>
        </div>

        <!-- Suggested Budget Split -->
        <div class="p-5 bg-amber-50/40 rounded-2xl border border-amber-200/60">
          <div class="flex items-center justify-between mb-3">
            <h4 class="text-xs font-bold uppercase tracking-widest text-amber-900">Illustrative Budget Allocation</h4>
            <span class="text-sm font-bold text-amber-800">${idea.est_budget}</span>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            ${Object.entries(idea.budget_split || {}).map(([category, percent]) => `
              <div class="bg-white p-3 rounded-xl border border-amber-100 text-center">
                <span class="text-lg font-bold text-amber-700 block">${percent}</span>
                <span class="text-[11px] text-slate-500 font-medium block truncate">${category}</span>
              </div>
            `).join('')}
          </div>
        </div>

        <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pt-4 border-t border-slate-100">
          <div class="text-xs text-slate-400">
            *Curated editorial inspiration (GenAI service ready for automated vendor dispatch).
          </div>
          <button 
            type="button"
            onclick="App.applyIdeaToPlanner('${idea.id}')"
            class="w-full sm:w-auto py-3 px-6 rounded-xl font-bold text-sm gold-gradient-bg text-slate-950 shadow hover:shadow-md flex items-center justify-center gap-2 cursor-pointer">
            <span>Apply to Planner</span>
            <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>
        </div>
      </div>
    `;

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    if (window.lucide) lucide.createIcons();
  },

  closeIdeaModal() {
    const modal = document.getElementById('idea-detail-modal');
    if (modal) modal.classList.add('hidden');
    document.body.style.overflow = 'auto';
  },

  applyIdeaToPlanner(ideaId) {
    const idea = this.recommendations.find(r => r.id === ideaId);
    if (!idea) return;

    this.closeIdeaModal();
    this.planEventPreselected(idea.event_type, idea.theme_match || null);
    
    const titleInput = document.getElementById('planner-title');
    if (titleInput) titleInput.value = idea.title;

    if (idea.guest_count_val) {
      const gInput = document.getElementById('planner-guests');
      const gSlider = document.getElementById('planner-guests-slider');
      if (gInput) gInput.value = idea.guest_count_val;
      if (gSlider) gSlider.value = idea.guest_count_val;
    }

    if (idea.budget_val) {
      const bInput = document.getElementById('planner-budget');
      const bSlider = document.getElementById('planner-budget-slider');
      if (bInput) bInput.value = idea.budget_val;
      if (bSlider) bSlider.value = idea.budget_val;
    }

    this.updatePlannerBudgetBreakdown();
    this.showToast(`Applied concept '${idea.title}' to your planner!`, 'success');
  },

  // ----------------- PLANNER ENGINE -----------------
  setupPlannerCalculations() {
    const guestInput = document.getElementById('planner-guests');
    const guestSlider = document.getElementById('planner-guests-slider');
    const budgetInput = document.getElementById('planner-budget');
    const budgetSlider = document.getElementById('planner-budget-slider');

    if (guestInput && guestSlider) {
      guestSlider.addEventListener('input', (e) => {
        guestInput.value = e.target.value;
        this.updatePlannerBudgetBreakdown();
      });
      guestInput.addEventListener('input', (e) => {
        guestSlider.value = e.target.value;
        this.updatePlannerBudgetBreakdown();
      });
    }

    if (budgetInput && budgetSlider) {
      budgetSlider.addEventListener('input', (e) => {
        budgetInput.value = e.target.value;
        this.updatePlannerBudgetBreakdown();
      });
      budgetInput.addEventListener('input', (e) => {
        budgetSlider.value = e.target.value;
        this.updatePlannerBudgetBreakdown();
      });
    }

    const typeSelect = document.getElementById('planner-event-type');
    if (typeSelect) {
      typeSelect.addEventListener('change', (e) => {
        this.populateThemeDropdownForEvent(e.target.value);
        this.updatePlannerBudgetBreakdown();
      });
    }

    this.updatePlannerBudgetBreakdown();
  },

  updatePlannerBudgetBreakdown() {
    const budgetVal = parseFloat(document.getElementById('planner-budget')?.value || 25000);
    const guestsVal = parseInt(document.getElementById('planner-guests')?.value || 100);

    const costPerGuest = Math.round(budgetVal / Math.max(1, guestsVal));
    const costPerGuestEl = document.getElementById('planner-cost-per-guest');
    if (costPerGuestEl) costPerGuestEl.textContent = `$${costPerGuest}`;

    // Allocation percentages: Venue (35%), Catering (30%), Decor & Florals (15%), Photo & Video (12%), Entertainment (8%)
    const venueAmt = Math.round(budgetVal * 0.35);
    const cateringAmt = Math.round(budgetVal * 0.30);
    const decorAmt = Math.round(budgetVal * 0.15);
    const photoAmt = Math.round(budgetVal * 0.12);
    const musicAmt = Math.round(budgetVal * 0.08);

    const venueEl = document.getElementById('alloc-venue');
    const cateringEl = document.getElementById('alloc-catering');
    const decorEl = document.getElementById('alloc-decor');
    const photoEl = document.getElementById('alloc-photo');
    const musicEl = document.getElementById('alloc-music');

    if (venueEl) venueEl.textContent = window.formatCurrency(venueAmt);
    if (cateringEl) cateringEl.textContent = window.formatCurrency(cateringAmt);
    if (decorEl) decorEl.textContent = window.formatCurrency(decorAmt);
    if (photoEl) photoEl.textContent = window.formatCurrency(photoAmt);
    if (musicEl) musicEl.textContent = window.formatCurrency(musicAmt);
  },

  async handleSaveEvent(e) {
    if (e) e.preventDefault();

    const title = document.getElementById('planner-title')?.value.trim();
    const eventType = document.getElementById('planner-event-type')?.value;
    const theme = document.getElementById('planner-theme')?.value;
    const date = document.getElementById('planner-date')?.value;
    const guests = parseInt(document.getElementById('planner-guests')?.value || 50);
    const budget = parseFloat(document.getElementById('planner-budget')?.value || 15000);
    const venue = document.getElementById('planner-venue')?.value;
    const notes = document.getElementById('planner-notes')?.value;
    const saveBtn = document.getElementById('planner-save-btn');

    if (!title) {
      this.showToast('Please provide a title for your celebration.', 'warning');
      document.getElementById('planner-title')?.focus();
      return;
    }

    try {
      if (saveBtn) {
        saveBtn.disabled = true;
        saveBtn.innerHTML = `<span>Saving...</span>`;
      }

      const res = await fetch('/api/events', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title,
          event_type: eventType,
          theme: theme || 'Custom Style',
          guest_count: guests,
          budget,
          target_date: date || new Date().toISOString().split('T')[0],
          venue_preference: venue || 'Curated Venue',
          notes
        })
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Failed to save event.');

      this.userEvents.unshift(data.event);
      this.updateEventsBadge();
      this.renderUserEvents();
      this.showToast(data.message, 'success');

      this.switchTab('my-events');
    } catch (err) {
      this.showToast(err.message, 'error');
    } finally {
      if (saveBtn) {
        saveBtn.disabled = false;
        saveBtn.innerHTML = `<span>Save to My Events</span><i data-lucide="check" class="w-4 h-4"></i>`;
        if (window.lucide) lucide.createIcons();
      }
    }
  },

  // ----------------- RENDER MY EVENTS -----------------
  renderUserEvents() {
    const container = document.getElementById('my-events-grid');
    const emptyState = document.getElementById('my-events-empty');
    if (!container) return;

    if (this.userEvents.length === 0) {
      container.classList.add('hidden');
      if (emptyState) emptyState.classList.remove('hidden');
      return;
    }

    container.classList.remove('hidden');
    if (emptyState) emptyState.classList.add('hidden');

    container.innerHTML = this.userEvents.map(ev => {
      const matchedTheme = this.themes.find(t => t.name === ev.theme);
      const matchedType = this.eventTypes.find(t => t.title === ev.event_type);
      const bgImg = matchedTheme ? matchedTheme.image : (matchedType ? matchedType.image : 'https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=800&q=80');

      return `
        <div class="card-hover-lift bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-md flex flex-col justify-between">
          <div>
            <div class="relative h-44 bg-slate-900 overflow-hidden">
              <img 
                src="${bgImg}" 
                alt="${ev.title}"
                onerror="window.handleImageError(this, '${ev.title}', '${ev.event_type}')"
                class="w-full h-full object-cover"
              />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/30 to-black/30"></div>
              <span class="absolute top-3 left-3 bg-amber-400 text-slate-950 text-xs font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full">
                ${ev.event_type}
              </span>
              <span class="absolute top-3 right-3 bg-emerald-500/90 text-white text-[11px] font-semibold px-2 py-0.5 rounded-full backdrop-blur-sm">
                ${ev.status}
              </span>
              <div class="absolute bottom-3 left-3 right-3 text-white">
                <span class="text-xs text-amber-200 block font-medium">${ev.theme || 'Custom Theme'}</span>
                <h4 class="font-serif text-lg font-bold text-white truncate drop-shadow-sm">${ev.title}</h4>
              </div>
            </div>

            <div class="p-5 space-y-3">
              <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-100">
                  <span class="text-slate-400 block mb-0.5">Budget</span>
                  <span class="font-bold text-slate-800 text-sm">${window.formatCurrency(ev.budget)}</span>
                </div>
                <div class="p-2.5 bg-slate-50 rounded-xl border border-slate-100">
                  <span class="text-slate-400 block mb-0.5">Guest Count</span>
                  <span class="font-bold text-slate-800 text-sm">${ev.guest_count} Guests</span>
                </div>
              </div>

              <div class="text-xs text-slate-600 space-y-1">
                <div class="flex items-center gap-2">
                  <i data-lucide="calendar" class="w-3.5 h-3.5 text-amber-600"></i>
                  <span>Target Date: <strong>${ev.target_date}</strong></span>
                </div>
                <div class="flex items-center gap-2">
                  <i data-lucide="map-pin" class="w-3.5 h-3.5 text-amber-600"></i>
                  <span class="truncate">Venue: <strong>${ev.venue_preference}</strong></span>
                </div>
              </div>

              ${ev.notes ? `
                <div class="p-2.5 bg-amber-50/50 rounded-xl border border-amber-100 text-xs text-amber-900 line-clamp-2">
                  "${ev.notes}"
                </div>
              ` : ''}
            </div>
          </div>

          <div class="p-5 pt-0 flex items-center justify-between border-t border-slate-100 mt-2">
            <button 
              type="button"
              onclick="App.planEventPreselected('${ev.event_type}', '${ev.theme}')"
              class="text-xs font-semibold text-amber-700 hover:text-amber-800 flex items-center gap-1 cursor-pointer">
              <i data-lucide="edit-3" class="w-3.5 h-3.5"></i>
              <span>Customize</span>
            </button>
            <button 
              type="button"
              onclick="App.deleteEvent('${ev.id}')"
              class="text-xs text-rose-500 hover:text-rose-700 font-medium flex items-center gap-1 cursor-pointer">
              <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
              <span>Remove</span>
            </button>
          </div>
        </div>
      `;
    }).join('');

    if (window.lucide) lucide.createIcons();
  },

  async deleteEvent(eventId) {
    if (!confirm('Are you sure you want to remove this event from your planner?')) return;

    try {
      const res = await fetch(`/api/events/${eventId}`, { method: 'DELETE' });
      if (!res.ok) throw new Error('Failed to delete event');
      
      this.userEvents = this.userEvents.filter(e => e.id !== eventId);
      this.updateEventsBadge();
      this.renderUserEvents();
      this.showToast('Event removed from your planner.', 'info');
    } catch (err) {
      this.showToast(err.message, 'error');
    }
  },

  // ----------------- RENDER VENDORS -----------------
  renderVendors() {
    const container = document.getElementById('vendors-grid');
    if (!container) return;

    container.innerHTML = this.vendors.map(v => `
      <div class="card-hover-lift bg-white rounded-2xl overflow-hidden border border-slate-200/90 shadow-sm flex flex-col justify-between">
        <div>
          <div class="relative aspect-16-10 bg-slate-900 overflow-hidden">
            <img 
              src="${v.image}" 
              alt="${v.name}"
              onerror="window.handleImageError(this, '${v.name}', 'Vendor')"
              class="w-full h-full object-cover"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/20 to-black/20"></div>
            <span class="absolute top-3 left-3 bg-slate-900/80 text-amber-300 text-xs font-semibold px-2.5 py-1 rounded-full backdrop-blur-md border border-amber-500/20">
              ${v.badge}
            </span>
            <span class="absolute bottom-3 right-3 bg-amber-400 text-slate-950 font-bold text-xs px-2 py-0.5 rounded-md shadow-sm">
              ${v.price_tier}
            </span>
          </div>

          <div class="p-6">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-amber-700 tracking-wide uppercase">${v.category}</span>
              <div class="flex items-center gap-1 text-xs font-bold text-slate-800">
                <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400 text-amber-400"></i>
                <span>${v.rating}</span>
                <span class="text-slate-400 font-normal">(${v.reviews})</span>
              </div>
            </div>

            <h4 class="font-serif text-xl font-bold text-slate-900 mt-1">${v.name}</h4>
            <p class="text-xs text-slate-500 flex items-center gap-1 mt-1">
              <i data-lucide="map-pin" class="w-3.5 h-3.5 text-slate-400"></i>
              ${v.location}
            </p>
            <p class="text-xs text-slate-600 mt-3 leading-relaxed">
              ${v.specialty}
            </p>
          </div>
        </div>

        <div class="p-6 pt-0">
          <button 
            type="button"
            onclick="App.showToast('Inquiry concierge placeholder ready for next release.', 'info')"
            class="w-full py-2.5 px-4 rounded-xl border border-slate-300 hover:border-amber-400 text-slate-800 hover:text-amber-800 font-semibold text-xs transition-colors flex items-center justify-center gap-1.5 bg-slate-50 hover:bg-amber-50/50 cursor-pointer">
            <i data-lucide="send" class="w-3.5 h-3.5"></i>
            <span>Request Consultation</span>
          </button>
        </div>
      </div>
    `).join('');

    if (window.lucide) lucide.createIcons();
  },

  // ----------------- TOAST SYSTEM -----------------
  showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const icons = {
      success: `<i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-400 shrink-0"></i>`,
      error: `<i data-lucide="alert-circle" class="w-5 h-5 text-rose-400 shrink-0"></i>`,
      warning: `<i data-lucide="alert-triangle" class="w-5 h-5 text-amber-400 shrink-0"></i>`,
      info: `<i data-lucide="sparkles" class="w-5 h-5 text-amber-400 shrink-0"></i>`
    };

    const toast = document.createElement('div');
    toast.className = `toast-animate pointer-events-auto flex items-center gap-3 py-3 px-5 rounded-2xl shadow-xl text-sm font-medium text-white border glass-panel-dark border-amber-500/30 max-w-md w-full backdrop-blur-md`;

    toast.innerHTML = `
      ${icons[type] || icons.info}
      <span class="flex-1">${message}</span>
      <button onclick="this.parentElement.remove()" class="text-slate-400 hover:text-white transition-colors cursor-pointer">
        <i data-lucide="x" class="w-4 h-4"></i>
      </button>
    `;

    container.appendChild(toast);
    if (window.lucide) lucide.createIcons();

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translate(-50%, -10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 4200);
  },

  closeAllModals() {
    this.closeThemeModal();
    this.closeIdeaModal();
    Auth.closeModal('register-modal');
    Auth.closeModal('forgot-modal');
  }
};

window.App = App;

// Bootstrap on DOM loaded
document.addEventListener('DOMContentLoaded', () => {
  Auth.init();
  App.init();

  // Prevent accidental text carets / I-beam cursors when clicking informational cards and modals
  document.addEventListener('mousedown', (e) => {
    const isInput = e.target.closest('input, textarea, select');
    if (!isInput) {
      const isModalOrCard = e.target.closest('#theme-detail-modal, #idea-detail-modal, .planning-card');
      if (isModalOrCard) {
        if (window.getSelection) {
          window.getSelection().removeAllRanges();
        }
        const isInteractive = e.target.closest('button, [onclick], a');
        if (!isInteractive) {
          e.preventDefault();
        }
      }
    }
  });
});
