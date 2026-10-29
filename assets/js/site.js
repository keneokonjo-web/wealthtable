/* The Wealth Table: site behaviour. Plain JS, no framework. */
(function () {
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const root = document.documentElement;
  const cfg = window.WT_CONFIG || {};

  /* ---- Register buttons -> Luma (plain link, opens in a new tab) ---- */
  function luma() {
    const url = (cfg.LUMA_URL || '').trim();
    const fallback = 'mailto:info@thewealthtableglobal.com?subject=' + encodeURIComponent('Register my interest: The Wealth Table');
    $$('[data-luma]').forEach(a => {
      a.href = url || fallback;
      if (url) { a.target = '_blank'; a.rel = 'noopener'; }
    });
  }

  /* ---- scroll reveal (hero is driven by the load-up animation instead) ---- */
  function reveal() {
    const els = $$('[data-reveal],.veil,.mask').filter(e => !e.closest('.hero'));
    if (reduce || !('IntersectionObserver' in window)) { els.forEach(e => e.classList.add('is-in')); return; }
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { (e.target._veil || e.target).classList.add('is-in'); io.unobserve(e.target); } }), { threshold: .12, rootMargin: '0px 0px -6% 0px' });
    els.forEach(e => { if (e.classList.contains('veil')) { e.parentElement._veil = e; io.observe(e.parentElement); } else io.observe(e); });
  }

  /* ---- parallax ---- */
  function parallax() {
    if (reduce) return;
    const els = $$('[data-par]'); if (!els.length) return;
    let tick = false;
    const run = () => {
      const vh = innerHeight;
      els.forEach(el => {
        const r = el.parentElement.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        el.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - vh / 2) * -(parseFloat(el.dataset.par) || .1)).toFixed(1) + 'px,0)';
      });
      tick = false;
    };
    addEventListener('scroll', () => { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true });
    addEventListener('resize', run); run();
  }

  function faq() { $$('.faq details').forEach(d => d.addEventListener('toggle', () => { if (d.open) $$('.faq details').forEach(o => { if (o !== d) o.open = false; }); })); }

  /* ---- lightbox for gallery pages ---- */
  function lightbox() {
    const figs = $$('[data-lb]'); if (!figs.length) return;
    const lb = document.createElement('div'); lb.className = 'lb'; lb.hidden = true;
    lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Photo viewer');
    lb.innerHTML = '<button class="lb-x" aria-label="Close">×</button><button class="lb-p" aria-label="Previous photo">‹</button><img alt=""><button class="lb-n" aria-label="Next photo">›</button>';
    document.body.appendChild(lb);
    const im = $('img', lb); let i = 0;
    const show = n => { i = (n + figs.length) % figs.length; im.src = figs[i].dataset.lb; im.alt = $('img', figs[i]).alt; };
    figs.forEach((f, k) => { f.tabIndex = 0; f.setAttribute('role', 'button'); f.addEventListener('click', () => { show(k); lb.hidden = false; document.body.style.overflow = 'hidden'; }); f.addEventListener('keydown', e => { if (e.key === 'Enter') f.click(); }); });
    const close = () => { lb.hidden = true; document.body.style.overflow = ''; };
    $('.lb-x', lb).onclick = close; lb.onclick = e => { if (e.target === lb) close(); };
    $('.lb-p', lb).onclick = () => show(i - 1); $('.lb-n', lb).onclick = () => show(i + 1);
    addEventListener('keydown', e => { if (lb.hidden) return; if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(i - 1); if (e.key === 'ArrowRight') show(i + 1); });
  }

  /* ---- menu overlay ---- */
  function menu() {
    const m = $('#menu'); if (!m) return;
    const set = o => { m.classList.toggle('open', o); document.body.style.overflow = o ? 'hidden' : ''; $('#openMenu').setAttribute('aria-expanded', o); };
    $('#openMenu').onclick = () => set(true); $('#closeMenu').onclick = () => set(false);
    $$('#menu a').forEach(a => a.addEventListener('click', () => set(false)));
    addEventListener('keydown', e => { if (e.key === 'Escape') set(false); });
  }

  /* ---- floating bar tints to the section behind it (Ballena behaviour) ---- */
  function tint() {
    const nav = $('#nav'); if (!nav) return;
    const secs = $$('[data-nb]').filter(e => e !== nav);
    const run = () => {
      const y = nav.getBoundingClientRect().top + 25; let cur = null;
      secs.forEach(s => { const r = s.getBoundingClientRect(); if (r.top <= y && r.bottom > y) cur = s; });
      if (!cur) return;
      const ink = cur.dataset.fg === 'ink';
      nav.style.setProperty('--nb', cur.dataset.nb);
      nav.style.setProperty('--fg', ink ? '#262a1a' : '#f8f2e5');
      nav.style.setProperty('--nbtxt', ink ? '#f8f2e5' : '#262a1a');
      nav.classList.toggle('dark', ink);
    };
    addEventListener('scroll', run, { passive: true }); run();
  }

  /* ---- hero video: starts right after the load-up animation, fades in over the photo ---- */
  function heroVideo() {
    const v = $('.hero-video'); if (!v || reduce) return;
    if (navigator.connection && navigator.connection.saveData) return;
    const go = () => { const p = v.play(); if (p && p.then) p.then(() => v.classList.add('on')).catch(() => {}); };
    if (v.readyState >= 3) go(); else { v.addEventListener('canplay', go, { once: true }); v.load(); }
  }

  /* ---- load-up animation ---- */
  function preload() {
    const pre = $('.pre');
    const done = () => { root.classList.remove('is-loading'); root.classList.add('is-loaded'); heroVideo(); };
    if (!pre || reduce) { if (pre) pre.remove(); done(); return; }
    const countEl = $('.count', pre), bar = $('.bar', pre);
    const MIN = 2900, t0 = performance.now();
    let loaded = document.readyState === 'complete', finished = false;
    if (!loaded) addEventListener('load', () => { loaded = true; });
    const finish = () => {
      if (finished) return; finished = true;
      if (countEl) countEl.textContent = '100'; if (bar) bar.style.transform = 'scaleX(1)';
      setTimeout(() => { pre.classList.add('out'); done(); setTimeout(() => pre.remove(), 1700); }, 260);
    };
    (function tick(now) {
      const p = Math.min((now - t0) / MIN, 1), eased = 1 - Math.pow(1 - p, 2.2);
      const shown = Math.min(99, Math.round(eased * 100));
      if (countEl) countEl.textContent = String(shown).padStart(2, '0');
      if (bar) bar.style.transform = 'scaleX(' + eased.toFixed(3) + ')';
      if (p >= 1 && loaded) { finish(); return; }
      if (now - t0 > 7000) { finish(); return; }          /* never trap the visitor */
      requestAnimationFrame(tick);
    })(t0);
  }

  document.addEventListener('DOMContentLoaded', () => { luma(); reveal(); parallax(); faq(); lightbox(); menu(); tint(); preload(); });
})();
