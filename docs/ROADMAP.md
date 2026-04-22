# Roadmap & Améliorations Futures

Ce document liste les 5 améliorations validées à implémenter pour améliorer l'expérience utilisateur sans ajouter de complexité.

## 1. Remplissage automatique via l'ISBN
- **Page :** `02_Ajouter_livre.py`
- **Objectif :** Permettre à l'utilisateur de scanner ou taper un code-barre (ISBN). L'application appellera une API (ex: Google Books) pour préremplir le titre, l'auteur, le résumé et l'URL de la couverture.
- **Bénéfice :** Gain de temps massif lors de l'inventaire.

## 2. Dashboard d'Accueil Visuel
- **Page :** `Accueil.py`
- **Objectif :** Ajouter des indicateurs clés (métriques Streamlit) générés automatiquement.
  - Nombre total de livres.
  - Livres actuellement disponibles.
  - Livres en retard (avec une liste rapide).
- **Bénéfice :** Vue globale instantanée de la santé de la bibliothèque.

## 3. Code Couleur Dynamique pour les Retours
- **Page :** `05_Historique.py` et `06_Gerer_Livres.py`
- **Objectif :** Colorer les dates de retour selon l'urgence :
  - **Vert** : Rendu à temps ou reste > 7 jours.
  - **Orange** : Reste < 3 jours.
  - **Rouge** : En retard.
- **Bénéfice :** L'œil repère immédiatement les actions urgentes.

## 4. Bouton "Relancer les retardataires" en 1 Clic
- **Page :** `Accueil.py` ou `06_Gerer_Livres.py`
- **Objectif :** Un bouton manuel déclenchant la logique de `notifications.py` pour envoyer des emails à tous les retardataires actuels.
- **Bénéfice :** L'admin contrôle l'envoi d'emails sans aucune friction.

## 5. Filtres Rapides sur le Catalogue
- **Page :** `01_Catalogue.py`
- **Objectif :** Remplacer ou compléter la recherche par des boutons de filtres rapides : *Tous*, *Disponibles*, *Empruntés*.
- **Bénéfice :** Évite de chercher un livre pour découvrir ensuite qu'il n'est pas là.
