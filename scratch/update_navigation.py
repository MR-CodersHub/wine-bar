import os
import re

root_dir = r"d:\MR CodersHub\Front-end Projects\May Day\wine-bar-main\wine-bar-main"

html_files = []
for dirpath, _, filenames in os.walk(root_dir):
    for f in filenames:
        if f.endswith(".html"):
            html_files.append(os.path.join(dirpath, f))

print(f"Found {len(html_files)} HTML files to update.")

# New stylesheet rules
new_styles = """/* ── NAVBAR ACTIVE STATE ── */
    .nav-link {
      position: relative;
      padding-bottom: 2px;
    }
    .nav-link::after {
      content: '';
      position: absolute;
      bottom: -4px;
      left: 0;
      width: 0;
      height: 2px;
      border-radius: 999px;
      background: #6B1F24;
      transition: width .3s ease;
    }
    .dark .nav-link::after {
      background: #C8A97E;
    }
    .nav-link:hover::after,
    .nav-link.active::after {
      width: 100%;
    }
    .nav-link.active {
      color: #6B1F24;
      font-weight: 600;
    }
    .dark .nav-link.active {
      color: #C8A97E;
    }
    /* ── MOBILE NAV ACTIVE ── */
    .mobile-nav-link.active {
      color: #6B1F24;
      font-weight: 600;
      border-left: 3px solid #6B1F24;
      padding-left: 10px;
    }
    .dark .mobile-nav-link.active {
      color: #C8A97E;
      border-left-color: #C8A97E;
    }
    """

# New JS block
new_js = """// INITIALIZE ICONS & MOBILE MENU & THEME TOGGLE
    const html = document.documentElement;
    const themeToggle = document.getElementById('themeToggle');
    const menuBtn = document.getElementById('menuBtn');
    const mobileMenu = document.getElementById('mobileMenu');

    // Check and set initial theme
    if (
      localStorage.theme === 'dark' ||
      (
        !('theme' in localStorage) &&
        window.matchMedia('(prefers-color-scheme: dark)').matches
      )
    ) {
      html.classList.add('dark');
    } else {
      html.classList.remove('dark');
    }

    // Function to set toggle button icon
    function updateThemeIcon() {
      const themeIcon = themeToggle ? themeToggle.querySelector('i') : null;
      if (themeIcon) {
        if (html.classList.contains('dark')) {
          themeIcon.setAttribute('data-lucide', 'sun');
        } else {
          themeIcon.setAttribute('data-lucide', 'moon');
        }
        lucide.createIcons();
      }
    }

    // Initialize theme icon
    if (themeToggle) {
      updateThemeIcon();
      
      themeToggle.addEventListener('click', () => {
        html.classList.toggle('dark');
        if (html.classList.contains('dark')) {
          localStorage.theme = 'dark';
        } else {
          localStorage.theme = 'light';
        }
        updateThemeIcon();
      });
    } else {
      lucide.createIcons();
    }

    // Mobile Menu handler with icon toggling (menu <-> x)
    if (menuBtn && mobileMenu) {
      menuBtn.addEventListener('click', () => {
        const isHidden = mobileMenu.classList.contains('hidden');
        if (isHidden) {
          mobileMenu.classList.remove('hidden');
          const menuIcon = menuBtn.querySelector('i');
          if (menuIcon) {
            menuIcon.setAttribute('data-lucide', 'x');
            lucide.createIcons();
          }
        } else {
          mobileMenu.classList.add('hidden');
          const menuIcon = menuBtn.querySelector('i');
          if (menuIcon) {
            menuIcon.setAttribute('data-lucide', 'menu');
            lucide.createIcons();
          }
        }
      });
    }

    // Close mobile menu on window resize
    window.addEventListener('resize', () => {
      if (window.innerWidth >= 1024) { // lg breakpoint
        if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
          mobileMenu.classList.add('hidden');
          const menuIcon = menuBtn ? menuBtn.querySelector('i') : null;
          if (menuIcon) {
            menuIcon.setAttribute('data-lucide', 'menu');
            lucide.createIcons();
          }
        }
      }
    });"""

# Header template for root
root_header_template = """  <!-- NAVBAR -->
  <header class="fixed top-0 w-full z-50">

    <nav class="glass bg-white/70 dark:bg-black/20 border-b border-black/5 dark:border-white/10">

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10">

        <div class="h-20 flex items-center justify-between">

          <!-- LOGO -->
          <a href="./index.html"
            class="font-heading text-2xl sm:text-3xl md:text-4xl tracking-wide flex items-center gap-1.5 sm:gap-2 shrink-0">
            <img src="./assets/images/brand-logo.png" alt="brand-logo" class="w-8 sm:w-10 md:w-[44px] h-auto shrink-0">
            <span>Vintara</span>
          </a>

          <!-- MENU -->
          <div class="hidden lg:flex items-center gap-6 xl:gap-10 text-sm">

            <a href="./index.html" class="nav-link {home_act}">
              Home
            </a>

            <a href="./pages/home.html" class="nav-link {home2_act}">
              Home 2
            </a>

            <a href="./pages/about.html" class="nav-link {about_act}">
              About
            </a>

            <a href="./pages/service.html" class="nav-link {service_act}">
              Service
            </a>

            <a href="./pages/wine-menu.html" class="nav-link {menu_act}">
              Wine Menu
            </a>

            <a href="./pages/blog.html" class="nav-link {blog_act}">
              Blog
            </a>

            <a href="./pages/contact.html" class="nav-link {contact_act}">
              Contact
            </a>

          </div>

          <!-- RIGHT -->
          <div class="flex items-center gap-2 sm:gap-4 shrink-0">

            <!-- TOGGLE -->
            <button id="themeToggle"
              class="w-10 h-10 sm:w-11 sm:h-11 rounded-full border border-black/10 dark:border-white/10 flex items-center justify-center hover:scale-105 shrink-0">
              <i data-lucide="moon" class="w-4 h-4 sm:w-5 sm:h-5"></i>
            </button>

            <!-- MOBILE MENU BTN -->
            <button id="menuBtn"
              class="lg:hidden w-10 h-10 sm:w-11 sm:h-11 rounded-full border border-black/10 dark:border-white/10 flex items-center justify-center shrink-0">
              <i data-lucide="menu" class="w-4 h-4 sm:w-5 sm:h-5"></i>
            </button>

          </div>

        </div>

      </div>

    </nav>

    <!-- MOBILE MENU -->
    <div id="mobileMenu"
      class="hidden lg:hidden bg-white dark:bg-[#120d0d] border-b border-black/5 dark:border-white/10">

      <div class="px-6 py-6 flex flex-col gap-5 text-sm">

        <a href="./index.html" class="mobile-nav-link {home_act}">Home</a>
        <a href="./pages/home.html" class="mobile-nav-link {home2_act}">Home 2</a>
        <a href="./pages/about.html" class="mobile-nav-link {about_act}">About</a>
        <a href="./pages/service.html" class="mobile-nav-link {service_act}">Service</a>
        <a href="./pages/wine-menu.html" class="mobile-nav-link {menu_act}">Wine Menu</a>
        <a href="./pages/blog.html" class="mobile-nav-link {blog_act}">Blog</a>
        <a href="./pages/contact.html" class="mobile-nav-link {contact_act}">Contact</a>

      </div>

    </div>

  </header>"""

# Header template for pages
pages_header_template = """  <!-- NAVBAR -->
  <header class="fixed top-0 w-full z-50">

    <nav class="glass bg-white/70 dark:bg-black/20 border-b border-black/5 dark:border-white/10">

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-10">

        <div class="h-20 flex items-center justify-between">

          <!-- LOGO -->
          <a href="../index.html"
            class="font-heading text-2xl sm:text-3xl md:text-4xl tracking-wide flex items-center gap-1.5 sm:gap-2 shrink-0">
            <img src="../assets/images/brand-logo.png" alt="brand-logo" class="w-8 sm:w-10 md:w-[44px] h-auto shrink-0">
            <span>Vintara</span>
          </a>

          <!-- MENU -->
          <div class="hidden lg:flex items-center gap-6 xl:gap-10 text-sm">

            <a href="../index.html" class="nav-link {home_act}">
              Home
            </a>

            <a href="./home.html" class="nav-link {home2_act}">
              Home 2
            </a>

            <a href="./about.html" class="nav-link {about_act}">
              About
            </a>

            <a href="./service.html" class="nav-link {service_act}">
              Service
            </a>

            <a href="./wine-menu.html" class="nav-link {menu_act}">
              Wine Menu
            </a>

            <a href="./blog.html" class="nav-link {blog_act}">
              Blog
            </a>

            <a href="./contact.html" class="nav-link {contact_act}">
              Contact
            </a>

          </div>

          <!-- RIGHT -->
          <div class="flex items-center gap-2 sm:gap-4 shrink-0">

            <!-- TOGGLE -->
            <button id="themeToggle"
              class="w-10 h-10 sm:w-11 sm:h-11 rounded-full border border-black/10 dark:border-white/10 flex items-center justify-center hover:scale-105 shrink-0">
              <i data-lucide="moon" class="w-4 h-4 sm:w-5 sm:h-5"></i>
            </button>

            <!-- MOBILE MENU BTN -->
            <button id="menuBtn"
              class="lg:hidden w-10 h-10 sm:w-11 sm:h-11 rounded-full border border-black/10 dark:border-white/10 flex items-center justify-center shrink-0">
              <i data-lucide="menu" class="w-4 h-4 sm:w-5 sm:h-5"></i>
            </button>

          </div>

        </div>

      </div>

    </nav>

    <!-- MOBILE MENU -->
    <div id="mobileMenu"
      class="hidden lg:hidden bg-white dark:bg-[#120d0d] border-b border-black/5 dark:border-white/10">

      <div class="px-6 py-6 flex flex-col gap-5 text-sm">

        <a href="../index.html" class="mobile-nav-link {home_act}">Home</a>
        <a href="./home.html" class="mobile-nav-link {home2_act}">Home 2</a>
        <a href="./about.html" class="mobile-nav-link {about_act}">About</a>
        <a href="./service.html" class="mobile-nav-link {service_act}">Service</a>
        <a href="./wine-menu.html" class="mobile-nav-link {menu_act}">Wine Menu</a>
        <a href="./blog.html" class="mobile-nav-link {blog_act}">Blog</a>
        <a href="./contact.html" class="mobile-nav-link {contact_act}">Contact</a>

      </div>

    </div>

  </header>"""

for file_path in html_files:
    rel_path = os.path.relpath(file_path, root_dir)
    filename = os.path.basename(file_path)
    is_root = os.path.dirname(rel_path) == ""
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Determine which link should be active
    states = {
        "home_act": "", "home2_act": "", "about_act": "", "service_act": "",
        "menu_act": "", "blog_act": "", "contact_act": ""
    }
    
    if filename == "index.html":
        states["home_act"] = "active"
    elif filename == "home.html":
        states["home2_act"] = "active"
    elif filename == "about.html":
        states["about_act"] = "active"
    elif filename == "wine-menu.html":
        states["menu_act"] = "active"
    elif filename.startswith("service"):
        states["service_act"] = "active"
    elif filename.startswith("blog"):
        states["blog_act"] = "active"
    elif filename == "contact.html":
        states["contact_act"] = "active"
        
    header_template = root_header_template if is_root else pages_header_template
    formatted_header = header_template.format(**states)

    # 1. Replace the entire NAVBAR header block
    header_pattern = r'<!-- NAVBAR -->\s*<header.*?</header>'
    new_content, count_header = re.subn(header_pattern, formatted_header, content, flags=re.DOTALL)
    
    if count_header == 0:
        # Fallback: find first <header>...</header>
        fallback_header_pattern = r'<header.*?</header>'
        new_content, count_header = re.subn(fallback_header_pattern, formatted_header, new_content, count=1, flags=re.DOTALL)

    # 2. Replace style overrides in <style>
    styles_pattern = r'/\*\s*──\s*NAVBAR ACTIVE STATE\s*──\s*\*/.*?(/\*\s*──\s*FOOTER\s*──\s*\*/|</style>)'
    new_content, count_styles = re.subn(styles_pattern, lambda m: new_styles + m.group(1), new_content, flags=re.DOTALL)
    
    # Fallback for styles if they aren't marked with comments
    if count_styles == 0:
        style_block_pattern = r'(</style>)'
        new_content, count_styles = re.subn(style_block_pattern, r'\n    ' + new_styles + r'\1', new_content, count=1)

    # 3. Replace theme/menu toggling JavaScript logic
    js_pattern = r'lucide\.createIcons\(\);.*?themeToggle\.addEventListener\(\s*[\'"]click[\'"]\s*,\s*\(\)\s*=>\s*\{.*?\}\s*\);'
    new_content, count_js = re.subn(js_pattern, new_js, new_content, flags=re.DOTALL)
    
    # Fallback for JS if spacing/format slightly different
    if count_js == 0:
        # Fallback target: replace from lucide.createIcons(); up to click toggle handler
        fallback_js_pattern = r'lucide\.createIcons\(\);.*?(themeToggle\.addEventListener\(\s*[\'"]click[\'"]\s*,\s*\(\)\s*=>\s*\{.*?\}\s*\);|themeToggle\.addEventListener\(\s*[\'"]click[\'"]\s*,\s*function.*?\}\s*\);)'
        new_content, count_js = re.subn(fallback_js_pattern, new_js, new_content, flags=re.DOTALL)

    # If it still has 0 js replacement, let's look for standard mobile menu toggle
    if count_js == 0:
        # Let's try replacing from '// MOBILE MENU' to the end of themeToggle listener
        fallback_js_pattern2 = r'//\s*MOBILE MENU.*?themeToggle\.addEventListener\(\s*[\'"]click[\'"]\s*,\s*\(\)\s*=>\s*\{.*?\}\s*\);'
        new_content, count_js = re.subn(fallback_js_pattern2, new_js, new_content, flags=re.DOTALL)

    if count_header > 0 or count_styles > 0 or count_js > 0:
        print(f"Updated {rel_path} -> Header: {count_header}, Styles: {count_styles}, JS: {count_js}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        print(f"No changes made to {rel_path}")
