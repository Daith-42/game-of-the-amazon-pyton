# ──────── ✦ Game of the Amazons ✦ ────────

> Game of the Amazons en python

Projet en bînome réalisé dans le cadre de la première année à SUPINFO - Python uniquement.

✦ ━━━━━━━━━━━━━━━ ✦ ━━━━━━━━━━━━━━━ ✦

## À propos du projet
Le projet consiste à développer en Python un jeu de réflexion et de logique créé par Walter Zamkauskas, également connu sous le nom de "Game of the Amazons". Il s'agit d'un jeu de stratégie à deux joueurs où chacun doit bloquer les mouvements de l'adversaire en déplaçant ses pions et en tirant des flèches.

## Règles du jeu
> Lien des règles du jeu: https://en.wikipedia.org/wiki/Game_of_the_Amazons

### Objectifs pédagogiques
- Concevoir un jeu simple en Python avec TKinter
- Optimiser la qualité et la clarté du code

✦ ━━━━━━━━━━━━━━━ ✦ ━━━━━━━━━━━━━━━ ✦

## Cahier des charges

### Modalités de Réalisation
- Travail en **binôme**
- Soutenance orale
- Interdiction stricte d'utiliser des IA génératives

## Règles du jeu

### Principe de base
- Deux joueurs s'affrontent sur un plateau carré de taille n × n (généralement 6, 8 ou 10). Le joueur 1 dispose de pions rouges, le joueur 2 de pions bleus.

### Déroulement d'un Tour
Chaque joueur effectue successivement:
- Sélection
- Déplacement
- Tir de flèche (condamner une case en tirant une flèche depuis la position d'arrivée)

### Contraintes de Déplacement
- Seules les cases vides peuvent être traversées
- Impossible de sauter par-dessus un autre pion
- Impossible de sauter par-dessus une case bloquée par une flèche
- Pas de capture ni d'empilement de pions *(sauf variante "killer")*
- Les flèches suivent les mêmes règles de trajectoire que les pions

### Condition de Victoire
- Un joueur perd lorsque tous ses pions sont bloqués et qu'aucun déplacement n'est possible.

## Spécifications techniques
- Language: Python
- Interface graphique: Tkinter
- Programation orientée objet

## Architecture logicielle obligatoire

### Classe "algorithmes"
- Gestion de la structure de données du plateau
- Initialisation du plateau selon la configuration
- Validation de la sélection d'un pion
- Validation du déplacement d'un pion
- Validation du tir d'une flèche
- Mise à jour du plateau après chaque action
- Aucun élément graphique dans cette classe

### Classe "jeu"
- Gestion complète de l'interface graphique
- Déclaration et positionnement des widgets
- Affichage des messages et fenêtres
- Contient une instance de la classe "algorithmes"
- Aucune logique dans cette classe

## Organisation des fichiers
- Un fichier .py par classe
- Au minimum 2 fichiers de configuration supplémentaires avec des tailles différentes

✦ ━━━━━━━━━━━━━━━ ✦ ━━━━━━━━━━━━━━━ ✦

## Bonus réalisés
- Prévisualisation des coups
- Page laucher
- Themes de couleurs
- Images en tant que pions et flèches
- Sauvegarde des parties
- Taille des cases choisissable
- Choix du nom du joueur
- Possibilité de jouer contre l'ordinateur

✦ ━━━━━━━━━━━━━━━ ✦ ━━━━━━━━━━━━━━━ ✦

## Contributeurs
- **David Ameline** [![GitHub](https://img.shields.io/badge/GitHub-Daith--42-181717?style=flat&logo=github)](https://github.com/Daith-42)
- **Antonin MAUGIN** [![GitHub](https://img.shields.io/badge/GitHub-Antoo42-181717?style=flat&logo=github)](https://github.com/Antoo42)

# ──────── ✦ Game of the Amazons ✦ ────────
