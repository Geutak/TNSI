""" jeu de rôles simple , avec des listes """
import random
nom=[]
espece=[]
points_de_vie=[]
points_d_attaque =[]
points_de_defense=[]
max_life=100
print(" Combien de joueurs ?")
nombre_joueurs= int(input())
print(nombre_joueurs)
for i in range(nombre_joueurs):
    points_de_vie.append(max_life)
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
    points_de_vie[b]-=abs(random.randint(1,points_d_attaque[a])-random.randint(1,points_de_defense[b]))
    points_de_vie[a]-=abs(random.randint(1,points_d_attaque[b])-random.randint(1,points_de_defense[a]))
    """ Remarque : du moment qu'on se bat, on perd .... """
    print('points de vie de {0}  : {1}'.format(nom[a],points_de_vie[a]))
    print('points de vie de {0}  : {1}'.format(nom[b],points_de_vie[b]))
def repos(a):
    if points_de_vie[a] == max_life:
        print("le joueur {0} a deja ses points de vie au max il n'est pas fatigué".format(nom[a]))
        return
    points_de_vie[a] = int(points_de_vie[a]*random.randint(1.10,1.25))
    if points_de_vie[a]>max_life:
        points_de_vie[a]=max_life
    print("le joueur {0} s'est reposé , il posséde maintenant {1} point de vie".format(nom[a],points_de_vie[a]))