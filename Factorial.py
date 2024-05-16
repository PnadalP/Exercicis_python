nombre = int(input("Introdueix un nombre per treure  el factorial: "))
i = 1
factorial = 1
while (i < nombre + 1 ):
    factorial = factorial * i
    i = i + 1
print(factorial)
