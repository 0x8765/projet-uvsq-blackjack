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

def tirer_carte(paquet):
    """
    Prend en paramètre une liste de tuple
    Renvoie le dernier tuple de la liste et le supprime
    """
    return paquet.pop()

def valeur_carte(carte):
    """
    Prend en paramètre un tuple qui correspond a une carte
    Renvoie la valeur de la carte sous forme d'entier
    """
    nom = carte[0] 

    if nom in ['Valet', 'Dame', 'Roi']: 
        return 10
    elif nom == 'As': 
        return 11  
    else:
        return int(nom)
