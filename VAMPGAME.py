
def print_intro():
    print("Welcome to the VampireSpawn")
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

##STATS
def show_stats(players):
    print("\n ========== \nPlayer Status \n ----------")
    for key, p in players.items():
        print(f"{p["Name"]} | HP: {p['hp']} | Energy: {p['energy']}")
        print(" ==========")
        


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
    if choice == "A":
        if attacker["energy"] >= 6:
            attacker["energy"] -= 6
            defender["hp"] -= 10
            print(f" {attacker['Name']} use Dagger Slash!!")
        else: 
            print("Not enough Energy..")
    
    elif choice == "B":
        if attacker["energy"] >= 25:
            attacker["energy"] -= 25
            defender["hp"] -= 40
            print(f"{attacker['Name']} use Vampiric Claws!")
        else:
            print("Not enough energy...")
    
    elif choice == "C":
        if attacker["energy"] >= 10:
            attacker["energy"] -= 10
            attacker["dodge"] = True
            print(f"{attacker['Name']} The player temporarily morphs into a bat! dodges any attacks from the opponents in the current round!")
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
    



##Round_Rest

 #-- Flow of the game --
print_intro()
players = create_players()

print(f"\n Let The duel between {players['Player1']['Name']} and {players['Player2']['Name']} begins!")
show_stats(players)

show_skills()

p1_choice = input(f"{players['Player1']['Name']}, choose your skills: ")
p2_choice = input(f"{players['Player2']['Name']}, choose your skills: ")


use_skill(players["Player1"], players["Player2"], p1_choice)
use_skill(players["Player2"], players["Player1"], p2_choice)

show_stats(players)

