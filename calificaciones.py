def calcular_nota_final(**notas):
    '''
    Calcula la nota final, con o sin recuperación.
    Debe indicarse el parámetro final= y/o recuperacion=.
    '''
    if not set(notas.keys()) <= {'final', 'recuperacion'}:
        raise KeyError("Claves inválidas: " + str(set(notas.keys()) - {'final', 'recuperacion'}))

    if not all(map(lambda x: 0<=x<=10, notas.values())):
        raise ValueError("Todas las notas deben estar entre 0 y 10")
    
    nota = 0
    if 'final' in notas:
        nota = notas['final']
    if 'recuperacion' in notas and notas['recuperacion'] > nota:
        nota = notas['recuperacion']
    return nota


notas = {}
while True:
    k=input("Calificación (final,recuperacion; vacío para terminar): ")
    if not k: break
    v=float(input("Nota obtenida: "))
    notas[k] = v
    
print("Nota resultante:", calcular_nota_final(**notas))
