def occurrence_max(chaine):
    dico = {}
    maxi = 0
    chaine2 = ""
    for valeur in chaine:
        if valeur in dico:
            dico[valeur] += 1
        else:
            dico[valeur] = 1

    for cle, valeur_2 in dico.items():
        if valeur_2 > maxi:
            maxi = valeur_2
            chaine2 = cle
    return chaine2


ch = 'je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'
print(occurrence_max(ch))

print(occurrence_max('abababababab'))
