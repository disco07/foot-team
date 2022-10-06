def has_numbers(input):
    return any(char.isdigit() for char in input)


def checkCount(players, position):
    count = 0
    for player in players:
        if player["poste"] == position:
            count += 1

    if position == "G" and count == 1:
        return True
    elif position != "G" and count == 2:
        return True
    else:
        return False


def enter_player(players):
    positions = ["A", "D", "AD", "AG", "M", "G"]

    while len(players) < 2:
        try:
            num = int(input("Quel est le numéro du joueur ?; Le numero doit être entre 0 et 9 \n"))
        except ValueError:
            print("La donnée saisie n'est pas valide\n")
            continue

        firstname = input(
            f"Quel est le prénom du joueur numéro {num} ?; Le prénom doit être en caractère alphabetique \n")
        if has_numbers(firstname) == True:
            print("La donnée saisie n'est pas valide\n")
            continue

        lastname = input(f"Quel est le nom du joueur numéro {num} ?; Le nom doit être en caractère alphabetique \n")
        if has_numbers(lastname) == True:
            print("La donnée saisie n'est pas valide\n")
            continue

        print(f"Dans quel poste joue le joueur Numéro {num} ?")
        print(
            "A pour attaquant, D pour défenseur, AD pour aile droite et AG pour aile gauche M pour milieu et G pour gardien")
        position = input("\n")
        if position not in positions:
            print("La donnée saisie n'est pas valide")
            continue

        if checkCount(players, position) == True:
            print("Le nombre de place pour ce poste a atteint sa limite")
            continue

        player = {"numero": num, "prenom": firstname, "nom": lastname, "poste": position}
        players.append(player)


def player_team(players):
    teams = ["P", "R"]
    check = True
    while check:
        for p in players:
            numero = p["numero"]
            prenom = p["prenom"]
            nom = p["nom"]
            print(f"Est ce que le joueur {numero}, {nom} {prenom} est principal ou remplaçant ?")
            print("L'utilisateur doit répondre P ou R")
            team = input()
            if team not in teams:
                print("La donnée saisie n'est pas valide")
                player_team()

            p["team"] = team

        break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    players = []

    enter_player(players)
    player_team(players)

    team_p = []
    team_r = []
    for p in players:
        if p["team"] == "P":
            team_p.append(p)
        else:
            team_r.append(p)

    print("------Equipe principale------")
    print(team_p)
    print("------Equipe remplaçante------")
    print(team_r)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
