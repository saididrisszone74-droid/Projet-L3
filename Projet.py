from tkinter import *

# Fenetre Principale 
fenetre = Tk()
fenetre.title("Théorie et Algorithme des Graphes")
fenetre.geometry("800x500")


barre_menu = Menu(fenetre,bg='#173B57',fg='white',
                  activebackground='#2E8B57',activeforeground='white')
barre_menu.add_cascade(label="Fichier")
barre_menu.add_cascade(label="Créaton")
barre_menu.add_cascade(label="Affichage")
barre_menu.add_cascade(label="Execution")
barre_menu.add_cascade(label="Edition")
fenetre.config(menu=barre_menu)
fenetre.mainloop()