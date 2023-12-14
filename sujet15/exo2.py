class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à
    13)"""

    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10,
    Valet, Dame, Roi"""

    def getNom(self):
        if (int(self.Valeur) > 1 and int(self.Valeur) < 11):
            return str(self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur,
    carreau, trefle"""

    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur]


class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    def remplir(self):
        for i in range(13):
            for j in range(4):
                self.contenu.append(Carte(j, i))

    def getCarteAt(self, pos):
        return self.contenu[pos]


unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(12)
print(uneCarte.getNom() + " de " + uneCarte.getCouleur())
