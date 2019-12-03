def maximo(arreglo):
    max = arreglo[0]
    for i in arreglo:
        if i > max:
            max = i
    return max