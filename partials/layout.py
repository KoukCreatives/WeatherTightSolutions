"""Global partials: head, header, footer, contact section, forms, logo strip.
Edit here once and rebuild (python3 build.py) to update every page."""
from icons import *

PHONE_AKL = "0800 532 578"
PHONE_AKL_TEL = "0800532578"
PHONE_WKO = "021 163 6232"
PHONE_WKO_TEL = "0211636232"

SUPPLIERS = [
    ("master-builders", "Registered Master Builders"),
    ("master-inspector", "Registered Master Inspector Association NZ"),
    ("lbp", "Licensed Building Practitioner"),
    ("branz", "BRANZ"),
    ("nzgbc", "New Zealand Green Building Council"),
    ("bcito", "BCITO"),
    ("hazardco", "HazardCo"),
    ("no-cowboys", "No Cowboys"),
    ("most-trusted-2025", "Most Trusted Winner 2025"),
]


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0c1620">
<link rel="icon" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
"""


def header(services, active=""):
    def cls(key):
        return "nav__link is-active" if key == active else "nav__link"
    drop = "".join(
        f'<a href="{s["slug"]}.html"><img src="assets/img/{s["img"]}.jpg" alt="" loading="lazy">'
        f'<div><strong>{s["name"]}</strong><span>{s["short"]}</span></div></a>' for s in services)
    mob = "".join(f'<a class="sub" href="{s["slug"]}.html">{s["name"]}</a>' for s in services)
    return f"""
<div class="topbar">
  <div class="container">
    <div class="topbar__left">
      <span class="topbar__item">{PIN}Auckland and Waikato</span>
      <span class="topbar__item hide-md">{CLOCK}Mon to Sat, 8.30am to 5.00pm</span>
    </div>
    <div class="topbar__right">
      <span class="topbar__item"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>Rated 5.0 on Google</span>
      <a class="topbar__item" href="tel:{PHONE_AKL_TEL}">{PHONE}Auckland {PHONE_AKL}</a>
      <a class="topbar__item" href="tel:{PHONE_WKO_TEL}">{PHONE}Waikato {PHONE_WKO}</a>
    </div>
  </div>
</div>
<header class="header">
  <div class="container">
    <a class="logo" href="index.html" aria-label="Weather Tight Solutions home"><img src="assets/img/logo.png" alt="Weather Tight Solutions, building inspection specialists" width="630" height="213"></a>
    <ul class="nav">
      <li><a class="{cls('home')}" href="index.html">Home</a></li>
      <li><a class="{cls('about')}" href="about.html">About</a></li>
      <li class="has-drop"><a class="{cls('services')}" href="weathertight-building-inspections.html">Services {CHEV}</a>
        <div class="drop">{drop}</div></li>
      <li><a class="{cls('peer')}" href="peer-reviews.html">Peer Reviews</a></li>
      <li><a class="{cls('inspector')}" href="qualified-building-inspector-auckland.html">Our Inspector</a></li>
      <li><a class="{cls('contact')}" href="contact.html">Contact</a></li>
    </ul>
    <div class="header__cta">
      <a class="header__phone" href="tel:{PHONE_AKL_TEL}"><span class="icon-circle pulse">{PHONE}</span><div><small>Call us free</small><strong>{PHONE_AKL}</strong></div></a>
      <a class="btn btn--yellow" href="contact.html#quote">Free Quote {ARROW}</a>
    </div>
    <div class="mobile-actions">
      <a class="icon-circle" href="tel:{PHONE_AKL_TEL}" aria-label="Call {PHONE_AKL}">{PHONE}</a>
      <button class="burger" data-open-menu aria-label="Open menu"><span></span></button>
    </div>
  </div>
</header>
<div class="drawer" aria-hidden="true">
  <div class="drawer__bg" data-close-menu></div>
  <div class="drawer__panel">
    <div class="drawer__head"><img src="assets/img/logo-white.png" alt="Weather Tight Solutions"><button class="drawer__close" data-close-menu aria-label="Close menu">&times;</button></div>
    <nav>
      <a href="index.html">Home</a><a href="about.html">About</a>
      <a href="weathertight-building-inspections.html">Services</a>{mob}
      <a href="peer-reviews.html">Peer Reviews</a>
      <a href="qualified-building-inspector-auckland.html">Our Inspector</a>
      <a href="contact.html">Contact</a>
    </nav>
    <a class="btn btn--yellow btn--block" href="contact.html#quote">Get a Free Quote {ARROW}</a>
    <a class="btn btn--blue btn--block" href="tel:{PHONE_AKL_TEL}">{PHONE} {PHONE_AKL}</a>
  </div>
</div>
<main id="main">
"""


def quote_form(services, title="Get a free quote", sub="Fill out the form and we will contact you within 24 hours.", tag="h2", fid="quote"):
    opts = "".join(f"<option>{s['name']}</option>" for s in services) + "<option>Free peer review</option><option>Something else</option>"
    return f"""
<div class="form-card" id="{fid}">
  <{tag}>{title}</{tag}>
  <p>{sub}</p>
  <form data-quote novalidate>
    <div class="form-grid">
      <div class="field"><input id="{fid}-name" name="name" placeholder=" " required><label for="{fid}-name">Full name</label></div>
      <div class="field"><input id="{fid}-phone" name="phone" type="tel" placeholder=" " required><label for="{fid}-phone">Phone</label></div>
      <div class="field full"><input id="{fid}-email" name="email" type="email" placeholder=" " required><label for="{fid}-email">Email address</label></div>
      <div class="field full"><select id="{fid}-service" name="service">{opts}</select><label for="{fid}-service">Service required</label></div>
      <div class="field full"><input id="{fid}-address" name="address" placeholder=" "><label for="{fid}-address">Property address or suburb</label></div>
      <div class="field full"><textarea id="{fid}-msg" name="message" placeholder=" "></textarea><label for="{fid}-msg">How can we help?</label></div>
    </div>
    <button class="btn btn--yellow btn--block" type="submit" style="margin-top:16px">Request My Free Quote {ARROW}</button>
    <p class="form-note">{LOCK}Your details are private. No spam, ever.</p>
    <div class="form-success"><span class="check">{CHECK}</span><h3>Thank you, we have your request</h3><p>Our team will be in touch within 24 hours. Need us sooner? Call <a href="tel:{PHONE_AKL_TEL}"><strong>{PHONE_AKL}</strong></a>.</p></div>
  </form>
</div>"""


def banner(services, h1, text, eyebrow, crumbs=None, checks=None, inner=True, img="hero-villa", form_title="Get a free quote"):
    crumb_html = ""
    if crumbs:
        parts = ['<a href="index.html">Home</a>']
        for label, href in crumbs:
            parts.append('<span class="sep"></span>')
            parts.append(f'<a href="{href}">{label}</a>' if href else f"<span>{label}</span>")
        crumb_html = f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'
    checks = checks or ["Free peer review of existing reports", "Full thermal imaging", "Easy to read reports", "Full indemnity insurance"]
    check_html = "".join(f'<li><span class="check">{CHECK}</span>{c}</li>' for c in checks)
    return f"""
<section class="hero{' hero--inner' if inner else ''}">
  <div class="hero__bg"><img src="assets/img/{img}.jpg" alt="" fetchpriority="high"></div>
  <div class="container hero__grid">
    <div class="hero__content">
      {crumb_html}
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="hero__text">{text}</p>
      <ul class="hero__checks">{check_html}</ul>
      <div class="btn-row">
        <a class="btn btn--yellow" href="#quote">Get a Free Quote {ARROW}</a>
        <a class="btn btn--white" href="tel:{PHONE_AKL_TEL}">{PHONE} Call {PHONE_AKL}</a>
      </div>
      <div class="hero__trust">
        <img src="assets/img/logos/most-trusted-2025.png" alt="Most Trusted Winner 2025">
        <img src="assets/img/logos/master-inspector.png" alt="Registered Master Inspector">
        <div class="rating"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><strong>5.0 Google rating</strong><small>Trusted by Auckland and Waikato homeowners</small></div>
      </div>
    </div>
    {quote_form(services, title=form_title)}
  </div>
</section>"""


def logo_strip(title="Accredited, certified and trusted by"):
    items = "".join(f'<div class="marquee__item"><img src="assets/img/logos/{f}.png" alt="{a}" loading="lazy"></div>' for f, a in SUPPLIERS)
    return f"""
<section class="logos" aria-label="Accreditations and partners">
  <div class="logos__head">{title}</div>
  <div class="logos__mask"><div class="marquee">{items}{items.replace('alt="', 'aria-hidden="true" alt="')}</div></div>
</section>"""


def contact_section(services):
    return f"""
<section class="section section--mist" id="contact">
  <div class="container">
    <div class="head center reveal">
      <span class="eyebrow">Get in touch</span>
      <h2>Book your inspection with a qualified expert</h2>
      <p class="lead">Two local offices covering Auckland, Hamilton, Waikato and Cambridge. Send us a message and we will respond within 24 hours.</p>
    </div>
    <div class="contact reveal">
      <div class="contact__info">
        <div class="office">
          <span class="icon-circle">{PIN}</span>
          <div><h3>Auckland office</h3><p>25 A Wilkinson Road, Ellerslie, Auckland</p><p><a href="tel:{PHONE_AKL_TEL}">{PHONE_AKL}</a></p></div>
        </div>
        <div class="office">
          <span class="icon-circle">{PIN}</span>
          <div><h3>Waikato office</h3><p>2/225 Te Miro Road, Te Miro, Waikato</p><p><a href="tel:{PHONE_WKO_TEL}">{PHONE_WKO}</a></p></div>
        </div>
        <div class="office">
          <span class="icon-circle">{CLOCK}</span>
          <div><h3>Hours of operation</h3><p>8.30am to 5.00pm, Monday to Saturday</p></div>
        </div>
        <div class="map-tabs">
          <button class="is-active" data-q="25A Wilkinson Road, Ellerslie, Auckland 1051">Auckland</button>
          <button data-q="225 Te Miro Road, Te Miro, Waikato">Waikato</button>
        </div>
        <div class="map"><iframe title="Weather Tight Solutions location map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=25A%20Wilkinson%20Road%2C%20Ellerslie%2C%20Auckland%201051&z=14&output=embed"></iframe></div>
      </div>
      <div class="contact__form">
        {quote_form(services, title="Send us a message", sub="Tell us about your property and we will come back to you with a quote within 24 hours.", fid="contact-form")}
      </div>
    </div>
  </div>
</section>"""


def footer(services):
    svc = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in services)
    return f"""
</main>
<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <a class="footer__logo" href="index.html"><img src="assets/img/logo-white.png" alt="Weather Tight Solutions" loading="lazy"></a>
        <p>Specialist professional weathertight and building inspections across Auckland and Waikato. Detailed, easy to read reports you can trust, since 2010.</p>
        <div class="footer__badges">
          <img src="assets/img/logos/most-trusted-2025.png" alt="Most Trusted 2025" loading="lazy">
          <img src="assets/img/logos/master-inspector.png" alt="Registered Master Inspector" loading="lazy">
          <img src="assets/img/logos/no-cowboys.png" alt="No Cowboys" loading="lazy">
        </div>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{svc}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="qualified-building-inspector-auckland.html">Qualified building inspector</a></li>
          <li><a href="peer-reviews.html">Free peer reviews</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="contact.html#quote">Free quote request</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul class="footer__contact">
          <li>{PHONE}<span><strong>Auckland</strong><br><a href="tel:{PHONE_AKL_TEL}">{PHONE_AKL}</a></span></li>
          <li>{PHONE}<span><strong>Waikato</strong><br><a href="tel:{PHONE_WKO_TEL}">{PHONE_WKO}</a></span></li>
          <li>{CLOCK}<span>Mon to Sat<br>8.30am to 5.00pm</span></li>
          <li>{PIN}<span>Auckland, Hamilton, Waikato, Cambridge</span></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="container footer__bottom">
    <span>&copy; 2023 to <span data-year></span> Weather Tight Solutions NZ Ltd. All rights reserved.</span>
    <span><a href="#">Privacy Policy</a> &nbsp;&middot;&nbsp; <a href="#">Sitemap</a></span>
  </div>
</footer>
<a class="float-call" href="tel:{PHONE_AKL_TEL}" aria-label="Call now {PHONE_AKL}"><span class="icon-circle">{PHONE}</span><span><small>Free call</small>Call Now</span></a>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""
