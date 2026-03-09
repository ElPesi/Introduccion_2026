def contar_valor(arr, valor):
    count = 0
    for x in arr:
        if x == valor:
            count += 1
    return count

print(contar_valor([2,4,5], 2))