edad = int(input("Indica tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
    print("Bienvenido al club.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres menor de edad.")

# Esta se ejecuta incondicionalmente
print("Gracias por venir.")
