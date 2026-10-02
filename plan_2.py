from tkinter import *
from tkinter import filedialog,messagebox


# Fenetre
fenetre = Tk()
fenetre.title("Théorie et Algorithme des Graphes")
fenetre.iconbitmap("photo.ico")
fenetre.geometry("800x500")

zone_texte = Text(fenetre,wrap="word")
zone_texte.pack(fill=BOTH,expand=True)

fichier_courant = None


def nouveau_fichier(event=None):
    global fichier_courant
    if not demander_enregistrer():
        return  # l'utilisateur a annulé, on ne fait rien
    zone_texte.delete("1.0",END)
    fichier_courant=None
    zone_texte.edit_modified(False)
    fenetre.title("Théorie et Algorithme des Graphes - Nouveau")


def ouvrir(event=None):
    global fichier_courant
    if not demander_enregistrer():
        return
    chemin = filedialog.askopenfilename(
        filetypes=[
            ("Fichier texte", "*.txt"),
            ("Fichier graphe", "*.graphe"),
            ("Fichier Python", "*.py"),
            ("Fichier C", "*.c"),
            ("Fichier JSON", "*.json"),
            ("Tous les fichiers", "*.*")
        ]
    )
    if chemin:
        with open(chemin,"r",encoding="utf-8") as f:
            contenu = f.read()
        zone_texte.delete("1.0",END)
        zone_texte.insert("1.0",contenu)
        fichier_courant=chemin
        zone_texte.edit_modified(False)
        fenetre.title("Théorie et Algorithme des Graphes - "+chemin)


def enregistrer_sous(event=None):
    global fichier_courant
    chemin = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Fichier texte", "*.txt"),
            ("Fichier graphe", "*.graphe"),
            ("Fichier Python", "*.py"),
            ("Fichier C", "*.c"),
            ("Fichier JSON", "*.json"),
            ("Tous les fichiers", "*.*")
        ]
    )
    if chemin:
        with open(chemin,"w",encoding="utf-8") as f:
            f.write(zone_texte.get("1.0",END))
        fichier_courant=chemin
        zone_texte.edit_modified(False)
        fenetre.title("Théorie et Algorithme des Graphes - "+chemin)
        return True
    return False  # l'utilisateur a annulé la boîte de dialogue


def enregistrer(event=None):
    if fichier_courant is None:
        return enregistrer_sous()
    else:
        with open(fichier_courant,"w",encoding="utf-8") as f:
            f.write(zone_texte.get("1.0",END))
        zone_texte.edit_modified(False)
        messagebox.showinfo("Enregistrer","Fichier enregistré.")
        return True


def demander_enregistrer():
    """
    Vérifie si le texte a été modifié. Si oui, demande à l'utilisateur
    s'il veut enregistrer avant de continuer (fermer/quitter/nouveau/ouvrir).
    Retourne True si on peut continuer, False si l'utilisateur annule.
    """
    if not zone_texte.edit_modified():
        return True  # rien n'a changé, pas besoin de demander

    reponse = messagebox.askyesnocancel(
        "Enregistrer les modifications ?",
        "Le fichier a été modifié. Voulez-vous enregistrer avant de continuer ?"
    )
    if reponse is None:      # Annuler
        return False
    elif reponse is True:    # Oui, enregistrer
        return enregistrer()
    else:                    # Non, continuer sans enregistrer
        return True


def fermer(event=None):
    global fichier_courant
    if not demander_enregistrer():
        return
    zone_texte.delete("1.0",END)
    fichier_courant=None
    zone_texte.edit_modified(False)
    fenetre.title("Théorie et Algorithme des Graphes ")


def quitter(event=None):
    if not demander_enregistrer():
        return
    fenetre.destroy()


# Menu Principal
barre_menu = Menu(fenetre)

# 5 Button
Menu_Fichier = Menu(barre_menu,tearoff=0)
Menu_Fichier.add_command(label="Nouveau Fichier",accelerator="Ctrl+N",command=nouveau_fichier)
Menu_Fichier.add_command(label="Ouvrir",accelerator="Ctrl+O",command=ouvrir)
Menu_Fichier.add_command(label="Enregistrer",accelerator="Ctrl+S",command=enregistrer)
Menu_Fichier.add_command(label="Enregistrer Sous",accelerator="Ctrl+Maj+S",command=enregistrer_sous)
Menu_Fichier.add_command(label="Fermer",accelerator="Ctrl+W",command=fermer)
Menu_Fichier.add_command(label="Quitter",accelerator="Ctrl+Q",command=quitter)



Menu_Creation = Menu(barre_menu,tearoff=0)


Graphe_Non_Oriente = Menu(Menu_Creation,tearoff=0)
Graphe_Non_Oriente.add_command(label="Aret")
Graphe_Non_Oriente.add_command(label="Sommet")

Graphe_Oriente = Menu(Menu_Creation,tearoff=0)
Graphe_Oriente.add_command(label="Arc")
Graphe_Oriente.add_command(label="Sommet")

Menu_Creation.add_cascade(label="Graphe Non Oriente",menu=Graphe_Non_Oriente)
Menu_Creation.add_cascade(label="Graphe Oriente",menu=Graphe_Oriente)

Menu_Affichage = Menu(barre_menu,tearoff=0)

Menu_Execution = Menu(barre_menu,tearoff=0)

Menu_Edition = Menu(barre_menu,tearoff=0)


barre_menu.add_cascade(label="Fichier",menu=Menu_Fichier,state="normal")
barre_menu.add_cascade(label="Création",menu=Menu_Creation,state="disabled")
barre_menu.add_cascade(label="Affichage",menu=Menu_Affichage,state="normal")
barre_menu.add_cascade(label="Exécution",menu=Menu_Execution,state="normal")
barre_menu.add_cascade(label="Édition",menu=Menu_Edition,state="normal")



fenetre.config(menu=barre_menu)

fenetre.bind("<Control-n>",nouveau_fichier)
fenetre.bind("<Control-o>",ouvrir)
fenetre.bind("<Control-s>",enregistrer)
fenetre.bind("<Control-Shift-S>",enregistrer_sous)
fenetre.bind("<Control-w>",fermer)
fenetre.bind("<Control-q>",quitter)

# Si l'utilisateur ferme avec le X de la fenêtre, on vérifie aussi
fenetre.protocol("WM_DELETE_WINDOW", quitter)

fenetre.mainloop()
