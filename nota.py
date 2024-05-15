nota = int(input("Introdueix la nota: "))
if nota < 0:
    print("Nota no vàlida")
elif nota < 5:
    print("Suspens")
elif nota == 5:
    print("Aprovat")
elif nota == 6:
    print("Bé")
elif nota <= 8:
    print("Notable")
elif nota <= 10:
    print("Excel·lent")
else:
    print("Nota no vàlida")