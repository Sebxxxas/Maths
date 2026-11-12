# Generates notes2.html (taller 2: factorización, dominio y límites)
import os
D = os.path.dirname(os.path.abspath(__file__))

def F(n, d): return f'<span class="fr"><span>{n}</span><span>{d}</span></span>'
def LIM(u): return f'<span class="lim"><span>lím</span><span class="u">{u}</span></span>'
def SQ(x): return f'<span class="sq">{x}</span>'
def BOX(x, c='g'): return f'<span class="box {c}" data-c="{c}">{x}</span>'
def HL(x): return f'<span class="hl">{x}</span>'
def CN(x): return f'<span class="cn">{x}</span>'
def ln(x, cls='', style=''):
    st = f' style="{style}"' if style else ''
    return f'<span class="ln {cls}"{st}>{x}</span>'
def side(wrong, fixes, s='one', cls='ind2', c='r'):
    w = ''.join(ln(x) for x in (wrong if isinstance(wrong, list) else [wrong]))
    f = ''.join(fixes)
    return f'<div class="side {cls}"><div class="wrong" data-s="{s}" data-c="{c}">{w}</div><div class="fix">{f}</div></div>'
def WR(x, s='one', c='r'):  # inline crossed text
    return f'<span class="wrong" data-s="{s}" data-c="{c}">{x}</span>'
def ex(n, title, pts='[0,5 pts]'):
    return ln(f'<span class="huge" style="font-size:44px">{n}.</span> {title} <span class="pts">{pts}</span>', 'ex')
def paso(t): return ln(t, 'pasos ind')
def nota(t, c='p', size='sm', cls='ind2'): return ln(t, f'{size} {c} {cls}')
def wrapln(t, cls='sm ind2', w=660): return f'<span class="ln {cls}" style="white-space:normal;width:{w}px">{t}</span>'
def sketch(k, w, h, extra='', style=''): return f'<div class="sketch" data-k="{k}" {extra} style="width:{w}px;height:{h}px;{style}"></div>'
sup = lambda x: f'<sup>{x}</sup>'
s2, s3 = sup(2), sup(3)

pages = []

# ---------------- PAGE 1 ----------------
pages.append([
 ln(f'<span class="ul2" data-c="b">Taller: Factorización, Dominio y Límites</span>', 'h1', 'font-size:40px'),
 ln('Fecha: 12 / 11 / 26 &nbsp;&nbsp; Nombre: <span class="b ul" data-c="b">Sebastián Rodríguez</span>', 'sm k', 'margin-left:330px'),
 ex(1, f'Factorizar &nbsp;P(x) = 6x{s3} − 7x{s2} − 20x'),
 paso('Paso 1 — Factor común'),
 nota('todos los términos tienen x &nbsp;·&nbsp; MCD(6, 7, 20) = 1 → solo saco x', 'p', 'sm'),
 side(f'P(x) = 2x(3x{s2} − 7x − 10)', [ln('✗ 7 no se divide entre 2 !!', 'sm r'), ln(f'P(x) = x(6x{s2} − 7x − 20)', 'b')], 'two'),
 paso(f'Paso 2 — Trinomio ax{s2} + bx + c &nbsp;<span class="xs k">(método ac / aspa)</span>'),
 ln(f'6x{s2} − 7x − 20 &nbsp;→&nbsp; a = 6 , b = −7 , c = −20', 'ind2'),
 ln(f'a · c = 6 · (−20) = −120 &nbsp;&nbsp;<span class="sm p">busco m · n = −120 &nbsp;y&nbsp; m + n = −7</span>', 'ind2'),
 ln('pruebo parejas:', 'sm ind2'),
 ln(f'{WR("−12 y 10 → suma −2", "one")} &nbsp; {WR("−10 y 12 → suma 2", "one")} &nbsp; {WR("−20 y 6 → suma −14", "one", "k")}', 'ind3 sm'),
 side('15 y −8 → suma 7', [ln('✗ me da +7, necesito −7 → cambio signos', 'xs r'), ln(f'{HL("−15 y 8")} → (−15)(8) = −120 ✓', 'g'), ln('−15 + 8 = −7 ✓', 'g', 'margin-left:60px')], 'two', 'ind3'),
 ln(f'6x{s2} − 7x − 20 = 6x{s2} − 15x + 8x − 20', 'ind2'),
 ln(f'= (6x{s2} − 15x) + (8x − 20)', 'ind2', 'margin-left:150px'),
 side('= 3x(2x − 5) + 4(2x + 5)', [ln('✗ 4 · 5 = 20 pero el signo es −', 'xs r'), ln('= 3x(2x − 5) + 4(2x − 5)')], 'two', 'ind2" style="margin-left:150px'),
 ln('= (2x − 5)(3x + 4)', 'ind2', 'margin-left:150px'),
 ln(f'∴ &nbsp;{BOX("P(x) = x(3x + 4)(2x − 5)")}', 'lg ind'),
 ln(f'Comprobación: (3x + 4)(2x − 5) = 6x{s2} − 15x + 8x − 20 = 6x{s2} − 7x − 20 ✓', 'sm b ind2'),
 nota('casos usados: factor común monomio + trinomio de la forma ax² + bx + c', 'p', 'xs'),
])

# ---------------- PAGE 2 ----------------
pages.append([
 ex(2, f'Factorizar &nbsp;Q(x) = x{s3} + 3x{s2} − 4x − 12'),
 paso('Paso 1 — Agrupación (de 2 en 2)'),
 side(f'(x{s3} + 3x{s2}) − (4x − 12)', [ln('✗ al sacar el − cambia el signo del 12', 'xs r'), ln(f'Q(x) = (x{s3} + 3x{s2}) + (−4x − 12)'), ln(f'= (x{s3} + 3x{s2}) − (4x + 12)', '', 'margin-left:70px')], 'two'),
 paso('Paso 2 — Factor común en cada grupo'),
 ln(f'x{s3} + 3x{s2} = x{s2}(x + 3) &nbsp;&nbsp;&nbsp; 4x + 12 = 4(x + 3)', 'ind2'),
 side(f'= x{s2}(x + 3) − 4(x − 3)', [ln('✗ 12 / 4 = +3 → (x + 3)', 'xs r'), ln(f'= x{s2}(x + 3) − 4(x + 3)')], 'zig'),
 paso('Paso 3 — Factor común por agrupación: (x + 3)'),
 ln(f'= (x + 3)(x{s2} − 4)', 'ind2'),
 paso('Paso 4 — Diferencia de cuadrados'),
 nota('a² − b² = (a − b)(a + b)', 'b', 'sm'),
 side(f'x{s2} − 4 = (x − 2){s2}', [ln(f'✗ (x − 2){s2} = x{s2} − 4x + 4 ≠ x{s2} − 4', 'xs r'), ln(f'x{s2} − 4 = x{s2} − 2{s2} = (x − 2)(x + 2)')], 'x'),
 ln(f'∴ &nbsp;{BOX("Q(x) = (x + 3)(x − 2)(x + 2)")}', 'lg ind'),
 ln('Comprobación con x = 1 :', 'sm b ind2'),
 ln(f'Q(1) = 1 + 3 − 4 − 12 = −12 &nbsp;&nbsp;y&nbsp;&nbsp; (1 + 3)(1 − 2)(1 + 2) = (4)(−1)(3) = −12 ✓', 'sm b ind3'),

 ex(3, f'Factorizar &nbsp;R(x) = 27x{s3} − 8(x − 1){s3}'),
 paso('Paso 1 — Escribir como cubos'),
 ln(f'27x{s3} = (3x){s3}', 'ind2'),
 side(f'8(x − 1){s3} = (8x − 8){s3}', [ln('✗ la raíz cúbica de 8 es 2, no 8', 'xs r'), ln(f'8(x − 1){s3} = [2(x − 1)]{s3} = (2x − 2){s3}')], 'two'),
 ln(f'⟹ a = 3x , &nbsp; b = 2x − 2 &nbsp;&nbsp;<span class="sm p">(diferencia de cubos)</span>', 'ind2'),
 side(f'a{s3} − b{s3} = (a − b)(a{s2} − ab + b{s2})', [ln('✗ esa es la de suma de cubos', 'xs r'), ln(f'a{s3} − b{s3} = (a − b)(a{s2} + ab + b{s2})', 'b')], 'zig'),
])

# ---------------- PAGE 3 ----------------
pages.append([
 paso('Paso 2 — Primer factor (a − b)'),
 side('3x − 2x − 2 = x − 2', [ln('✗ −(2x − 2) = −2x + 2', 'xs r'), ln(f'a − b = 3x − (2x − 2) = 3x − 2x + 2 = {HL("x + 2")}')], 'two'),
 paso('Paso 3 — Segundo factor (a² + ab + b²)'),
 ln(f'a{s2} = (3x){s2} = 9x{s2}', 'ind2'),
 ln(f'ab = 3x(2x − 2) = 6x{s2} − 6x', 'ind2'),
 side(f'b{s2} = (2x − 2){s2} = 4x{s2} + 4', [ln('✗ falta el doble producto: 2(2x)(2) = 8x', 'xs r'), ln(f'b{s2} = (2x){s2} − 2(2x)(2) + 2{s2} = 4x{s2} − 8x + 4')], 'two'),
 ln(f'a{s2} + ab + b{s2} = 9x{s2} + 6x{s2} − 6x + 4x{s2} − 8x + 4', 'ind2'),
 side(f'= 19x{s2} − 2x + 4', [ln('✗ −6x − 8x = −14x', 'xs r'), ln(f'= {HL(f"19x{s2} − 14x + 4")}')], 'one', 'ind3'),
 nota(f'¿se factoriza más? Δ = (−14){s2} − 4(19)(4) = 196 − 304 = −108 &lt; 0 → no', 'p', 'xs', 'ind3'),
 ln(f'∴ &nbsp;{BOX(f"R(x) = (x + 2)(19x{s2} − 14x + 4)")}', 'lg ind'),
 ln(f'Comprobación x = 0 : R(0) = 0 − 8(−1){s3} = 8 &nbsp;y&nbsp; (2)(4) = 8 ✓', 'sm b ind2'),

 ex(4, f'f(x) = {F(SQ("2x − 6"), f"x{s2} − 7x + 12")}'),
 ln('<span class="lab">a)</span> Tipo de función', 'ind md bold'),
 side('Es una función racional', [ln('✗ tiene x dentro de una raíz', 'xs r'), ln(f'Es una función algebraica {HL("irracional fraccionaria")}', 'b')], 'two'),
 wrapln('→ es irracional porque la variable está dentro de un radical y fraccionaria porque es un cociente cuyo denominador tiene x.', 'sm ind2', 640),
 ln('<span class="lab">b)</span> Dominio natural', 'ind md bold'),
 paso('Restricción 1 — radicando ≥ 0 (raíz de índice par)'),
 ln('2x − 6 ≥ 0 ⟹ 2x ≥ 6 ⟹', 'ind2'),
 side('x ≥ −3', [ln('✗ 6/2 = +3', 'xs r'), ln(f'{HL("x ≥ 3")}')], 'one', 'ind2" style="margin-left:300px;margin-top:-38px'),
])

# ---------------- PAGE 4 ----------------
pages.append([
 paso('Restricción 2 — denominador ≠ 0'),
 ln(f'x{s2} − 7x + 12 ≠ 0 &nbsp; <span class="sm p">busco dos números: producto 12, suma −7</span>', 'ind2'),
 side('(x − 6)(x − 1)', [ln('✗ (−6)(−1) = 6, no 12', 'xs r'), ln('(x − 3)(x − 4) ≠ 0 ⟹ x ≠ 3 &nbsp;y&nbsp; x ≠ 4')], 'blot', c='k'),
 paso('Intersección de restricciones'),
 ln('x ≥ 3 &nbsp; y &nbsp; x ≠ 3 &nbsp; y &nbsp; x ≠ 4 &nbsp; ⟹ &nbsp; x &gt; 3 , x ≠ 4', 'ind2'),
 sketch('NL', 420, 60, 'data-min="1" data-max="7" data-pts="3:o,4:o" data-segs="3,4;4,inf"', 'margin-left:120px'),
 side('Dom f = [3 , 4) ∪ (4 , +∞)', [ln('✗ en x = 3 el denominador da 0 → se excluye', 'xs r')], 'two'),
 ln(f'∴ &nbsp;{BOX("Dom f = (3 , 4) ∪ (4 , +∞)")}', 'lg ind'),

 ex(5, f'g(x) = ln {F("x + 2", "5 − x")}'),
 paso('Componentes'),
 ln(f'• logarítmica: ln(u) solo existe si &nbsp;{HL("u &gt; 0")}', 'ind2'),
 ln(f'• racional: u = {F("x + 2", "5 − x")} → denominador ≠ 0 ⟹ x ≠ 5', 'ind2'),
 side(f'{F("x + 2", "5 − x")} ≥ 0', [ln('✗ ln(0) no existe → tiene que ser estrictamente &gt; 0', 'xs r'), ln(f'{F("x + 2", "5 − x")} &gt; 0')], 'two'),
 paso('Puntos críticos'),
 ln('x + 2 = 0 ⟹ x = −2', 'ind2'),
 side('5 − x = 0 ⟹ x = −5', [ln('✗ paso la x: 5 = x', 'xs r'), ln('5 − x = 0 ⟹ x = 5')], 'one'),
])

# ---------------- PAGE 5 ----------------
pages.append([
 paso('Tabla de signos'),
 '<table class="tb ind" style="font-size:22px;margin-left:60px"><tr><td></td><td>(−∞, −2)</td><td>(−2, 5)</td><td>(5, +∞)</td></tr>'
 '<tr><td>x + 2</td><td class="r">−</td><td class="g">+</td><td class="g">+</td></tr>'
 '<tr><td>5 − x</td><td class="g">+</td><td class="g">+</td><td class="r">−</td></tr>'
 '<tr><td class="bold">cociente</td><td class="r bold">−</td><td class="g bold">+</td><td class="r bold">−</td></tr></table>',
 nota('pruebo: x = 0 → 2/5 &gt; 0 ✓ &nbsp;&nbsp; x = 6 → 8/(−1) &lt; 0 ✗ &nbsp;&nbsp; x = −3 → −1/8 &lt; 0 ✗', 'p', 'xs'),
 side('Dom g = (−∞, −2) ∪ (5, +∞)', [ln('✗ tomé los intervalos negativos, necesito el +', 'xs r')], 'x'),
 sketch('NL', 420, 60, 'data-min="-4" data-max="7" data-pts="-2:o,5:o" data-segs="-2,5"', 'margin-left:120px'),
 ln(f'∴ &nbsp;{BOX("Dom g = (−2 , 5)")}', 'lg ind'),
 wrapln('−2 y 5 son abiertos: en −2 el argumento es 0 (ln 0 no existe) y en 5 el denominador es 0.', 'xs p ind2', 640),

 ex(6, f'{LIM("x→−2")} {F(f"3x{s3} + 4x{s2} − 5x + 2", SQ(f"x{s2} + 5") + " + 3")}'),
 paso('Propiedades que uso'),
 ln(f'(1) lím del cociente = cociente de los lím (si el lím del denominador ≠ 0)', 'sm ind2'),
 ln(f'(2) lím de un polinomio = sustitución directa (suma, constante, potencia)', 'sm ind2'),
 ln(f'(3) lím {SQ("g(x)")} = {SQ("lím g(x)")} &nbsp;(si lím g(x) ≥ 0)', 'sm ind2'),
 paso('Numerador'),
 ln(f'{LIM("x→−2")} (3x{s3} + 4x{s2} − 5x + 2) = 3(−2){s3} + 4(−2){s2} − 5(−2) + 2', 'ind2'),
 side(f'(−2){s3} = 8', [ln('✗ exponente impar → queda negativo', 'xs r'), ln(f'(−2){s3} = −8 ⟹ 3(−8) = −24')], 'two', 'ind3'),
 ln(f'4(−2){s2} = 4(4) = 16', 'ind3'),
 ln('−5(−2) = −10', 'ind3'),
 ln('= −24 + 16 − 10 + 2 = −16', 'ind3'),
])

# ---------------- PAGE 6 ----------------
pages.append([
 paso('Denominador'),
 ln(f'{LIM("x→−2")} ({SQ(f"x{s2} + 5")} + 3) = {SQ(f"(−2){s2} + 5")} + 3', 'ind2'),
 side(f'= {SQ("−4 + 5")} + 3 = 1 + 3 = 4', [ln(f'✗ (−2){s2} = +4', 'xs r'), ln(f'= {SQ("4 + 5")} + 3 = {SQ("9")} + 3 = 3 + 3 = 6')], 'two', 'ind3'),
 side(f'{SQ("9")} = ±3', [ln('✗ la raíz principal es solo +3', 'xs r')], 'one', 'ind3'),
 nota('6 ≠ 0 → puedo usar la propiedad del cociente ✓', 'g', 'sm', 'ind3'),
 paso('Resultado'),
 side(f'= {F("−16", "6")} = −{F("8", "6")}', [ln(f'= {F("−16", "6")} = {F("−8", "3")}'), ln('✗ simplifiqué solo arriba', 'xs r')], 'zig', 'ind2'),
 ln(f'∴ &nbsp;{LIM("x→−2")} {F(f"3x{s3} + 4x{s2} − 5x + 2", SQ(f"x{s2} + 5") + " + 3")} = {BOX("−" + F("8", "3"))}', 'lg ind'),

 ex(7, f'{LIM("x→3")} {F(f"2x{s2} − 5x − 3", f"x{s3} − 27")}'),
 paso('Paso 1 — Sustitución directa'),
 ln(f'{F(f"2(9) − 15 − 3", "27 − 27")} = {F("0", "0")} &nbsp;→ indeterminación, hay que factorizar', 'ind2'),
 paso('Paso 2 — Numerador (trinomio ax² + bx + c)'),
 ln('a · c = 2(−3) = −6 &nbsp;&nbsp; <span class="sm p">m · n = −6 , m + n = −5</span>', 'ind2'),
 side('−3 y 2', [ln('✗ suma −1', 'xs r'), ln(f'{HL("−6 y 1")} ✓')], 'one'),
 ln(f'2x{s2} − 6x + x − 3 = 2x(x − 3) + 1(x − 3) = (x − 3)(2x + 1)', 'ind2'),
 paso('Paso 3 — Denominador (diferencia de cubos)'),
 side(f'x{s3} − 27 = (x − 3){s3}', [ln(f'✗ (x − 3){s3} tiene más términos', 'xs r'), ln(f'x{s3} − 27 = x{s3} − 3{s3} = (x − 3)(x{s2} − 3x + 9)')], 'two'),
])

# ---------------- PAGE 7 ----------------
pages.append([
 paso('Paso 4 — Simplificar y evaluar'),
 ln(f'{LIM("x→3")} {F(CN("(x − 3)") + "(2x + 1)", CN("(x − 3)") + f"(x{s2} − 3x + 9)")} = {LIM("x→3")} {F("2x + 1", f"x{s2} − 3x + 9")}', 'ind2'),
 side(f'= {F("6", "9 − 9 + 9")}', [ln('✗ 2(3) + 1 = 7', 'xs r'), ln(f'= {F("2(3) + 1", "9 − 9 + 9")} = {F("7", "9")}')], 'one', 'ind2'),
 ln(f'∴ &nbsp;{BOX(F("7", "9"))}', 'lg ind'),

 ex(8, f'{LIM("x→4")} {F(SQ("2x + 1") + " − 3", f"x{s2} − 16")}'),
 paso('Paso 1 — Sustitución'),
 ln(f'{F(SQ("9") + " − 3", "16 − 16")} = {F("0", "0")} &nbsp; → indeterminado', 'ind2'),
 paso('Paso 2 — Racionalizar (conjugado del numerador)'),
 ln(f'{F(SQ("2x + 1") + " − 3", f"x{s2} − 16")} · {F(SQ("2x + 1") + " + 3", SQ("2x + 1") + " + 3")} = {F(f"({SQ("2x + 1")}){s2} − 3{s2}", f"(x{s2} − 16)({SQ("2x + 1")} + 3)")}', 'ind2'),
 side('2x + 1 − 3 = 2x − 2', [ln(f'✗ 3{s2} = 9', 'xs r'), ln(f'numerador: 2x + 1 − 9 = 2x − 8 = {HL("2(x − 4)")}')], 'two'),
 paso('Paso 3 — Factorizar el denominador'),
 side(f'x{s2} − 16 = (x − 4){s2}', [ln('✗ diferencia de cuadrados', 'xs r'), ln(f'x{s2} − 16 = (x − 4)(x + 4)')], 'x'),
 paso('Paso 4 — Simplificar'),
 ln(f'{LIM("x→4")} {F("2" + CN("(x − 4)"), CN("(x − 4)") + "(x + 4)(" + SQ("2x + 1") + " + 3)")} = {LIM("x→4")} {F("2", "(x + 4)(" + SQ("2x + 1") + " + 3)")}', 'ind2'),
 ln(f'= {F("2", "(8)(" + SQ("9") + " + 3)")} = {F("2", "8 · 6")} = {F("2", "48")}', 'ind2'),
])

# ---------------- PAGE 8 ----------------
pages.append([
 side(f'= {F("1", "12")}', [ln(f'= {F("1", "24")} &nbsp;<span class="xs r">✗ 48 / 2 = 24</span>')], 'one', 'ind3'),
 ln(f'∴ &nbsp;{BOX(F("1", "24"))}', 'lg ind'),
 ex(9, 'Función a trozos h(x)'),
 ln(f'h(x) = <span class="brace"><span>{F(f"x{s2} − 4", "x − 2")} &nbsp; si x &lt; 2</span><span>5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; si x = 2</span><span>3x − 2 &nbsp;&nbsp; si x &gt; 2</span></span>', 'ind'),
 paso('Límite por la izquierda (x → 2⁻) → uso el 1er tramo'),
 side(f'{LIM("x→2⁻")} h(x) = h(2) = 5', [ln('✗ para x &lt; 2 NO se usa h(2)', 'xs r')], 'two'),
 ln(f'{LIM("x→2⁻")} {F(f"x{s2} − 4", "x − 2")} = {F("4 − 4", "2 − 2")} = {F("0", "0")} → factorizo', 'ind2'),
 side(f'{F(f"x{s2} − 4", "x − 2")} = x − 2', [ln('✗ se cancela (x − 2), queda (x + 2)', 'xs r')], 'zig'),
 ln(f'= {LIM("x→2⁻")} {F(CN("(x − 2)") + "(x + 2)", CN("(x − 2)"))} = {LIM("x→2⁻")} (x + 2) = 2 + 2 = {HL("4")}', 'ind2'),
 paso('Límite por la derecha (x → 2⁺) → uso 3x − 2'),
 side('= 3(2 − 2) = 0', [ln('✗ el 3 multiplica solo a x', 'xs r'), ln(f'{LIM("x→2⁺")} (3x − 2) = 3(2) − 2 = 6 − 2 = {HL("4")}')], 'two'),
 paso('Conclusión'),
 ln(f'{LIM("x→2⁻")} h(x) = {LIM("x→2⁺")} h(x) = 4', 'ind2'),
 side('como h(2) = 5 ≠ 4 , el límite no existe', [ln('✗ el límite no depende del valor h(2)', 'xs r')], 'two'),
 ln(f'⟹ {BOX(f"{LIM("x→2")} h(x) = 4 &nbsp;sí existe")}', 'lg ind'),
 wrapln('Obs: h(2) = 5 ≠ 4 → el límite existe pero h no es continua en x = 2 (discontinuidad evitable).', 'xs p ind2', 640),
])

# ---------------- PAGE 9 ----------------
pages.append([
 ex(10, 'Hallar k para que exista el límite en x = 1'),
 ln(f'f(x) = <span class="brace"><span>kx{s2} + 3x − 1 &nbsp;&nbsp;&nbsp;&nbsp; si x ≤ 1</span><span>{F(f"x{s2} − 1", "x − 1")} + 2k &nbsp;&nbsp; si x &gt; 1</span></span>', 'ind'),
 paso('Límite por la izquierda (x → 1⁻)'),
 ln(f'{LIM("x→1⁻")} (kx{s2} + 3x − 1) = k(1){s2} + 3(1) − 1', 'ind2'),
 side('= k + 3 + 1 = k + 4', [ln('✗ es −1', 'xs r'), ln(f'= k + 3 − 1 = {HL("k + 2")}')], 'two', 'ind3'),
 paso('Límite por la derecha (x → 1⁺)'),
 ln(f'{LIM("x→1⁺")} ( {F(f"x{s2} − 1", "x − 1")} + 2k ) &nbsp; <span class="sm p">sustituyo: 0/0</span>', 'ind2'),
 side('0/0 = 0 ⟹ lím = 2k', [ln('✗ 0/0 es indeterminado, hay que factorizar', 'xs r')], 'x', 'ind3'),
 ln(f'{F(f"x{s2} − 1", "x − 1")} = {F(CN("(x − 1)") + "(x + 1)", CN("(x − 1)"))} = x + 1 → 1 + 1 = 2', 'ind3'),
 ln(f'⟹ {LIM("x→1⁺")} f(x) = {HL("2 + 2k")}', 'ind3'),
 paso('Igualar los dos límites laterales'),
 ln('k + 2 = 2 + 2k', 'ind2 lg'),
 side('k − 2k = 2 + 2 ⟹ −k = 4 ⟹ k = −4', [ln('✗ el 2 de la izquierda pasa restando', 'xs r'), ln('k − 2k = 2 − 2 ⟹ −k = 0')], 'two'),
 ln(f'⟹ {BOX("k = 0", "g")}', 'xl ind'),
 paso('Verificación'),
 ln('izquierda: 0 + 2 = 2 &nbsp;&nbsp; derecha: 2 + 2(0) = 2 ✓', 'ind2 b'),
 ln(f'⟹ {LIM("x→1")} f(x) = 2 existe ✓', 'ind2 b'),
 ln('¡Listo! ✓', 'lg g', 'margin-top:30px;margin-left:440px;transform:rotate(-4deg)'),
])

html = ['<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Taller de Factorización y Límites</title>',
        '<link rel="stylesheet" href="hand.css"><style>body{font-size:25.5px} .ln{margin-top:6px;margin-bottom:6px} .box:has(.lim){padding-bottom:.45em} .pasos{margin-top:12px!important}</style><script src="rough.js"></script><script src="hand.js"></script></head><body>']
for pg in pages:
    html.append('<div class="page"><svg class="under"></svg><div class="content">' + '\n'.join(pg) + '</div><svg class="over"></svg></div>')
html.append('</body></html>')
out='\n'.join(html).replace('⁻','<sup>−</sup>').replace('⁺','<sup>+</sup>'); open(os.path.join(D, 'notes2.html'), 'w').write(out)
print('ok', len(pages))
