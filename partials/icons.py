"""Inline SVG icons (stroke based, currentColor)."""

def _svg(paths, vb="0 0 24 24", cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="{vb}" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')

PHONE = _svg('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>')
ARROW = _svg('<path d="M5 12h14M13 6l6 6-6 6"/>', cls="arrow")
ARROW_L = _svg('<path d="M19 12H5M11 6l-6 6 6 6"/>')
ARROW_UR = _svg('<path d="M7 17 17 7M8 7h9v9"/>')
CHECK = _svg('<path d="m5 12 5 5L20 7"/>')
PIN = _svg('<path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>')
CLOCK = _svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')
CHEV = _svg('<path d="m6 9 6 6 6-6"/>')
LOCK = _svg('<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>')
SHIELD = _svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>')
SCALE = _svg('<path d="M12 3v18M5 7h14M7 7l-3 7a3 3 0 0 0 6 0zM17 7l-3 7a3 3 0 0 0 6 0z"/>')
USER = _svg('<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>')
GAVEL = _svg('<path d="m14 13-7.5 7.5a2.1 2.1 0 0 1-3-3L11 10"/><path d="m16 16 6-6M8 8l6-6M9 7l8 8M21 11l-8-8"/>')
DROP = _svg('<path d="M12 2.7s6 6.4 6 11.3a6 6 0 0 1-12 0c0-4.9 6-11.3 6-11.3z"/>')
THERMO = _svg('<path d="M14 14.8V4a2 2 0 0 0-4 0v10.8a4 4 0 1 0 4 0z"/>')
REPORT = _svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>')
SEARCH = _svg('<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>')
HOME = _svg('<path d="M3 10.5 12 3l9 7.5V21a1 1 0 0 1-1 1h-5v-7H9v7H4a1 1 0 0 1-1-1z"/>')
BOLT = _svg('<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>')
CAL = _svg('<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>')
TOOL = _svg('<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L2 10l8-8z"/>')
QUOTE = ('<svg class="q" viewBox="0 0 48 48" fill="currentColor" aria-hidden="true"><path d="M20 10v8c-5 0-8 3-8 8h8v14H4V26C4 16 10 10 20 10zm24 0v8c-5 0-8 3-8 8h8v14H28V26c0-10 6-16 16-16z"/></svg>')
