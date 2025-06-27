age = int(input("Veuillez entrez l'age de l'enfant : "))

if age >= 6 and age <=7:
    print("la categorie de l'enfant est POUSSIN")
elif age >= 8 and age <=9:
    print("la categorie de l'enfant est PUPILLE")
elif age >= 10 and age <= 11:
    print("la categorie de l'enfant est MINIME")
elif age >= 12 and age <= 16:
    print("la categorie de l'nefant est CADET")
else:
    print("La categorie n'existe pas")