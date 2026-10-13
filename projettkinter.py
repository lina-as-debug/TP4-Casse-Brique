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

# class Balle:
#     def __init__(self, canvas):
#         self.canvas = canvas
        
#         # Réglages de la balle
#         x = 230       # Position de départ horizontale (milieu de l'écran environ)
#         y = 150       # Position de départ verticale (au milieu du ciel)
#         taille = 20   # Diamètre du cercle en pixels
        
#         # Création du cercle (x1, y1, x2, y2)
#         # Tkinter nous renvoie son numéro d'identité unique qu'on stocke dans self.id
#         self.id = self.canvas.create_oval(x, y, x + taille, y + taille, fill='pink', outline='')
#         self.vitesse_x = 3  # Se déplace de 3 pixels vers la droite
#         self.vitesse_y = 3  # Se déplace de 3 pixels vers le bas

#     def deplacer(self):
#         # Cette ligne applique le mouvement en diagonale (X et Y bougent en même temps)
#         self.canvas.move(self.id, self.vitesse_x, self.vitesse_y)

#         # 2. On récupère ses nouvelles coordonnées [x1, y1, x2, y2]
#         coords = self.canvas.coords(self.id)

#         # --- REBOND GAUCHE ET DROITE ---
#         # coords[0] = bord gauche de la balle | coords[2] = bord droit de la balle
#         # Le canvas fait 480 pixels de large
#         if coords[0] <= 0 or coords[2] >= 480:
#             self.vitesse_x = -self.vitesse_x  # On inverse la direction horizontale

#             # --- REBOND PLAFOND (HAUT) ---
#         # coords[1] = haut de la balle
#         if coords[1] <= 0:
#             self.vitesse_y = -self.vitesse_y  # On inverse la direction verticale


class Balle:
    # On ajoute "raquette" dans les arguments pour que la balle puisse la voir
    def __init__(self, canvas, raquette):
        self.canvas = canvas
        self.raquette = raquette  # La balle se souvient de la raquette
        
        x = 230       
        y = 150       
        taille = 20   
        self.id = self.canvas.create_oval(x, y, x + taille, y + taille, fill='yellow', outline='')
        
        self.vitesse_x = 3  
        self.vitesse_y = -3  

    def deplacer(self):
        self.canvas.move(self.id, self.vitesse_x, self.vitesse_y)
        coords = self.canvas.coords(self.id)
        
        # 1. Rebonds sur les murs (inchangé)
        if coords[0] <= 0 or coords[2] >= 480:
            self.vitesse_x = -self.vitesse_x  
        if coords[1] <= 0:
            self.vitesse_y = -self.vitesse_y  

        # 2. --- REBOND SUR LA RAQUETTE ---
        # On récupère la position actuelle de la raquette bleue [x1, y1, x2, y2]
        coords_raquette = self.canvas.coords(self.raquette.id)
        
        # On vérifie si le bas de la balle (coords[3]) touche le haut de la raquette (coords_raquette[1])
        if coords[3] >= coords_raquette[1] and coords[3] <= coords_raquette[3]:
            # On vérifie si la balle est bien alignée horizontalement avec la raquette
            if coords[2] >= coords_raquette[0] and coords[0] <= coords_raquette[2]:
                self.vitesse_y = -self.vitesse_y # Rebond vers le haut !

        # 3. --- DÉTECTION DE LA DÉFAITE ---
        # Si le haut de la balle dépasse le bas du canvas (300px), c'est perdu
        if coords[1] > 300:
            self.vitesse_x = 0
            self.vitesse_y = 0
            # Ici, la balle s'arrête. On verra après pour afficher un texte "Game Over"


    
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
        self.ma_raquette = Raquette(self.canvas, self.rect_id )

        # C'EST ICI QU'IL FAUT METTRE LA LIGNE, POUR APPELER LA CLASS BALLE !
        self.ma_balle = Balle(self.canvas, self.ma_raquette)

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

        self.animer_jeu()


        # Lancer la fenêtre
        self.window.mainloop()

    def animer_jeu(self):
        # On demande à la balle d'avancer
        self.ma_balle.deplacer()
        
        # On demande à la fenêtre de relancer cette fonction dans 20 millisecondes
        self.window.after(20, self.animer_jeu)

# Lancement du jeu
jeu = CasseBrique()