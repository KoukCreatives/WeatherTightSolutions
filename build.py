"""Static site builder. Global header/footer/contact live in partials/layout.py.
Run: python3 build.py   (writes the .html pages into the repo root)"""
import os, re, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "partials"))
from icons import *
from layout import *
from content import SERVICES, PEER, QUALS, WHY, REVIEWS, STEPS, FAQ

S = SERVICES


SMALL = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "of", "on", "or", "the", "to", "with", "is"}


def title_case(text, first=True):
    out = []
    for w in re.split(r"(\s+)", text):
        if not w.strip():
            out.append(w); continue
        low = w.lower()
        if not first and low in SMALL:
            out.append(low)
        elif w.isupper() and len(w) > 1:
            out.append(w)  # acronyms: CCC, COA, NZ
        else:
            out.append(w[0].upper() + w[1:])
        first = False
    return "".join(out)


def cap_headings(html):
    def fix(m):
        state = {"first": True}
        def txt(t):
            if not t.group(0).strip():
                return t.group(0)
            r = title_case(t.group(0), state["first"]); state["first"] = False; return r
        inner = re.sub(r"(?<=>)[^<]+|^[^<]+", txt, m.group(2))
        return f"<{m.group(1)}{inner}</{m.group(1)[:2]}>"
    return re.sub(r"<(h[12][^>]*>)(.*?)</h[12]>", fix, html, flags=re.S)


def page(fname, title, desc, active, body):
    html = cap_headings(head(title, desc) + header(S, active) + body + contact_section(S) + footer(S))
    assert "\u2014" not in html, f"em dash found in {fname}"
    with open(os.path.join(ROOT, fname), "w") as f:
        f.write(html)
    print("built", fname)


# ---------- reusable sections ----------
def service_cards(items, cols=""):
    out = []
    for n, s in enumerate(items, 1):
        out.append(f"""
<a class="card" href="{s['slug']}.html">
  <div class="card__img"><img src="assets/img/{s['img']}.jpg" alt="{s['name']}" loading="lazy"><span class="card__num">{n:02d}</span></div>
  <div class="card__body"><h3>{s['name']}</h3><p>{s['short']}</p><span class="card__more"><i>{ARROW_UR}</i>Learn more</span></div>
</a>""")
    return f'<div class="cards {cols} stagger">{"".join(out)}</div>'


def services_section(title="Specialist inspections for every stage of ownership", eyebrow="Our services", items=None, mist=True):
    items = items or S
    return f"""
<section class="section{' section--mist' if mist else ''}">
  <div class="container">
    <div class="head reveal">
      <div><span class="eyebrow">{eyebrow}</span><h2>{title}</h2></div>
      <p>Pre purchase and pre sale inspections, new build inspections, invasive and destructive testing and remedial work requirements for residential and commercial properties.</p>
    </div>
    {service_cards(items, 'cards--3' if len(items) == 3 else '')}
  </div>
</section>"""


def stats():
    return """
<div class="container" style="margin-top:clamp(56px,7vw,100px)">
  <div class="stats reveal">
    <div class="stat"><strong><span data-count="2010">2010</span></strong><span>Established, after years in specialist recladding</span></div>
    <div class="stat"><strong><span data-count="10">10</span><sup>+</sup></strong><span>Industry qualifications and memberships</span></div>
    <div class="stat"><strong><span data-count="8">8</span></strong><span>Specialist inspection and repair services</span></div>
    <div class="stat"><strong><span data-count="24">24</span><sup>h</sup></strong><span>Response to every quote request</span></div>
  </div>
</div>"""


def process():
    steps = "".join(f'<div class="step"><div class="step__n">0{i}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(STEPS, 1))
    return f"""
<section class="section section--dark">
  <div class="container">
    <div class="head reveal">
      <div><span class="eyebrow">How it works</span><h2>A simple process with <span class="text-yellow">no surprises</span></h2></div>
      <p>From your first call to your final report, you always know what is happening and why.</p>
    </div>
    <div class="process stagger">{steps}</div>
  </div>
</section>"""


def why_section():
    items = "".join(f'<div class="why__item"><div class="why__icon">{ic}</div><h3>{t}</h3><p>{d}</p></div>' for ic, t, d in WHY)
    return f"""
<section class="section">
  <div class="container split">
    <div class="reveal-l">
      <span class="eyebrow">Why choose us</span>
      <h2>Industry leading inspections, <span class="text-blue">delivered with care</span></h2>
      <p class="lead">Weather Tight Solutions provides industry leading weathertight and building inspections and reports, carried out by an accredited inspector with full indemnity insurance and additional wet home cover.</p>
      <div class="btn-row" style="margin-top:30px"><a class="btn btn--blue" href="contact.html#quote">Book an Inspection {ARROW}</a></div>
    </div>
    <div class="why stagger">{items}</div>
  </div>
</section>"""


def peer_band():
    return f"""
<section class="section" style="padding-top:0">
  <div class="container">
    <div class="band reveal">
      <div>
        <span class="eyebrow">Unique to Weather Tight Solutions</span>
        <h2>Already have a report? We will peer review it for free.</h2>
        <p>Get an expert second opinion on the accuracy of your existing weathertightness or building report, at no cost to you.</p>
      </div>
      <div class="btn-row"><a class="btn btn--yellow" href="peer-reviews.html">Request a Free Peer Review {ARROW}</a></div>
    </div>
  </div>
</section>"""


def quals_section():
    q = "".join(f'<li><span class="check">{CHECK}</span>{x}</li>' for x in QUALS)
    logos = "".join(f'<div><img src="assets/img/logos/{f}.png" alt="{a}" loading="lazy"></div>' for f, a in SUPPLIERS)
    return f"""
<section class="section section--mist">
  <div class="container split">
    <div class="reveal-l">
      <span class="eyebrow">Qualifications and associations</span>
      <h2>Credentials that ensure an <span class="text-blue">excellent service</span></h2>
      <p class="lead">Trained by the New Zealand Institute of Building Surveyors to their highest level, and backed by the industry bodies New Zealanders trust.</p>
      <ul class="quals">{q}</ul>
    </div>
    <div class="logo-grid stagger">{logos}</div>
  </div>
</section>"""


def reviews_section():
    slides = "".join(f"""<div class="slide"><blockquote class="quote">{QUOTE}<p>{t}</p>
<footer><span class="avatar">{n[0]}</span><div><strong>{n}</strong><small>Google review</small></div></footer></blockquote></div>""" for n, t in REVIEWS)
    return f"""
<section class="section section--dark">
  <div class="container reviews">
    <div class="reveal-l">
      <span class="eyebrow">Client reviews</span>
      <h2>Trusted by buyers, sellers and building owners</h2>
      <div class="score"><strong>5.0</strong><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p style="margin:0">Rated by our clients on Google. Winner, Most Trusted 2025.</p></div>
    </div>
    <div class="reveal-r">
      <div class="slider"><div class="slides">{slides}</div></div>
      <div class="slider__nav"><button class="arrow" data-prev aria-label="Previous review">{ARROW_L}</button><button class="arrow" data-next aria-label="Next review">{ARROW}</button><div class="dots"></div></div>
    </div>
  </div>
</section>"""


def faq_section(items=FAQ):
    d = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}<i>+</i></summary><div>{a}</div></details>' for i, (q, a) in enumerate(items))
    return f"""
<section class="section">
  <div class="container split" style="align-items:start">
    <div class="reveal-l">
      <span class="eyebrow">Questions answered</span>
      <h2>Frequently asked questions</h2>
      <p class="lead">Still unsure what you need? Call us and talk to a qualified inspector, not a call centre.</p>
      <div class="btn-row" style="margin-top:26px"><a class="btn btn--dark" href="tel:{PHONE_AKL_TEL}">{PHONE} {PHONE_AKL}</a></div>
      <div class="areas" style="justify-content:flex-start">
        {''.join(f'<span>{PIN}{a}</span>' for a in ['Auckland','Hamilton','Waikato','Cambridge'])}
      </div>
    </div>
    <div class="faq reveal-r">{d}</div>
  </div>
</section>"""


def about_split(title, paras, img="house-auckland", rev=False, eyebrow="About Weather Tight Solutions", ticks=None, signature=True):
    p = "".join(f"<p>{x}</p>" for x in paras)
    t = ""
    if ticks:
        t = '<ul class="ticks ticks--2">' + "".join(f'<li><span class="check">{CHECK}</span>{x}</li>' for x in ticks) + "</ul>"
    sig = """<div class="signature"><span class="avatar">MW</span><div><strong>Mark Waters</strong><small>Founder and accredited building inspector</small></div></div>""" if signature else ""
    return f"""
<section class="section">
  <div class="container split{' split--rev' if rev else ''}">
    <div class="split__media reveal-l">
      <div class="media-frame"><img class="parallax-img" src="assets/img/{img}.jpg" alt="Auckland home inspected by Weather Tight Solutions" loading="lazy"></div>
      <div class="media-deco"></div>
      <div class="media-badge"><strong>2010</strong><span>Established<br>in Auckland</span></div>
      <div class="media-chip"><img src="assets/img/logos/master-inspector.png" alt=""><div><strong>Registered Master</strong><small>Inspector Association</small></div></div>
    </div>
    <div class="reveal-r">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{title}</h2>
      {p}{t}
      <div class="btn-row" style="margin-top:28px"><a class="btn btn--yellow" href="contact.html#quote">Get a Free Quote {ARROW}</a><a class="btn btn--dark" href="about.html">Our Story {ARROW}</a></div>
      {sig}
    </div>
  </div>
</section>"""


# ---------- pages ----------
def build_home():
    body = banner(S, inner=False,
        eyebrow="Auckland and Waikato building inspectors",
        h1="Specialist weathertight and building inspections <em>you can trust</em>",
        text="Detailed inspections and comprehensive, easy to read reports from an accredited professional building inspector. Buy, sell and maintain your property with confidence.",
        form_title="Get your free quote")
    body += logo_strip()
    body += about_split("Expert building inspections by a qualified building inspector", [
        "Mark Waters is an accredited professional building inspector trained by the New Zealand Institute of Building Surveyors, achieving their highest level of training. All reports encompass NZS 4306:2005, the Standard for Residential Property Inspections.",
        "Using the right technology for the right job, and carrying full indemnity insurance with additional wet home cover, you can be confident when buying or selling your property."],
        ticks=["NZIBS highest level training", "NZS 4306:2005 reporting", "Full indemnity insurance", "Additional wet home cover"])
    body += stats().replace('margin-top:clamp(56px,7vw,100px)', 'margin-top:0;margin-bottom:clamp(72px,9vw,140px)')
    body += services_section()
    body += process()
    body += why_section()
    body += peer_band()
    body += quals_section()
    body += reviews_section()
    body += faq_section()
    page("index.html", "Weather Tight Solutions | Weathertight and Building Inspections Auckland and Waikato",
         "Specialist weathertight and building inspections across Auckland and Waikato. Thermal imaging, invasive testing, free peer reviews and easy to read reports.", "home", body)


def build_service(s, active="services"):
    others = [x for x in S if x["slug"] != s["slug"]][:3]
    p = "".join(f"<p>{x}</p>" for x in s["intro"])
    ticks = "".join(f'<li><span class="check">{CHECK}</span>{x}</li>' for x in s["ticks"])
    feats = "".join(f'<div class="feature"><div class="why__icon">{ic}</div><h3>{t}</h3><p>{d}</p></div>' for ic, t, d in s["features"])
    act = lambda x: ' class="is-active"' if x["slug"] == s["slug"] else ""
    side = "".join(f'<li><a href="{x["slug"]}.html"{act(x)}>{x["name"]}<span>&#8250;</span></a></li>' for x in S)
    body = banner(S, eyebrow="Weather Tight Solutions", h1=s["h1"], text=s["lead"],
                  crumbs=[("Services", "weathertight-building-inspections.html"), (s["name"], None)],
                  img=s["img"])
    body += logo_strip("Accredited and trusted by")
    body += f"""
<section class="section">
  <div class="container content-layout">
    <div class="prose">
      <div class="split" style="grid-template-columns:1fr;gap:40px">
        <div class="media-frame reveal"><img src="assets/img/{s['img']}.jpg" alt="{s['name']}" style="aspect-ratio:16/9" loading="lazy"></div>
      </div>
      <div class="reveal" style="margin-top:46px">
        <span class="eyebrow">Overview</span>
        <h2>{s['name']} done properly</h2>
        {p}
        <h3>What is included</h3>
        <ul class="ticks ticks--2">{ticks}</ul>
      </div>
      <div class="feature-grid stagger" style="margin-top:20px">{feats}</div>
    </div>
    <aside class="aside-card reveal-r">
      <h3>Our services</h3>
      <ul>{side}</ul>
      <p>Talk to a qualified inspector today.</p>
      <a class="btn btn--yellow btn--block" href="#quote">Get a Free Quote {ARROW}</a>
      <a class="btn btn--blue btn--block" style="margin-top:12px" href="tel:{PHONE_AKL_TEL}">{PHONE} {PHONE_AKL}</a>
    </aside>
  </div>
</section>"""
    body += process()
    body += f'<div style="height:clamp(72px,9vw,140px)"></div>' + peer_band()
    body += services_section("Related services", "Explore more", others)
    body += faq_section()
    page(f"{s['slug']}.html", f"{s['name']} Auckland and Waikato | Weather Tight Solutions", s["lead"], active, body)


def build_about():
    body = banner(S, eyebrow="About us",
        h1="Building inspection specialists <em>since 2010</em>",
        text="Founded by Mark Waters after years running a specialist recladding company, Weather Tight Solutions gives building owners and buyers across Auckland and Waikato answers they can rely on.",
        crumbs=[("About", None)], img="house-auckland")
    body += logo_strip()
    body += about_split("A passion for quality, built over two decades", [
        "Mark Waters started as a property developer in 2002, where he developed a passion for delivering quality projects. As years passed, he saw a gap in the market for a specialist in weathertightness issues.",
        "Wanting to learn more, Mark regularly travelled to Australia and the United States to further his education in design principles and inspection and diagnosis techniques, and spent time developing the best remedial solutions to issues raised by building inspections.",
        "In 2010, after years of running a specialist recladding construction company, Mark established Weather Tight Solutions NZ Ltd. Since then, he and his team of qualified building contractors have worked with building owners and buyers in the Auckland and Waikato regions."],
        eyebrow="Our story")
    body += stats().replace('margin-top:clamp(56px,7vw,100px)', 'margin-top:0;margin-bottom:clamp(72px,9vw,140px)')
    body += why_section().replace('class="section"', 'class="section section--mist"', 1)
    body += quals_section().replace("section section--mist", "section", 1)
    body += reviews_section()
    body += peer_band().replace('style="padding-top:0"', '')
    page("about.html", "About Weather Tight Solutions | Building Inspection Specialists",
         "Weather Tight Solutions NZ Ltd was established in 2010 by Mark Waters. Specialist weathertight and building inspections across Auckland and Waikato.", "about", body)


def build_inspector():
    body = banner(S, eyebrow="Qualified building inspector Auckland",
        h1="Expert building inspections by a <em>qualified inspector</em>",
        text="Weather Tight Solutions completes detailed inspections and gives you confidence by supplying comprehensive, easy to read reports. Accredited, insured and trusted across Auckland and Waikato.",
        crumbs=[("Qualified Building Inspector Auckland", None)])
    body += logo_strip()
    body += about_split("An accredited professional building inspector", [
        "Mark is an accredited professional building inspector trained by the New Zealand Institute of Building Surveyors, achieving their highest level of training. All reports encompass NZS 4306:2005 Standard for Residential Property Inspections.",
        "Using the right technology for the right job, and carrying full indemnity insurance with additional wet home cover, you can be confident when buying or selling your property.",
        "Call Weather Tight Solutions NZ Ltd today for a reliable and accurate weathertight building inspection of your residential or commercial building."],
        eyebrow="Meet your inspector", ticks=["Diploma in Building Surveying", "Registered Master Builder", "Licensed Building Practitioner", "Member of Standards NZ"])
    body += services_section("At Weather Tight Solutions we specialise in", "What we do")
    body += peer_band().replace('style="padding-top:0"', '')
    body += quals_section().replace("section section--mist", "section section--mist", 1)
    body += why_section()
    body += reviews_section()
    body += faq_section()
    page("qualified-building-inspector-auckland.html", "Qualified Building Inspector Auckland | Registered Building Inspector",
         "Expert building inspections by a qualified, accredited building inspector in Auckland. Comprehensive, easy to read reports to NZS 4306:2005.", "inspector", body)


def build_contact():
    body = banner(S, eyebrow="Contact us",
        h1="Talk to a <em>qualified inspector</em> today",
        text="Call us free on 0800 532 578 in Auckland or 021 163 6232 in Waikato, or send the form and we will come back to you within 24 hours.",
        crumbs=[("Contact", None)], checks=["Response within 24 hours", "Open Monday to Saturday", "Auckland and Waikato offices", "Free, no obligation quotes"], img="house-auckland")
    body += logo_strip()
    page("contact.html", "Contact Weather Tight Solutions | Auckland and Waikato",
         "Contact Weather Tight Solutions for weathertight and building inspections in Auckland and Waikato. Call 0800 532 578 or 021 163 6232.", "contact", body)


if __name__ == "__main__":
    build_home()
    for s in S:
        build_service(s)
    build_service(PEER, active="peer")
    build_about()
    build_inspector()
    build_contact()
