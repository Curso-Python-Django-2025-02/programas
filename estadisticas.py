
def media(*muestras):
    suma = 0
    for x in muestras:
        suma += x
    return suma / len(muestras)

def varianza(*muestras):
    muestras2 = map(lambda x: x**2, muestras)
    return media(*muestras2) - media(*muestras)**2


muestras = []
print("Introduzca las muestras (una por línea, vacío para terminar).")
while True:
    entrada = input("> ")
    if not entrada: break
    muestras.append(float(entrada))

print("Número de muestras introducidas: ", len(muestras))
print("Media: ", media(*muestras))
print("Varianza: ", varianza(*muestras))
    
