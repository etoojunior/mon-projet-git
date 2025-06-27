import math

R = float(input("Veuillez saisir le rayon de la sphère : "))

V = (4 * math.pi * (R**3))/3

print("Le volume de la sphère est : ", format(V, ".2f"))