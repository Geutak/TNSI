class Pile:
    """une pile est une structure de données qui fonctionne suivant le principe LIFO (Last In First Out)
     : on ne peut récupérer que la dernière donnée qui a été rajoutée à la pile.
      lorsqu'on rajoute une donnée, on dit qu'on empile,lorsq'on l'enléve on dit qu'on dépile"""
    def __init__(self, nom, taille=0):
        self.nom = nom
        self.taille = taille
        self.contenu = [None]*self.taille

    def est_vide(self):
        """On dira qu'une Pile est vide si elle ne contient que des None quelque soit sa taille"""
        return self.contenu == [None]*self.taille

    def empiler(self,element):
        """on rajoute une donnée à la fin de la Pile"""
        self.contenu.append(element)
        self.taille+=1

    def depiler(self):
        """on enleve une donnée à la fin de la Pile"""

        self.taille-=1
        return self.contenu.pop(-1)

    def extaire(self,index):
        """on extrait la donnée située en position index depuis le haut de la pile"""
        position = 0
        if position==0:
            position = 1
            pile_temp = Pile("pile_de_stockage")
            pile_temp.empiler(self.depiler())
        while index!=position:
            position+=1
            pile_temp.empiler(self.depiler())
        if index==position:
            resultat = self.depiler()
        for i in range(len(pile_temp.contenu)):
            self.empiler(pile_temp.depiler())

        return resultat

    def inserer(self,index,valeur):
        position = 0
        if position==0:
            position = 1
            pile_temp = Pile("pile_de_stockage")
            pile_temp.empiler(self.depiler())
        while index!=position:
            position+=1
            pile_temp.empiler(self.depiler())
        if index==position:
            self.empiler(valeur)
        for i in range(len(pile_temp.contenu)):
            self.empiler(pile_temp.depiler())


class File:
    """une file est une structure de données qui fonctionne suivant le principe FIFO (First In First Out)
         : on ne peut récupérer que la premiere donnée qui a été rajoutée à la pile.
          lorsqu'on rajoute une donnée, on dit qu'on ajoute,lorsq'on l'enléve on dit qu'on retire"""

    def __init__(self, nom, taille=0):
        self.nom = nom
        self.taille = taille
        self.contenu = [None] * self.taille

    def est_vide(self):
        """On dira qu'une File est vide si elle ne contient que des None quelque soit sa taille"""
        return self.contenu == [None] * self.taille

    def ajouter(self, element):
        """on rajoute une donnée au debut de la File"""
        self.contenu.append(element)
        self.taille += 1

    def retirer(self):
        """on enleve une donnée au debut de la File"""
        self.contenu.pop(0)
        self.taille -= 1