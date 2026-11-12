# Generates notes3.html — Parcial 2 (factorización, dominio y límites), flujo con paginado automático
import os, random
D = os.path.dirname(os.path.abspath(__file__))
R = random.Random(20261112)

SIZES = {None: [26, 27, 28, 29, 30, 31, 33], 'xs': [18, 19, 20, 21], 'sm': [21, 22, 23, 24, 25],
         'lg': [33, 35, 37, 39], 'xl': [40, 44, 48], 'pasos': [23, 24, 25, 27], 'ex': [33, 35, 38, 41]}
RED = False

def F(n, d): return f'<span class="fr"><span>{n}</span><span>{d}</span></span>'
def LIM(u): return f'<span class="lim"><span>lím</span><span class="u">{u}</span></span>'
def SQ(x): return f'<span class="sq">{x}</span>'
def BOX(x, c='k'):
    if RED: return f'<span class="box rr" data-c="red">{x}</span>'
    return f'<span class="box">{x}</span>'
def HL(x): return f'<span class="ul">{x}</span>'
def CN(x): return f'<span class="cn">{x}</span>'

def ln(x, cls='', style='', fixed=False):
    if RED: cls = ' '.join('rr' if t == 'r' else t for t in cls.split())
    toks = cls.split()
    key = next((t for t in toks if t in SIZES), None)
    if not fixed and not any(t in ('h1', 'huge', 'md') for t in toks):
        style = f'font-size:{R.choice(SIZES[key])}px;' + style
    st = f' style="{style}"' if style else ''
    return f'<span class="ln {cls}"{st}>{x}</span>'

def side(wrong, fixes, s='one', cls='ind2', c='r', mstyle='', stack=False):
    if stack: mstyle = 'flex-direction:column;gap:0;' + mstyle
    w = ''.join(ln(x) for x in (wrong if isinstance(wrong, list) else [wrong]))
    st = f' style="{mstyle}"' if mstyle else ''
    return f'<div class="side {cls}"{st}><div class="wrong" data-s="{s}" data-c="{c}">{w}</div><div class="fix">{"".join(fixes)}</div></div>'
def WR(x, s='one', c='r'): return f'<span class="wrong" data-s="{s}" data-c="{c}">{x}</span>'
def ex(n, title, pts='[0,5 pts]'):
    return ('<div class="sep kn"></div>' + ln(f'<span class="tag" style="font-size:{R.choice([21,22,23])}px">EJERCICIO {n}</span> &nbsp;<span class="pts">{pts}</span>', 'kn', fixed=True)
            + ln(title, 'ex kn'))
def paso(t): return ln(f'<span class="ul">{t}</span>', 'pasos ind kn')
def nota(t, c='p', size='sm', cls='ind2'): return ln(t, f'{size} {c} {cls}')
def wrapln(t, cls='sm ind2', w=640):
    return ln(t, cls, f'white-space:normal;width:{w}px')
def sketch(k, w, h, extra='', style=''): return f'<div class="sketch" data-k="{k}" {extra} style="width:{w}px;height:{h}px;{style}"></div>'
def SUST(paras, title='Sustentación'):
    out = [ln(f'<span class="tag" style="font-size:22px">{title.upper()}</span>', 'ind kn', 'margin-top:16px', fixed=True)]
    for p in paras:
        out.append(f'<div class="sust ind2" style="margin-top:4px;margin-bottom:4px">{wrapln(p, R.choice(["sm","sm","xs"]) + " k", 610)}</div>')
    return out
def table(rows, style=''):
    h = f'<table class="tb ind" style="font-size:{R.choice([19,20,21,22])}px;{style}">'
    for r in rows: h += '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return h + '</table>'
sup = lambda x: f'<sup>{x}</sup>'
s2, s3 = sup(2), sup(3)

B = []  # flow of blocks
add = B.extend

# ================= ENCABEZADO =================
add([
 ln('<span class="tag" style="font-size:34px">PARCIAL 2</span>', '', 'text-align:center;margin-top:4px', fixed=True),
 ln('<span class="tag" style="font-size:18px">FACTORIZACIÓN, DOMINIO Y LÍMITES</span>', '', 'text-align:center;margin-top:-6px', fixed=True),
 ln('Nombre: <span class="ul">Sebastián Rodríguez</span> &nbsp;&nbsp; Fecha: 12/11/26', 'sm', 'margin-left:300px;margin-top:10px', fixed=True),
])

# ================= 1 =================
add([
 ex(1, f'Factorizar &nbsp;P(x) = 6x{s3} − 7x{s2} − 20x'),
 paso('Paso 1 — Factor común'),
 nota('miro los tres términos: 6x³ , −7x² , −20x', 'k', 'sm'),
 nota('coeficientes: MCD(6, 7, 20) = 1 &nbsp;·&nbsp; variable: la menor potencia es x¹ → saco x', 'p', 'xs'),
 side(f'P(x) = 2x(3x{s2} − 7x − 10)', [ln('✗ 7 no se divide entre 2 !!', 'sm r'), ln(f'P(x) = x(6x{s2} − 7x − 20)', 'b')], 'two'),
 side(f'P(x) = x{s2}(6x − 7 − 20)', [ln('✗ el último término solo tiene x¹', 'xs r')], 'x', 'ind3'),
 paso(f'Paso 2 — Trinomio ax{s2} + bx + c &nbsp;<span class="xs k">(método ac / aspa)</span>'),
 ln(f'6x{s2} − 7x − 20 &nbsp;→&nbsp; a = 6 , b = −7 , c = −20', 'ind2'),
 ln(f'a · c = 6 · (−20) = −120', 'ind2'),
 nota('busco dos números m y n con &nbsp; m · n = −120 &nbsp; y &nbsp; m + n = −7', 'p', 'sm'),
 ln('pruebo parejas de factores de 120:', 'sm ind2'),
 ln(f'{WR("−12 y 10 → suma −2")} &nbsp; {WR("−10 y 12 → suma 2")} &nbsp; {WR("−20 y 6 → suma −14", "one", "k")}', 'ind3 sm'),
 ln(f'{WR("−24 y 5 → suma −19")} &nbsp; {WR("−30 y 4 → suma −26", "one", "k")}', 'ind3 sm'),
 side('15 y −8 → suma 7', [ln('✗ me da +7, necesito −7 → cambio signos', 'xs r'), ln(f'{HL("−15 y 8")} → (−15)(8) = −120 ✓', 'g'), ln('−15 + 8 = −7 ✓', 'g', 'margin-left:60px')], 'two', 'ind3'),
 paso('Paso 3 — Desdoblar el término central y agrupar'),
 ln(f'6x{s2} − 7x − 20 = 6x{s2} − 15x + 8x − 20', 'ind2'),
 ln(f'= (6x{s2} − 15x) + (8x − 20)', 'ind2', 'margin-left:150px'),
 side('= 3x(2x − 5) + 4(2x + 5)', [ln('✗ 4 · 5 = 20 pero el signo es −', 'xs r'), ln('= 3x(2x − 5) + 4(2x − 5)')], 'two', 'ind2', mstyle='margin-left:150px'),
 side('= (2x − 5)(3x − 4)', [ln('✗ el 4 venía con +', 'xs r')], 'zig', 'ind2', mstyle='margin-left:150px'),
 ln('= (2x − 5)(3x + 4)', 'ind2', 'margin-left:150px'),
 ln(f'∴ &nbsp;{BOX("P(x) = x(3x + 4)(2x − 5)")}', 'lg ind'),
 paso('Comprobación 1 — multiplicando'),
 ln(f'(3x + 4)(2x − 5) = 6x{s2} − 15x + 8x − 20 = 6x{s2} − 7x − 20', 'sm b ind2'),
 ln(f'x · (6x{s2} − 7x − 20) = 6x{s3} − 7x{s2} − 20x ✓', 'sm b ind2'),
 paso('Comprobación 2 — raíces'),
 ln(f'x = 0 &nbsp;;&nbsp; 3x + 4 = 0 → x = −{F("4","3")} &nbsp;;&nbsp; 2x − 5 = 0 → x = {F("5","2")}', 'ind2'),
 side(f'P({F("5","2")}) = 6({F("125","8")}) − 7({F("25","4")}) − 50 = 93,75 − 43,75 − 50 = 1', [ln('✗ 93,75 − 43,75 = 50 → 50 − 50 = 0', 'xs r'), ln(f'P({F("5","2")}) = 0 ✓', 'g')], 'one', 'ind2', stack=True),
 *SUST([
   'Primero apliqué <span class="wrong" data-s="one">fator</span> <b>factor común monomio</b> porque los tres términos tienen la variable x; el MCD de los coeficientes es 1, entonces solo sale x.',
   'El factor que queda, 6x² − 7x − 20, es un <b>trinomio de la forma ax² + bx + c</b> con a ≠ 1. Por eso usé el <span class="wrong" data-s="blot">metodo de</span> método ac: busqué dos números cuyo producto sea a·c = −120 y cuya suma sea b = −7, que son −15 y 8.',
   'Con esos números desdoblé −7x en −15x + 8x, agrupé de dos en dos y saqué el factor común binomio (2x − 5). La factorización es completa porque los tres factores son de primer grado.',
 ]),
])

# ================= 2 =================
add([

 ex(2, f'Factorizar &nbsp;Q(x) = x{s3} + 3x{s2} − 4x − 12'),
 paso('Paso 1 — Agrupación (de 2 en 2)'),
 side(f'(x{s3} + 3x{s2}) − (4x − 12)', [ln('✗ al sacar el − cambia el signo del 12', 'xs r'), ln(f'Q(x) = (x{s3} + 3x{s2}) + (−4x − 12)'), ln(f'= (x{s3} + 3x{s2}) − (4x + 12)', '', 'margin-left:70px')], 'two'),
 nota('agrupo el 1º con el 2º y el 3º con el 4º porque tienen factores comunes', 'p', 'xs'),
 paso('Paso 2 — Factor común en cada grupo'),
 ln(f'x{s3} + 3x{s2} = x{s2}(x + 3)', 'ind2'),
 side('4x + 12 = 2(2x + 6)', [ln('✗ no saqué el MCD completo: es 4', 'xs r'), ln('4x + 12 = 4(x + 3)')], 'one'),
 side(f'= x{s2}(x + 3) − 4(x − 3)', [ln('✗ 12 / 4 = +3 → (x + 3)', 'xs r'), ln(f'= x{s2}(x + 3) − 4(x + 3)')], 'zig'),
 paso('Paso 3 — Factor común por agrupación: (x + 3)'),
 ln(f'= (x + 3)(x{s2} − 4)', 'ind2'),
 paso('Paso 4 — Diferencia de cuadrados'),
 nota('a² − b² = (a − b)(a + b) &nbsp; con a = x , b = 2', 'b', 'sm'),
 side(f'x{s2} − 4 = (x − 2){s2}', [ln(f'✗ (x − 2){s2} = x{s2} − 4x + 4 ≠ x{s2} − 4', 'xs r'), ln(f'x{s2} − 4 = x{s2} − 2{s2} = (x − 2)(x + 2)')], 'x'),
 side(f'x{s2} − 4 = (x − 4)(x + 4)', [ln('✗ la raíz de 4 es 2', 'xs r')], 'one', 'ind3'),
 ln(f'∴ &nbsp;{BOX("Q(x) = (x + 3)(x − 2)(x + 2)")}', 'lg ind'),
 paso('Comprobación — evaluando'),
 ln(f'Q(1) = 1 + 3 − 4 − 12 = −12 &nbsp;y&nbsp; (4)(−1)(3) = −12 ✓', 'sm b ind2'),
 ln('raíces: Q(−3) = −27 + 27 + 12 − 12 = 0 ✓ &nbsp; Q(2) = 8 + 12 − 8 − 12 = 0 ✓', 'sm b ind2'),
 side('Q(−2) = −8 + 12 − 8 − 12 = −16', [ln('✗ −4(−2) = +8', 'xs r'), ln('Q(−2) = −8 + 12 + 8 − 12 = 0 ✓', 'sm b')], 'two', 'ind2'),
 paso('Comprobación — Ruffini con x = −3'),
 table([['', '1', '3', '−4', '−12'], ['−3', '', '−3', '0', '12'], ['', '1', '0', '−4', '<span class="g">0 ✓</span>']], 'margin-left:80px'),
 nota('cociente: x² − 4 → coincide con el paso 3', 'p', 'xs'),
 *SUST([
   'Como el polinomio tiene cuatro términos <span class="wrong" data-s="one">y ninguno</span> sin factor común en todos, usé <b>factor común por agrupación</b>: en el primer par sale x² y en el segundo sale 4, quedando el binomio común (x + 3).',
   'El factor x² − 4 es una <b>diferencia de cuadrados</b> porque x² y 4 = 2² son cuadrados perfectos separados por un signo menos, entonces se escribe como (x − 2)(x + 2).',
   'Lo comprobé evaluando las raíces −3, 2 y −2 (todas dan 0) y con división sintética, así que está en su mínima expresión.',
 ]),
])

# ================= 3 =================
add([

 ex(3, f'Factorizar &nbsp;R(x) = 27x{s3} − 8(x − 1){s3}'),
 paso('Paso 1 — Escribir cada término como un cubo'),
 ln(f'27 = 3{s3} ⟹ 27x{s3} = (3x){s3}', 'ind2'),
 side(f'8(x − 1){s3} = (8x − 8){s3}', [ln('✗ la raíz cúbica de 8 es 2, no 8', 'xs r'), ln(f'8(x − 1){s3} = [2(x − 1)]{s3} = (2x − 2){s3}')], 'two'),
 ln(f'⟹ a = 3x , &nbsp; b = 2x − 2 &nbsp;&nbsp;<span class="sm p">(diferencia de cubos)</span>', 'ind2'),
 side(f'a{s3} − b{s3} = (a − b)(a{s2} − ab + b{s2})', [ln('✗ esa es la de suma de cubos', 'xs r'), ln(f'a{s3} − b{s3} = (a − b)(a{s2} + ab + b{s2})', 'b')], 'zig'),
 paso('Paso 2 — Primer factor (a − b)'),
 side('3x − 2x − 2 = x − 2', [ln('✗ −(2x − 2) = −2x + 2', 'xs r'), ln(f'a − b = 3x − (2x − 2) = 3x − 2x + 2 = {HL("x + 2")}')], 'two'),
 paso('Paso 3 — Segundo factor (a² + ab + b²)'),
 side(f'a{s2} = 3x{s2}', [ln('✗ el 3 también se eleva', 'xs r'), ln(f'a{s2} = (3x){s2} = 9x{s2}')], 'one'),
 ln(f'ab = 3x(2x − 2) = 6x{s2} − 6x', 'ind2'),
 side(f'b{s2} = (2x − 2){s2} = 4x{s2} + 4', [ln('✗ falta el doble producto: 2(2x)(2) = 8x', 'xs r'), ln(f'b{s2} = (2x){s2} − 2(2x)(2) + 2{s2} = 4x{s2} − 8x + 4')], 'two'),
 ln(f'a{s2} + ab + b{s2} = 9x{s2} + 6x{s2} − 6x + 4x{s2} − 8x + 4', 'ind2'),
 nota('agrupo semejantes: x² → 9 + 6 + 4 = 19 &nbsp; x → −6 − 8 = −14 &nbsp; constante → 4', 'p', 'xs', 'ind3'),
 side(f'= 19x{s2} − 2x + 4', [ln('✗ −6x − 8x = −14x', 'xs r'), ln(f'= {HL(f"19x{s2} − 14x + 4")}')], 'one', 'ind3'),
 paso('Paso 4 — ¿Se puede factorizar más?'),
 ln(f'Δ = b{s2} − 4ac = (−14){s2} − 4(19)(4) = 196 − 304 = −108 &lt; 0', 'ind2'),
 nota('discriminante negativo → no tiene raíces reales → es irreducible', 'p', 'sm', 'ind3'),
 ln(f'∴ &nbsp;{BOX(f"R(x) = (x + 2)(19x{s2} − 14x + 4)")}', 'lg ind'),
 paso('Comprobación — desarrollando los dos lados'),
 ln(f'(x − 1){s3} = x{s3} − 3x{s2} + 3x − 1', 'sm b ind2'),
 ln(f'R(x) = 27x{s3} − 8x{s3} + 24x{s2} − 24x + 8 = 19x{s3} + 24x{s2} − 24x + 8', 'sm b ind2'),
 ln(f'(x + 2)(19x{s2} − 14x + 4) = 19x{s3} − 14x{s2} + 4x + 38x{s2} − 28x + 8', 'sm b ind2'),
 side(f'= 19x{s3} + 52x{s2} − 24x + 8', [ln('✗ −14 + 38 = 24', 'xs r')], 'one', 'ind2', stack=True),
 ln(f'= 19x{s3} + 24x{s2} − 24x + 8 ✓ iguales', 'sm b ind3'),
 ln(f'x = 1 : &nbsp;R(1) = 27 − 0 = 27 &nbsp;y&nbsp; (3)(19 − 14 + 4) = 3 · 9 = 27 ✓', 'sm b ind2'),
 *SUST([
   'Reconocí una <b>diferencia de cubos</b> porque 27x³ = (3x)³ y 8(x − 1)³ = (2x − 2)³ son cubos perfectos restados. <span class="wrong" data-s="blot">Aplique</span> Apliqué a³ − b³ = (a − b)(a² + ab + b²) con a = 3x y b = 2x − 2.',
   'Al simplificar el primer factor hay que repartir el signo menos: 3x − (2x − 2) = x + 2. En el segundo factor desarrollé cada producto y reduje términos semejantes.',
   'El trinomio 19x² − 14x + 4 tiene discriminante negativo, por eso no se factoriza en los reales. La comprobación desarrollando ambos lados da el mismo polinomio.',
 ]),
])

# ================= 4 =================
add([

 ex(4, f'f(x) = {F(SQ("2x − 6"), f"x{s2} − 7x + 12")}'),
 ln('<span class="lab">a)</span> Tipo de función', 'ind bold kn'),
 side('Es una función racional', [ln('✗ tiene x dentro de una raíz', 'xs r'), ln(f'Es algebraica {HL("irracional fraccionaria")}', 'b')], 'two'),
 side('Es trascendente', [ln('✗ solo usa operaciones algebraicas (raíz, cociente, potencias)', 'xs r')], 'x', 'ind3'),
 wrapln('→ irracional: la variable está dentro de un radical. &nbsp;→ fraccionaria: es un cociente y el denominador depende de x.', 'sm ind2', 620),
 ln('<span class="lab">b)</span> Dominio natural', 'ind bold kn'),
 paso('Restricción 1 — radicando ≥ 0 (raíz de índice par)'),
 ln('2x − 6 ≥ 0', 'ind2'),
 ln('2x ≥ 6 &nbsp; <span class="xs p">(sumo 6)</span>', 'ind2'),
 side('x ≥ −3', [ln('✗ 6/2 = +3', 'xs r'), ln(f'x ≥ 3 &nbsp;<span class="xs p">(divido entre 2, positivo → no cambia)</span>')], 'one'),
 ln(f'{HL("[3 , +∞)")}', 'ind3'),
 paso('Restricción 2 — denominador ≠ 0'),
 ln(f'x{s2} − 7x + 12 ≠ 0 &nbsp; <span class="sm p">busco: producto 12, suma −7</span>', 'ind2'),
 side('(x − 6)(x − 1)', [ln('✗ (−6)(−1) = 6, no 12', 'xs r'), ln('(x − 3)(x − 4) ≠ 0')], 'blot', c='k'),
 side('(x − 2)(x − 6)', [ln('✗ suma −8', 'xs r')], 'one', 'ind3'),
 ln('⟹ x − 3 ≠ 0 → x ≠ 3 &nbsp;&nbsp;&nbsp; x − 4 ≠ 0 → x ≠ 4', 'ind2'),
 paso('Intersección de restricciones'),
 ln('x ≥ 3 &nbsp; y &nbsp; x ≠ 3 &nbsp; y &nbsp; x ≠ 4 &nbsp; ⟹ &nbsp; x &gt; 3 , x ≠ 4', 'ind2'),
 sketch('NL', 420, 60, 'data-min="1" data-max="7" data-pts="3:o,4:o" data-segs="3,4;4,inf"', 'margin-left:120px'),
 side('Dom f = [3 , 4) ∪ (4 , +∞)', [ln('✗ en x = 3 el denominador da 0 → se excluye', 'xs r')], 'two'),
 ln(f'∴ &nbsp;{BOX("Dom f = (3 , 4) ∪ (4 , +∞)")}', 'lg ind'),
 paso('Comprobación con valores'),
 table([['x', '2', '3', '3,5', '4', '5'],
        ['2x − 6', '−2 ✗', '0', '1', '2', '4'],
        ['denominador', '2', '<span class="r">0 ✗</span>', '−0,25', '<span class="r">0 ✗</span>', '2'],
        ['f(x)', '<span class="r">no</span>', '<span class="r">no</span>', '<span class="g">−4</span>', '<span class="r">no</span>', '<span class="g">1</span>']]),
 nota('x = 3,5 : √1 / (12,25 − 24,5 + 12) = 1/(−0,25) = −4 ✓ &nbsp;&nbsp; x = 5 : √4 / 2 = 1 ✓', 'p', 'xs'),
 *SUST([
   'La función tiene dos condiciones: la raíz cuadrada (índice par) solo está definida en los reales si el radicando es mayor o igual que cero, y una fracción no existe si su denominador es cero.',
   'De la primera <span class="wrong" data-s="one">ecuación</span> inecuación sale x ≥ 3. Para la segunda factoricé el trinomio x² − 7x + 12 = (x − 3)(x − 4) y excluí x = 3 y x = 4.',
   'El dominio es la intersección de ambas condiciones. Aunque x = 3 cumple la raíz, anula el denominador, por eso el intervalo empieza abierto en 3.',
 ]),
])

# ================= 5 =================
RED = True
add([

 ex(5, f'g(x) = ln {F("x + 2", "5 − x")}'),
 paso('Componentes de la función compuesta'),
 ln(f'g(x) = ln(u(x)) &nbsp;con&nbsp; u(x) = {F("x + 2", "5 − x")}', 'ind2'),
 ln(f'• externa — logarítmica: ln(u) solo existe si {HL("u &gt; 0")}', 'ind2'),
 nota('dominio de ln: (0, +∞) ; es creciente y ln(1) = 0', 'p', 'xs', 'ind3'),
 ln(f'• interna — racional: denominador ≠ 0 ⟹ 5 − x ≠ 0 ⟹ x ≠ 5', 'ind2'),
 side(f'{F("x + 2", "5 − x")} ≥ 0', [ln('✗ ln(0) no existe → tiene que ser estrictamente &gt; 0', 'xs r'), ln(f'{F("x + 2", "5 − x")} &gt; 0')], 'two'),
 side(f'x + 2 &gt; 5 − x', [ln('✗ no se puede pasar a multiplicar sin saber el signo', 'xs r')], 'x', 'ind3'),
 paso('Puntos críticos'),
 ln('numerador: x + 2 = 0 ⟹ x = −2', 'ind2'),
 side('5 − x = 0 ⟹ x = −5', [ln('✗ paso la x: 5 = x', 'xs r'), ln('denominador: 5 − x = 0 ⟹ x = 5')], 'one'),
 paso('Tabla de signos'),
 '<table class="tb ind" style="font-size:21px;margin-left:60px"><tr><td></td><td>(−∞, −2)</td><td>(−2, 5)</td><td>(5, +∞)</td></tr>'
 '<tr><td>x + 2</td><td class="r">−</td><td class="g">+</td><td class="g">+</td></tr>'
 '<tr><td>5 − x</td><td class="g">+</td><td class="g">+</td><td class="r">−</td></tr>'
 '<tr><td class="bold">cociente</td><td class="r bold">−</td><td class="g bold">+</td><td class="r bold">−</td></tr></table>',
 nota('pruebo: x = 0 → 2/5 &gt; 0 ✓ &nbsp;&nbsp; x = 6 → 8/(−1) &lt; 0 ✗ &nbsp;&nbsp; x = −3 → −1/8 &lt; 0 ✗', 'p', 'xs'),
 side('Dom g = (−∞, −2) ∪ (5, +∞)', [ln('✗ tomé los intervalos negativos, necesito el +', 'xs r')], 'x'),
 sketch('NL', 420, 60, 'data-min="-4" data-max="7" data-pts="-2:o,5:o" data-segs="-2,5"', 'margin-left:120px'),
 ln(f'∴ &nbsp;{BOX("Dom g = (−2 , 5)")}', 'lg ind'),
 paso('Comprobación'),
 ln(f'g(0) = ln {F("2","5")} = ln 0,4 ≈ −0,916 ✓ existe', 'sm b ind2'),
 ln(f'g(−2) = ln {F("0","7")} = ln 0 ✗ &nbsp;&nbsp; g(5) = ln {F("7","0")} ✗ &nbsp;&nbsp; g(6) = ln(−8) ✗', 'sm b ind2'),
 nota('cerca de −2 : u → 0⁺ ⟹ g → −∞ &nbsp;&nbsp; cerca de 5 : u → +∞ ⟹ g → +∞', 'p', 'xs'),
 *SUST([
   'g es la composición de una función logarítmica con una racional. El logaritmo natural solo está definido para argumentos estrictamente positivos, y la racional exige que su denominador no sea cero.',
   'Planteé la inecuación (x + 2)/(5 − x) &gt; 0. No multipliqué en cruz <span class="wrong" data-s="one">ya que</span> porque el signo de 5 − x cambia; en su lugar usé los puntos críticos −2 y 5 y una tabla de signos.',
   'El cociente es positivo solo en (−2, 5). Los extremos se excluyen: en −2 el argumento vale 0 y en 5 el denominador se anula.',
 ]),
])

RED = False
# ================= 6 (resultado erróneo a propósito) =================
add([

 ex(6, f'{LIM("x→−2")} {F(f"3x{s3} + 4x{s2} − 5x + 2", SQ(f"x{s2} + 5") + " + 3")}'),
 paso('Propiedades que voy a usar'),
 ln('(P1) lím [f/g] = lím f / lím g &nbsp;si lím g ≠ 0', 'sm ind2'),
 ln('(P2) lím [f ± g] = lím f ± lím g', 'sm ind2'),
 ln('(P3) lím [c · f] = c · lím f', 'sm ind2'),
 ln('(P4) lím x<sup>n</sup> = a<sup>n</sup> &nbsp;(potencia) &nbsp;y&nbsp; lím c = c', 'sm ind2'),
 ln(f'(P5) lím {SQ("g(x)")} = {SQ("lím g(x)")} &nbsp;si lím g(x) ≥ 0', 'sm ind2'),
 paso('Numerador — (P2), (P3) y (P4)'),
 ln(f'{LIM("x→−2")} (3x{s3} + 4x{s2} − 5x + 2) = 3·{LIM("x→−2")}x{s3} + 4·{LIM("x→−2")}x{s2} − 5·{LIM("x→−2")}x + {LIM("x→−2")}2', 'ind2'),
 ln(f'= 3(−2){s3} + 4(−2){s2} − 5(−2) + 2', 'ind2'),
 side(f'(−2){s3} = 8', [ln('✗ exponente impar → queda negativo', 'xs r'), ln(f'(−2){s3} = (−2)(−2)(−2) = −8 ⟹ 3(−8) = −24')], 'two', 'ind3'),
 side(f'4(−2){s2} = −16', [ln('✗ exponente par → positivo', 'xs r'), ln(f'4(−2){s2} = 4(4) = 16')], 'one', 'ind3'),
 ln('−5(−2) = −10', 'ind3'),
 ln('= −24 + 16 − 10 + 2 = −16', 'ind3'),
 paso('Denominador — (P2) y (P5)'),
 ln(f'{LIM("x→−2")} ({SQ(f"x{s2} + 5")} + 3) = {SQ(f"{LIM("x→−2")}(x{s2} + 5)")} + 3 = {SQ(f"(−2){s2} + 5")} + 3', 'ind2'),
 side(f'= {SQ("−4 + 5")} + 3 = 1 + 3 = 4', [ln(f'✗ (−2){s2} = +4', 'xs r'), ln(f'= {SQ("4 + 5")} + 3 = {SQ("9")} + 3 = 3 + 3 = 6')], 'two', 'ind3'),
 side(f'{SQ("9")} = ±3', [ln('✗ la raíz principal es solo +3', 'xs r')], 'one', 'ind3'),
 nota('9 ≥ 0 → vale (P5) ✓ &nbsp;&nbsp; 6 ≠ 0 → vale (P1) ✓', 'g', 'sm', 'ind3'),
 paso('Resultado — (P1)'),
 side(f'= {F("−16", "6")} = −{F("8", "6")}', [ln(f'= {F("−16", "6")} = {F("−8", "3")}'), ln('✗ simplifiqué solo arriba', 'xs r')], 'zig', 'ind2'),
 side(f'= −2,6', [ln('✗ mejor dejarlo en fracción', 'xs r')], 'one', 'ind3'),
 ln(f'∴ &nbsp;{LIM("x→−2")} {F(f"3x{s3} + 4x{s2} − 5x + 2", SQ(f"x{s2} + 5") + " + 3")} = {BOX("−" + F("8", "3"))}', 'lg ind'),
 *SUST([
   'No hay <span class="wrong" data-s="blot">indetermi</span> indeterminación: el denominador en x = −2 vale 6 ≠ 0, así que el límite se calcula por evaluación directa usando las propiedades de los límites.',
   'En el numerador separé la suma con (P2), saqué las constantes con (P3) y evalué cada potencia con (P4). En el denominador metí el límite dentro de la raíz con (P5), que se puede porque el radicando es positivo.',
   'Finalmente, con (P1), el límite del cociente es el cociente de los límites del numerador y del denominador.',
 ]),
])

# ================= 7 (resultado erróneo a propósito) =================
add([

 ex(7, f'{LIM("x→3")} {F(f"2x{s2} − 5x − 3", f"x{s3} − 27")}'),
 paso('Paso 1 — Sustitución directa'),
 ln(f'numerador: 2(3){s2} − 5(3) − 3 = 18 − 15 − 3 = 0', 'ind2'),
 side(f'2(3){s2} = 36', [ln('✗ primero la potencia: 3² = 9 → 2·9 = 18', 'xs r')], 'one', 'ind3'),
 ln(f'denominador: 3{s3} − 27 = 27 − 27 = 0', 'ind2'),
 ln(f'⟹ {F("0", "0")} &nbsp;→ indeterminación, hay que factorizar', 'ind2'),
 nota('si los dos dan 0 en x = 3 → (x − 3) es factor de ambos (teorema del factor)', 'p', 'xs'),
 paso('Paso 2 — Numerador (trinomio ax² + bx + c)'),
 ln('a · c = 2(−3) = −6 &nbsp;&nbsp; <span class="sm p">m · n = −6 , m + n = −5</span>', 'ind2'),
 side('−3 y 2', [ln('✗ suma −1', 'xs r'), ln(f'{HL("−6 y 1")} ✓ &nbsp;(−6)(1) = −6 , −6 + 1 = −5')], 'one'),
 ln(f'2x{s2} − 5x − 3 = 2x{s2} − 6x + x − 3', 'ind2'),
 side('= 2x(x − 3) − 1(x − 3)', [ln('✗ +x − 3 = +1(x − 3)', 'xs r'), ln('= 2x(x − 3) + 1(x − 3) = (x − 3)(2x + 1)')], 'two'),
 nota('chequeo: (x − 3)(2x + 1) = 2x² + x − 6x − 3 = 2x² − 5x − 3 ✓', 'b', 'xs'),
 paso('Paso 3 — Denominador (diferencia de cubos)'),
 side(f'x{s3} − 27 = (x − 3){s3}', [ln(f'✗ (x − 3){s3} tiene más términos', 'xs r'), ln(f'x{s3} − 27 = x{s3} − 3{s3} = (x − 3)(x{s2} − 3x + 9)')], 'two'),
 paso('Paso 4 — Simplificar y evaluar'),
 ln(f'{LIM("x→3")} {F(CN("(x − 3)") + "(2x + 1)", CN("(x − 3)") + f"(x{s2} − 3x + 9)")} = {LIM("x→3")} {F("2x + 1", f"x{s2} − 3x + 9")}', 'ind2'),
 nota('puedo cancelar porque x → 3 pero x ≠ 3', 'p', 'xs', 'ind3'),
 side(f'= {F("6", "9 − 9 + 9")}', [ln('✗ 2(3) + 1 = 7', 'xs r'), ln(f'= {F("2(3) + 1", "3² − 3(3) + 9")} = {F("7", "9 − 9 + 9")} = {F("7", "9")}')], 'one', 'ind2'),
 ln(f'∴ &nbsp;{BOX(F("7", "9"))}', 'lg ind'),
 *SUST([
   'Al sustituir x = 3 se obtiene 0/0, que es una indeterminación; eso indica (por el <span class="wrong" data-s="one">teorma</span> teorema del factor) que (x − 3) es factor común del numerador y del denominador.',
   'Factoricé el numerador como trinomio ax² + bx + c con el método ac y el denominador como diferencia de cubos x³ − 3³.',
   'Simplifiqué el factor (x − 3), que es válido porque en el límite x se acerca a 3 sin ser 3, y luego evalué por sustitución directa.',
 ]),
])

# ================= 8 =================
add([

 ex(8, f'{LIM("x→4")} {F(SQ("2x + 1") + " − 3", f"x{s2} − 16")}'),
 paso('Paso 1 — Sustitución'),
 ln(f'{F(SQ("2(4) + 1") + " − 3", "4² − 16")} = {F(SQ("9") + " − 3", "16 − 16")} = {F("0", "0")} &nbsp; → indeterminado', 'ind2'),
 paso('Paso 2 — Racionalizar (conjugado del numerador)'),
 nota('conjugado de √(2x + 1) − 3 → √(2x + 1) + 3 &nbsp;·&nbsp; (a − b)(a + b) = a² − b²', 'p', 'xs'),
 ln(f'{F(SQ("2x + 1") + " − 3", f"x{s2} − 16")} · {F(SQ("2x + 1") + " + 3", SQ("2x + 1") + " + 3")} = {F(f"({SQ("2x + 1")}){s2} − 3{s2}", f"(x{s2} − 16)({SQ("2x + 1")} + 3)")}', 'ind2'),
 side(f'({SQ("2x + 1")}){s2} = 4x{s2} + 1', [ln('✗ la raíz y el cuadrado se cancelan', 'xs r'), ln(f'({SQ("2x + 1")}){s2} = 2x + 1')], 'x'),
 side('2x + 1 − 3 = 2x − 2', [ln(f'✗ 3{s2} = 9', 'xs r'), ln(f'numerador: 2x + 1 − 9 = 2x − 8 = {HL("2(x − 4)")}')], 'two'),
 paso('Paso 3 — Factorizar el denominador'),
 side(f'x{s2} − 16 = (x − 4){s2}', [ln('✗ es diferencia de cuadrados', 'xs r'), ln(f'x{s2} − 16 = x{s2} − 4{s2} = (x − 4)(x + 4)')], 'x'),
 paso('Paso 4 — Simplificar'),
 ln(f'{LIM("x→4")} {F("2" + CN("(x − 4)"), CN("(x − 4)") + "(x + 4)(" + SQ("2x + 1") + " + 3)")} = {LIM("x→4")} {F("2", "(x + 4)(" + SQ("2x + 1") + " + 3)")}', 'ind2'),
 paso('Paso 5 — Evaluar'),
 ln(f'= {F("2", "(4 + 4)(" + SQ("9") + " + 3)")} = {F("2", "8 · 6")} = {F("2", "48")}', 'ind2'),
 side(f'= {F("1", "12")}', [ln(f'= {F("1", "24")} &nbsp;<span class="xs r">✗ 48 / 2 = 24</span>')], 'one', 'ind3'),
 ln(f'∴ &nbsp;{BOX(F("1", "24"))} &nbsp;<span class="sm p">≈ 0,0417</span>', 'lg ind'),
 paso('Comprobación numérica'),
 table([['x', '3,99', '3,999', '4,001', '4,01'], ['f(x)', '0,04174', '0,04167', '0,04166', '0,04159']]),
 nota('se acerca a 0,0417 = 1/24 por los dos lados ✓', 'g', 'sm'),
 *SUST([
   'La sustitución directa da 0/0. Como el numerador tiene una raíz restada, multipliqué numerador y denominador por su <span class="wrong" data-s="one">conjugdo</span> conjugado para usar la diferencia de cuadrados y eliminar el radical de arriba.',
   'Así el numerador queda 2x − 8 = 2(x − 4), y el denominador x² − 16 se factoriza como diferencia de cuadrados (x − 4)(x + 4). El factor (x − 4) se cancela porque x ≠ 4.',
   'Al final evalué directamente y verifiqué con una tabla de valores cerca de 4.',
 ]),
])

# ================= 9 =================
RED = True
add([

 ex(9, 'Función a trozos h(x)'),
 ln(f'h(x) = <span class="brace"><span>{F(f"x{s2} − 4", "x − 2")} &nbsp; si x &lt; 2</span><span>5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; si x = 2</span><span>3x − 2 &nbsp;&nbsp; si x &gt; 2</span></span>', 'ind'),
 paso('Límite por la izquierda (x → 2⁻) → uso el 1er tramo'),
 side(f'{LIM("x→2⁻")} h(x) = h(2) = 5', [ln('✗ para x &lt; 2 NO se usa h(2)', 'xs r')], 'two'),
 ln(f'{LIM("x→2⁻")} {F(f"x{s2} − 4", "x − 2")} = {F("4 − 4", "2 − 2")} = {F("0", "0")} → factorizo (dif. de cuadrados)', 'ind2'),
 side(f'{F(f"x{s2} − 4", "x − 2")} = x − 2', [ln('✗ se cancela (x − 2), queda (x + 2)', 'xs r')], 'zig'),
 ln(f'= {LIM("x→2⁻")} {F(CN("(x − 2)") + "(x + 2)", CN("(x − 2)"))} = {LIM("x→2⁻")} (x + 2) = 2 + 2 = {HL("4")}', 'ind2'),
 table([['x', '1,9', '1,99', '1,999'], ['h(x)', '3,9', '3,99', '3,999']]),
 paso('Límite por la derecha (x → 2⁺) → uso 3x − 2'),
 side('= 3(2 − 2) = 0', [ln('✗ el 3 multiplica solo a x', 'xs r'), ln(f'{LIM("x→2⁺")} (3x − 2) = 3(2) − 2 = 6 − 2 = {HL("4")}')], 'two'),
 table([['x', '2,1', '2,01', '2,001'], ['h(x)', '4,3', '4,03', '4,003']]),
 paso('Conclusión'),
 ln(f'{LIM("x→2⁻")} h(x) = {LIM("x→2⁺")} h(x) = 4', 'ind2'),
 side('como h(2) = 5 ≠ 4 , el límite no existe', [ln('✗ el límite no depende del valor h(2)', 'xs r')], 'two'),
 ln(f'⟹ {BOX(f"{LIM("x→2")} h(x) = 4 &nbsp;sí existe")}', 'lg ind'),
 paso('Extra — ¿es continua en x = 2?'),
 ln('1) h(2) = 5 existe ✓ &nbsp;&nbsp; 2) lím h(x) = 4 existe ✓', 'sm ind2'),
 ln('3) lím h(x) = h(2) ? &nbsp; 4 ≠ 5 ✗', 'sm ind2'),
 nota('⟹ no es continua: discontinuidad evitable (hay un "hueco" en (2, 4) y un punto suelto en (2, 5))', 'p', 'xs'),
 *SUST([
   'Un límite bilateral existe si y solo si los dos límites laterales existen y son iguales.',
   'Por la <span class="wrong" data-s="blot">derecha</span> izquierda usé el tramo (x² − 4)/(x − 2), que daba 0/0, así que lo factoricé como diferencia de cuadrados y simplifiqué. Por la derecha usé 3x − 2, que es un polinomio y se evalúa directo.',
   'Ambos laterales valen 4, por eso el límite existe y vale 4. El valor h(2) = 5 no interviene en el límite, solo en la continuidad.',
 ]),
])

RED = False
# ================= 10 =================
add([

 ex(10, 'Hallar k para que exista el límite en x = 1'),
 ln(f'f(x) = <span class="brace"><span>kx{s2} + 3x − 1 &nbsp;&nbsp;&nbsp;&nbsp; si x ≤ 1</span><span>{F(f"x{s2} − 1", "x − 1")} + 2k &nbsp;&nbsp; si x &gt; 1</span></span>', 'ind'),
 nota('condición: el límite existe ⇔ lím por la izquierda = lím por la derecha', 'b', 'sm'),
 paso('Límite por la izquierda (x → 1⁻) → 1er tramo'),
 ln(f'{LIM("x→1⁻")} (kx{s2} + 3x − 1) = k(1){s2} + 3(1) − 1', 'ind2'),
 side('= k + 3 + 1 = k + 4', [ln('✗ es −1', 'xs r'), ln(f'= k + 3 − 1 = {HL("k + 2")}')], 'two', 'ind3'),
 paso('Límite por la derecha (x → 1⁺) → 2º tramo'),
 ln(f'{LIM("x→1⁺")} ( {F(f"x{s2} − 1", "x − 1")} + 2k ) &nbsp; <span class="sm p">sustituyo: (1 − 1)/(1 − 1) = 0/0</span>', 'ind2'),
 side('0/0 = 0 ⟹ lím = 2k', [ln('✗ 0/0 es indeterminado, hay que factorizar', 'xs r')], 'x', 'ind3'),
 side(f'{F(f"x{s2} − 1", "x − 1")} = x − 1', [ln('✗ (x − 1)(x + 1) / (x − 1) = x + 1', 'xs r')], 'one', 'ind3'),
 ln(f'{F(f"x{s2} − 1", "x − 1")} = {F(CN("(x − 1)") + "(x + 1)", CN("(x − 1)"))} = x + 1 → 1 + 1 = 2', 'ind3'),
 ln(f'⟹ {LIM("x→1⁺")} f(x) = {HL("2 + 2k")}', 'ind3'),
 paso('Igualar los dos límites laterales'),
 ln('k + 2 = 2 + 2k', 'ind2 lg'),
 side('k − 2k = 2 + 2 ⟹ −k = 4 ⟹ k = −4', [ln('✗ el 2 de la izquierda pasa restando', 'xs r'), ln('k − 2k = 2 − 2')], 'two'),
 ln('−k = 0 &nbsp; ⟹ &nbsp; k = 0', 'ind3'),
 ln(f'⟹ {BOX("k = 0", "g")}', 'xl ind'),
 paso('Verificación'),
 ln('con k = 0 : &nbsp; f(x) = 3x − 1 (x ≤ 1) &nbsp;y&nbsp; (x² − 1)/(x − 1) (x &gt; 1)', 'sm ind2'),
 ln('izquierda: 0 + 2 = 2 &nbsp;&nbsp; derecha: 2 + 2(0) = 2 ✓', 'ind2 b'),
 table([['x', '0,99', '0,999', '1', '1,001', '1,01'], ['f(x)', '1,97', '1,997', '2', '2,001', '2,01']]),
 ln(f'⟹ {LIM("x→1")} f(x) = 2 &nbsp;existe ✓', 'ind2 b'),
 *SUST([
   'Para que el límite bilateral exista los límites laterales deben ser iguales. El de la izquierda se calcula con el polinomio kx² + 3x − 1 (evaluación directa) y da k + 2.',
   'El de la derecha daba 0/0 en la fracción; al factorizar x² − 1 como diferencia de cuadrados y cancelar (x − 1) queda x + 1 → 2, así que el límite es 2 + 2k.',
   'Igualando k + 2 = 2 + 2k se obtiene k = 0, y con <span class="wrong" data-s="one">este</span> ese valor ambos laterales valen 2, lo que confirma el resultado.',
 ]),
])

html = ['<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Parcial 2</title>',
        '<link rel="stylesheet" href="hand2.css"><style>.ln{margin-top:6px;margin-bottom:6px} .box:has(.lim){padding-bottom:.45em} .pasos{margin-top:12px!important} .sust .ln{margin:2px 0}</style>',
        '<script src="rough.js"></script><script src="hand2.js"></script></head><body class="chars"><div class="page cover"><svg class="under"></svg><div class="content"></div><div class="spine"></div><svg class="over"></svg></div><div id="flow">']
html += B
html.append('</div></body></html>')
out = '\n'.join(html).replace('⁻', '<sup>−</sup>').replace('⁺', '<sup>+</sup>')
open(os.path.join(D, 'notes4.html'), 'w').write(out)
print('ok', len(B))
