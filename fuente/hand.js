// Hand-drawn post-processing: glyphs, word jitter, rough.js overlays.
(function(){
let seed = 1337;
const rnd = () => { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
const J = (a) => (rnd() * 2 - 1) * a;

// ---------- glyphs (unicode chars missing from the handwriting font) ----------
const G = {
  '→': [12, 'M1,5.2 C4,5 8,5.3 11,5 M7.6,2.4 C8.8,3.4 10,4.3 11.1,5 C10,5.8 8.8,6.7 7.8,7.8'],
  '⟹': [16, 'M1,3.9 L12.5,3.8 M1,6.4 L12.5,6.3 M10.5,1.4 C12,2.6 13.6,3.9 15,5.1 C13.6,6.3 12,7.6 10.6,8.8'],
  '⇒': [13, 'M1,3.9 L9.5,3.8 M1,6.4 L9.5,6.3 M7.8,1.6 C9,2.7 10.6,3.9 12,5.1 C10.6,6.3 9,7.5 7.9,8.6'],
  '⇔': [15, 'M3,3.9 L12,3.8 M3,6.4 L12,6.3 M4.6,1.6 C3.6,2.7 2.2,3.9 1,5.1 C2.2,6.3 3.6,7.5 4.5,8.6 M10.4,1.6 C11.4,2.7 12.8,3.9 14,5.1 C12.8,6.3 11.4,7.5 10.5,8.6'],
  '≤': [9, 'M7.5,1.8 C5.6,2.8 3.6,3.8 1.6,4.8 C3.6,5.7 5.6,6.6 7.5,7.4 M1.6,9 L7.6,8.9'],
  '≥': [9, 'M1.6,1.8 C3.5,2.8 5.5,3.8 7.5,4.8 C5.5,5.7 3.5,6.6 1.6,7.4 M1.5,9 L7.5,8.9'],
  '≠': [9, 'M1,4 L8,3.9 M1,6.6 L8,6.5 M6,1.4 L3,9.2'],
  '≈': [9, 'M1,4.3 C2.5,2.8 4.3,5.4 5.8,4.2 C6.6,3.5 7.4,3.4 8.2,3.9 M1,7.2 C2.5,5.7 4.3,8.3 5.8,7.1 C6.6,6.4 7.4,6.3 8.2,6.8'],
  '∞': [14, 'M7,5.6 C5.2,2.6 1.6,2.6 1.6,5.6 C1.6,8.6 5.2,8.6 7,5.6 C8.8,2.6 12.4,2.6 12.4,5.6 C12.4,8.6 8.8,8.6 7,5.6'],
  'ε': [6.6, 'M5.8,4.3 C4.6,3.1 1.6,3.2 1.8,4.9 C1.9,6 3.4,6.1 4.6,6 C2.4,6 1,6.8 1.3,8.1 C1.7,9.4 4.4,9.4 5.9,8.3'],
  'δ': [7, 'M5.6,1.7 C4.4,0.7 1.6,0.9 2.4,2.5 C3.2,4 6.1,4.6 6.1,6.9 C6.1,8.6 4.7,9.4 3.4,9.3 C1.9,9.2 1,8.2 1,6.8 C1,5.3 2.5,4.4 4.2,4.2'],
  '✓': [10, 'M1,5.6 C2,6.6 3,7.6 3.9,8.8 C5.6,5.8 7.6,3.2 10,0.6'],
  '✗': [9, 'M1,1.4 C3.6,4 5.6,6.4 8,9 M8,1.2 C5.6,3.6 3.4,6.2 1.2,9'],
  '∴': [8, 'M4,2.6 l.1,.1 M1.5,7.6 l.1,.1 M6.5,7.6 l.1,.1'],
  '∪': [9, 'M1.5,2.2 C1.4,6.8 2.6,8.9 4.6,8.9 C6.6,8.9 7.6,6.8 7.6,2.2'],
  '∈': [8, 'M7.3,2.4 C3,1.6 1.2,3.5 1.2,5.3 C1.2,7.1 3,8.7 7.3,8.1 M1.4,5.3 L6.6,5.2'],
  '±': [8, 'M1,4.4 L7,4.3 M4,1.4 L4,7.3 M1,8.6 L7,8.5'],
};
const GKEYS = Object.keys(G);
function jitterPath(d, a){ return d.replace(/-?\d+(\.\d+)?/g, n => (parseFloat(n) + J(a)).toFixed(2)); }
function glyphSVG(ch){
  const [w, d] = G[ch];
  const sw = ch === '∴' ? 1.7 : 0.9;
  const small = 'εδ'.includes(ch);
  return `<svg class="gl${small?' small':''}" viewBox="-0.5 ${small?2.5:0} ${w+1} ${small?7.5:10}" style="width:${(w+1)/10*(small?0.62/0.75:0.8)}em"><path d="${jitterPath(d,0.22)}" fill="none" stroke="currentColor" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
}

function walkText(root, fn){
  const tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
  const nodes = []; let n; while((n = tw.nextNode())) nodes.push(n);
  nodes.forEach(fn);
}
const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');

function processText(root){
  walkText(root, node => {
    if (node.parentElement.closest('svg')) return;
    const t = node.nodeValue;
    if (!t.trim()) return;
    let html = '';
    // split into words / spaces, wrap words, swap glyphs
    t.split(/(\s+)/).forEach(tok => {
      if (!tok) return;
      if (/^\s+$/.test(tok)) { html += tok; return; }
      let inner = '';
      for (const ch of tok) inner += GKEYS.includes(ch) ? glyphSVG(ch) : esc(ch);
      const ty = J(0.05).toFixed(3), r = J(1.1).toFixed(2), sc = (1 + J(0.035)).toFixed(3);
      html += `<span class="w" style="display:inline-block;transform:translateY(${ty}em) rotate(${r}deg) scale(${sc})">${inner}</span>`;
    });
    const span = document.createElement('span');
    span.innerHTML = html;
    node.replaceWith(...span.childNodes);
  });
}

// ---------- overlay drawing ----------
function rel(el, page){
  const a = el.getBoundingClientRect(), p = page.getBoundingClientRect();
  return {x:a.left-p.left, y:a.top-p.top, w:a.width, h:a.height, r:a.right-p.left, b:a.bottom-p.top};
}
function inkOf(el){ return getComputedStyle(el).color; }

function drawPage(page){
  const over = page.querySelector('svg.over'), under = page.querySelector('svg.under');
  const rc = rough.svg(over);
  const pen = (stroke, extra) => Object.assign({stroke, strokeWidth:1.5, roughness:0.55, bowing:0.6, disableMultiStroke:true, seed: Math.floor(rnd()*1e6)}, extra||{});
  const add = n => over.appendChild(n);

  // fraction bars
  page.querySelectorAll('.fr').forEach(fr => {
    const [n, d] = fr.children; const R = rel(fr, page);
    const y = (rel(n,page).b + rel(d,page).y)/2 + 1;
    add(rc.line(R.x + J(2) + 1, y + J(1), R.r + J(2) - 1, y + J(1.2), pen(inkOf(fr), {strokeWidth:1.6})));
  });
  // square roots
  page.querySelectorAll('.sq').forEach(sq => {
    const R = rel(sq, page); const fs = parseFloat(getComputedStyle(sq).fontSize);
    const x0 = R.x + 1, top = R.y + 2, bot = R.b - 2;
    const pts = [[x0, bot - (bot-top)*0.42], [x0 + fs*0.13, bot - (bot-top)*0.5], [x0 + fs*0.27, bot + J(1)], [x0 + fs*0.5, top + J(1)], [R.r + J(3), top + J(1.5)]];
    add(rc.linearPath(pts, pen(inkOf(sq), {strokeWidth:1.6, roughness:0.4})));
  });
  // over-bar (e.g. C̄)
  page.querySelectorAll('.ov').forEach(el => { const R = rel(el,page);
    add(rc.line(R.x+2, R.y+3, R.r-1, R.y+2+J(1), pen(inkOf(el), {strokeWidth:1.4}))); });
  // underline
  page.querySelectorAll('.ul,.ul2').forEach(el => {
    const R = rel(el, page); const c = el.dataset.c ? `var(--${el.dataset.c})` : inkOf(el);
    const col = el.dataset.c ? getComputedStyle(document.documentElement).getPropertyValue('--'+el.dataset.c) : c;
    add(rc.line(R.x - 3, R.b - 1 + J(1), R.r + 6, R.b - 2 + J(2), pen(col, {strokeWidth:2, bowing:1.2})));
    if (el.classList.contains('ul2')) add(rc.line(R.x + 6, R.b + 4 + J(1), R.r + 2, R.b + 3 + J(2), pen(col, {strokeWidth:1.6, bowing:1.2})));
  });
  // answer boxes
  page.querySelectorAll('.box').forEach(el => {
    const R = rel(el, page);
    const col = el.dataset.c ? getComputedStyle(document.documentElement).getPropertyValue('--'+el.dataset.c) : inkOf(el);
    const x = R.x - 2, y = R.y - 1, w = R.w + 4, h = R.h + 2;
    // pen loop with overshoot at the start corner
    const pts = [[x + 8, y + J(1.5) - 2], [x + w + J(2), y + J(2)], [x + w + J(2), y + h + J(2)], [x + J(2), y + h + J(2)], [x + J(2), y + J(1.5)], [x + 22, y - 3 + J(1)]];
    add(rc.linearPath(pts, pen(col, {strokeWidth:1.8, roughness:0.7})));
  });
  // cancellations (slash)
  page.querySelectorAll('.cn').forEach(el => { const R = rel(el,page);
    add(rc.line(R.x - 1, R.b - 1, R.r + 2, R.y + 2, pen(getComputedStyle(document.documentElement).getPropertyValue('--r'), {strokeWidth:1.6}))); });
  // strike-throughs
  page.querySelectorAll('.wrong').forEach(el => {
    const R = rel(el, page); const s = el.dataset.s || 'one';
    const col = el.dataset.c === 'k' ? inkOf(el) : getComputedStyle(document.documentElement).getPropertyValue('--r');
    const o = pen(col, {strokeWidth:1.9, roughness:0.8, bowing:1});
    // find text line rows inside wrong block
    const rows = [...el.querySelectorAll(':scope > .ln')];
    const boxes = rows.length ? rows.map(r => rel(r, page)) : [R];
    if (s === 'x') {
      add(rc.line(R.x - 4, R.y + 2, R.r + 4, R.b - 2, o));
      add(rc.line(R.x - 2, R.b - 1, R.r + 3, R.y + 3, o));
    } else if (s === 'blot') {
      boxes.forEach(B => {
        for (let pass = 0; pass < 3; pass++) {
          const pts = []; let up = pass % 2 === 0; const ym = B.y + B.h*0.55;
          for (let x = B.x - 3; x < B.r + 4; x += 4 + J(1.5)) { pts.push([x, ym + (up ? -B.h*0.3 : B.h*0.25) + J(3)]); up = !up; }
          add(rc.curve(pts, pen(col, {strokeWidth:2.2, roughness:0.5})));
        }
      });
    } else if (s === 'zig') {
      boxes.forEach(B => {
        const pts = []; const step = 9; let up = true; const ym = B.y + B.h*0.52;
        for (let x = B.x - 3; x < B.r + 4; x += step + J(2)) { pts.push([x, ym + (up ? -B.h*0.17 : B.h*0.13) + J(2)]); up = !up; }
        add(rc.curve(pts, pen(col, {strokeWidth:1.5, roughness:0.4})));
      });
    } else {
      boxes.forEach(B => {
        const ym = B.y + B.h*0.55;
        add(rc.line(B.x - 4, ym + 3 + J(1), B.r + 5, ym - 3 + J(1), o));
        if (s === 'two') add(rc.line(B.x - 2, ym + 9 + J(1), B.r + 3, ym + 1 + J(1), o));
      });
    }
  });
  // tables
  page.querySelectorAll('table.tb').forEach(t => {
    const col = inkOf(t);
    const T = rel(t, page);
    const o = pen(col, {strokeWidth:1.4, roughness:0.6, bowing:0.4});
    add(rc.linearPath([[T.x + J(2), T.y + J(2)], [T.r + J(2), T.y + J(2)], [T.r + J(2), T.b + J(2)], [T.x + J(2), T.b + J(2)], [T.x + J(1), T.y - 2]], o));
    const rows = [...t.rows];
    rows.slice(1).forEach(r => { const R = rel(r, page); add(rc.line(T.x - 2 + J(2), R.y + J(1), T.r + 3 + J(2), R.y + J(1.5), o)); });
    [...rows[0].cells].slice(1).forEach(c => { const C = rel(c, page); add(rc.line(C.x + J(1.5), T.y - 2 + J(2), C.x + J(1.5), T.b + 3 + J(2), o)); });
  });
  // braces for piecewise
  page.querySelectorAll('.brace').forEach(el => {
    const R = rel(el, page); const x = R.x + 13, t = R.y + 2, b = R.b - 2, m = (t + b)/2;
    const d = `M${x+5},${t} C${x-1},${t} ${x+2},${m-6} ${x-1},${m-2} C${x-3},${m} ${x-5},${m} ${x-7},${m} C${x-5},${m} ${x-3},${m} ${x-1},${m+2} C${x+2},${m+6} ${x-1},${b} ${x+5},${b}`;
    add(rc.path(d, pen(inkOf(el), {strokeWidth:1.7, roughness:0.3})));
  });
  // highlighter (under text)
  page.querySelectorAll('.hl').forEach(el => {
    const R = rel(el, page); const c = el.dataset.c || 'rgba(255,221,0,.42)';
    const pad = 2, y0 = R.y + R.h*0.12, y1 = R.b - R.h*0.05;
    const poly = document.createElementNS('http://www.w3.org/2000/svg','polygon');
    poly.setAttribute('points', [[R.x-pad+J(2), y0+J(1.5)], [R.r+pad+J(3), y0+J(1.5)], [R.r+pad+J(3), y1+J(1.5)], [R.x-pad+J(2), y1+J(1.5)]].map(p=>p.join(',')).join(' '));
    poly.setAttribute('fill', c);
    under.appendChild(poly);
  });
  // hand-drawn arrows: <span class="arr" data-from="id" data-to="id">
  page.querySelectorAll('[data-arrow-to]').forEach(el => {
    const tgt = page.querySelector('#' + el.dataset.arrowTo); if (!tgt) return;
    const A = rel(el, page), B = rel(tgt, page);
    const col = getComputedStyle(document.documentElement).getPropertyValue('--' + (el.dataset.ac || 'r'));
    const sx = A.r + 4, sy = A.y + A.h/2, ex = B.x - 6, ey = B.y + B.h/2;
    const mx = (sx + ex)/2, my = Math.min(sy, ey) - 18;
    add(rc.curve([[sx, sy], [mx, my], [ex, ey]], pen(col, {strokeWidth:1.6, roughness:0.3})));
    const ang = Math.atan2(ey - my, ex - mx);
    [0.5, -0.5].forEach(da => add(rc.line(ex, ey, ex - 10*Math.cos(ang + da), ey - 10*Math.sin(ang + da), pen(col, {strokeWidth:1.6}))));
  });
  // sketches
  page.querySelectorAll('.sketch').forEach(el => drawSketch(el, page, rc, pen, add));
}

function drawSketch(el, page, rc, pen, add){
  const R = rel(el, page); const kind = el.dataset.k;
  const css = v => getComputedStyle(document.documentElement).getPropertyValue('--' + v);
  const k = css('k'), b = css('b'), r = css('r'), g = css('g'), p = css('p');
  const txt = (x, y, s, col, size) => { const t = document.createElementNS('http://www.w3.org/2000/svg','text');
    t.setAttribute('x', x); t.setAttribute('y', y); t.setAttribute('fill', col); t.setAttribute('font-family','Hand'); t.setAttribute('font-size', size||17);
    t.setAttribute('font-weight', 500); t.textContent = s; add(t); };
  const arrowHead = (x, y, ang, col) => [0.5, -0.5].forEach(da => add(rc.line(x, y, x - 8*Math.cos(ang+da), y - 8*Math.sin(ang+da), pen(col,{strokeWidth:1.4}))));
  const W = R.w, H = R.h, X = R.x, Y = R.y;
  if (kind === 'H') {
    // H(x) = (2x^2-8)/(x^2-9) ; window x[-7,7] y[-6,8]
    const sx = x => X + (x + 7) / 14 * W, sy = y => Y + (8 - y) / 14 * H;
    add(rc.line(X, sy(0), X + W, sy(0), pen(k,{strokeWidth:1.3}))); arrowHead(X+W, sy(0), 0, k);
    add(rc.line(sx(0), Y + H, sx(0), Y, pen(k,{strokeWidth:1.3}))); arrowHead(sx(0), Y, -Math.PI/2, k);
    const dash = {strokeWidth:1.3, strokeLineDash:[6,5]};
    add(rc.line(sx(3), Y + 4, sx(3), Y + H - 4, pen(r, dash)));
    add(rc.line(sx(-3), Y + 4, sx(-3), Y + H - 4, pen(r, dash)));
    add(rc.line(X + 4, sy(2), X + W - 4, sy(2), pen(g, dash)));
    const f = x => (2*x*x - 8)/(x*x - 9);
    const seg = (a, c) => { const pts = []; for (let i = 0; i <= 40; i++) { const x = a + (c - a) * i / 40; const y = f(x); if (y < 7.6 && y > -5.6) pts.push([sx(x), sy(y)]); } add(rc.curve(pts, pen(b, {strokeWidth:2, roughness:0.35}))); };
    seg(-6.9, -3.12); seg(-2.86, 2.86); seg(3.12, 6.9);
    txt(sx(3) + 4, Y + 16, 'x = 3', r); txt(sx(-3) - 46, Y + 16, 'x = −3', r); txt(X + W - 46, sy(2) + 18, 'y = 2', g);
  } else if (kind === 'N') {
    const sx = t => X + 18 + t / 30 * (W - 30), sy = y => Y + H - 14 - y / 95 * (H - 24);
    add(rc.line(X + 10, sy(0), X + W, sy(0), pen(k,{strokeWidth:1.3}))); arrowHead(X+W, sy(0), 0, k);
    add(rc.line(sx(0), Y + H - 6, sx(0), Y, pen(k,{strokeWidth:1.3}))); arrowHead(sx(0), Y, -Math.PI/2, k);
    add(rc.line(sx(0), sy(80), X + W - 6, sy(80), pen(r, {strokeWidth:1.3, strokeLineDash:[6,5]})));
    const pts = []; for (let i = 0; i <= 40; i++) { const t = 29 * i / 40; pts.push([sx(t), sy(80*t*t/(t*t+25))]); }
    add(rc.curve(pts, pen(b, {strokeWidth:2, roughness:0.3})));
    add(rc.circle(sx(5), sy(40), 7, pen(g,{strokeWidth:1.6, fill:g, fillStyle:'solid'})));
    add(rc.line(sx(5), sy(40), sx(5), sy(0), pen(g,{strokeWidth:1.1, strokeLineDash:[4,4]})));
    txt(sx(5) + 7, sy(40) + 18, '(5, 40)', g); txt(sx(0) - 20, sy(80) + 5, '80', r); txt(X + W - 70, sy(80) - 6, 'N = 80', r);
    txt(X + W - 12, sy(0) + 18, 't', k); txt(sx(0) + 6, Y + 12, 'N', k);
  } else if (kind === 'C') {
    const sx = x => X + 18 + x / 1200 * (W - 30), sy = y => Y + H - 14 - (y - 20) / 50 * (H - 24);
    add(rc.line(X + 10, Y + H - 14, X + W, Y + H - 14, pen(k,{strokeWidth:1.3}))); arrowHead(X+W, Y+H-14, 0, k);
    add(rc.line(sx(0), Y + H - 6, sx(0), Y, pen(k,{strokeWidth:1.3}))); arrowHead(sx(0), Y, -Math.PI/2, k);
    const pts = []; for (let i = 0; i <= 50; i++) { const x = 60 + 1120 * i / 50; const y = 2500/x + 35 + 0.02*x; if (y < 69) pts.push([sx(x), sy(y)]); }
    add(rc.curve(pts, pen(b, {strokeWidth:2, roughness:0.3})));
    add(rc.circle(sx(353.6), sy(49.14), 7, pen(g,{strokeWidth:1.6, fill:g, fillStyle:'solid'})));
    txt(sx(353.6) - 20, sy(49.14) + 22, 'mín', g); txt(X + W - 16, Y + H - 20, 'x', k); txt(sx(0) + 6, Y + 12, 'costo medio', k);
    txt(sx(800), sy(64), 'sigue creciendo', r);
  } else if (kind === 'NL') {
    const lo = +el.dataset.min, hi = +el.dataset.max;
    const sx = v => X + 14 + (v - lo) / (hi - lo) * (W - 28); const y = Y + H/2;
    add(rc.line(X, y, X + W, y, pen(k,{strokeWidth:1.4}))); arrowHead(X + W, y, 0, k);
    (el.dataset.segs || '').split(';').filter(Boolean).forEach(sg => { const [a, c] = sg.split(',').map(v => v === 'inf' ? hi + (hi-lo)*0.04 : v === '-inf' ? lo - (hi-lo)*0.04 : +v);
      add(rc.line(sx(a), y - 1, sx(c), y - 1, pen(b,{strokeWidth:4.5, roughness:0.4}))); });
    (el.dataset.pts || '').split(',').filter(Boolean).forEach(pt => { const [v, t] = pt.split(':'); const open = t !== 'c';
      add(rc.circle(sx(+v), y, 10, pen(r,{strokeWidth:1.8, fill: open ? '#fdfdfa' : r, fillStyle:'solid'})));
      txt(sx(+v) - 6, y + 24, v.replace('-', '−'), k, 17); });
  } else if (kind === 'P') {
    // parabola neighbourhood picture for 2b
    const sx = x => X + 22 + (x - 2.86) / 0.3 * (W - 34), sy = y => Y + H - 14 - (y - 9.1) / 1.8 * (H - 24);
    add(rc.line(X + 10, Y + H - 14, X + W, Y + H - 14, pen(k,{strokeWidth:1.3}))); arrowHead(X+W, Y+H-14, 0, k);
    add(rc.line(X + 22, Y + H - 6, X + 22, Y, pen(k,{strokeWidth:1.3}))); arrowHead(X+22, Y, -Math.PI/2, k);
    const band = (y, c) => add(rc.line(X + 22, sy(y), X + W - 8, sy(y), pen(c, {strokeWidth:1.2, strokeLineDash:[5,5]})));
    band(9.5, g); band(10.5, g); band(10, k);
    const pts = []; for (let i = 0; i <= 30; i++) { const x = 2.9 + 0.24 * i / 30; pts.push([sx(x), sy(x*x + 1)]); }
    add(rc.curve(pts, pen(b, {strokeWidth:2, roughness:0.3})));
    [[Math.sqrt(8.5), 9.5], [Math.sqrt(9.5), 10.5], [3, 10]].forEach(([x, y], i) => add(rc.line(sx(x), sy(y), sx(x), Y + H - 14, pen(i === 2 ? k : r, {strokeWidth:1.1, strokeLineDash:[4,4]}))));
    txt(sx(Math.sqrt(8.5)) - 14, Y + H + 4, 'x1', r, 16); txt(sx(3) - 4, Y + H + 4, '3', k, 16); txt(sx(Math.sqrt(9.5)) - 2, Y + H + 4, 'x2', r, 16);
    txt(X - 4, sy(10.5) + 5, '10,5', g, 15); txt(X - 2, sy(9.5) + 5, '9,5', g, 15);
    
  }
}

window.handify = async function(){
  await document.fonts.ready;
  document.querySelectorAll('.page').forEach((pg, i) => {
    seed = 1000 + i * 97;
    // line jitter
    pg.querySelectorAll('.ln').forEach(l => { if (!l.style.transform) l.style.transform = `translateX(${J(2.5).toFixed(1)}px) rotate(${J(0.35).toFixed(2)}deg)`; });
    processText(pg.querySelector('.content'));
  });
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  document.querySelectorAll('.page').forEach((pg, i) => { seed = 5000 + i * 131; drawPage(pg); });
  // overflow report
  const rep = [];
  document.querySelectorAll('.page').forEach((pg, i) => {
    const c = pg.querySelector('.content'); const P = pg.getBoundingClientRect();
    let maxB = 0; c.querySelectorAll('*').forEach(e => { const b = e.getBoundingClientRect().bottom - P.top; if (b > maxB) maxB = b; });
    let maxR = 0; c.querySelectorAll('.ln,.side,.fix,.wrong').forEach(e => { const r = e.getBoundingClientRect().right - P.left; if (r > maxR) maxR = r; });
    rep.push({page: i + 1, bottom: Math.round(maxB), right: Math.round(maxR)});
  });
  window.__report = rep; document.body.dataset.ready = '1';
};
})();
