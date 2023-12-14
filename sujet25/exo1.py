def recherche(tab):
    lst = []
    for valeur in range(1, len(tab)):
        print(lst[valeur-1])
        if lst[valeur-1] + 1 == valeur:
            lst.append((valeur-1, valeur))
    return lst


print(recherche([1, 4, 5, 3]))
print(recherche([7, 1, 2, 5, 3, 4]))
print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))
