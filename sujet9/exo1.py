def moyenne(tab):
    somme = 0
    coeff = 0
    for valeur in tab:
        somme += (valeur[0]*valeur[1])
        coeff += valeur[1]

    moyenne = somme/coeff
    return moyenne


print(moyenne([(15, 2), (9, 1), (12, 3)]))
