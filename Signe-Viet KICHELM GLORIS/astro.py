import os
def verif_mois(m):
    """fonction prenant en entrée le mois de naissance(m) de l'utilisateur
    et qui verifie si le mois entré par l'utilisateur et bien correct (entre 1 et 12) sinon elle leve une erreur"""
    try:
        if m < 1 or m > 12:
            raise ValueError
    except ValueError:
        print("votre mois doit être en chiffres et entre 1 et 12.")
        raise


def verif_jour(j,m, bis):
    """fonction prenant en entrée le jour et le mois de naissance ainsi qu'un bouléen pour savoir si l'aanée et bissextile
    et qui verifie si le jour entré par l'utilisateur et bien correct sinon elle leve une erreur"""
    jour_max = [31,None,31,30,31,30,31,31,30,31,30,31]
    try:

        x = jour_max[m]
        if m == 2 and bis:
            x = 29
        elif m == 2 and not bis:
            x = 28

        if 1 > j or j> x:
            raise ValueError
    except ValueError:
        print("votre jour doit être en chiffres et entre 1 et {}.".format(x))
        raise
def demander_date():
    """fonction qui demande à l'utilisateur sa date de naissance avec un input
        cette fonction comporte des exceptions afin de gérer les erreurs d'entrées de l'utilisateur
        et qui retourne son jour, son mois et son année de naissance dans 3 variables distinctes"""
    while True:
        try:
            d = input('Entrez votre date de naissance au format jj/mm/aaaa')
            d = d.split("/")
            j = int(d[0])
            m = int(d[1])
            a = int(d[2])
            break
        except ValueError:
            print("Ta date de naissance doit etre en chiffre au format jj/mm/aaaa  doit être en chiffres.")

        except IndexError:
            print("Vous avez oublié une partie de votre date de naissance.")
    return j, m, a
def get_caractere(r):
    """cette fonction crée une liste comportant:
     les différent caractères de chacun des 12 signes vietnamiens
     et return celui du signe de l'utilisateur"""

    with open("caractere.txt.txt","r",encoding="utf-8") as file :
        print(type(file))
        liste_caractère = file.readlines()
    return liste_caractère[r]

def signe_viet(a):
    """fonction qui crée une liste des 12 signes vietnamien et renvoie son index en calculant r:
    le reste du quotient  l'année de naissance de l'utilisateur et de 12 car il y a 12 signes vietnamiens
    cette fonction indique donc à l'utilisateur son signe vietnamien ainssi que son caractère associé car
    elle fait appel à get_caractere(r) (définit plus haut) avec comme parametre r calculé juste avant """

    signe_vietnamien = ["singe","coq","chien","cochon","rat","buffle","tigre","chat","dragon","serpent","cheval","chèvre"]
    r = a%12
    if signe_vietnamien[r] == "chèvre":
        genre = "de la"
    else:
        genre = "du"
    return r, signe_vietnamien[r], genre

def annee_bissextile(a):
    """fonction prenant en entrée une année a
        en renvoit True si l'année et bissextile ou False si elle ne l'est pas"""
    if a % 4 == 0 :
        if a % 100==0:
            if a % 400 !=0:
                return False
        return True
    return False