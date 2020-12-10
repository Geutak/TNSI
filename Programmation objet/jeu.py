class Noeud:
    """un noeud d'un arbre binaire"""
    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droite = d

    def taille(self):
        if self.droite is None and self.gauche is None:
            return 1
        elif self.droite is None:
            return 1 + self.gauche.taille()
        elif self.gauche is None:
            return 1+self.droite.taille()
        return 1+self.gauche.taille()+self.droite.taille()

    def hauteur(self):
        if self.droite is None and self.gauche is None:
            return 1
        elif self.droite is None:
            return 1 + self.gauche.hauteur()
        elif self.gauche is None:
            return 1+self.droite.hauteur()
        return 1+max(self.gauche.hauteur(),self.droite.hauteur())

    def parcours_infixe(self):
        if self is None:
            return
        if self.gauche != None:
            self.gauche.parcours_infixe()
        print(self.valeur)
        if self.droite!=None:
            self.droite.parcours_infixe()

    def afficher(self):
        if self is None:
            return
        print("(",end="")
        self.gauche.afficher()
        print(self.valeur)
        self.droite.afficher()
        print(")", end="")

