from tkinter import Tk, Canvas, Event, TOP, BOTH, BOTTOM, X, Frame,Label,LEFT,RIGHT, Button
from collections import deque
class Raquette:
    def __init__(self, canvas, rectangle_id):
        self.canvas = canvas
        self.id = rectangle_id
        self.vitesse = 10  # Nombre de pixels déplacés à chaque appui sur une touche

    def deplacer_gauche(self, event):
        # Récupère les coordonnées actuelles de la raquette [x1, y1, x2, y2]
        coords = self.canvas.coords(self.id)
        # Empêche la raquette de sortir par la gauche (bord à X = 0)
        if coords[0] > 0:
            self.canvas.move(self.id, -self.vitesse, 0)

    def deplacer_droite(self, event):
        coords = self.canvas.coords(self.id)
        # Empêche la raquette de sortir par la droite (bord à X = 480)
        if coords[2] < 480:
            self.canvas.move(self.id, self.vitesse, 0)


class Balle:
    def __init__(self, canvas, raquette, jeu_principal):
        self.canvas = canvas
        self.raquette = raquette  
        self.jeu = jeu_principal  # Lien vers la classe principale pour modifier le score/briques
        
        # Création graphique de la balle (ovale jaune)
        self.id = self.canvas.create_oval(230, 150, 250, 170, fill='yellow', outline='')
        
        # Vecteurs de déplacement (pixels par rafraîchissement)
        self.vitesse_x = 3  
        self.vitesse_y = -3  

    def réinitialiser(self):
        """Repositionne la balle au centre de l'écran après la perte d'une vie."""
        self.canvas.coords(self.id, 230, 150, 250, 170)
        self.vitesse_x = 3
        self.vitesse_y = -3  # Redémarre vers le haut

    def deplacer(self):
        # Déplace l'objet graphiquement selon ses vitesses x et y
        self.canvas.move(self.id, self.vitesse_x, self.vitesse_y)
        coords = self.canvas.coords(self.id)  # Récupère [x1, y1, x2, y2] de la balle
        
        # Rebond sur les murs latéraux (gauche/droite)
        if coords[0] <= 0 or coords[2] >= 480:
            self.vitesse_x = -self.vitesse_x  
        # Rebond sur le mur du haut
        if coords[1] <= 0:
            self.vitesse_y = -self.vitesse_y  

        # Rebond sur la raquette (Loi de Descartes)
        coords_raquette = self.canvas.coords(self.raquette.id)
        if coords[3] >= coords_raquette[1] and coords[3] <= coords_raquette[3]:
            if coords[2] >= coords_raquette[0] and coords[0] <= coords_raquette[2]:
                self.vitesse_y = -abs(self.vitesse_y) # Rebondit vers le haut

        # --- GESTION DE LA LISTE ---
        # On parcourt la liste des briques pour tester si la balle en touche une.
        for brique_id in list(self.jeu.briques):
            coords_brique = self.canvas.coords(brique_id)
            # Vérification de l'impact géométrique (Intersection Balle et Brique)
            if (coords[2] >= coords_brique[0] and coords[0] <= coords_brique[2] and
                coords[3] >= coords_brique[1] and coords[1] <= coords_brique[3]):
                
                self.vitesse_y = -self.vitesse_y  # Inversion de la trajectoire
                self.canvas.delete(brique_id)    # Supprime le rectangle du canvas
                
                # STRUCTURE LISTE : On extrait chirurgicalement la brique détruite du tableau
                self.jeu.briques.remove(brique_id) 
                
                self.jeu.ajouter_points(2)
                self.jeu.ajouter_evenement("Brique détruite ! +2")
                
                # Condition de victoire : S'il n'y a plus aucune brique dans la liste
                if len(self.jeu.briques) == 0:
                    self.jeu.gagner_partie()
                return 

        # Si le haut de la balle (coords[1]) dépasse le bas de la zone de jeu (300px)
        if coords[1] > 300:
            self.jeu.perdre_une_vie()


class CasseBrique:
    
    def __init__(self):
        # 1. Configuration de la fenêtre Tkinter
        self.window = Tk()
        self.window.title("Jeu Casse-Brique")
        self.window.geometry("480x400") 
        self.window.config(background='black')

        self.en_cours = False  
        self.score = 0

        # =====================================================================
        # IMPORTANT : On crée d'abord TOUTES les structures de données
        # =====================================================================
        self.briques = []           # Crée la LISTE vide pour les briques
        self.pile_vies = []         # Crée la PILE vide pour les vies
        self.file_evenements = deque(maxlen=3) # Crée la FILE d'événements

        # 2. Zone d'affichage graphique (Le canevas)
        self.canvas = Canvas(self.window, width=480, height=300, background='black', highlightthickness=0)
        self.canvas.pack(side=TOP, fill=BOTH, expand=True)

        # 3. Création graphique et logique de la raquette et de la balle
        self.rect_id = self.canvas.create_rectangle(210, 280, 270, 300, fill='blue', outline='')
        self.ma_raquette = Raquette(self.canvas, self.rect_id)
        self.ma_balle = Balle(self.canvas, self.ma_raquette, self)

        # 4. Interface d'informations du bas (Frame)
        self.bas_frame = Frame(self.window, bg='black')
        self.bas_frame.pack(side=BOTTOM, fill=X, padx=10, pady=5)

        self.label_score = Label(self.bas_frame, text="Score: 0", font=("Courier", 10), bg='black', fg='yellow')
        self.label_score.pack(side=LEFT, padx=5)

        self.label_vies = Label(self.bas_frame, text="Vies: ", font=("Courier", 10), bg='black', fg='red')
        self.label_vies.pack(side=LEFT, padx=20)

        # 5. Nouveau panneau d'affichage épuré
        self.label_journal = Label(self.window,text="Points gagnés : 0", 
                                font=("Courier", 10, "bold"), bg='black', fg='lightgray')
        self.label_journal.pack(side=BOTTOM, fill=X, pady=5)

        # 6. Boutons interactifs
        self.btn_quitter = Button(self.bas_frame, text="Quitter", font=("Courier", 10), bg='red', fg='white', command=self.window.destroy)
        self.btn_quitter.pack(side=RIGHT, padx=5)

        self.btn_demarrer = Button(self.bas_frame, text="Démarrer", font=("Courier", 10), bg='green', fg='white', command=self.demarrer_jeu)
        self.btn_demarrer.pack(side=RIGHT, padx=5)

        # =====================================================================
        # APPELS DES FONCTIONS : Uniquement à la fin, une fois que tout existe !
        # =====================================================================
        self.creer_plusieurs_rangees_briques() # Remplit self.briques
        self.initialiser_pile_vies()           # Remplit self.pile_vies

        # Capture des entrées clavier
        self.window.bind("<Left>", self.ma_raquette.deplacer_gauche)
        self.window.bind("<Right>", self.ma_raquette.deplacer_droite)

        # Boucle d'écoute principale de Tkinter
        self.window.mainloop()


    def creer_plusieurs_rangees_briques(self):
        largeur_brique = 55
        hauteur_brique = 15
        espace = 5
        offset_x = 3
        offset_y = 20
        
        # Le dégradé à 3 couleurs 
        couleurs_rangees = ['yellow', 'green', 'red'] 

        for ligne, couleur in enumerate(couleurs_rangees):
            for col in range(8):
                x1 = offset_x + col * (largeur_brique + espace)
                y1 = offset_y + ligne * (hauteur_brique + espace)
                x2 = x1 + largeur_brique
                y2 = y1 + hauteur_brique
                
                id_brique = self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline='black')
                self.briques.append(id_brique)

    def initialiser_pile_vies(self):
        """Ajoute 3 éléments dans notre PILE."""
        for _ in range(3):
            self.pile_vies.append("♥") # On pousse (push) un coeur sur le dessus de la pile
        self.mettre_a_jour_affichage_vies()

    def mettre_a_jour_affichage_vies(self):
        # Transforme le tableau ['♥', '♥'] en texte lisible "Vies: ♥ ♥"
        self.label_vies.config(text="Vies: " + " ".join(self.pile_vies))

    def ajouter_evenement(self, message=None):
        # ATTENTION : Utilisez bien le tiret du bas du 8 (_) et AUCUN espace !
        briques_detruites = 24 - len(self.briques)
        vies_restantes = len(self.pile_vies)
        
        # Construction de la ligne de texte
        texte_statistiques = f"Points gagnés : {self.score}"
        self.label_journal.config(text=texte_statistiques)

    def perdre_une_vie(self):
        self.en_cours = False  # Coupe momentanément l'animation (pause)
        
        if len(self.pile_vies) > 0:
            # STRUCTURE PILE : On retire le dernier élément inséré (LIFO)
            self.pile_vies.pop() 
            self.mettre_a_jour_affichage_vies()
            self.ajouter_evenement("Vie perdue !")
            
            # S'il n'y a plus aucun coeur dans la PILE = Défaite totale
            if len(self.pile_vies) == 0:
                self.game_over()
            else:
                self.ma_balle.réinitialiser()
                self.ajouter_evenement("Appuyez sur Démarrer")

    def ajouter_points(self, points):
        self.score += points
        self.label_score.config(text=f"Score: {self.score}")

    def demarrer_jeu(self):
        # Bloque le bouton si le jeu tourne déjà ou si la partie est finie
        if not self.en_cours and len(self.pile_vies) > 0 and len(self.briques) > 0:
            self.en_cours = True
            self.ajouter_evenement("C'est parti !")
            self.animer_jeu()

    def animer_jeu(self):
        """Le moteur d'animation (S'exécute en boucle toutes les 15 millisecondes)."""
        if self.en_cours:
            self.ma_balle.deplacer()
            # Rappelle automatiquement cette fonction après 15ms
            self.window.after(15, self.animer_jeu)

    def game_over(self):
        self.en_cours = False
        self.canvas.create_text(240, 150, text="GAME OVER", fill="red", font=("Courier", 26, "bold"))
        self.ajouter_evenement("Défaite : Plus de vies !")

    def gagner_partie(self):
        self.en_cours = False
        self.canvas.create_text(240, 150, text="VICTOIRE !", fill="green", font=("Courier", 26, "bold"))
        self.ajouter_evenement("Victoire ! Bien joué !")

if __name__ == "__main__":
    jeu = CasseBrique()