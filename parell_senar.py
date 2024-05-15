nombre = int(input("Introdueix un nombre: "))
if nombre % 2 == 0:
    i=2
    print("El nombre és parell")
else:
    i=1
    print("El nombre és senar")
while (i <= nombre):
    print(i)
    i = i + 2