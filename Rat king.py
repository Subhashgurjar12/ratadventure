import random
from random import randint
# +------------------------
# | Text for various menus
# +------------------------

main_text = ["New Game",\
             "Resume Game",\
#             "View Leaderboard",\
             "Exit Game"]
town_text = ["View Character",\
             "View Map",\
             "Move",\
             "Rest",\
             "Save Game",\
             "Exit Game"]
open_text = ["View Character",\
             "View Map",\
             "Move",\
             "Sense Orb",\
             "Exit Game"]
fight_text = ["Attack",\
              "Run"]
world_map = [['H/T', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', ' T ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', '   ', ' T ', '   ', '   '],
             ['   ', ' T ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', ' T ', '   ', '   ', '   '],
             ['   ', '   ', '   ', '   ', '   ', '   ', '   ', ' K ']]

pi=0
pj=0
hp=20
day=1
rhp=10
dmax=4
dmin=2
defence=1
orbi=7
orbj=0
orb=0
rmin=1
rmax=3
rdefence=1
kmin=8
kmax=12
kdefence=5
khp=25


def ttext(town_text):
    n = 0
    for t in town_text:
        n=n+1
        print(n,")",t)

#function for town i.e whenever the player enters the toen he will face the following options
def town():
    global hp
    global day
    print("Day",str(day)+": You are in a town.")
    print("1)",town_text[0])
    print("2)",town_text[1])
    print("3)",town_text[2])
    print("4)",town_text[3])
    print("5)",town_text[4])
    print("6)",town_text[5])
    choice=int(input("Enter choice: "))
    print("")
    if(choice==1):
        character()

    elif(choice==2):
        map()

    elif(choice==3):
        move()

    elif(choice==4):
        print("You are fully healed.")
        if hp<20:
            hp=20
        if(day>0):
                day=day+1

    #saving the game
    elif(choice==5):
        f= open("savefile.txt","w+")
        f.write(str(dmin))
        f.write("\n")
        f.write(str(dmax))
        f.write("\n")
        f.write(str(hp))
        f.write("\n")
        f.write(str(pi))
        f.write("\n")
        f.write(str(pj))
        f.write("\n")
        f.write(str(rhp))
        f.write("\n")
        f.write(str(day))
        f.write("\n")
        f.write(str(khp))
        f.write("\n")
        f.close()


    #exiting the game
    elif(choice==6):
        exit()
    #if the player chooses the invalid option
    else:
        print("Wrong button pressed,please try again")
    town()
        
            
        

#when the player wants to move from one place to another
def move():
    map()
    global day
    global pi
    global pj
    if(day>0):
        day=day+1


       
    print("W = up; A = left; S = down; D = right")
    choice=input("Enter choice: ")
    print("")

    #converting the input to uppercase
    choice=choice.upper()
    
    
    #if player chooses to play w
    if(choice=="W"):
        if(pi-1<0):
            print("Wrong button pressed,please try again")
            move()
        p_state=world_map[pi-1][pj]
        if(p_state==" T "):
            world_map[pi-1][pj]="H/T"
        elif(p_state=="   "):
            world_map[pi-1][pj]=" H "
        elif(p_state==" K "):
            world_map[pi-1][pj]="H/K"
        # loading the previous state in the map
        if(world_map[pi][pj]==" H "):
            world_map[pi][pj]="   "
        if(world_map[pi][pj]=="H/T"):
            world_map[pi][pj]=" T "
        pi=pi-1
        
    #if player chooses to play s    
    elif(choice=="S"):
        p_state=world_map[pi+1][pj]
        if(pi+1>7):
            print("Wrong button pressed,please try again")
            move()
        if(p_state==" T "):
            world_map[pi+1][pj]="H/T"
        elif(p_state=="   "):
            world_map[pi+1][pj]=" H "
        if(p_state==" K "):
            world_map[pi+1][pj]="H/K"
        # loading the previous state in the map
        if(world_map[pi][pj]==" H "):
            world_map[pi][pj]="   "
        if(world_map[pi][pj]=="H/T"):
            world_map[pi][pj]=" T "

        pi=pi+1

    #if player chooses to play a        
    elif(choice=="A"):
        p_state=world_map[pi][pj-1]
        if(pj-1 <0):
            print("Wrong button pressed,please try again")
            move()
        if(p_state==" T "):
            world_map[pi][pj-1]="H/T"
        elif(p_state=="   "):
            world_map[pi][pj-1]=" H "
        if(p_state==" K "):
            world_map[pi][pj-1]="H/K"
        # loading the previous state in the map
        if(world_map[pi][pj]==" H "):
            world_map[pi][pj]="   "
        if(world_map[pi][pj]=="H/T"):
            world_map[pi][pj]=" T "

        pj=pj-1

    #if player chooses to play d        
    elif(choice=="D"):
        p_state=world_map[pi][pj+1]
        if(pj+1>7):
            print("Wrong button pressed,please try again")
            move()
        if(p_state==" T "):
            world_map[pi][pj+1]="H/T"
        elif(p_state=="   "):
            world_map[pi][pj+1]=" H "
        elif(p_state==" K "):
            world_map[pi][pj+1]="H/K"
        # loading the previous state in the map
        if(world_map[pi][pj]==" H "):
            world_map[pi][pj]="   "
        if(world_map[pi][pj]=="H/T"):
            world_map[pi][pj]=" T "

        pj=pj+1

    else:
        print("Wrong button pressed,please try again")
        move()

    map()

    #when the player comes to the location where the orb is kept
    if(pi==orbi and pj==orbj):
        senseorb()
    if rhp>0:
        if(world_map[pi][pj]==" H "):
            combat()
    if(world_map[pi][pj]=="H/K"):
        ratking()
    if(world_map[pi][pj]=="H/T"):
        town()
    
    outside()    
        


def combat():
    global rhp
    print("Day "+str(day)+": You are out in the open.")
    ratencounter()

#whenever the rat attacks he will have the following options    
def ratencounter():
    print("Encounter! - Rat")
    print("  Damage: "+str(rmin)+"-"+str(rmax))
    print(" Defence: "+str(rdefence))
    print("HP:",rhp)
    print("1) Attack")
    print("2) Run")
    choice=int(input("Enter Choice: "))
    print("")
    if(choice==1):
        attack()
    elif(choice==2):
        run()
    else:
        print("Wrong button pressed,please try again")
        ratencounter()

#when player chooses to attack the rat        
def attack():
    global rhp
    global hp
    r1 = random.randint(dmin,dmax)
    r2 = random.randint(rmin,rmax)
    r1=r1-rdefence
    r2=r2-defence

    print("You deal "+str(r1)+" damage to the Rat")
    if(r1>0):
        rhp=rhp-r1
        if(rhp<=0):
            outside()
    if(rhp>0):       
        print("Ouch! The Rat hit you for "+str(r2)+" damage!")
        if(r2>0):
            hp=hp-r2
            if(hp<=0):
                killed()
                
        print("You have "+str(hp)+" left.")
        ratencounter()

#when coward player chooses to run from his enemy or rat
def run():
    global rhp
    if(rhp<10):
        rhp=10
    print("You run and hide.")
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Sense Orb")
    print("5) Exit Game")
    choice=int(input("Enter Choice: "))
    print("")
    if(choice==1):
        combat()
    elif(choice==2):
        combat()
    elif(choice==3):
        move()
    elif(choice==4):
        combat()
    elif(choice==5):
        exit()
    else:
        print("Wrong button pressed,please try again")
        run()

#when the player gets killed 
def killed():
    print("killed")
    print(hp)
    exit()
    

#when the players has killed or either has outrun the enemy
def outside():
    print("The Rat is dead! You are victorious!")
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Sense Orb")
    print("5) Exit Game")
    choice=int(input("Enter Choice: "))
    print("")

    if(choice==1):
        character()
    elif(choice==2):
        map()
    elif(choice==3):
        move()
    elif(choice==4):
        senseorb()
    elif(choice==5):
        exit()
    else:
        print("Wrong button pressed,please try again")
    outside()
    


#when the player chooses to sense the orb this function guides him to move towards it by giving its direction
def senseorb():
    global orb
    global day
    global defence
    global dmax
    global dmin
    global hp

    if(day>1):
        day=day+1
    if(pi==orbi and pj>orbj):
        print("You sense that the Orb of Power is to the west.")
    elif(pi==orbi and pj<orbj):
        print("You sense that the Orb of Power is to the east.")
    elif(pi>orbi and pj==orbj):
        print("You sense that the Orb of Power is to the north.")
    elif(pi<orbi and pj==orbj):
        print("You sense that the Orb of Power is to the south.")
    elif(pi<orbi and pj<orbj):
        print("You sense that the Orb of Power is to the southeast.")
    elif(pi>orbi and pj>orbj):
        print("You sense that the Orb of Power is to the northwest.")
    elif(pi<orbi and pj>orbj):
        print("You sense that the Orb of Power is to the southwest.")
    elif(pi>orbi and pj<orbj):
        print("You sense that the Orb of Power is to the northeast.")
    if(pi==orbi and pj==orbj):
        print("You found the Orb of Power!")
        print("Your attack increases by 5!")
        print("Your defence increases by 5!")
        if(defence<6):
            defence=6
        if(dmin<7):
            dmin=7
        if(dmax<9):
            dmax=9
        if(hp<25):
            hp=hp+5
        if(orb<1):
            orb=1
    print("Day "+str(day)+": You are out in the open.")
    print("1) View Character")
    print("2) View Map")
    print("3) Move")
    print("4) Sense Orb")
    print("5) Exit Game")
    choice=int(input("Enter Choice: "))
    print("")
    
    if(choice==1):
        character()
    elif(choice==2):
        map()
    elif(choice==3):
        move()
    elif(choice==4):
        senseorb()
    elif(choice==5):
        exit()
    else:
        print("Wrong button pressed,please try again")
        senseorb()

        
#when player encounters the king
def ratking():
    print("Day "+str(day)+": You see the Rat King!")
    print("Encounter! - Rat King")
    print("Damage: 8-12")
    print("Defence:  5")
    print("HP: "+str(khp))
    print("1) Attack")
    print("2) Run")
    choice=int(input("Enter Choice: "))
    print("")
    if(choice==1):
        kattack()
    elif(choice==2):
        krun()
    else:
        print("Wrong button pressed,please try again")
        ratking()

#when there is a fight between the kingrat and our player       
def kattack():
    r1 = random.randint(dmin,dmax)
    r2 = random.randint(kmin,kmax)
    r1=r1-kdefence
    r2=r2-defence
    global khp
    global hp
    print("You deal "+str(r1)+" damage to the Rat King")
    if(r1>0):
        khp=khp-r1
        if(khp<=0):
            win()
    if(r2>0):
        hp=hp-r2
        if(hp<=0):
            killed()
    print("Ouch! The Rat King hit you for "+str(r2)+" damage!")
    print("You have "+str(hp)+" left.")
    if(khp>0):
        kingencounter()

    

#when our player has finally won
def win():
    print("The Rat King is dead! You are victorious!")
    print("Congratulations, you have defeated the Rat King!")
    print("The world is saved! You win!")
    exit()

#whenever the player encounters the kingrat
def kingencounter():
    print("Encounter! - Rat King")
    print("Damage: 8-12")
    print("Defence:  5")
    print("HP: "+str(khp))
    print("1) Attack")
    print("2) Run")
    choice=int(input("Enter Choice: "))
    print("")
    if(choice==1 and orb==1):
        kattack()
    elif(choice==1 and orb==0):
        nattack()
    elif(choice==2):
        krun()
    else:
        print("Wrong button pressed,please try again")
        kingencounter()

#when the player dont have have orb but still chooses to attack the king        
def nattack():
    global hp
    print("You do not have the Orb of Power - the Rat King is immune!")
    print("You deal 0 damage to the Rat King")
    r2 = random.randint(kmin,kmax)
    r2=r2-defence
    print("Ouch! The Rat King hit you for "+str(r2)+" damage!")
    if(hp>0):
        hp=hp-r2
        if(hp<=0):
            killed()
    print("You have "+str(hp)+" HP left.")
    kingencounter()

#when the player wants to check on himself,his strength,hp etc
def character():
    print("The Hero")
    print("  Damage: "+str(dmin)+"-"+str(dmax))
    print(" Defence: "+str(defence))
    print("      HP:",hp)

    if(orb==1):
        print("You are holding the Orb of Power.")
    
#when the player chooses to see the map
def map():
    a="";
    for i in range (0,8):
        print("+---+---+---+---+---+---+---+---+")
        a=""
        for j in range (0,8):            
            a=a+"|"+world_map[i][j]
        print(a+"|")
    print("+---+---+---+---+---+---+---+---+")

    

    
#game welcoming the player        
print("Welcome to Ratventure!")
print("----------------------")


#the first menu
def first():
    print("1)",main_text[0],"\n2)",main_text[1],"\n3)",main_text[2])

    choice=int(input("Enter choice: "))
    print("")
    if choice==1 :
        town()
    elif choice==2 :
        f=open("savegame.txt", "r")
        if f.mode == 'r':
            contents =f.read()
            dmin=contents
            contents =f.read()
            dmax=contents
            contents =f.read()
            hp=contents
            contents =f.read()
            pi=contents
            contents =f.read()
            pj=contents
            contents=f.read
            rhp=contents
            contents=f.read
            day=f.read
            contents=f.read
            khp=f.read
            
        world_map[0][0]=" T "
        p_state=world_map[pi][pj]
        
        if(p_state==" T "):
            world_map[pi][pj]="H/T"
            town()
    elif(choice==3):
        exit()
    else:
        print("Wrong button pressed,please try again")




    
#menu
print("1)",main_text[0],"\n2)",main_text[1],"\n3)",main_text[2])

choice=int(input("Enter choice: "))
print("")
if choice==1 :
    town()
elif choice==2 :
    f=open("savefile.txt", "r")
    
    contents =f.readlines()
    dmin=contents[0]
    dmax=contents[1]
    hp=contents[2]
    pi=contents[3]
    pj=contents[4]
    rhp=contents[5]
    day=contents[6]
    khp=contents[7]



elif(choice==3):
    exit()
else:
    print("Wrong button pressed,please try again")
    first()
pi=int(pi)
pj=int(pj)
world_map[0][0]=" T "
world_map[pi][pj]="H/T"
town()

