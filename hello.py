class Magasin:
    def __init__(self):
        # Dictionnaire : { "nom_produit": quantité }
        self.stock = {}

    def ajouter(self, produit, quantite):
        """Ajouter une quantité de produit au stock."""
        if produit in self.stock:
            self.stock[produit] += quantite
        else:
            self.stock[produit] = quantite
        print(f"{quantite} ajouté(s) à {produit}. Stock actuel : {self.stock[produit]}")

    def retirer(self, produit, quantite):
        """Retirer une quantité du stock."""
        if produit not in self.stock:
            print(f"Erreur : {produit} n'existe pas dans le stock.")
            return
        
        if quantite > self.stock[produit]:
            print(f"Erreur : stock insuffisant pour {produit}.")
            return

        self.stock[produit] -= quantite
        print(f"{quantite} retiré(s) de {produit}. Stock actuel : {self.stock[produit]}")

    def afficher_stock(self):
        """Afficher tous les produits et leurs quantités."""
        if not self.stock:
            print("Le stock est vide.")
        else:
            print("\n--- STOCK DU MAGASIN ---")
            for produit, quantite in self.stock.items():
                print(f"{produit} : {quantite}")
            print("------------------------\n")


# Exemple d'utilisation :
mag = Magasin()

mag.ajouter("Riz", 50)
mag.ajouter("Sucre", 30)
mag.retirer("Riz", 10)
mag.afficher_stock()

