def occurrence_lettres(phrase):
    dico = {}
    for lettre in phrase:
        if lettre in dico:
            dico[lettre] += 1
        else:
            dico[lettre] = 1
    return dico


print(occurrence_lettres("Hello world !"))
