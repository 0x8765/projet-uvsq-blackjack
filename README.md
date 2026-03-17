# Projet Informatique UVSQ - Blackjack

## Description

Blackjack est un jeu de cartes qui consiste à atteindre le score le plus proche de 21 sans dépasser.
Le joueur affronte le croupier.

## Installation

Aucun module n'est nécessaire pour ce projet.
Veuillez néanmoins avoir Python 3.10 ou supérieur installé sur votre ordinateur et créer un environnement virtuel.

### Linux/MacOS

```bash
python3 -m venv venv

source venv/bin/activate

python3 blackjack.py
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate

python blackjack.py
```

## Règles du jeu

- Le joueur et le croupier reçoivent deux cartes au début du jeu, une carte du croupier est cachée au joueur.
- Le joueur peut choisir de tirer une carte supplémentaire ou de rester.
- Le croupier doit rester si son score est supérieur ou égal à 17.
- Le joueur gagne si son score est supérieur au score du croupier et inférieur ou égal à 21.
- Le croupier gagne si son score est supérieur au score du joueur et inférieur ou égal à 21.
- Si le joueur ou le croupier dépasse 21, il perd.

### Fait par

**Victor Lepin**
**Maceo Teboul**
**Ayah Moursi**
**Samuel ?**