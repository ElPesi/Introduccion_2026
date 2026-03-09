def suma_matrices(A, B):
    resultado = []

    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)

    return resultado

print(suma_matrices([[1,2,5],[2,6,2],[6,3,1]], [[1,2,5],[2,6,2],[6,3,1]]))