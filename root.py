# Rational Root Theorem
# finding the root for polynomial equation p/q
# Sympy Library --> pip install sympy
from sympy import *


g = var('x')
p = Poly(12*x**3+8*x**2-3*x-2, gen=g)
print(roots(p))








