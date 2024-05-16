import random
aleatori = random.randint(1,100)
for i in range(1,10):
    numero = int(input("Introdueix un número entre 1 i 100: "))
    if (numero == aleatori):
        print("Has encertat!")
        break
    elif (numero < aleatori):
        print("Has fallat, el número és més gran")
    elif (numero > aleatori):
        print("Has fallat, el número és més petit")
print("El número era", aleatori)