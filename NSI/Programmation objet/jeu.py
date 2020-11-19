from classes_jeu import *
from tkinter import *
def creer_perso(fen):
    def create(nb_perso):
        nb_perso=int(nb_perso.get())
        lbl_nom = Label()
        lbl_espece = Label()
        lbl_equipe = Label()
        entry_nom = Entry()
        entry_espece = Entry()
        entry_equipe = Entry()
        for perso in range(nb_perso):
            lbl_nom.config(text="nom du joueur {0}".format(perso+1))
            lbl_nom.pack()
            lbl_espece.config(text="espece du joueur {0}".format(perso + 1))
            lbl_espece.pack()
            lbl_equipe.config(text="equipe du joueur {0}".format(perso+1))
            lbl_equipe.pack()
            perso = Personnage(nom, espece, equipe)
            print(vars(perso))
    lbl_nb_de_perso = Label(text="nombre de joueur")
    lbl_nb_de_perso.pack()
    nb_perso = Entry()
    nb_perso.pack()
    btn_nb = Button(text="creer les joueur",command=lambda : create(nb_perso))
    btn_nb.pack()
