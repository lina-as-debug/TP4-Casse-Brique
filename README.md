# TP4-Casse-Brique

Jeu Casse-Brique
1. Présentation du projet

Ce projet consiste à réaliser un jeu Casse-Brique en langage Python, en utilisant la programmation orientée objet et la bibliothèque Tkinter pour l'interface graphique.

Le but du jeu est de détruire toutes les briques à l'aide d'une balle et d'une raquette, sans perdre ses trois vies.

2. Règles du jeu
Utiliser les flèches gauche et droite pour déplacer la raquette.
Appuyer sur le bouton « Démarrer » pour lancer la balle.
La balle rebondit sur les murs et sur la raquette.
Chaque brique détruite rapporte 2 points.
Le joueur dispose de 3 vies.
Si les 3 vies sont perdues, la partie est terminée (Game Over).
Si toutes les briques sont détruites, le joueur gagne la partie.
3. Programmation orientée objet

Le jeu est organisé autour de trois classes principales :

Raquette : gère les déplacements de la raquette.
Balle : gère les déplacements de la balle et les collisions.
CasseBrique : gère le jeu, les briques, les vies et le score.
4. Structures de données utilisées

Liste :

Fichier : projetrenouveler.py
Variable : self.briques
Rôle : stocker les identifiants des briques présentes dans le jeu. Une brique est retirée de la liste lorsqu'elle est détruite.

Pile :

Fichier : projetrenouveler.py
Variable : self.pile_vies
Rôle : stocker les trois vies du joueur. Une vie est retirée avec la méthode pop() lorsqu'elle est perdue (principe LIFO).

File :

Fichier : projetrenouveler.py
Variable : self.file_evenements
Rôle : stocker les derniers événements du jeu avec une capacité maximale de trois éléments (structure FIFO).

5. Tests
Le fichier test_casse_brique.py contient les tests unitaires réalisés avec le module unittest.

Les tests vérifient notamment :

La création des briques.
L'ajout des points.
L'affichage des points gagnés.
L'initialisation des vies.
Pour lancer les tests :python -m unittest test_casse_brique.py -v

7. Dépôt GitHub
Adresse du répertoire Git :https://github.com/lina-as-debug/TP4-Casse-Brique.git