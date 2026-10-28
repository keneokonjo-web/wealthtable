/* Shared behaviour. Plain JS, no framework. */
(function () {
  const W = window.WT;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => [...(r || document).querySelectorAll(s)];
  window.$ = $; window.$$ = $$;

  /* scroll reveal: [data-reveal], .veil, .mask */
  function reveal() {
    const els = $$('[data-reveal],.veil,.mask');
    if (reduce || !('IntersectionObserver' in window)) { els.forEach(e => e.classList.add('is-in')); return; }
    /* a clipped .veil can't be observed itself, so watch its parent and reveal the veil */
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { (e.target._veil || e.target).classList.add('is-in'); io.unobserve(e.target); } }), { threshold: .12, rootMargin: '0px 0px -6% 0px' });
    els.forEach(e => { if (e.classList.contains('veil')) { e.parentElement._veil = e; io.observe(e.parentElement); } else io.observe(e); });
  }

  /* parallax: [data-par="0.1"] translates against scroll; parent is the reference box */
  function parallax() {
    if (reduce) return;
    const els = $$('[data-par]'); if (!els.length) return;
    let tick = false;
    const run = () => {
      const vh = innerHeight;
      els.forEach(el => {
        const r = (el.parentElement).getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        const k = parseFloat(el.dataset.par) || .1;
        el.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - vh / 2) * -k).toFixed(1) + 'px,0)';
      });
      tick = false;
    };
    addEventListener('scroll', () => { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true });
    addEventListener('resize', run); run();
  }

  /* registration modal, opened by any [data-register]; [data-table="Lagos"] preselects a table */
  function modal() {
    const m = document.createElement('div');
    m.className = 'rg'; m.id = 'rg'; m.hidden = true;
    m.setAttribute('role', 'dialog'); m.setAttribute('aria-modal', 'true'); m.setAttribute('aria-labelledby', 'rgT');
    m.innerHTML = '<div class="rg-scrim" data-close></div><div class="rg-panel"><button class="rg-x" data-close aria-label="Close">Close</button>' +
      '<p class="rg-eyebrow">The Wealth Table</p><h2 id="rgT">Register your interest</h2>' +
      '<p class="rg-sub">' + W.gives[0] + ' ' + W.gives[1] + '</p>' +
      '<form class="wl" data-waitlist><label><span>Email</span><input type="email" required autocomplete="email" placeholder="you@email.com"></label>' +
      '<label><span>First name</span><input type="text" required autocomplete="given-name" placeholder="First name"></label>' +
      '<label><span>Preferred table</span><select required></select></label>' +
      '<button class="rg-go" type="submit">Join the waitlist</button><small>' + W.consent + '</small><p class="demo-note">Concept preview: this form does not send data.</p></form>' +
      '<p class="wl-ok" hidden>Thank you. You are on the list.</p></div>';
    document.body.appendChild(m);
    let last = null;
    const open = (table) => {
      last = document.activeElement; m.hidden = false; void m.offsetWidth; m.classList.add('is-open'); document.body.style.overflow = 'hidden';
      const s = $('select', m); if (table) [...s.options].forEach(o => { if (o.text.startsWith(table)) s.value = o.text; });
      setTimeout(() => $('input', m).focus(), 250);
    };
    const close = () => { m.classList.remove('is-open'); document.body.style.overflow = ''; setTimeout(() => { m.hidden = true; }, 800); if (last) last.focus(); };
    document.addEventListener('click', e => {
      const t = e.target.closest('[data-register]'); if (t) { e.preventDefault(); open(t.dataset.table); return; }
      if (e.target.closest('[data-close]') && !m.hidden) close();
    });
    addEventListener('keydown', e => { if (e.key === 'Escape' && !m.hidden) close(); });
  }

  /* waitlist forms (inline and modal). Demo only, no backend. */
  function forms() {
    $$('form[data-waitlist]').forEach(f => {
      const sel = $('select', f);
      if (sel && !sel.options.length) sel.innerHTML = '<option value="" disabled selected>Select preferred table</option>' + W.tables.map(t => '<option>' + t + '</option>').join('');
      f.addEventListener('submit', e => {
        e.preventDefault();
        const ok = f.parentElement.querySelector('.wl-ok'); f.hidden = true; if (ok) ok.hidden = false;
      });
    });
    $$('[data-table]:not([data-register])').forEach(b => b.addEventListener('click', () => {
      const s = $('form[data-waitlist] select'); if (s) [...s.options].forEach(o => { if (o.text.startsWith(b.dataset.table)) s.value = o.text; });
    }));
  }

  function faq() { $$('.faq details').forEach(d => d.addEventListener('toggle', () => { if (d.open) $$('.faq details').forEach(o => { if (o !== d) o.open = false; }); })); }

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

  /* intro overlay, once per session */
  function intro() {
    const o = $('.intro'); const done = () => document.documentElement.classList.add('is-ready');
    if (!o) { done(); return; }
    let seen = false; try { seen = sessionStorage.getItem('wt-intro-2'); } catch (e) {}
    if (seen || reduce) { o.remove(); done(); return; }
    setTimeout(() => { o.classList.add('out'); done(); try { sessionStorage.setItem('wt-intro-2', '1'); } catch (e) {} setTimeout(() => o.remove(), 1400); }, 1500);
  }

  function switcher() { const s = $('.switcher'); if (s) $$('a', s).forEach(a => { if (location.pathname.endsWith(a.getAttribute('href'))) a.setAttribute('aria-current', 'page'); }); }

  /* helper used by every concept to draw a photo */
  window.photo = (n, alt, extra) => '<img src="' + W.img(n) + '" alt="' + (alt || W.alt[n] || '') + '" loading="lazy" ' + (extra || '') + '>';

  window.WTinit = function () { intro(); modal(); forms(); faq(); lightbox(); reveal(); parallax(); switcher(); };
})();
