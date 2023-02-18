import func

# raw data
AB = int(input("AB: "))
AC = int(input("AC: "))
BC = int(input("BC: "))

a = BC
b = AC
c = AB

cos_A = (b**2 + c**2 - a**2) / (2*b*c)
cos_B = (c**2 + a**2 - b**2) / (2*c*a)
cos_C = (a**2 + b**2 - c**2) / (2*a*b)

#calculation
perimeter = a + b+ c
semiperimeter = perimeter / 2

area = func.area(a, b, c)

ang_A = func.cos_to_angle(cos_A)
ang_B = func.cos_to_angle(cos_B)
ang_C = func.cos_to_angle(cos_C)

circumradius = func.circumradius(a, ang_A)
inradius = func.inradius(area, semiperimeter)

h_a = func.height(area, a)
h_b = func.height(area, b)
h_c = func.height(area, c)

m_a = func.median(a, b, c)
m_b = func.median(b, a, c)
m_c = func.median(c, a, b)

AD = func.bisector(a, b, c)
BD = func.bisector(b, a, c)
CD = func.bisector(c, a, b)


#printing
print()
print("            A ")
print("           / \ ")
print("          /   \ ")
print("         /     \ ")
print("        /       \ ")
print("       /         \ ")
print("      B --------- C ")
print()
print("Side a:", a)
print("Side b:", b)
print("Side c:", c)
print()
print("Angle A:", ang_A)
print("Angle B:", ang_B)
print("Angle C:", ang_C)
print()
print("Area:", area)
print("Perimeter:", perimeter)
print("Semiperimeter:", semiperimeter)
print()
print("Circumradius:", circumradius)
print("Inradius:", inradius)
print()
print("Height a:", h_a)
print("Height b:", h_b)
print("Height c:", h_c)
print()
print("Median a:", m_a)
print("Median b:", m_b)
print("Median c:", m_c)
print()
print("Bisector A(AD):", AD)
print("Bisector B(BD):", BD)
print("Bisector C(CD):", CD)
print()