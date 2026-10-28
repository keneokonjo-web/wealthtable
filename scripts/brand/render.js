// Renders queued HTML pages to PNG/PDF with Playwright. usage: node render.js jobs.json
const { chromium } = require('playwright');
const jobs = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8'));
(async () => {
  const b = await chromium.launch();
  let ok = 0;
  for (const j of jobs) {
    const ctx = await b.newContext({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: j.scale || 1 });
    const p = await ctx.newPage();
    try {
      await p.goto(j.html, { waitUntil: 'load' });
      await p.evaluate(() => document.fonts.ready);
      await p.waitForTimeout(150);
      if (j.pdf) await p.pdf({ path: j.out, width: j.w + 'px', height: j.h + 'px', printBackground: true, pageRanges: j.pages || '' });
      else await p.screenshot({ path: j.out, omitBackground: !!j.transparent });
      ok++;
    } catch (e) { console.log('FAIL', j.out, e.message); }
    await ctx.close();
  }
  await b.close();
  console.log('rendered', ok, '/', jobs.length);
})();
