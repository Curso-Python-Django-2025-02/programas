# Valores iniciales: los dos primeros términos de la sucesión
a = 0
b = 1
# Repetimos estas operaciones para calcular el siguiente término
# y actualizar las variables.
while a < 1000:
    c = a + b
    print(a)
    a, b = b, c
