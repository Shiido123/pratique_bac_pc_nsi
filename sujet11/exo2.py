def tri_bulles(T):
    n = len(T)
    for i in range(0, n, -1):
        for j in range(i):
            if T[j] > T[i]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


print(tri_bulles([0, 5, 4, 9, 8, 7]))
