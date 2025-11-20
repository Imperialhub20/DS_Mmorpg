
def print_intro():
    print("\nWelcome to the VampireSpawn")
    print("Fight for the right to ascend into vampire Lord")
    print("Use your vampiric moves to outsmart your opponent.\n")
    print("Players, enter your names...\n")

##PLAYERS
def create_players():
    
    name1 = input("Enter Player1 username: ")
    name2 = input("Enter Player2 username: ")
    
    players = {


##PLAYER1
        "Player1": {
        "Name" : name1,
        "hp": 100,
        "energy" : 50,
        "dodge" : False
        },
        
       
##PLAYER2
        "Player2": {
        "Name" : name2,
        "hp": 100,
        "energy" : 50,
        "dodge" : False
       
    }
}
    return players

##Night round
def start_night(night_number):
    print("\n === Night" + str(night_number) + " ===" )
    

##STATS
def show_stats(players):
    print("\n ========== \nPlayer Status \n ----------")
    for key, p in players.items():
        print(f"{p["Name"]} | HP: {p['hp']} | Energy: {p['energy']}")
        print(" ==========")
        
##valid skill
def get_valid_skill(player_name):
    valid_choices = ["A", "B", "C", "D", "E"]

    while True:
        choice = input(f"{player_name}, choose your skill (A-E): ")

        if choice in valid_choices:
            return choice
        else:
            print("Invalid input. Please use CAPITAL letters A, B, C, D, or E only.\n")

##SKILLS
def show_skills():
    print("\nAvailable moves: ")
    print("A. Dagger Slash (10 dmaage; -6 energy)")
    print("B. Vampiric Claws (40 damage; -25 energy)")
    print("C. Dodge: Bat Form (nullifies incoming attack; -10 energy)")
    print("D. Drain Life (Deals 6 damage then heals self by 10; -13 energy)")
    print("E. Do Nothing (-0 energy)\n")


##PLAYERMOVE
def use_skill(attacker, defender, choice):

    attacker["dodge"] = False

    if choice == "A":
        if attacker["energy"] >= 6:
            attacker["energy"] -= 6
            defender["hp"] -= 10
            print(f"{attacker['Name']} use Dagger Slash!! (-6 Energy)")
        else: 
            print("Not enough Energy..")
    
    elif choice == "B":
        if attacker["energy"] >= 25:
            attacker["energy"] -= 25
            defender["hp"] -= 40
            print(f"{attacker['Name']} use Vampiric Claws! (-25 Energy)")
        else:
            print("Not enough energy...")
    
    elif choice == "C":
        if attacker["energy"] >= 10:
            attacker["energy"] -= 10
            attacker["dodge"] = True
            print(f"{attacker['Name']} The player temporarily morphs into a bat! (-10 Energy)")
        else:
            print(f"{attacker['Name']} Not enough energy...")
    
    elif choice == "D":
        if attacker["energy"] >= 13:
            attacker["energy"] -= 13
            attacker["hp"] += 10
            if not defender["dodge"]:
                defender["hp"] -= 6
            print(f"{attacker['Name']} used Drain life! (gain 10hp, -6 to opponent)")
        else:
            print(f"{attacker['Name']} Not enough energy...")

    elif choice == "E":
        print(f"{attacker['Name']} used Do nothing!")
    else:
        print("He done nothing...")

def rest_third_round(players):
    if players["energy"] == 0:
        print(f"{players['Name']} had a **Partial Rest** (+20HP, +13Energy).")
        players['hp'] += 20
        players['energy'] += 13
    else:
        print(f"{players['Name']} had a **Full rest** (+25HP, +20Energy).")
        players['hp'] += 25
        players['energy'] += 20



 #flow of the game

 ##Introduction
 
while True:  #Play again loop

    print_intro()
    players = create_players()

    night_number = 1

    print(f"\nLet the duel between {players['Player1']['Name']} and {players['Player2']['Name']} begin!")

    #MAIN BATTLE LOOP
    while players["Player1"]["hp"] > 0 and players["Player2"]["hp"] > 0:

        print(f"\n === Night {night_number} ===")
        show_stats(players)
        show_skills()

        #Players choose moves
        p1_choice = get_valid_skill(players["Player1"]["Name"])
        p2_choice = get_valid_skill(players["Player2"]["Name"])

        #Execute moves
        use_skill(players["Player1"], players["Player2"], p1_choice)
        use_skill(players["Player2"], players["Player1"], p2_choice)

        #Check defeat
        if players["Player1"]["hp"] <= 0 or players["Player2"]["hp"] <= 0:
            break

        #Every 3rd round = Rest (after battle)
        if night_number % 3 == 0:
            print("\n === After a long battle, both Vampires rest in their coffins... ===\n")
            rest_third_round(players["Player1"])
            rest_third_round(players["Player2"])
            print()

        night_number += 1

    #END GAME RESULTS
    if players["Player1"]["hp"] <= 0 and players["Player2"]["hp"] <= 0:
        print("Both players have fallen... It's a draw!")
    elif players["Player1"]["hp"] <= 0:
        print(f"{players['Player2']['Name']} has ascended as the new Vampire Lord!")
    else:
        print(f"{players['Player1']['Name']} has ascended as the new Vampire Lord!")

    #PLAY AGAIN
    play_again = input("\nWould you like to play again? (Y/N): ").upper()
    if play_again != "Y":
        print("Farewell... until the next blood moon.")
        break

