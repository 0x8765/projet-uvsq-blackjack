####################
#
# Projet Info UVSQ
# Blackjack
# Victor, Maceo, Ayah, Sammuel
#
####################


import random
import tkinter as tk


def creer_paquet():
    """Cree et retourne un paquet de 52 cartes."""
    valeurs = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Valet",
        "Dame",
        "Roi",
        "As",
    ]
    couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]
    paquet = []
    for couleur in couleurs:
        for valeur in valeurs:
            paquet.append((valeur, couleur))
    return paquet


def melanger_paquet(paquet):
    """Melange le paquet dans un ordre aleatoire."""
    random.shuffle(paquet)


def tirer_carte(paquet):
    """Retire la derniere carte du paquet et la retourne."""
    return paquet.pop()


def valeur_carte(carte):
    """Retourne la valeur numerique d'une carte. Les figures valent 10, l'As vaut 11."""
    nom = carte[0]
    if nom in ["Valet", "Dame", "Roi"]:
        return 10
    elif nom == "As":
        return 11
    else:
        return int(nom)


def calculer_score(main):
    """Calcule et retourne le score total d'une main. Ajuste la valeur des As si on depasse 21."""
    score = 0
    nombre_as = 0
    for carte in main:
        score += valeur_carte(carte)
        if carte[0] == "As":
            nombre_as += 1
    while score > 21 and nombre_as > 0:
        score -= 10
        nombre_as -= 1
    return score


def est_blackjack(main):
    """Retourne True si la main est un Blackjack (2 cartes qui font 21)."""
    return len(main) == 2 and calculer_score(main) == 21


def determiner_message(main_joueur, main_croupier):
    """Compare les deux mains et retourne le message de resultat et sa couleur."""

    # recuperation des variables
    score_joueur = calculer_score(main_joueur)
    score_croupier = calculer_score(main_croupier)
    bj_joueur = est_blackjack(main_joueur)
    bj_croupier = est_blackjack(main_croupier)

    # renvoie du message en fonction du score
    if score_joueur > 21:
        return "Vous avez depasse 21 ! Le croupier gagne.", "red"
    if score_croupier > 21:
        return "Le croupier a depasse 21 ! Vous gagnez !", "green"
    if bj_joueur and bj_croupier:
        return "Egalite ! Les deux ont un Blackjack !", "orange"
    if bj_joueur:
        return "BLACKJACK ! Vous gagnez !", "green"
    if bj_croupier:
        return "Le croupier a un Blackjack. Vous perdez.", "red"
    if score_joueur > score_croupier:
        return f"Vous gagnez ! ({score_joueur} > {score_croupier})", "green"
    if score_croupier > score_joueur:
        return f"Le croupier gagne. ({score_croupier} > {score_joueur})", "red"
    return f"Egalite ! ({score_joueur} = {score_croupier})", "orange"


# variables globales de la partie
paquet = []
main_joueur = []
main_croupier = []
cadre_cartes_joueur = None
cadre_cartes_croupier = None
label_score_joueur = None
label_score_croupier = None
label_message = None
bouton_tirer = None
bouton_rester = None

# Symboles et couleurs pour chaque couleur de carte
SYMBOLES = {
    "Coeur": ("♥", "red"),
    "Carreau": ("♦", "red"),
    "Trefle": ("♣", "black"),
    "Pique": ("♠", "black"),
}


def creer_widget_carte(parent, carte):
    """Cree et retourne un widget carte (un Frame blanc avec valeur et symbole)."""
    valeur, couleur = carte
    symbole, couleur_texte = SYMBOLES[couleur]

    # Raccourcit les noms longs pour que la carte reste petite
    abreviations = {"Valet": "V", "Dame": "D", "Roi": "R", "As": "A"}
    valeur_affichee = abreviations.get(valeur, valeur)

    # creation d'un frame blanc qui sert de background pour la carte
    cadre = tk.Frame(parent, bg="white", relief="raised", bd=2, width=60, height=90)
    cadre.pack_propagate(False)  # garde la taille fixe

    # ajout de la valeur et couleur de la carte dans le cadre
    tk.Label(
        cadre,
        text=valeur_affichee,
        font=("Helvetica", 12, "bold"),
        fg=couleur_texte,
        bg="white",
        anchor="nw",
    ).pack(anchor="nw", padx=4, pady=2)

    tk.Label(
        cadre, text=symbole, font=("Helvetica", 22), fg=couleur_texte, bg="white"
    ).pack(expand=True)

    return cadre


def creer_widget_carte_cachee(parent):
    """Cree et retourne un widget pour la carte cachee du croupier (dos de carte)."""
    cadre = tk.Frame(parent, bg="#2244aa", relief="raised", bd=2, width=60, height=90)
    cadre.pack_propagate(False)

    tk.Label(
        cadre, text="?", font=("Helvetica", 30, "bold"), fg="white", bg="#2244aa"
    ).pack(expand=True)

    return cadre


def vider_cadre(cadre):
    """Supprime tous les widgets enfants d'un cadre."""
    for widget in cadre.winfo_children():
        widget.destroy()


def afficher_mains(cacher_deuxieme):
    """Vide et reconstruit les zones de cartes du joueur et du croupier."""
    # Cartes du joueur
    vider_cadre(cadre_cartes_joueur)
    for carte in main_joueur:
        widget = creer_widget_carte(cadre_cartes_joueur, carte)
        widget.pack(side="left", padx=4)
    label_score_joueur.config(text=f"Score : {calculer_score(main_joueur)}")

    # Cartes du croupier
    vider_cadre(cadre_cartes_croupier)
    for i, carte in enumerate(main_croupier):
        if cacher_deuxieme and i == 1:
            widget = creer_widget_carte_cachee(cadre_cartes_croupier)
        else:
            widget = creer_widget_carte(cadre_cartes_croupier, carte)
        widget.pack(side="left", padx=4)

    if cacher_deuxieme:
        label_score_croupier.config(text="Score : ?")
    else:
        label_score_croupier.config(text=f"Score : {calculer_score(main_croupier)}")


def desactiver_boutons():
    """Desactive les boutons Tirer et Rester en fin de partie."""
    bouton_tirer.config(state="disabled")
    bouton_rester.config(state="disabled")


def activer_boutons():
    """Reactive les boutons Tirer et Rester au debut d'une nouvelle partie."""
    bouton_tirer.config(state="normal")
    bouton_rester.config(state="normal")


def nouvelle_partie():
    """Reinitialise le jeu et distribue les cartes pour une nouvelle partie."""
    global paquet, main_joueur, main_croupier

    paquet = creer_paquet()
    melanger_paquet(paquet)
    main_joueur = []
    main_croupier = []

    # distribuer 2 cartes au joueur et au croupier
    for i in range(2):
        main_joueur.append(tirer_carte(paquet))
        main_croupier.append(tirer_carte(paquet))

    activer_boutons()
    afficher_mains(cacher_deuxieme=True)
    label_message.config(text="A vous de jouer !", fg="cyan")

    if est_blackjack(main_joueur) or est_blackjack(main_croupier):
        fin_de_partie()


def joueur_tire():
    """Le joueur tire une carte. Verifie s'il depasse 21 ou atteint exactement 21."""
    main_joueur.append(tirer_carte(paquet))
    afficher_mains(cacher_deuxieme=True)

    if calculer_score(main_joueur) > 21:
        afficher_mains(cacher_deuxieme=False)
        label_message.config(text="Vous avez depasse 21 ! Le croupier gagne.", fg="red")
        desactiver_boutons()
    elif calculer_score(main_joueur) == 21:
        joueur_reste()


def joueur_reste():
    """Le joueur reste : le croupier joue automatiquement jusqu'a 17, puis on determine le gagnant."""
    while calculer_score(main_croupier) < 17:
        main_croupier.append(tirer_carte(paquet))
    fin_de_partie()


def fin_de_partie():
    """Revele toutes les cartes et affiche le resultat de la partie."""
    afficher_mains(cacher_deuxieme=False)
    desactiver_boutons()
    message, couleur = determiner_message(main_joueur, main_croupier)
    label_message.config(text=message, fg=couleur)


def construire_fenetre(fenetre):
    """Cree tous les elements graphiques de la fenetre (labels, boutons, zones de cartes)."""
    global cadre_cartes_joueur, cadre_cartes_croupier
    global label_score_joueur, label_score_croupier
    global label_message, bouton_tirer, bouton_rester

    fenetre.title("Blackjack")
    fenetre.resizable(False, False)

    # label du titre
    tk.Label(
        fenetre, text="♠ ♥ BLACKJACK ♦ ♣", font=("Helvetica", 20, "bold"), pady=10
    ).pack()

    # Zone croupier
    tk.Label(fenetre, text="Croupier", font=("Helvetica", 13, "bold")).pack()
    cadre_cartes_croupier = tk.Frame(fenetre, height=100, pady=6)
    cadre_cartes_croupier.pack()
    label_score_croupier = tk.Label(fenetre, text="", font=("Helvetica", 11))
    label_score_croupier.pack(pady=(0, 10))

    # Zone joueur
    tk.Label(fenetre, text="Joueur", font=("Helvetica", 13, "bold")).pack()
    cadre_cartes_joueur = tk.Frame(fenetre, height=100, pady=6)
    cadre_cartes_joueur.pack()
    label_score_joueur = tk.Label(fenetre, text="", font=("Helvetica", 11))
    label_score_joueur.pack(pady=(0, 10))

    # Message de resultat
    label_message = tk.Label(fenetre, text="", font=("Helvetica", 12), pady=4)
    label_message.pack()

    # Boutons
    cadre_boutons = tk.Frame(fenetre)
    cadre_boutons.pack(pady=8)

    # lier les boutons avec les fonction du programme
    bouton_tirer = tk.Button(
        cadre_boutons,
        text="Tirer une carte",
        font=("Helvetica", 11),
        width=16,
        command=joueur_tire,
    )
    bouton_tirer.grid(row=0, column=0, padx=6)

    bouton_rester = tk.Button(
        cadre_boutons,
        text="Rester",
        font=("Helvetica", 11),
        width=16,
        command=joueur_reste,
    )
    bouton_rester.grid(row=0, column=1, padx=6)

    tk.Button(
        fenetre,
        text="Nouvelle partie",
        font=("Helvetica", 11),
        width=20,
        command=nouvelle_partie,
    ).pack(pady=(0, 12))


# lancement du programme
fenetre = tk.Tk()
construire_fenetre(fenetre)
nouvelle_partie()
fenetre.mainloop()
