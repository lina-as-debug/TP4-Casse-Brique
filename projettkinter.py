from tkinter import  *

# class Raquette:
#     def __init__(self, canvas, rectangle_id):
#         self.canvas = canvas
#         self.id = rectangle_id
#         self.vitesse = 15  # Vitesse de déplacement en pixels

#     def deplacer_gauche(self, event):
#         # canvas.move(id, x, y) -> déplace de -15px sur l'axe X (gauche)
#         # On vérifie qu'on ne sort pas du canvas à gauche
#         coords = self.canvas.coords(self.id)
#         if coords[0] > 0:
#             self.canvas.move(self.id, -self.vitesse, 0)

#     def deplacer_droite(self, event):
#         # canvas.move(id, x, y) -> déplace de +15px sur l'axe X (droite)
#         # On vérifie qu'on ne sort pas du canvas à droite (largeur max 300)
#         coords = self.canvas.coords(self.id)
#         if coords[2] < 300:
#             self.canvas.move(self.id, self.vitesse, 0)


# class CasseBrique:
#     def __init__(self):
#             # 1. Créer la fenêtre
#             self.window = Tk()
#             self.window.title("Jeu Casse-Brique")
#             self.window.geometry("480x360")
#             self.window.config(background='black')

#             # 2. Score (Placé en haut à droite)
#             self.label_title = Label(self.window, text="Score: 0", font=("Courier", 10), bg='black', fg='yellow')
#             self.label_title.pack(side=RIGHT, anchor="n", padx=10, pady=10)

#             # 3. Frame du bas (La boîte qui contient tout)
#             self.bas_frame = Frame(self.window, bg='black')
#             self.bas_frame.pack(side=BOTTOM, fill=X, padx=10, pady=10)

#             # --- CORRECTION DES BOUTONS EN PREMIER ---
#             # On affiche d'abord le bouton quitter tout à droite
#             self.btn_quitter = Button(self.bas_frame, text="quitter", font=("Courier", 10), bg='red', fg='white', command=self.window.destroy)
#             self.btn_quitter.pack(side=RIGHT, anchor=SE, padx=5)

#             # Puis le bouton démarrer juste à côté
#             self.btn_demarrer = Button(self.bas_frame, text="démarrer", font=("Courier", 10), bg='red', fg='white')
#             self.btn_demarrer.pack(side=RIGHT, anchor=SE, padx=5)

#             # --- CORRECTION DU CANVAS EN DEUXIÈME ---
#             self.width = 300
#             self.height = 150
#             # On enlève "expand=True", on laisse side=LEFT. 
#             # Le canvas va occuper ses 300px à gauche sans écraser les boutons à droite.
#             self.canvas = Canvas(self.bas_frame, width=self.width, height=self.height, background='black', highlightthickness=0)
#             self.canvas.pack(side=LEFT, anchor=CENTER)

#             # 5. Création visuelle du rectangle (la raquette)
#             self.rect_id = self.canvas.create_rectangle(120, 130, 180, 150, fill='blue', outline='')

#             # 6. Initialisation de la classe Raquette
#             self.ma_raquette = Raquette(self.canvas, self.rect_id)

#             # 8. Lier les touches du clavier
#             self.window.bind("<Left>", self.ma_raquette.deplacer_gauche)
#             self.window.bind("<Right>", self.ma_raquette.deplacer_droite)

#         # Lancer la fenêtre
#             self.window.mainloop()
# jeu = CasseBrique()


from tkinter import *

class Raquette:
    def __init__(self, canvas, rectangle_id):
        self.canvas = canvas
        self.id = rectangle_id
        self.vitesse = 15  # Vitesse de déplacement en pixels

    def deplacer_gauche(self, event):
        coords = self.canvas.coords(self.id)
        if coords[0] > 0:
            self.canvas.move(self.id, -self.vitesse, 0)

    def deplacer_droite(self, event):
        coords = self.canvas.coords(self.id)
        # La largeur du canvas étant maintenant de 480, on s'arrête à 480
        if coords[2] < 480:
            self.canvas.move(self.id, self.vitesse, 0)


class CasseBrique:
    def __init__(self):
        # 1. Créer la fenêtre
        self.window = Tk()
        self.window.title("Jeu Casse-Brique")
        self.window.geometry("480x360")
        self.window.config(background='black')

        # 2. Zone de jeu (Le Canvas prend toute la largeur du haut de la fenêtre)
        self.width = 480
        self.height = 300  # Donne une grande zone pour le jeu au-dessus de la barre
        self.canvas = Canvas(self.window, width=self.width, height=self.height, background='black', highlightthickness=0)
        self.canvas.pack(side=TOP, fill=BOTH, expand=True)

        # 3. Création de la raquette tout en bas du Canvas (y1=280, y2=300)
        # Elle est centrée au départ (x1=210, x2=270 pour une longueur de 60px)
        self.rect_id = self.canvas.create_rectangle(210, 280, 270, 300, fill='blue', outline='')

        # 4. Initialisation de la classe Raquette
        self.ma_raquette = Raquette(self.canvas, self.rect_id)

        # 5. Frame du bas (La barre d'outils tout en bas)
        self.bas_frame = Frame(self.window, bg='black')
        self.bas_frame.pack(side=BOTTOM, fill=X, padx=10, pady=10)

        # 6. Le Score (Placé à GAUCHE dans la frame du bas)
        self.label_title = Label(self.bas_frame, text="Score: 0", font=("Courier", 10), bg='black', fg='yellow')
        self.label_title.pack(side=LEFT, anchor=SW, padx=5)

        # 7. Les Boutons (Placés à DROITE dans la frame du bas)
        # On affiche d'abord quitter tout à droite
        self.btn_quitter = Button(self.bas_frame, text="quitter", font=("Courier", 10), bg='red', fg='white', command=self.window.destroy)
        self.btn_quitter.pack(side=RIGHT, anchor=SE, padx=5)

        # Puis démarrer juste à côté
        self.btn_demarrer = Button(self.bas_frame, text="démarrer", font=("Courier", 10), bg='red', fg='white')
        self.btn_demarrer.pack(side=RIGHT, anchor=SE, padx=5)

        # 8. Lier les touches du clavier
        self.window.bind("<Left>", self.ma_raquette.deplacer_gauche)
        self.window.bind("<Right>", self.ma_raquette.deplacer_droite)

        # Lancer la fenêtre
        self.window.mainloop()

# Lancement du jeu
jeu = CasseBrique()