from sympy import *

x,y,z,nu =symbols('x y z nu')
init_printing(use_unicode=True)
Eq(x,y)
print(solve(Eq(x**2,1),x) )

