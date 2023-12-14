def RechercheMinMax(tab):
    dico = {}
    mini = tab[0]
    maxi = 0
    for valeur in tab:
        if valeur < mini:
            mini = valeur
        if valeur > maxi:
            maxi = valeur

    dico["min"] = mini
    dico["max"] = maxi

    return dico


print(RechercheMinMax([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
