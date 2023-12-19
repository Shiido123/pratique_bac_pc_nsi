a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'],
     'C': ['', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'],
     'H': ['', '']}


def taille(arbre, lettre):

    if lettre == '':
        return 0

    compteur = 1
    compteur += taille(arbre, arbre[lettre][0])
    compteur += taille(arbre, arbre[lettre][1])

    return compteur


print(taille(a, 'F'))
