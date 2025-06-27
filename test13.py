N1 = float(input("Veuillez saisir N1 : "))
N2 = float(input("Veuillez saisir N2 : "))
N3 = float(input("Veuillez saisir N3 : "))

moyenne = (N1+N2+N3)/3

print("la moyenne de l'etudiant est ", format(moyenne, ".2f"))

if moyenne < 10:
    print("La mension de l'etudiant est : Insuffisant")
elif moyenne >= 10 and moyenne < 12:
    print("La mension de l'etudiant est : Passable")
elif moyenne >= 12 and moyenne < 14:
    print("la mension de l'etudiant est : Assez bien")
elif moyenne >=14 and moyenne < 16:
    print("La mension de l'etudiant est : Bien")
else:
    print("La moyenne de l'etudiant est : Très bien")