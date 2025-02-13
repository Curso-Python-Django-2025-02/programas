contador = 0

def hanoi(n, origen, destino, auxiliar):
    global contador
    # Mover n-1 discos de origen a auxiliar
    if n>1:
        hanoi(n-1, origen, auxiliar, destino)
    # Mover n-ésimo disco de origen a destino
    contador += 1
    print("Mover disco de tamaño ", n, "de", origen, "a", destino)
    # Mover n-1 discos de auxiliar a destino
    if n>1:
        hanoi(n-1, auxiliar, destino, origen)



hanoi(8, 'A', 'B', 'C')
print("Movimientos:", contador)
