import random
import time


class Personnage:
    """ personnage de type générique """

    points_de_vie = 100
    points_de_vie_max = 100
    potion_de_vie = False
    mage_liste = []
    heure_de_coucher = 0
    coucher = False
    liste_equipe = ["verte","rouge","bleue"]
    def __init__(self, nom, espece, equipe=None):
        if equipe==None:
            self.equipe=self.liste_equipe[random.randint(0,2)]
        self.nom = nom
        self.espece = espece
        self.equipe = equipe
        if self.espece == "guerrier":
            self.points_attaque = 5
            self.points_defense = 3
            self.stamina = 13
        if self.espece == "archer":
            self.points_attaque = 5
            self.points_defense = 7
            self.stamina = 10
        if self.espece == "mage":
            self.points_attaque = 3
            self.points_defense = 3
            self.stamina = 8
            self.potion_de_vie = True
            self.mage_liste.append(self)
        self.stamina_max = self.stamina
        print("le joueur {0} a été créé il est de l'équipe {1} et de l'espece {2}".format(self.nom, self.equipe, self.espece))

    def inlife(self):
        if self.points_de_vie <= 0:
            print("le joueur {0} est mort".format(self.nom))
            return False
        return True

    def meme_equipe(self, joueur):
        if self.equipe == joueur.equipe:
            return True
        return False

    def attaquer(self, adversaire, nombre_decoup=1):
        if self.coucher:
            print("le joueur {0} dort il ne peut pas attaquer !".format(self.nom))
            return
        if adversaire.inlife() and self.inlife():
            if self.meme_equipe(adversaire):
                print(
                    "le joueur {0} et le joueur {1} sont tout les deux de l'equipe {2} un joueur ne peux pas attaquer un joueur de son equipe !".format(
                        self.nom, adversaire.nom, self.equipe))
                return
            coups_portes = 0
            for coup in range(nombre_decoup):
                if self.stamina == 0:
                    break
                coups_portes += 1
                self.stamina -= 1
                adversaire.points_de_vie -= (self.points_attaque - adversaire.points_defense)

            print("le joueur {0} donne {1} coup(s) au joueur {3} il reste {2} de vie au joueur {3}".format(self.nom,
                                                                                                           coups_portes,
                                                                                                           adversaire.points_de_vie,
                                                                                                           adversaire.nom))
            adversaire.inlife()
            if self.stamina == 0:
                print("le joueur {0} n'a plus de stamina il ne peut plus attaquer (une sieste s'impose !)".format(
                    self.nom))
        if random.randint(0, 5) == 1:
            time.sleep(3)
            print("\n\n\nil y a une reunion de mages dans la foret le(s) joueur(s) suivant doivent y aller :")
            for player in self.mage_liste:
                if player.espece == "mage":
                    print(player.nom)

    def repos(self):
        if self.heure_de_coucher != 0:
            print("le joueur{0} dort deja !".format(self.nom))
            return
        if self.points_de_vie == self.points_de_vie_max and self.stamina == self.stamina_max:
            print("le joueur {0} a deja ses points de vie et sa stamina au max il n'est pas fatigué".format(self.nom))
            return
        self.heure_de_coucher = int(time.time())
        self.coucher = True

    def reveil(self):
        if self.heure_de_coucher == 0:
            print("le joueur {0} est ne dort pas !".format(self.nom))
            return
        temps_de_sommeil = int(time.time() - self.heure_de_coucher)
        self.heure_de_coucher = 0
        self.points_de_vie = int(self.points_de_vie * random.uniform(1.10, 1.25))
        if self.stamina <= 2:
            self.stamina = random.randint(int(self.stamina_max / 4), int(self.stamina_max / 2))
        self.stamina = self.stamina * 2
        if self.points_de_vie > self.points_de_vie_max:
            self.points_de_vie = self.points_de_vie_max
        if self.stamina > self.stamina_max:
            self.stamina = self.stamina_max
        print(
            "le joueur {0} s'est reposé pendant {1} heures, il posséde maintenant {2} point de vie et {3} de stamina".format(
                self.nom, temps_de_sommeil / 50, self.points_de_vie, self.stamina))
        self.coucher=False

    def revive(self, mort):
        if mort.points_de_vie > 0:
            print("le joueur {0} n'est pas mort".format(mort.nom))
            return
        if self.potion_de_vie:
            if self.equipe != mort.equipe:
                print(
                    "le joueur {0} ({1}) et le joueur {2} ({3}) ne sont pas de la même équipe il faut etre de la même equipe pour revive !".format(
                        self.nom, self.equipe, mort.nom, mort.equipe))
                return
            mort.points_de_vie = self.points_de_vie_max
            mort.points_de_vie = self.stamina_max
            print(
                "le joueur {0} revient à la vie avec {2} points de vie et toute sa stamina ! (il peut remercier {1}!)\nle joueur {1} ne possede plus de potion de vie".format(
                    mort.nom, self.nom, mort.points_de_vie))
            self.potion_de_vie = False
        elif self.espece != "mage":
            print(
                "seul les mages peuvent faire revivre ou alors vous pouvez en trouver en vous baladans dans la foret")
        else:
            print("vous ne pouvez utiliser qu'une seul fois votre potion de vie")

    def info(self):
        print(vars(self))

    def balade(self):
        if self.coucher:
            print("le joueur {0} dort encore il ne peux pas se balader".format(self.nom))
            return
        if self.espece == "mage":
            if self.potion_de_vie and random.randint(0, 1):
                self.points_de_vie = False
                print(
                    "vous vous trouvez face à un loup vous vous enfuyez mais dans votre fuite vous faites tomber votre potion de vie")

        if random.randint(0, 1):
            gouter = input(
                "Oh ! on dirais bien qu'un mage qui passait par là a fait tomber une potion voulez vous la gouter ? (o/n)")
            if gouter == "o":
                if random.randint(0, 1):
                    self.points_de_vie -= 75
                    if self.points_de_vie < 0: self.points_de_vie = 0
                    print("cette potion etait un poison ! vous perdez 75 hp vous en avez maintenant {0}".format(
                        self.points_de_vie))
                    self.inlife()
                else:
                    print(
                        "wouaw vous venez de trouver une potion de vie vous pouvez maintenant faire revivre un joueur tel un mage !")
                    self.potion_de_vie = True