from classes_jeu import *
from jeu import *
from tkinter import *
fen = Tk()
fen.title("jeu.py")
fen.geometry("500x500")
def main():

    creer_perso(fen)

launch_btn = Button(text="nouvelle partie", command=main)
launch_btn.pack()
fen.mainloop()