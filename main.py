def has_numbers(input):
    """
    Check if input is on string format
    :param input:
    :return:
    """
    return any(char.isdigit() for char in input)


def check_count(players, position):
    """
    Check if player's position exists or not
    :param players:
    :param position:
    :return: boolean
    """
    count = 0
    for player in players:
        if player["poste"] == position:
            count += 1

    return (position == "G" and count == 1) or (position != "G" and count == 2)


def check_number_player(players, num):
    """
    Check if player's number exists or not
    :param players:
    :param num:
    :return: boolean
    """
    count = 0
    for player in players:
        if player["numero"] == num:
            count += 1

    return count == 1


def enter_player(players):
    """

    :param players:
    :return: array of player with player infos
    """
    positions = ["A", "D", "AD", "AG", "M", "G"]

    while len(players) < 22:
        try:
            num = int(input("Quel est le numéro du joueur ?; Le numero doit être entre 0 et 9 \n"))
        except ValueError:
            print("La donnée saisie n'est pas valide\n")
            continue
        if check_number_player(players, num):
            print("Un joueur possède déjà ce numero")
            continue

        firstname = input(
            f"Quel est le prénom du joueur numéro {num} ?; Le prénom doit être en caractère alphabetique \n")
        if has_numbers(firstname):
            print("La donnée saisie n'est pas valide\n")
            continue

        lastname = input(f"Quel est le nom du joueur numéro {num} ?; Le nom doit être en caractère alphabetique \n")
        if has_numbers(lastname):
            print("La donnée saisie n'est pas valide\n")
            continue

        print(f"Dans quel poste joue le joueur Numéro {num} ?")
        print(
            "A pour attaquant, D pour défenseur, AD pour aile droite et AG pour aile gauche M pour milieu et G pour "
            "gardien")
        position = input("\n")
        if position not in positions:
            print("La donnée saisie n'est pas valide")
            continue

        if check_count(players, position):
            print("Le nombre de place pour ce poste a atteint sa limite")
            continue

        player = {"numero": num, "prenom": firstname, "nom": lastname, "poste": position}
        players.append(player)


def player_team(players):
    """

    :param players:
    :return: array of players with player's team infos
    """
    teams = ["P", "R"]

    while True:
        for p in players:
            numero = p["numero"]
            prenom = p["prenom"]
            nom = p["nom"]
            print(f"Est ce que le joueur {numero}, {nom} {prenom} est principal ou remplaçant ?")
            print("L'utilisateur doit répondre P ou R")
            team = input()
            if team not in teams:
                print("La donnée saisie n'est pas valide")
                player_team(players)

            p["team"] = team

        break


if __name__ == '__main__':
    players = []

    print("********************Constitution de l'équipe********************")
    enter_player(players)

    print("********************Principal ou Remplaçant********************")
    player_team(players)

    team_p = []
    team_r = []
    for p in players:
        if p["team"] == "P":
            team_p.append(p)
        else:
            team_r.append(p)

    print("-------------------Equipe principale-------------------")
    print(team_p)

    print("-------------------Equipe remplaçante-------------------")
    print(team_r)
