s = open('gen5.py').read()
def ins_after(anchor, new):
    global s
    assert s.count(anchor) == 1, anchor[:50]
    s = s.replace(anchor, anchor + new)
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:50]
    s = s.replace(a, b)

rep("""ln('<span class="tag" style="font-size:34px">PARCIAL 2</span>', '', 'text-align:center;margin-top:4px', fixed=True),""",
    """ln('<span class="tag" style="font-size:38px">PARCIAL</span>', '', 'text-align:center;margin-top:4px', fixed=True),""")
rep(""" ln('<span class="tag" style="font-size:18px">FACTORIZACIÓN, DOMINIO Y LÍMITES</span>', '', 'text-align:center;margin-top:-6px', fixed=True),\n""", "")
rep("<title>Parcial 2</title>", "<title>Parcial</title>")

# ex 4
ins_after(" paso('Restricción 2 — denominador ≠ 0'),\n",
 " side(f'x{s2} − 7x + 12 &gt; 0', [ln('✗ no es inecuación: abajo solo tiene que ser ≠ 0', 'xs r')], 'zig'),\n")
# ex 5
ins_after(" side('5 − x = 0 ⟹ x = −5', [ln('✗ paso la x: 5 = x', 'xs r'), ln('denominador: 5 − x = 0 ⟹ x = 5')], 'one'),\n",
 " side('en (5, +∞): 5 − x es +', [ln('✗ x = 6 → 5 − 6 = −1 → es negativo', 'xs r')], 'two'),\n"
 " side('(x + 2)(5 − x) &gt; 0 ⟹ x &gt; −2 y x &gt; 5', [ln('✗ no, mejor la tabla', 'xs r')], 'x'),\n")
# ex 6
rep(" ln('= −24 + 16 + 10 + 2 = 4', 'ind3'),\n",
 " side('−24 + 16 = 8', [ln('✗ −24 + 16 = −8', 'xs r'), ln('= −24 + 16 + 10 + 2 = −8 + 12 = 4')], 'zig', 'ind3'),\n")
# ex 7
ins_after(" ln(f'{LIM(\"x→3\")} {F(CN(\"(x − 3)\") + \"(2x + 1)\", CN(\"(x − 3)\") + f\"(x{s2} + 3x + 9)\")} = {LIM(\"x→3\")} {F(\"2x + 1\", f\"x{s2} + 3x + 9\")}', 'ind2'),\n",
 " side('3² + 3(3) + 9 = 9 + 9 + 9 = 18', [ln('✗ 9 + 9 + 9 = 27', 'xs r')], 'two', 'ind3'),\n"
 " side(f'cancelo los x: {F(\"2 + 1\", \"x + 3 + 9\")}', [ln('✗ solo se cancelan factores, no términos sueltos', 'xs r')], 'x', 'ind3'),\n")
# ex 8 — full wrong attempt + more slips
ins_after(" nota('conjugado de √(2x + 1) − 3 → √(2x + 1) + 3 &nbsp;·&nbsp; (a − b)(a + b) = a² − b²', 'p', 'xs'),\n",
 " ln('1er intento:', 'sm ind', fixed=True),\n"
 " *ATT([\n"
 "   ln(f'({SQ(\"2x + 1\")} − 3)({SQ(\"2x + 1\")} + 3) = 2x + 1 − 9 = 2x − 8', 'ind2'),\n"
 "   ln(f'{LIM(\"x→4\")} {F(\"2x − 8\", f\"x{s2} − 16\")} = {LIM(\"x→4\")} {F(\"2(x − 4)\", \"(x − 4)(x + 4)\")} = {F(\"2\", \"8\")} = {BOX(F(\"1\", \"4\"))}', 'ind2'),\n"
 " ], '✗ multipliqué el conjugado solo arriba!! también va en el denominador → lo vuelvo a hacer ↓'),\n")
ins_after(" ln(f'= {F(\"2\", \"(4 + 4)(\" + SQ(\"9\") + \" + 3)\")} = {F(\"2\", \"8 · 6\")} = {F(\"2\", \"48\")}', 'ind2'),\n",
 " side(f'{SQ(\"9\")} + 3 = 9 + 3 = 12', [ln('✗ √9 = 3 → 3 + 3 = 6', 'xs r')], 'two', 'ind3'),\n"
 " side('(4 + 4) = 16', [ln('✗ 4 + 4 = 8, no 4 · 4', 'xs r')], 'zig', 'ind3'),\n")
# ex 9
ins_after(" paso('Límite por la derecha (x → 2⁺) → uso 3x − 2'),\n",
 " side('= 3(2) − 2 = 5', [ln('✗ 6 − 2 = 4', 'xs r')], 'two'),\n")
# ex 10
ins_after(" ln(f'{LIM(\"x→1⁻\")} (kx{s2} + 3x − 1) = k(1){s2} + 3(1) − 1', 'ind2'),\n",
 " side(f'k(1){s2} = 2k', [ln('✗ 1² = 1 → k · 1 = k', 'xs r')], 'zig', 'ind3'),\n")
ins_after(" ln('k + 2 = 2 + 2k', 'ind2 lg'),\n",
 " side('k + 2k = 2 − 2 ⟹ 3k = 0', [ln('✗ al pasar 2k cambia de signo: k − 2k', 'xs r')], 'two'),\n")
s = s.replace("'notes5.html'", "'notes6.html'")
open('gen6.py', 'w').write(s)
