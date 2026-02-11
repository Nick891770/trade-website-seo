# Website Performance Quick Wins — Action Checklist

lawselecservices.com | All steps are free | Created 10 Feb 2026

**Hosting confirmed**: Nginx on SiteGround (detected from server headers)

---

## STEP 1: Remove Plugin Bloat
**Where**: wp-admin > Plugins > Installed Plugins

- [ ] **Deactivate & delete WooCommerce** — not in use, removes JS/CSS/cart overhead from every page
- [ ] **Deactivate & delete LiteSpeed Cache** — caching features don't work on your Nginx server (requires LiteSpeed server or QUIC.cloud). Replaced by Speed Optimizer in Step 5
- [ ] **Check Contact Form 7 vs Forminator** — visit each form on the site, see which plugin actually powers it, deactivate the other one
- [ ] **Review ElementsKit** — if you're not using its widgets (fancy sliders, mega menus), deactivate it. Elementor Pro does most things natively
- [ ] **Review Google Site Kit** — if you check Analytics directly at analytics.google.com, deactivate this (it loads extra JS on the frontend)

**Expected result**: 3-5 fewer plugins, noticeably less JS/CSS loaded on every page.

---

## STEP 2: Fix the Logo Image
**Where**: wp-admin > Media Library

The logo (`Laws-Electrical-Standard-Logo-1-1-scaled.jpg`) is **2560x1762px** — massive for a logo.

Optimised version already created: `performance-snippets/optimised-images/laws-electrical-logo-400w.webp` (400x275, 7.5KB — 95% smaller)

- [ ] Upload `laws-electrical-logo-400w.webp` to Media Library
- [ ] Go to Elementor > Site Settings > Site Identity > update the logo to the new file
- [ ] Delete the old oversized version from Media Library

---

## STEP 3: Fix the Hero Image
**Where**: wp-admin > Media Library + Elementor page editor

The hero (`Artboard-–-22.png`) is **1678x1258px PNG (3MB!)** — wrong format for a photo.

Optimised version already created: `performance-snippets/optimised-images/hero-banner-1200w.webp` (1200x899, 116KB — 96% smaller)

- [ ] Upload `hero-banner-1200w.webp` to Media Library
- [ ] Edit the homepage in Elementor, swap the hero image to the new file
- [ ] In the image widget settings, set width to **1200** and height to **899**

---

## STEP 4: Bulk Image Optimisation
**Where**: wp-admin > Plugins > Add New

- [ ] Search for and install **ShortPixel Image Optimizer** (free tier = 100 images/month)
- [ ] Activate it and go through the setup wizard
- [ ] Set it to **convert uploads to WebP** automatically
- [ ] Enable **"Resize large images"** and cap at **1920px wide**
- [ ] Run **bulk optimisation** on existing Media Library images
- [ ] Wait for it to process (may take a few minutes)

---

## STEP 5: Configure Speed Optimizer (SiteGround)
**Where**: wp-admin > Speed Optimizer (already installed)

This is SiteGround's own plugin (formerly called "SG Optimizer"). It's built for your Nginx server. You already have it — just need to configure it.

- [ ] Go to **Speed Optimizer** in the wp-admin sidebar
- [ ] **Caching tab**:
  - [ ] Enable Dynamic Caching (NGINX Direct Delivery) — ON
  - [ ] Enable File-Based Caching — ON
  - [ ] Enable Memcached — ON (if available on your plan)
  - [ ] Browser Caching — should already be ON
- [ ] **Environment tab**:
  - [ ] Enable GZIP Compression — ON
  - [ ] Enable Browser Caching — ON
- [ ] **Frontend tab**:
  - [ ] Minify JavaScript — ON (test site after)
  - [ ] Minify CSS — ON (test site after)
  - [ ] Combine JavaScript — OFF (can cause issues with Elementor)
  - [ ] Combine CSS — OFF (can cause issues with Elementor)
  - [ ] Defer Render-blocking JS — ON (this replaces Snippet 3 below — use **one or the other**, not both)
- [ ] **Media tab**:
  - [ ] Lazy Load Media — ON
  - [ ] Generate WebP copies — ON (if available — this may overlap with ShortPixel)

**NOTE**: If Speed Optimizer's "Defer Render-blocking JS" is ON, do NOT activate Snippet 3 (defer JS) — they do the same thing and having both active can cause conflicts.

---

## STEP 6: Add Preconnect Hints
**Where**: wp-admin > Plugins > Add New (install Code Snippets plugin first)

- [ ] Install the **Code Snippets** plugin (free)
- [ ] Go to Snippets > Add New
- [ ] Name it: `Laws Electrical — Preconnect Hints`
- [ ] Paste the code from `performance-snippets/snippet-1-preconnect-hints.php`
- [ ] Set to **"Run snippet everywhere"**
- [ ] Save and Activate

---

## STEP 7: Fix font-display: swap
**Where**: Check Elementor first, then Code Snippets

- [ ] **First check**: Go to Elementor > Custom Fonts. If there's a `font-display` dropdown for the Items-Regular font, set it to **"swap"** and you're done — skip the code snippet
- [ ] **If no setting exists**: Go to Snippets > Add New
- [ ] Name it: `Laws Electrical — Font Display Swap`
- [ ] Paste the code from `performance-snippets/snippet-2-font-display-swap.php`
- [ ] Set to **"Run snippet everywhere"**
- [ ] Save and Activate

---

## STEP 8: Add Missing Image Dimensions
**Where**: Elementor page editor

Go through each page and ensure every image widget has explicit width and height. This prevents Cumulative Layout Shift (CLS).

Pages to check:
- [ ] Homepage
- [ ] /industrial-electrician-brisbane/
- [ ] /electrical-compliance-testing-brisbane/
- [ ] /maintenance-contracts/
- [ ] All suburb pages

**How**: Edit page in Elementor > click each image widget > in the left panel under Image Size, set width and height to match the actual display size.

---

## STEP 9: Defer Non-Critical JS
**Where**: Code Snippets plugin

**IMPORTANT**: Skip this step if you turned on Speed Optimizer's "Defer Render-blocking JS" in Step 5. They do the same thing.

- [ ] Go to Snippets > Add New
- [ ] Name it: `Laws Electrical — Defer Non-Critical JS`
- [ ] Paste the code from `performance-snippets/snippet-3-defer-js.php`
- [ ] Set to **"Only run in the front end"**
- [ ] Save and Activate
- [ ] **Test the site immediately** — check forms, navigation, dropdowns, sliders
- [ ] If something breaks, deactivate the snippet (it's safe to undo)

---

## STEP 10: Cloudflare Free CDN (Optional — Skip for Now)
Only do this if you want to go further after completing steps 1-9.

- [ ] Sign up at cloudflare.com (free plan)
- [ ] Point DNS nameservers to Cloudflare (involves changing nameservers at your domain registrar)
- [ ] Enable Auto Minify for JS/CSS/HTML
- [ ] Enable Brotli compression
- [ ] Set browser cache TTL to 1 month

---

## VERIFICATION (Do This After Steps 1-9)

- [ ] Clear Speed Optimizer cache: wp-admin > Speed Optimizer > Purge Cache
- [ ] Run PageSpeed Insights: https://pagespeed.web.dev/ — test homepage on both mobile and desktop
- [ ] Record the scores (compare to baseline)
- [ ] Test ALL pages for broken functionality:
  - [ ] Contact forms submit correctly
  - [ ] Navigation works (all menus, dropdowns)
  - [ ] Images all load correctly
  - [ ] No layout shifts or visual glitches
  - [ ] Mobile menu works
- [ ] Check Core Web Vitals in Google Search Console after a few days

---

## Files Reference

All code snippets are saved in:
```
laws-elec-skills/Website/performance-snippets/
├── snippet-1-preconnect-hints.php
├── snippet-2-font-display-swap.php
└── snippet-3-defer-js.php
```

Optimised images ready to upload:
```
laws-elec-skills/Website/performance-snippets/optimised-images/
├── laws-electrical-logo-400w.webp    (7.5KB — was 148KB)
└── hero-banner-1200w.webp            (116KB — was 3,024KB)
```

Image conversion tool (free, browser-based): https://squoosh.app

---

## Quick Priority Order

If you're short on time, do these first (biggest impact):

1. **Delete WooCommerce** (Step 1) — instant win, removes tons of bloat
2. **Fix the logo** (Step 2) — loads on every page, oversized
3. **Configure Speed Optimizer** (Step 5) — caching is the single biggest speed improvement
4. **Install ShortPixel** (Step 4) — bulk image compression
5. Everything else
