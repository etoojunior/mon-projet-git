R1 = float(input("Veuillez saisir la valuer de R1 : "))
R2 = float(input("Veuillez saisir la valuer de R2 : "))
R3 = float(input("Veuillez saisir la valuer de R3 : "))

#resistance en serie
Rser = R1 + R2 + R3

#resistance en paralele
Rpar =  (R1*R2*R3) / (R1*R2 + R1*R3 + R3*R2)

print("La valeur de la resistance en serie est : ", format(Rser, ".2f"))
print("La valeur de la resistance en parallèle est : ", format(Rpar, ".2f"))