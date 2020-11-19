class Pile:
    def __init__(self,nom ,taille):
        self.nom = nom
        self.taille = taille
        self.contenu = [None]*self.taille

    def est_vide(self):
        return self.contenu == [None]*self.taille

    def ajouter_pile(self,element):
        index = 0
        while self.contenu[index]!=None:
            index+=1
        try:
            self.contenu[index]=element
        except IndexError:
            print("la taille max du tableau a été atteinte")


    def enlever_pile(self):
        index = self.contenu.count(None)+1
        self.contenu[-index] = None

class File:
    def __init__(self,nom ,taille):
        self.nom = nom
        self.taille = taille
        self.contenu = [None]*self.taille

    def est_vide(self):
        return self.contenu == [None] * self.taille

    def ajouter_file(self,element):
        index = 0
        while self.contenu[index]!=None:
            index+=1
        try:
            self.contenu[index]=element
        except IndexError:
            print("la taille max du tableau a été atteinte")


    def enlever_file(self):
        self.contenu[0] = None

