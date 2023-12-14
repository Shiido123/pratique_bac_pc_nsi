def maxi(tab):
    maxi = 0
    num = 0
    for indice, valeur in enumerate(tab):
        if valeur > maxi:
            maxi = valeur
            num = indice
    return (maxi, num)


print(maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
