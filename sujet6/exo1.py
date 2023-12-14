def rendu(nombre):
    lst = [0, 0, 0]
    while nombre > 0:
        if nombre == 1:
            lst[2] += 1
            nombre = nombre-1
        elif nombre >= 2 and nombre < 5:
            lst[1] += 1
            nombre = nombre - 2
        elif nombre >= 5:
            lst[0] += 1
            nombre = nombre - 5
    return lst


print(rendu(13))
print(rendu(64))
# rendu de 89 ne fait pas [17,2,1] comme prétendu dans l'énoncé. En effet, 17*5=85 et 2*2=4. Pas besoin de 1.
print(rendu(89))
