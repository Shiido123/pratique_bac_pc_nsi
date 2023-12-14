def convertir(liste):
    """
    T est un tableau d’entiers, dont les ´el´ements sont 0 ou 1 et
    repr´esentant un entier ´ecrit en binaire.
    Renvoie l’entier positif dont la repr´esentation binaire
    est donn´ee par le tableau T
    """
    nombre = 0
    for indice, valeur in enumerate(reversed(liste)):
        if valeur == 1:
            nombre += 2**indice
    return nombre


print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))
