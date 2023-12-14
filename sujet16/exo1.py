def moyenne(tab):
    somme = 0
    if len(tab) == 0:
        return "erreur"
    for valeur in tab:
        somme += valeur
    moyenne = somme/len(tab)
    return moyenne


print(moyenne([1.0]))
print(moyenne([1.0, 2.0, 4.0]))
print(moyenne([]))
