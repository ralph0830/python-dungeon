import random as r

######Getting High Score#####

try:
    hs = open("highscore.txt","r+")
except:

    hs = open("highscore.txt","x")
    hs = open("highscore.txt","r+")

try:
    score = hs.readlines(1)
    score = int(score[0])

    leader = hs.readlines(2)
    leader = str(leader[0])
except:
    hs = open("highscore.txt","w")
    hs.write("0\n")
    hs.write("null")
    hs = open("highscore.txt","r")
    score = hs.readlines(1)
    score = int(score[0])
    leader = hs.readlines(2)
    leader = str(leader[0])

#####Introduction, Initializing player#####

print("\nWELCOME TO WONDERLANDS RPG!")
print("The High Score is:",score,"by",leader)
points = 0
player_name = input("\nEnter your hero's name: ")

#####Classes [health, attack 1 (only does set damage), attack 2 min, attack 2 max, attack 3 min, attack 3 max, heal min, heal max], Getting player's Class#####

knight = [100,10,5,15,0,25,5,10] #health: 100, attack 1: 10, attack 2: 5-15, attack 3: 5-25, heal: 5-10
mage = [50,15,10,20,-5,25,10,15] #health: 50, attack 1: 15, attack 2: 10-20, attack 3: -5-25, heal: 10-15
healer = [150,5,5,10,5,15,10,20] #health: 150, attack 1: 5, attack 2: 5-10, attack 3: 5-15, heal: 10-20

while True:
    print("\n1. Knight: Health: ",knight[0],"; Attack 1:",knight[1],"; Attack 2:",knight[2],"-",knight[3],"; Attack 3:",knight[4],"-",knight[5],"; Heal:",knight[6],"-",knight[7])
    print("2. Mage: Health: ",mage[0],"; Attack 1:",mage[1],"; Attack 2:",mage[2],"-",mage[3],"; Attack 3:",mage[4],"-",mage[5],"; Heal:",mage[6],"-",mage[7])
    print("3. Healer: Health: ",healer[0],"; Attack 1:",healer[1],"; Attack 2:",healer[2],"-",healer[3],"; Attack 3:",healer[4],"-",healer[5],"; Heal:",healer[6],"-",healer[7])
    player_class = input("\nSelect your class: 1, 2, or 3: ")
    if player_class == "1":
        player_class = knight
        print("You have selected the Knight")
        break
    if player_class == "2":
        player_class = mage
        print("You have selected the Mage")
        break
    if player_class == "3":
        player_class = healer
        print("You have selected the Healer")
        break
    else:
        print("Please select a valid class.")
        continue

player_heal_max = player_class[0]

#####Difficulty/Upgrade Functions#####

def level_up(player,health_max):
    while True:
        lv_choice = input("\nWould you like to:\n Increase max health by 20 (1)\n Increase Healing Factor by 5 (2)\n increase your damage by 5 (3) ")
        if lv_choice == "1":
            health_max += 20
            player[0] = health_max
            return player,health_max
        elif lv_choice == "2":
            player[6] +=5
            player[7] +=5
            player[0] = health_max
            return player, health_max
        elif lv_choice == "3":
            player[1] +=5
            player[2] +=5
            player[3] +=5
            player[4] +=5
            player[5] +=5
            player[0] = health_max
            return player, health_max
        else:
            print("Please enter in a valid number")
            continue

def difficulty(ai,health_max,level):
    if level == 1:
        return ai
    else:
        ai[0] = health_max+15*round(0.5*level+0.5)
        ai[1] +=5*round(0.5*level+0.5)
        ai[2] +=5*round(0.5*level+0.5)
        ai[3] +=5*round(0.5*level+0.5)
        ai[4] +=5*round(0.5*level+0.5)
        ai[5] +=5*round(0.5*level+0.5)
        ai[6] +=5*round(0.5*level+0.5)
        ai[7] +=5*round(0.5*level+0.5)
        return ai

def ai_stats(s):
    s[0] += r.randint(-20,20)
    s[1] += r.randint(-3,3)
    s[2] += r.randint(-3,3)
    s[3] += r.randint(-3,3)
    s[4] += r.randint(-3,3)
    s[5] += r.randint(-3,3)
    s[6] += r.randint(-3,3)
    s[7] += r.randint(-3,3)
    return s

#####Game Loop#####

level = 1
print("\n----------------------- GAME START -----------------------")

while True:
    #####Determining AI Class/Stats#####
    #####(AI classes must be in the Game loop otherwise if an enemy chooses the same class twice, it would have <=0 HP, thus being an instant win)#####
    ai_knight = [100,10,5,15,0,25,5,10] #health: 100, attack 1: 10, attack 2: 5-15, attack 3: 5-25, heal: 5-10
    ai_mage = [50,15,10,20,-5,25,10,15] #health: 50, attack 1: 15, attack 2: 10-20, attack 3: -5-25, heal: 10-15
    ai_healer = [150,5,5,10,5,15,10,20] #health: 150, attack 1: 5, attack 2: 5-10, attack 3: 5-15, heal: 10-20

    ai = r.randint(1,3)
    if ai == 1:
        ai = ai_stats(ai_knight)
        print("\nYou are fighiting a knight with",ai[0],"HP!")
    if ai == 2:
        ai = ai_stats(ai_mage)
        print("\nYou are fighiting a mage with",ai[0],"HP!")
    if ai == 3:
        ai = ai_stats(ai_healer)
        print("\nYou are fighiting a healer with",ai[0],"HP!")

    ai_heal_max = ai[0]
    ai = difficulty(ai,ai_heal_max,level)
    #####Gameplay Loop#####
    while True:
        #####Player Attack#####
        player_move = input("\nWould you like to use attack (1), attack (2), attack (3), or heal (4)? ")
        print("")
        if player_move == "1":
            player_damage = player_class[1]
            ai[0] = ai[0]- player_damage
            print(player_name," did",player_damage,"damage!")
        elif player_move == "2":
            player_damage = r.randint(player_class[2],player_class[3])
            ai[0] = ai[0]- player_damage
            print(player_name," did",player_damage,"damage!")
        elif player_move == "3":
            player_damage = r.randint(player_class[4],player_class[5])
            if player_damage<0:
                player_class[0] = player_class[0]+player_damage
                print(player_name," damaged themselves for",player_damage,"HP!")
            else:
                ai[0] = ai[0]- player_damage
                print(player_name," did",player_damage,"damage!")
        elif player_move == "4":
            player_heal = r.randint(player_class[6],player_class[7])
            if player_class[0] + player_heal > player_heal_max:
                player_class[0] = player_heal_max
            else:
                player_class[0] = player_class[0] + player_heal
            print(player_name," healed for",player_heal,"HP")
        else:
            print("Please enter in a valid move.")
            continue
        #####Detecting Death#####
        if player_class[0]<=0:
            break
        elif ai[0]<=0:
            points += player_class[0]*level
            level +=1
            print("You have bested your opponent! You Have",points,"points. \nNow starting level",level)
            player_class,player_heal_max = level_up(player_class,player_heal_max)
            break
        #####AI Turn#####
        if ai[0] <= (ai_heal_max/5):
            ai_move = r.sample(set([1,2,3,4,4,4]), 1)[0]
        elif ai[0] >= (ai_heal_max*.8):
            ai_move = r.sample(set([1,2,3,1,2,3,4]), 1)[0]
        elif ai[0] == ai_heal_max:
            ai_move = r.randint(1,3)
        else:
            ai_move = r.randint(1,4)

        if ai_move == 1:
            ai_damage = ai[1]
            player_class[0] = player_class[0]- ai_damage
            print("Your opponent did",ai_damage,"damage!")
        elif ai_move == 2:
            ai_damage = r.randint(ai[2],ai[3])
            player_class[0] = player_class[0]- ai_damage
            print("Your opponent did",ai_damage,"damage!")
        elif ai_move == 3:
            ai_damage = r.randint(ai[4],ai[5])
            if ai_damage<0:
                ai[0] = ai[0]+ai_damage
                print("Your opponent damaged themselves for",ai_damage,"HP!")
            else:
                player_class[0] = player_class[0]- ai_damage
                print("Your opponent did",ai_damage,"damage!")
        elif ai_move == 4:
            ai_heal = r.randint(ai[6],ai[7])
            if ai[0] + ai_heal > ai_heal_max:
                ai[0] = ai_heal_max
            else:
                ai[0] = ai[0] + ai_heal
            print("Your opponent healed for",ai_heal,"HP")
        #####Displaying HP#####   
        print("\nYour health is:",player_class[0],"HP")
        print("Your opponent's health is",ai[0],"HP")
        #####Detecting Loss#####
        if player_class[0]<=0:
            break
        elif ai[0]<=0:
            points += player_class[0]*level
            level +=1
            print("You have bested your opponent! You Have",points,"points. \nNow starting level",level)
            player_class,player_heal_max = level_up(player_class,player_heal_max)
            break
        else:
            continue
    #####Finishing Game, Checking/Updating High Score#####
    if player_class[0]<=0:
        print("\nYou Died! :(")
        if points>score:
            hs = open("highscore.txt","w")
            hs.write(str(points))
            hs.write("\n")
            print("You have the new high score of",points,"!")
            hs.write(player_name)
        else:
            print("\nYou finished with",points,"points.")
            print("The high score is:",score,"by",leader)
        input("")
        hs.close()
        break