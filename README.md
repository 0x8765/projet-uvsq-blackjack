# Projet Informatique UVSQ - Blackjack

## Description

Blackjack est un jeu de cartes qui consiste à atteindre le score le plus proche de 21 sans le dépasser.
Le joueur affronte le croupier.

## Installation

Aucun module ne doit être installé pour lancer ce projet.
Veuillez néanmoins avoir Python 3.10 ou supérieur installé sur votre ordinateur et créer un environnement virtuel.

### Linux/MacOS

```bash
python3 -m venv venv

source venv/bin/activate

python3 blackjack_ui.py
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate

python blackjack_ui.py
```

## Règles du jeu

- Le joueur et le croupier reçoivent deux cartes au début du jeu, une carte du croupier est cachée au joueur.
- Le joueur peut choisir de tirer une carte supplémentaire ou de rester.
- Le croupier doit rester si son score est supérieur ou égal à 17.
- Le joueur gagne si son score est supérieur au score du croupier et inférieur ou égal à 21.
- Le croupier gagne si son score est supérieur au score du joueur et inférieur ou égal à 21.
- Si le joueur ou le croupier dépasse 21, il perd.

## Logique de développement

Nous avons choisi de tout programmer dans des fonctions, ce qui améliore la détection des erreurs et simplifie la répartition du travail.
On a commencé par programmer une version sans l'interface utilisateur pour d'abord comprendre et savoir reproduire la logique du jeu en Python, une fois cela fait nous avons commencé à programmer l'UI qui est une grosse partie du code.
Notre programme utilise seulement les modules random, pour l'aléatoire, et tkinter pour l'interface utilisateur.

Sources utilisées lors du développement :
- [Documentation tkinter](https://docs.python.org/fr/3/library/tkinter.html)
- [Documentation Python](https://docs.python.org/3/)

### Fait par

**Victor Lepin**, 
**Maceo Teboul**, 
**Ayah Moursi**, 
**Samuel ?**, 
