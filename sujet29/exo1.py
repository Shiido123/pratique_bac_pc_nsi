def calcul(nombre):
    lst = [nombre]
    while nombre != 1:
        if nombre % 2 == 0:
            nombre = nombre/2
            lst.append(int(nombre))
        else:
            nombre = 3*nombre + 1
            lst.append(int(nombre))
    return lst


print(calcul(7))
