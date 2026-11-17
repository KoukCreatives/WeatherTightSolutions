# Weather Tight Solutions | Website draft

Static redesign draft for weathertightsolutions.co.nz.

## Structure
- `*.html` : generated pages (home, about, qualified inspector, contact, peer reviews and 8 service pages)
- `partials/layout.py` : **global** header, footer, contact section, quote form and supplier logo strip
- `partials/content.py` : services, qualifications, reviews, FAQ content
- `assets/css/style.css`, `assets/js/main.js` : styles and interactions
- `assets/img` : photos and supplier logos

## Editing
Change a partial or content, then rebuild every page:

```
python3 build.py
```

Preview locally with `python3 -m http.server` and open http://localhost:8000.

## Notes
- Container max width 1440px, 1880px on screens 1920px and wider.
- Quote forms show a success state only. Connect them to a form handler (e.g. Formspree, Netlify Forms or the CMS) before launch.
- Review excerpts are as displayed on the current site's Google review widget.
