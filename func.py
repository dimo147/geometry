import math as m
from sympy.solvers import solve
from sympy import Symbol
from sympy import Float

#degree
def get_info(degree):

    DEGREE = degree
    RADIAN = m.radians(DEGREE)

    COS = round(m.cos(RADIAN), 2)
    SIN = round(m.sin(RADIAN), 2)

    try:
        tan = round(SIN/COS, 2)
    except:
        tan = "Undefined"

    try:
        cot = round(COS/SIN, 2)
    except:
        cot = "Undefined"

    dataList = [SIN, COS , tan, cot]

    return dataList

def cos_to_angle(cos):
    angle = round(m.degrees(m.acos(cos)), 3)
    return angle

# triangle
def area(a, b, c):
    sp = (a+b+c) / 2
    return m.sqrt(sp*(sp-a)*(sp-b)*(sp-c))

def circumradius(a, ang_A):
    return (a / m.sin(m.radians(ang_A)))/2

def inradius(area, sp):
    return area / sp

def height(area, a):
    return area / (a/2)

def median(a, b, c):
    med = m.sqrt(((2 * b**2) + (2 * c**2) - a**2) / 4)
    return med

def bisector(a, b, c):
    x = Symbol("x")
    n = solve((a-x)*b - c*x, x)
    CD = Float(n[0])
    BD = a - CD
    bstr = m.sqrt(c * b - BD * CD)
    return bstr


if __name__ == "__main__":
    DEGREE = int(input("Degree: "))
    headers = [f"Sine({DEGREE}\u00b0)", f"Cosine({DEGREE}\u00b0)", f"Tangent({DEGREE}\u00b0)" , f"Cotangent({DEGREE}\u00b0)"]
    dataList = get_info(DEGREE)
    i = 0
    while i < len(headers):
        print("------")
        print(headers[i] + ": " + str(dataList[i]))
        i += 1
