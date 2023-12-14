def recherche(elt, tab):
    for indice, valeur in enumerate(tab):
        if valeur == elt:
            return indice
    return -1


print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))
