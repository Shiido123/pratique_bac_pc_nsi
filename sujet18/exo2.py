def insere(a, tab):
    l = list(tab)  # l contient les mêmes éléments que tab
    l.append(a)
    i = 0
    while a < len(tab):
        l[i+1] = 0
        l[i] = a
        i = i+1
    return l


print(insere(3, [1, 2, 4, 5]))
print(insere(10, [1, 2, 7, 12, 14, 25]))
print(insere(1, [2, 3, 4]))

#marche pas encore