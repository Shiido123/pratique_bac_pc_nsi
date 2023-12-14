class Maillon:
    # erreur au niveau du nombre de paramètres de la fonction.
    def __init__(self, v, dernier):
        self.valeur = v
        self.suivant = dernier


class File:
    def __init__(self):
        self.dernier_file = None

    def enfile(self, element):
        nouveau_maillon = Maillon(element, self.dernier_file)
        self.dernier_file = nouveau_maillon

    def est_vide(self):
        return self.dernier_file == None

    def affiche(self):
        maillon = self.dernier_file
        while maillon != None:
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self):
        if not self.est_vide():
            if self.dernier_file.suivant == None:
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = 0
            while maillon.suivant.suivant != None:
                maillon = maillon.suivant
            resultat = maillon.valeur
            maillon.suivant = None
            return resultat
        return None


F = File()
F.est_vide()
F.enfile(2)
F.affiche()
F.est_vide()

F.enfile(5)
F.enfile(7)
F.affiche()

F.defile()
F.defile()
F.affiche()
