def tri_selection(tab):
    for i in range(len(tab)):
        min_index = i
        for j in range(i+1, len(tab)):
            if tab[min_index] > tab[j]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
    return tab


print(tri_selection([64, 25, 12, 22, 11]))
