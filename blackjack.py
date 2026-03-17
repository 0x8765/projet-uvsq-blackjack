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


def calculer_score(main):
    """
    Prend en paramètre une liste de tuple qui correspond a une main
    Renvoie le score de la main sous forme d'entier
    """
    score = 0 
    nombre_as = 0  

    for carte in main: 
        score += valeur_carte(carte) 
        if carte[0] == 'As': 
            nombre_as += 1 
    
    while score > 21 and nombre_as > 0: 
        score -= 10       
        nombre_as -= 1   

    return score 


def est_blackjack(main):
    """
    Prend en paramètre une liste de tuple qui correspond a une main
    Renvoie True si la main est un blackjack, False sinon
    """
    blackjack = False 

    if len(main) == 2 and calculer_score(main) == 21: 
        blackjack = True 
    
    return blackjack 


def afficher_carte(carte):
    """
    Prend en paramètre un tuple qui correspond a une carte
    Renvoie une chaine de caractere qui correspond a la carte et a son score
    """
    return f"{carte[0]} de {carte[1]}"


def afficher_main(main, cacher_deuxieme=False):
    print("\n--- Main du joueur ---")

    for i, carte in enumerate(main): 
        if cacher_deuxieme and i == 1: 
            print("  [Carte cachée]") 
        else:
            print(f"  {afficher_carte(carte)}") 

    if not cacher_deuxieme: 
        score = calculer_score(main) 
        print(f"  → Score : {score}") 

def distribuer_cartes_initiales(paquet):
    main_joueur = [] 
    main_croupier = [] 

    for i in range(2): 
        main_joueur.append(tirer_carte(paquet)) 
        main_croupier.append(tirer_carte(paquet)) 

    return main_joueur, main_croupier 

def tour_joueur(main_joueur, paquet):
    while True:
        score = calculer_score(main_joueur)

        if score >= 21:
            break

        print("\nQue voulez-vous faire ?")
        print("  [T] Tirer une carte")
        print("  [R] Rester")

        choix = input("Votre choix : ")

        if choix == 'T': 
            nouvelle_carte = tirer_carte(paquet) 
            main_joueur.append(nouvelle_carte) 
            print(f"\n  Vous tirez : {afficher_carte(nouvelle_carte)}") 
            afficher_main(main_joueur, "Joueur") 
        elif choix == 'R': 
            print("\nVous décidez de rester.") 
            break 
        else:
            print("Choix invalide. Tapez 'T' pour tirer ou 'R' pour rester.")

    a_saute = calculer_score(main_joueur) > 21 
    if a_saute: 
        print("\n💥 Vous avez dépassé 21 ! Vous avez sauté !") 

    return a_saute 