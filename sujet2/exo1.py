def moyenne(tab):
    somme = 0
    if len(tab) == 0:
        return "erreur"
    for valeur in tab:
        somme += valeur
    moyenne = somme/len(tab)
    return moyenne


print(moyenne([5, 3, 8]))
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(moyenne([]))
