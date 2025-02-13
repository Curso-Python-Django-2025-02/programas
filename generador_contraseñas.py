#
# Generador de contraseñas robustas
#
# Genera una contraseña de N caracteres aleatorios
#
import random
import string

N = int(input("¿Qué longitud de contraseña quieres? "))
caracteres = string.ascii_letters + string.digits + string.punctuation

secuencia = random.choices(caracteres, k=N)

print("Contraseña generada: ", ''.join(secuencia))
