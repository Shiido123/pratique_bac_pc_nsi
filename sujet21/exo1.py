def nb_repetitions(elt, tab):
    compteur = 0
    for valeur in tab:
        if elt == valeur:
            compteur += 1

    return compteur


print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']))
print(nb_repetitions(12, [1, '! ', 7, 21, 36, 44]))
