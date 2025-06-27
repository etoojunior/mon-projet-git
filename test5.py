A = int(input("Veuillez saisir la valeur de A : "))
B = int(input("Veuillez saisir la valeur de B : "))

#première methode
#C = A
#A = B
#B = C

#deuxieme methode unique a python
A,B = B,A
print("La nouvelle valeur de A est : ", A)
print("La nouvelle valeur de B est : ", B)