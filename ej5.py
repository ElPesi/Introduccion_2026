def filtrar_menores(arr, valor):
    resultado = []
    for x in arr:
        if x < valor:
            resultado.append(x)
    return resultado

print(filtrar_menores([2,5,1,8], 3))
