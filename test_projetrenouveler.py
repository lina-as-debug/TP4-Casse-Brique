
import unittest
from casse_brique import CasseBrique


# ============================================================
# CLASSE POUR SIMULER LES ELEMENTS GRAPHIQUES
# ============================================================

class FauxLabel:

    def __init__(self):
        self.texte = ""

    def config(self, **kwargs):
        self.texte = kwargs.get("text", self.texte)


class FauxCanvas:

    def __init__(self):
        self.compteur = 0

    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        self.compteur += 1
        return self.compteur


# ============================================================
# TESTS DU JEU CASSE-BRIQUE
# ============================================================

class TestCasseBrique(unittest.TestCase):

    def setUp(self):
        # Création d'un objet sans ouvrir la fenêtre graphique
        self.jeu = CasseBrique.__new__(CasseBrique)

        self.jeu.score = 0
        self.jeu.briques = []
        self.jeu.pile_vies = []

        self.jeu.label_score = FauxLabel()
        self.jeu.label_vies = FauxLabel()
        self.jeu.label_journal = FauxLabel()

    # ========================================================
    # TEST 1 : CREATION DES BRIQUES
    # ========================================================

    def test_creation_briques(self):

        self.jeu.canvas = FauxCanvas()

        self.jeu.creer_plusieurs_rangees_briques()

        # Vérifie que 24 briques ont été créées
        self.assertEqual(len(self.jeu.briques), 24)

    # ========================================================
    # TEST 2 : AJOUT DES POINTS
    # ========================================================

    def test_ajouter_points(self):

        self.jeu.ajouter_points(2)

        # Vérifie que le score augmente de 2
        self.assertEqual(self.jeu.score, 2)

        # Vérifie l'affichage du score
        self.assertEqual(self.jeu.label_score.texte, "Score: 2")

    # ========================================================
    # TEST 3 : AFFICHAGE DES POINTS GAGNES
    # ========================================================

    def test_affichage_points_gagnes(self):

        self.jeu.score = 10
        self.jeu.ajouter_evenement()

        # Vérifie que seuls les points sont affichés
        self.assertEqual(
            self.jeu.label_journal.texte,
            "Points gagnés : 10"
        )

    # ========================================================
    # TEST 4 : INITIALISATION DES VIES
    # ========================================================

    def test_initialisation_vies(self):

        self.jeu.initialiser_pile_vies()

        # Vérifie que le joueur possède 3 vies
        self.assertEqual(len(self.jeu.pile_vies), 3)

        # Vérifie l'affichage des trois coeurs
        self.assertEqual(
            self.jeu.label_vies.texte,
            "Vies: ♥ ♥ ♥"
        )


# ============================================================
# EXECUTION DES TESTS
# ============================================================

if __name__ == "__main__":
    unittest.main()
