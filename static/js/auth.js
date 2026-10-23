/**
 * CelebrAI - Authentication Module
 * Handles Demo Authentication, Validation, Session State, and Security Indicators.
 */

const Auth = {
  currentUser: null,
  authToken: null,

  init() {
    // Check localStorage for existing session
    const savedUser = localStorage.getItem('celebrAi_user');
    const savedToken = localStorage.getItem('celebrAi_token');

    if (savedUser && savedToken) {
      try {
        this.currentUser = JSON.parse(savedUser);
        this.authToken = savedToken;
        this.onLoginSuccess(this.currentUser, false);
        return;
      } catch (e) {
        localStorage.removeItem('celebrAi_user');
        localStorage.removeItem('celebrAi_token');
      }
    }

    // Otherwise show login view
    this.showLoginView();
  },

  showLoginView() {
    const loginSection = document.getElementById('login-view');
    const appShell = document.getElementById('app-shell');
    if (loginSection) loginSection.classList.remove('hidden');
    if (appShell) appShell.classList.add('hidden');
  },

  hideLoginView() {
    const loginSection = document.getElementById('login-view');
    const appShell = document.getElementById('app-shell');
    if (loginSection) loginSection.classList.add('hidden');
    if (appShell) appShell.classList.remove('hidden');
  },

  togglePasswordVisibility(inputId, toggleBtnId) {
    const input = document.getElementById(inputId);
    const btn = document.getElementById(toggleBtnId);
    if (!input) return;

    if (input.type === 'password') {
      input.type = 'text';
      if (btn) btn.innerHTML = `<i data-lucide="eye-off" class="w-5 h-5 text-amber-400"></i>`;
    } else {
      input.type = 'password';
      if (btn) btn.innerHTML = `<i data-lucide="eye" class="w-5 h-5 text-slate-400 hover:text-white"></i>`;
    }
    if (window.lucide) lucide.createIcons();
  },

  fillDemoCredentials() {
    const emailInput = document.getElementById('login-email');
    const passInput = document.getElementById('login-password');
    if (emailInput && passInput) {
      emailInput.value = 'alexa.celebrate@example.com';
      passInput.value = 'CelebrAI2026!';
      this.clearError('login-error');
      
      // Visual flash effect on inputs
      emailInput.classList.add('ring-2', 'ring-amber-400');
      passInput.classList.add('ring-2', 'ring-amber-400');
      setTimeout(() => {
        emailInput.classList.remove('ring-2', 'ring-amber-400');
        passInput.classList.remove('ring-2', 'ring-amber-400');
      }, 700);

      window.App.showToast("Demo credentials loaded! Click 'Sign In' or 'Quick Demo Login'.", "info");
    }
  },

  async handleLogin(event) {
    if (event) event.preventDefault();
    this.clearError('login-error');

    const emailInput = document.getElementById('login-email');
    const passInput = document.getElementById('login-password');
    const loginBtn = document.getElementById('login-submit-btn');

    const email = emailInput ? emailInput.value.trim() : '';
    const password = passInput ? passInput.value : '';

    // Validation
    if (!email) {
      this.showError('login-error', 'Please enter your email address.');
      emailInput?.focus();
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      this.showError('login-error', 'Please provide a valid email format (e.g., name@domain.com).');
      emailInput?.focus();
      return;
    }

    if (!password) {
      this.showError('login-error', 'Please enter your password.');
      passInput?.focus();
      return;
    }

    if (password.length < 6) {
      this.showError('login-error', 'Password must contain at least 6 characters.');
      passInput?.focus();
      return;
    }

    // Button loading state
    const originalBtnText = loginBtn ? loginBtn.innerHTML : 'Sign In';
    if (loginBtn) {
      loginBtn.disabled = true;
      loginBtn.innerHTML = `
        <span class="inline-flex items-center gap-2">
          <svg class="animate-spin h-4 w-4 text-slate-900" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          Authenticating...
        </span>`;
    }

    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: email,
          password: password,
          is_demo: (email === 'alexa.celebrate@example.com')
        })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Login failed. Please verify credentials.');
      }

      // Success
      this.currentUser = data.user;
      this.authToken = data.token;
      localStorage.setItem('celebrAi_user', JSON.stringify(data.user));
      localStorage.setItem('celebrAi_token', data.token);

      this.onLoginSuccess(data.user, true, data.security_notice);
    } catch (err) {
      this.showError('login-error', err.message);
    } finally {
      if (loginBtn) {
        loginBtn.disabled = false;
        loginBtn.innerHTML = originalBtnText;
      }
    }
  },

  async handleRegister(event) {
    if (event) event.preventDefault();
    this.clearError('register-error');

    const name = document.getElementById('reg-name')?.value.trim();
    const email = document.getElementById('reg-email')?.value.trim();
    const password = document.getElementById('reg-password')?.value;
    const confirm = document.getElementById('reg-confirm-password')?.value;
    const submitBtn = document.getElementById('reg-submit-btn');

    if (!name) {
      this.showError('register-error', 'Please provide your full name.');
      return;
    }
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      this.showError('register-error', 'Please enter a valid email address.');
      return;
    }
    if (!password || password.length < 6) {
      this.showError('register-error', 'Password must be at least 6 characters.');
      return;
    }
    if (password !== confirm) {
      this.showError('register-error', 'Passwords do not match. Please re-enter.');
      return;
    }

    try {
      submitBtn.disabled = true;
      const res = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Registration failed.');

      this.currentUser = data.user;
      this.authToken = data.token;
      localStorage.setItem('celebrAi_user', JSON.stringify(data.user));
      localStorage.setItem('celebrAi_token', data.token);

      this.closeModal('register-modal');
      this.onLoginSuccess(data.user, true);
    } catch (err) {
      this.showError('register-error', err.message);
    } finally {
      if (submitBtn) submitBtn.disabled = false;
    }
  },

  async handleForgotPassword(event) {
    if (event) event.preventDefault();
    const emailInput = document.getElementById('forgot-email');
    const msgBox = document.getElementById('forgot-message');
    const email = emailInput ? emailInput.value.trim() : '';

    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      if (msgBox) {
        msgBox.innerHTML = `<span class="text-rose-400">Please enter a valid email address.</span>`;
        msgBox.classList.remove('hidden');
      }
      return;
    }

    try {
      const res = await fetch('/api/auth/forgot-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
      });
      const data = await res.json();
      if (msgBox) {
        msgBox.innerHTML = `<span class="text-emerald-400">✓ ${data.message}</span>`;
        msgBox.classList.remove('hidden');
      }
      setTimeout(() => {
        this.closeModal('forgot-modal');
        if (msgBox) msgBox.classList.add('hidden');
      }, 3200);
    } catch (e) {
      if (msgBox) {
        msgBox.innerHTML = `<span class="text-rose-400">Unable to process request right now.</span>`;
        msgBox.classList.remove('hidden');
      }
    }
  },

  onLoginSuccess(user, notify = true, securityNotice = null) {
    this.hideLoginView();
    
    // Update profile in navigation
    const userAvatar = document.getElementById('nav-user-avatar');
    const userName = document.getElementById('nav-user-name');
    const userRole = document.getElementById('nav-user-role');
    const demoBadge = document.getElementById('demo-auth-pill');

    if (userAvatar) userAvatar.src = user.avatar;
    if (userName) userName.textContent = user.name;
    if (userRole) userRole.textContent = user.role;
    if (demoBadge) {
      if (user.is_demo) {
        demoBadge.classList.remove('hidden');
      } else {
        demoBadge.classList.add('hidden');
      }
    }

    if (notify) {
      window.App.showToast(`Welcome back, ${user.name.split(' ')[0]}! Ready to plan unforgettable moments.`, 'success');
      if (securityNotice) {
        console.info(`[CelebrAI Security] ${securityNotice}`);
      }
    }

    // Refresh application views
    if (window.App && window.App.refreshData) {
      window.App.refreshData();
    }
    
    // Smooth scroll to top of home page
    window.scrollTo({ top: 0, behavior: 'smooth' });
  },

  logout() {
    this.currentUser = null;
    this.authToken = null;
    localStorage.removeItem('celebrAi_user');
    localStorage.removeItem('celebrAi_token');
    
    // Close any open menus
    const profileDropdown = document.getElementById('profile-dropdown');
    if (profileDropdown) profileDropdown.classList.add('hidden');

    this.showLoginView();
    window.App.showToast('You have been securely logged out.', 'info');
  },

  showError(elementId, message) {
    const el = document.getElementById(elementId);
    if (el) {
      el.textContent = message;
      el.classList.remove('hidden');
    }
  },

  clearError(elementId) {
    const el = document.getElementById(elementId);
    if (el) {
      el.textContent = '';
      el.classList.add('hidden');
    }
  },

  openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.remove('hidden');
  },

  closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.add('hidden');
  }
};

window.Auth = Auth;
