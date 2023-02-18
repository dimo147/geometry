from sympy import *
import os

eq = input("Math Problem: ")
os.system('cls' if os.name == 'nt' else 'clear')
eq = eq.replace(" ", "")
eq = eq.split("=")

x = symbols('x')
expr = eval(f"Eq({eq[0]},{eq[1]})")

exec(f"pprint(Eq({eq[0]},{eq[1]}))")
print()
sol = solve(expr)
for i in sol:
    print("x: ", end='')
    pprint(i)

# c = Eq(Rational(1/2)-((2*x-1)/4),Rational(3/4))
# pprint(c)
# pprint(solve(c))