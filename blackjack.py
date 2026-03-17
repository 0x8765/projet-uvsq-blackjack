import random


def creer_paquet():
    """
    Ne prend aucun paramètre
    Retourne un paquet de 52 cartes sous forme de liste de tuples
    """
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']

    paquet = [] 
    for couleur in couleurs: 
        for valeur in valeurs: 
            paquet.append((valeur, couleur)) 

    return paquet 


def melanger_paquet(paquet):
    """
    Prend en paramètre un paquet de cartes sous forme de liste de tuples
    Mélange la liste en place
    """
    random.shuffle(paquet)