s = open('gen4.py').read()
def cut(a, b, new):
    global s
    i = s.index(a); k = s.index(b)
    s = s[:i] + new + s[k:]

# --- no points
s = s.replace("""    return ('<div class="sep kn"></div>' + ln(f'<span class="tag" style="font-size:{R.choice([21,22,23])}px">EJERCICIO {n}</span> &nbsp;<span class="pts">{pts}</span>', 'kn', fixed=True)""",
              """    return ('<div class="sep kn"></div>' + ln(f'<span class="tag" style="font-size:{R.choice([21,22,23])}px">EJERCICIO {n}</span>', 'kn', fixed=True)""")
assert '<span class="pts">' not in s.split('def ex')[1].split('def paso')[0]

# --- short sustentación (one short paragraph, in order of exercises)
s = s.replace("def SUST(paras, title='Sustentación'):\n    out = [",
"""SHORT = iter([
 'Saqué factor común x y el trinomio 6x² − 7x − 20 lo <span class="wrong" data-s="one">factorize</span> factoricé con el método ac (−15 y 8).',
 'Agrupé de dos en dos, salió (x + 3) de factor común y x² − 4 es diferencia de cuadrados.',
 'Es diferencia de cubos con a = 3x y b = 2x − 2. El trinomio que queda no se factoriza porque Δ &lt; 0.',
 'Es irracional fraccionaria. Pedí radicando ≥ 0 y denominador ≠ 0 y tomé la <span class="wrong" data-s="blot">union</span> intersección.',
 'El ln necesita argumento &gt; 0, lo resolví con tabla de signos y queda (−2, 5).',
 'No hay indeterminación (abajo da 6), así que usé las propiedades y evalué directo.',
 'Daba 0/0: factoricé arriba con método ac y abajo con diferencia de cubos, cancelé (x − 3) y evalué.',
 'Daba 0/0, racionalicé con el conjugado, factoricé x² − 16 y <span class="wrong" data-s="one">simplifique</span> simplifiqué (x − 4).',
 'Los dos laterales dan 4, entonces el límite existe aunque h(2) = 5.',
 'Igualé los laterales: k + 2 = 2 + 2k ⟹ k = 0.',
])
def SUST(paras, title='Sustentación'):
    paras = [next(SHORT)]
    out = [""")

# --- more scribbles: random blotted mis-starts on body lines; stronger strikes
s = s.replace("""    st = f' style="{style}"' if style else ''
    return f'<span class="ln {cls}"{st}>{x}</span>'

def side(""", """    st = f' style="{style}"' if style else ''
    if not fixed and key is None and R.random() < 0.16 and 'kn' not in toks:
        x = f'<span class="wrong" data-s="blot" data-c="k">{R.choice(["=", "x", "(", "2", "3x", "= −", "lím", "x²"])}</span> ' + x
    return f'<span class="ln {cls}"{st}>{x}</span>'

def side(""")
s = s.replace("""def side(wrong, fixes, s='one', cls='ind2', c='r', mstyle='', stack=False):
""", """def side(wrong, fixes, s='one', cls='ind2', c='r', mstyle='', stack=False):
    if s == 'one' and R.random() < 0.4: s = R.choice(['zig', 'two', 'blot'])
""")
s = s.replace("def WR(x, s='one', c='r'): return", "def ATT(lines, note):\n    return [f'<div class=\"bigx\" style=\"position:relative;margin:6px 0 2px 0\">' + ''.join(lines) + '</div>', ln(note, 'sm r ind2')]\ndef WR(x, s='one', c='r'): return")

# --- exercise 3 with full wrong attempt then redo
cut("# ================= 3 =================", "# ================= 4 =================", r'''# ================= 3 =================
add([
 ex(3, f'Factorizar &nbsp;R(x) = 27x{s3} − 8(x − 1){s3}'),
 paso('Paso 1 — Escribir cada término como un cubo'),
 ln(f'27 = 3{s3} ⟹ 27x{s3} = (3x){s3}', 'ind2'),
 side(f'8(x − 1){s3} = (8x − 8){s3}', [ln('✗ la raíz cúbica de 8 es 2, no 8', 'xs r'), ln(f'8(x − 1){s3} = [2(x − 1)]{s3} = (2x − 2){s3}')], 'two'),
 ln(f'⟹ a = 3x , &nbsp; b = 2x − 2 &nbsp;&nbsp;<span class="sm">(diferencia de cubos)</span>', 'ind2'),
 side(f'a{s3} − b{s3} = (a − b)(a{s2} − ab + b{s2})', [ln('✗ esa es la de suma de cubos', 'xs r'), ln(f'a{s3} − b{s3} = (a − b)(a{s2} + ab + b{s2})')], 'zig'),
 ln('1er intento:', 'sm ind', fixed=True),
 *ATT([
   ln('a − b = 3x − 2x − 2 = x − 2', 'ind2'),
   ln(f'a{s2} + ab + b{s2} = 9x{s2} + (6x{s2} − 6x) + (4x{s2} − 8x + 4) = 19x{s2} − 14x + 4', 'ind2'),
   ln(f'R(x) = (x − 2)(19x{s2} − 14x + 4)', 'ind2 lg'),
   ln(f'compruebo x = 0 : R(0) = 0 − 8(−1){s3} = 8 &nbsp; pero (−2)(4) = −8 ✗✗', 'sm ind2'),
 ], '✗ no da!! el error está en a − b : −(2x − 2) = −2x + 2 &nbsp;→ lo vuelvo a hacer ↓'),
 paso('Paso 2 — Primer factor (a − b) — bien'),
 ln(f'a − b = 3x − (2x − 2) = 3x − 2x + 2 = {HL("x + 2")}', 'ind2'),
 paso('Paso 3 — Segundo factor (a² + ab + b²)'),
 side(f'a{s2} = 3x{s2}', [ln('✗ el 3 también se eleva', 'xs r'), ln(f'a{s2} = (3x){s2} = 9x{s2}')], 'one'),
 ln(f'ab = 3x(2x − 2) = 6x{s2} − 6x', 'ind2'),
 side(f'b{s2} = (2x − 2){s2} = 4x{s2} + 4', [ln('✗ falta el doble producto 8x', 'xs r'), ln(f'b{s2} = 4x{s2} − 8x + 4')], 'two'),
 ln(f'a{s2} + ab + b{s2} = 9x{s2} + 6x{s2} − 6x + 4x{s2} − 8x + 4 = {HL(f"19x{s2} − 14x + 4")}', 'ind2'),
 ln(f'Δ = (−14){s2} − 4(19)(4) = 196 − 304 = −108 &lt; 0 → no se factoriza más', 'sm ind2'),
 ln(f'∴ &nbsp;{BOX(f"R(x) = (x + 2)(19x{s2} − 14x + 4)")}', 'lg ind'),
 ln(f'compruebo x = 0 : R(0) = 8 &nbsp;y&nbsp; (2)(4) = 8 ✓ &nbsp;&nbsp; x = 1 : 27 &nbsp;y&nbsp; (3)(9) = 27 ✓', 'sm ind2'),
 *SUST([]),
])

''')

# --- exercises 6 and 7 with full wrong attempt then redo
cut("RED = False\n# ================= 6 (resultado erróneo a propósito) =================", "# ================= 8 =================", r'''RED = False
# ================= 6 =================
add([
 ex(6, f'{LIM("x→−2")} {F(f"3x{s3} + 4x{s2} − 5x + 2", SQ(f"x{s2} + 5") + " + 3")}'),
 paso('Propiedades'),
 ln('(P1) lím f/g = lím f / lím g &nbsp;si lím g ≠ 0 &nbsp;&nbsp; (P2) lím (f ± g) = lím f ± lím g', 'sm ind2'),
 ln(f'(P3) lím c·f = c·lím f &nbsp;&nbsp; (P4) lím x<sup>n</sup> = a<sup>n</sup> &nbsp;&nbsp; (P5) lím {SQ("g")} = {SQ("lím g")}', 'sm ind2'),
 ln('1er intento:', 'sm ind', fixed=True),
 *ATT([
   ln(f'num: 3(−2){s3} + 4(−2){s2} − 5(−2) + 2 = −24 + 16 − 10 + 2 = −16', 'ind2'),
   ln(f'den: {SQ(f"(−2){s2} + 5")} + 3 = {SQ("9")} + 3 = 6', 'ind2'),
   ln(f'= {F("−16", "6")} = {BOX("−" + F("8", "3"))}', 'ind2 lg'),
 ], '✗ mal el signo: −5 · (−2) = +10, no −10 → lo vuelvo a hacer ↓'),
 paso('Numerador — (P2), (P3), (P4)'),
 ln(f'{LIM("x→−2")} (3x{s3} + 4x{s2} − 5x + 2) = 3(−2){s3} + 4(−2){s2} − 5(−2) + 2', 'ind2'),
 side(f'(−2){s3} = 8', [ln('✗ impar → negativo', 'xs r'), ln(f'(−2){s3} = −8 → 3(−8) = −24')], 'two', 'ind3'),
 side(f'4(−2){s2} = −16', [ln('✗ par → positivo', 'xs r'), ln(f'4(−2){s2} = 4(4) = 16')], 'zig', 'ind3'),
 ln(f'−5(−2) = {HL("+10")} &nbsp;<span class="sm">(menos por menos)</span>', 'ind3'),
 ln('= −24 + 16 + 10 + 2 = 4', 'ind3'),
 paso('Denominador — (P2), (P5)'),
 side(f'= {SQ("−4 + 5")} + 3 = 4', [ln(f'✗ (−2){s2} = +4', 'xs r'), ln(f'{LIM("x→−2")} ({SQ(f"x{s2} + 5")} + 3) = {SQ("4 + 5")} + 3 = 3 + 3 = 6')], 'two', 'ind2'),
 ln('6 ≠ 0 → puedo usar (P1)', 'sm ind3'),
 paso('Resultado — (P1)'),
 side(f'= {F("4", "6")} = {F("1", "3")}', [ln('✗ 4/6 se simplifica entre 2', 'xs r'), ln(f'= {F("4", "6")} = {F("2", "3")}')], 'zig', 'ind2'),
 ln(f'∴ &nbsp;{LIM("x→−2")} {F(f"3x{s3} + 4x{s2} − 5x + 2", SQ(f"x{s2} + 5") + " + 3")} = {BOX(F("2", "3"))}', 'lg ind'),
 *SUST([]),
])

# ================= 7 =================
add([
 ex(7, f'{LIM("x→3")} {F(f"2x{s2} − 5x − 3", f"x{s3} − 27")}'),
 paso('Paso 1 — Sustitución directa'),
 ln(f'{F(f"2(9) − 15 − 3", "27 − 27")} = {F("0", "0")} &nbsp;→ indeterminación, factorizo', 'ind2'),
 side(f'2(3){s2} = 36', [ln('✗ primero la potencia: 2·9 = 18', 'xs r')], 'one', 'ind3'),
 paso('Paso 2 — Numerador (método ac)'),
 ln('a · c = 2(−3) = −6 &nbsp; <span class="sm">m · n = −6 , m + n = −5</span>', 'ind2'),
 side('−3 y 2', [ln('✗ suma −1', 'xs r'), ln(f'{HL("−6 y 1")} ✓')], 'one'),
 side('= 2x(x − 3) − 1(x − 3)', [ln('✗ es +1', 'xs r'), ln(f'2x{s2} − 6x + x − 3 = 2x(x − 3) + 1(x − 3) = (x − 3)(2x + 1)')], 'two'),
 ln('1er intento (denominador):', 'sm ind', fixed=True),
 *ATT([
   ln(f'x{s3} − 27 = (x − 3)(x{s2} − 3x + 9)', 'ind2'),
   ln(f'{LIM("x→3")} {F("2x + 1", f"x{s2} − 3x + 9")} = {F("7", "9 − 9 + 9")} = {BOX(F("7", "9"))}', 'ind2'),
 ], '✗ usé mal la fórmula: a³ − b³ = (a − b)(a² <b>+</b> ab + b²) → lo vuelvo a hacer ↓'),
 paso('Paso 3 — Denominador (diferencia de cubos) — bien'),
 side(f'x{s3} − 27 = (x − 3){s3}', [ln('✗ no', 'xs r'), ln(f'x{s3} − 27 = x{s3} − 3{s3} = (x − 3)(x{s2} + 3x + 9)')], 'x'),
 paso('Paso 4 — Simplificar y evaluar'),
 ln(f'{LIM("x→3")} {F(CN("(x − 3)") + "(2x + 1)", CN("(x − 3)") + f"(x{s2} + 3x + 9)")} = {LIM("x→3")} {F("2x + 1", f"x{s2} + 3x + 9")}', 'ind2'),
 side(f'= {F("6", "27")}', [ln('✗ 2(3) + 1 = 7', 'xs r'), ln(f'= {F("2(3) + 1", "9 + 9 + 9")} = {F("7", "27")}')], 'one', 'ind2'),
 ln(f'∴ &nbsp;{BOX(F("7", "27"))}', 'lg ind'),
 *SUST([]),
])

''')
s = s.replace("'notes4.html'", "'notes5.html'")
open('gen5.py', 'w').write(s)
