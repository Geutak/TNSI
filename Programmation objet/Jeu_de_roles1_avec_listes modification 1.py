""" jeu de rôles simple , avec des listes """
import random
nom=[]
espece=[]
points_de_vie=[]
points_d_attaque =[]
points_de_defense=[]
print(" Combien de joueurs ?")
nombre_joueurs= int(input())
print(nombre_joueurs)
for i in range(nombre_joueurs):
    points_de_vie.append(100)
    print('nom du joueur {} ?'.format(i))
    nom.append(input())
    print('espece du joueur {}  (guerrier ou archer )?'.format(i))
    espece.append(input())
    if espece[i]=="guerrier" :
        points_de_defense.append(3)
        points_d_attaque.append(5)
    if espece[i]=="archer" :
        points_de_defense.append(7)
        points_d_attaque.append(5)

def attaquer(a,b):
    for joueur in range(nombre_joueurs):
        if points_de_vie[joueur]<=0:
            print("le joueur {} est mort".format(nom[joueur]))
            return
    points_de_vie[b]-=abs(random.randint(1,points_d_attaque[a])-random.randint(1,points_de_defense[b]))
    points_de_vie[a]-=abs(random.randint(1,points_d_attaque[b])-random.randint(1,points_de_defense[a]))
    """ Remarque : du moment qu'on se bat, on perd .... """
    print('points de vie de {0}  : {1}'.format(nom[a],points_de_vie[a]))
    print('points de vie de {0}  : {1}'.format(nom[b],points_de_vie[b]))


