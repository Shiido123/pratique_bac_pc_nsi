def tri(tab):
    # i est le premier indice de la zone non tri´ee, j le dernier indice.
    # Au d´ebut, la zone non tri´ee est le tableau entier.
    i = 0
    j = len(tab)-1
    while i != j:
        if tab[i] == 0:
            i += 1
        else:
            tab[i], tab[j] = tab[j], tab[i]
            j -= 1
    return tab


print(tri([0, 1, 0, 1, 0, 1, 0, 1, 0]))
