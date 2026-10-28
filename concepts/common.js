/* Shared behaviour. Plain JS, no framework (Playbook §5). */
(function () {
  const W = window.WT;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  window.$ = $; window.$$ = $$;

  /* 5.5 scroll reveal */
  function reveal() {
    const els = $$('[data-reveal]');
    if (reduce || !('IntersectionObserver' in window)) { els.forEach(e => e.classList.add('in')); return; }
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .12, rootMargin: '0px 0px -6% 0px' });
    els.forEach(e => io.observe(e));
  }

  /* 5.6 parallax: [data-par="0.15"] on an oversized child */
  function parallax() {
    if (reduce) return;
    const els = $$('[data-par]'); if (!els.length) return;
    let tick = false;
    const run = () => {
      const vh = innerHeight;
      els.forEach(el => {
        const r = el.parentElement.getBoundingClientRect();
        if (r.bottom < -100 || r.top > vh + 100) return;
        const k = parseFloat(el.dataset.par) || .12;
        el.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - vh / 2) * -k).toFixed(1) + 'px,0)';
      });
      tick = false;
    };
    addEventListener('scroll', () => { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true });
    addEventListener('resize', run); run();
  }

  /* waitlist forms: [data-waitlist]. Demo only, no backend (stated in the form). */
  function forms() {
    $$('form[data-waitlist]').forEach(f => {
      const sel = $('select', f);
      if (sel && !sel.options.length) {
        sel.innerHTML = '<option value="" disabled selected>Select preferred table</option>' + W.tables.map(t => '<option>' + t + '</option>').join('');
      }
      f.addEventListener('submit', e => {
        e.preventDefault();
        const ok = $('.wl-ok', f.parentElement) || $('.wl-ok');
        f.hidden = true; if (ok) ok.hidden = false;
      });
    });
    $$('[data-pick]').forEach(b => b.addEventListener('click', () => {
      const s = $('form[data-waitlist] select'); if (s) { [...s.options].forEach(o => { if (o.text.startsWith(b.dataset.pick)) s.value = o.text; }); }
    }));
  }

  /* FAQ: native <details>, close others */
  function faq() {
    $$('.faq details').forEach(d => d.addEventListener('toggle', () => { if (d.open) $$('.faq details').forEach(o => { if (o !== d) o.open = false; }); }));
  }

  /* lightbox for galleries: [data-lb] images */
  function lightbox() {
    const imgs = $$('[data-lb]'); if (!imgs.length) return;
    const lb = document.createElement('div'); lb.className = 'lb'; lb.hidden = true;
    lb.innerHTML = '<button class="lb-x" aria-label="Close">×</button><button class="lb-p" aria-label="Previous">‹</button><img alt=""><button class="lb-n" aria-label="Next">›</button>';
    document.body.appendChild(lb);
    const im = $('img', lb); let list = [], i = 0;
    const show = n => { i = (n + list.length) % list.length; im.src = list[i].dataset.lb; im.alt = list[i].alt || ''; };
    imgs.forEach(el => el.addEventListener('click', () => { list = imgs.filter(x => x.closest('[data-set]') === el.closest('[data-set]')); show(list.indexOf(el)); lb.hidden = false; document.body.style.overflow = 'hidden'; }));
    const close = () => { lb.hidden = true; document.body.style.overflow = ''; };
    $('.lb-x', lb).onclick = close; lb.onclick = e => { if (e.target === lb) close(); };
    $('.lb-p', lb).onclick = () => show(i - 1); $('.lb-n', lb).onclick = () => show(i + 1);
    addEventListener('keydown', e => { if (lb.hidden) return; if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(i - 1); if (e.key === 'ArrowRight') show(i + 1); });
  }

  /* 5.4 intro overlay: plays once per session */
  function intro() {
    const o = $('.intro'); if (!o) return;
    let seen = false; try { seen = sessionStorage.getItem('wt-intro'); } catch (e) {}
    if (seen || reduce) { o.remove(); document.documentElement.classList.add('intro-done'); return; }
    setTimeout(() => { o.classList.add('out'); document.documentElement.classList.add('intro-done'); try { sessionStorage.setItem('wt-intro', '1'); } catch (e) {} setTimeout(() => o.remove(), 1300); }, 1700);
  }

  /* concept switcher strip */
  function switcher() {
    const s = $('.switcher'); if (!s) return;
    $$('a', s).forEach(a => { if (location.pathname.endsWith(a.getAttribute('href'))) a.setAttribute('aria-current', 'page'); });
  }

  window.WTinit = function () { intro(); reveal(); parallax(); forms(); faq(); lightbox(); switcher(); };
  document.addEventListener('DOMContentLoaded', () => { if (!window.WT_MANUAL_INIT) window.WTinit(); });
})();
