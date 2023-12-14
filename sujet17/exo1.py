def indice_du_min(tab):
    min = tab[0]
    indice_min = 0
    for indice, valeur in enumerate(tab):
        if valeur < min:
            min = valeur
            indice_min = indice
    return indice_min


print(indice_du_min([5]))
print(indice_du_min([2, 4, 1]))
print(indice_du_min([5, 3, 2, 2, 4]))
