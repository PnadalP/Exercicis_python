#Demanar sou brut
sou = int(input("Introdueix el sou brut: "))
#<20000 Descompte de 10%
if sou < 20000:
    print("El teu  sou amb descompte és: ", sou*0.9)
#>20000 <30000 Descompte de 20%
elif sou < 30000:
    print("El teu  sou amb descompte és: ", sou*0.8)
#>30000 <40000 Descompte de 25%
elif sou < 40000:
    print("El teu  sou amb descompte és: ", sou*0.75)
#>40000 <50000 Descompte de 30%
elif sou < 50000:
    print("El teu  sou amb descompte és: ", sou*0.7)
#>50000 Descompte de 45%
else:
    print("El teu  sou amb descompte és: ", sou*0.65)