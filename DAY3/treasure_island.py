# MINI PROJECT 3
# To build a "Chose your own adventure game"




print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

frst = input('You are at the cross roads. Which way do you go? "Left" or "Right"? ')
if frst == 'Left' or frst == 'left':
    lfrst = input("Do you want to walk forward or wait at your position now? Type your choice 'walk' or 'wait' ")
    if lfrst == 'walk' or lfrst == 'Walk':
        print("Game Over")
    elif lfrst == 'wait' or lfrst == 'Wait':
        lsec = input('You have a Cycle and a Surf Board in front of you to cross the ocean. Which one do you choose "Surfboard" or "Cycle"')
        if lsec == 'Cycle' or lsec == 'cycle':
            print("Game Over")
        elif lsec == 'Surfboard' or 'surfboard':
            print("You Win")
        else:
            print("Wrong Input. Check Again")
    else:
        print("Wrong Input. Check Again")
elif frst == 'right' or frst == 'Right':
    rfrst = input('Ocean Ahead!! You want to swim your way out or wait. Type either "swim" or "wait". ')
    if rfrst == 'Swim' or rfrst == 'swim':
        print("Game Over")
    elif rfrst == 'wait' or rfrst == 'Wait':
        rsec = input('A boat arrives. But there is a plank in front of you as well. You want to ride a "boat" or use "plank" as a surfboard?  ')
        if rsec == 'Plank' or rsec == 'plank':
            print("Game Over")
        elif rsec == 'Boat' or rsec == 'boat':
            print("You Win")
        else:
            print("Wrong Input. Check Again")
    else:
        print("Wrong Input. Check Again!")
else:
    print("Wrong Input. Check Again!")


