import os

print("options: ")
print("1) Triangle")
print("2) Circle")
print("3) Equation")
print("4) Exit")
print()

op = int(input("Enter: "))

os.system('cls' if os.name == 'nt' else 'clear')

if op == 1:
    exec(open("triangle.py").read())
elif op == 2:
    exec(open("circle.py").read())
elif op == 3:
    exec(open("eq_solver.py").read())
elif op == 4:
    exit()
else:
    print("invalid input")
