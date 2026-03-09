def multiplicar_matrices(A, B):
    resultado = []

    for i in range(len(A)):
        fila = []
        for j in range(len(B[0])):
            suma = 0
            for k in range(len(B)):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)

    return resultado

print(multiplicar_matrices([[1,2,5],[2,6,2],[6,3,1]], [[1,2,5],[2,6,2],[6,3,1]]))