/* Weather Tight Solutions | site interactions */
(function () {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  /* Sticky header + progress bar + floating call */
  const header = $('.header');
  const progress = $('.progress');
  const floatCall = $('.float-call');
  const onScroll = () => {
    const y = window.scrollY;
    header && header.classList.toggle('is-scrolled', y > 40);
    if (progress) {
      const h = document.documentElement.scrollHeight - innerHeight;
      progress.style.width = (h > 0 ? (y / h) * 100 : 0) + '%';
    }
    floatCall && floatCall.classList.toggle('is-visible', y > 280);
    $$('.parallax').forEach(el => {
      const r = el.getBoundingClientRect();
      const speed = parseFloat(el.dataset.speed || '0.08');
      el.style.transform = `translate3d(0, ${(r.top + r.height / 2 - innerHeight / 2) * -speed}px, 0)`;
    });
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Mobile drawer */
  const drawer = $('.drawer');
  const toggle = open => {
    drawer.classList.toggle('is-open', open);
    document.body.style.overflow = open ? 'hidden' : '';
  };
  $$('[data-open-menu]').forEach(b => b.addEventListener('click', () => toggle(true)));
  $$('[data-close-menu]').forEach(b => b.addEventListener('click', () => toggle(false)));
  addEventListener('keydown', e => e.key === 'Escape' && drawer && toggle(false));

  /* Reveal on scroll (banner content is never revealed, it shows immediately) */
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
    });
  }, { threshold: 0.14, rootMargin: '0px 0px -40px 0px' });
  $$('.stagger').forEach(g => [...g.children].forEach((c, i) => { c.style.setProperty('--i', i); c.classList.add('reveal'); }));
  $$('.reveal, .reveal-l, .reveal-r').forEach(el => io.observe(el));

  /* Counters */
  const cio = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      const el = en.target, end = +el.dataset.count, dur = 1600, t0 = performance.now();
      const tick = t => {
        const p = Math.min((t - t0) / dur, 1);
        el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      cio.unobserve(el);
    });
  }, { threshold: 0.6 });
  $$('[data-count]').forEach(el => cio.observe(el));

  /* Testimonials slider */
  $$('.slider').forEach(sl => {
    const track = $('.slides', sl), slides = $$('.slide', sl), dots = $('.dots', sl.parentElement);
    let i = 0, timer;
    slides.forEach((_, n) => {
      const b = document.createElement('button');
      b.setAttribute('aria-label', 'Go to review ' + (n + 1));
      b.addEventListener('click', () => go(n));
      dots && dots.appendChild(b);
    });
    const go = n => {
      i = (n + slides.length) % slides.length;
      track.style.transform = `translateX(${-i * 100}%)`;
      dots && [...dots.children].forEach((d, k) => d.classList.toggle('is-active', k === i));
      clearInterval(timer); timer = setInterval(() => go(i + 1), 6500);
    };
    const wrap = sl.parentElement;
    $('[data-prev]', wrap)?.addEventListener('click', () => go(i - 1));
    $('[data-next]', wrap)?.addEventListener('click', () => go(i + 1));
    go(0);
  });

  /* Map tabs */
  $$('.map-tabs button').forEach(btn => btn.addEventListener('click', () => {
    $$('.map-tabs button').forEach(b => b.classList.toggle('is-active', b === btn));
    $('.map iframe').src = 'https://maps.google.com/maps?q=' + encodeURIComponent(btn.dataset.q) + '&z=14&output=embed';
  }));

  /* Draft forms: show a success state (wire up to a real endpoint before launch) */
  $$('form[data-quote]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    if (!f.checkValidity()) { f.reportValidity(); return; }
    f.classList.add('is-sent');
  }));

  /* Year */
  $$('[data-year]').forEach(el => (el.textContent = new Date().getFullYear()));
})();
