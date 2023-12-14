def tri(tab):
# i est le premier indice de la zone non tri´ee, j le dernier indice.
# Au d´ebut, la zone non tri´ee est le tableau entier.
    i= tab[0]
    j= tab[-1]
    while i != j :
        if tab[i]== 0:
            i= tab[0]
        else :
            valeur = tab[j]
            tab[j] = tab[-1]
            ...
            j= ...
        ...

print(tri([0,1,0,1,0,1,0,1,0]))