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

    # boucle qui parcours les couleurs et pour chaque couleur attribut les 13 types de cartes
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


def texte_main(main, cacher_deuxieme=False):
    """Retourne le texte a afficher pour une main. Peut cacher la 2eme carte (pour le croupier)."""
    lignes = []
    for i, carte in enumerate(main):
        if cacher_deuxieme and i == 1:
            lignes.append("  [Carte cachee]")
        else:
            lignes.append(f"  {carte[0]} de {carte[1]}")
    if not cacher_deuxieme:
        lignes.append(f"  Score : {calculer_score(main)}")
    return "\n".join(lignes)


def determiner_message(main_joueur, main_croupier):
    """Compare les deux mains et retourne le message de resultat et sa couleur."""
    score_joueur = calculer_score(main_joueur)
    score_croupier = calculer_score(main_croupier)
    bj_joueur = est_blackjack(main_joueur)
    bj_croupier = est_blackjack(main_croupier)

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


# variables qui vont etres utilisées pour le jeu, a declarer ici pour le contexte

paquet = []
main_joueur = []
main_croupier = []

label_joueur = None
label_croupier = None
label_message = None
bouton_tirer = None
bouton_rester = None


def afficher_mains(cacher_deuxieme):
    """Met a jour les labels des mains dans la fenetre."""
    label_joueur.config(text=texte_main(main_joueur))
    label_croupier.config(text=texte_main(main_croupier, cacher_deuxieme))


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
    """Cree tous les elements graphiques de la fenetre (labels, boutons)."""
    global label_joueur, label_croupier, label_message, bouton_tirer, bouton_rester

    fenetre.title("Blackjack")
    fenetre.resizable(False, False)

    tk.Label(fenetre, text="BLACKJACK", font=("Helvetica", 20, "bold"), pady=10).pack()

    tk.Label(fenetre, text="Croupier", font=("Helvetica", 13, "bold")).pack()
    label_croupier = tk.Label(
        fenetre,
        text="",
        font=("Courier", 11),
        justify="left",
        width=35,
        anchor="w",
        relief="groove",
        padx=8,
        pady=6,
    )
    label_croupier.pack(padx=20, pady=4)

    tk.Label(fenetre, text="Joueur", font=("Helvetica", 13, "bold")).pack()
    label_joueur = tk.Label(
        fenetre,
        text="",
        font=("Courier", 11),
        justify="left",
        width=35,
        anchor="w",
        relief="groove",
        padx=8,
        pady=6,
    )
    label_joueur.pack(padx=20, pady=4)

    label_message = tk.Label(fenetre, text="", font=("Helvetica", 12), pady=6)
    label_message.pack()

    cadre_boutons = tk.Frame(fenetre)
    cadre_boutons.pack(pady=8)

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


fenetre = tk.Tk()
construire_fenetre(fenetre)
nouvelle_partie()
fenetre.mainloop()
