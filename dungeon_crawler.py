"""
Basic game loop:
    Enter room
    If monster fight it
    Loot the room 
    Choose a direction to go 
    Leave room    
"""
import csv
import sys

def move(position, direction):
    #Takes the player's current y position (y value) and moves them the direction they specify
    #Paremeters: y position and direction the player wants to go 
    #Returns the new position

    position_curr = position
    direction = direction.lower()

    if direction == "north":

        position = position_curr + 4

    elif direction == "south":

        position = position_curr - 4

    elif direction == "east":

        position = position_curr + 1
    
    elif direction == "west":

        position = position_curr - 1

    return position

def directions(position, doors):
    #Depending on the position the function will return a list with the direction the player can go 
    north = doors["North"]
    east = doors["East"]
    south = doors["South"]
    west = doors["West"]

    options = []
    
    if position in north:
        options.append("NORTH")
    if position in east:
        options.append("EAST")
    if position in south:
        options.append("SOUTH")
    if position in west:
        options.append("WEST")

    return options

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    #creates an empty dictionary
    dictionary = {}

    #opens the csv file in reading mode and gives it the name students
    with open(filename, "rt") as rooms:

        #reads the csv file 
        reader = csv.reader(rooms)

        #skips the first line of the text file 
        next(reader)

        for row_list in reader:

            if len(row_list) != 0:

                key = row_list[key_column_index]

                dictionary[key] = row_list

    #returns the dictionary with all the values from the csv file 
    return dictionary       


doors = {
    "North" : [10, 11, 3, 8, 5, 4, 1],
    "East" : [13, 6, 14, 7, 9, 10, 11, 3, 1, 2],
    "South" : [14, 7, 9, 12, 15, 8, 5],
    "West" : [14, 7, 12, 15, 10, 11, 3, 8, 4, 2]
}
items_spec = {1:"Short Sword", 
              15:"Great Sword", 
              11:"Potion", 
              6:"Flute", 
              4:"Book", 
              13:"Key"}

# End point: 16 (entrance 12)
# Key: 13 
#Start point: 1
rooms = {}
rooms = read_dictionary("rooms.csv", 0)
ROOM_NUM = 0
ROOM_NAME = 1
ROOM_DESC = 2
ROOM_DOORS = 3 #For refrence
MONST_CODE = 4
LOOT = 5
LOOT_TYPE = 6

new_desc = "You have defeated the goblin in this room. Aside from its body, nothing else of interest is in here."
boss_battle = "The ogre lies defeated on the floor. Hopefully now you can escape this place."



def main():
    print()
    print("Your Adventure Begins")
    print()
    print("You have found yourself in the sealed dungeon of an excentric king")
    print("You need to find your way out of the dungeon")
    position = 1
    prev_pos = 0
    gold = 0
    inventory = [f"Gold: {gold}"]

    while position != 16:
        #Prints room name and description (makes dictionary)
        #Prompts player to loot move or attack if there is a monster
        room = rooms[str(position)]

        name = room[ROOM_NAME]
        description = room[ROOM_DESC]
        monster = int(room[MONST_CODE])
        loot = int(room[LOOT])
        type = room[LOOT_TYPE]

        position_curr = position
        action = "Nothing"

        print()
        print(name)
        print(description)

        while monster != 0:
            run = False
            while monster != 0 and run == False:
                if monster == 1:
                    print("The goblin stands before you")
                    print("To get through this room you must ATTACK")
                    action = input("What would you like to do? ")
                    if "Short Sword" in inventory:
                        
                        if action.upper() == "ATTACK" and monster == 1:
                            print()
                            print("You easily defeat the goblin")
                            monster = 0
                            print()
                            print("Now that you have defeated the monster")
                        else: 
                            print()
                    else:
                        print("Without a weapon you are deafeated by the goblin")
                        print("Game Over")
                        sys.exit()
                if monster == 2:
                    print()
                    print("The ogre towers above you")
                    print("The door behind him has to be the exit")
                    print("To get through this room you must ATTACK")
                    print("However without the Great Sword or Flute you will be defeated")
                    while monster == 2 and run == False:
                        action = input("What would you like to do? (ATTACK or RUN): ")
                        print()
                    
                        if action.upper() == "RUN":
                            
                            print("You run away")
                            print("Luckily the ogre chose not to follow you")
                            print()
                            position = prev_pos
                            run = True
                        elif action.upper() == "ATTACK":
                            print("You have chosen to attack the ogre")
                            print("Hopefully you are prepared")
                            if "Great Sword" in inventory:
                                print("After a long fight the ogre finally falls")
                                print("You have defeated the ogre")
                                monster = 0
                            elif "Flute" in inventory:
                                print("The music coming from the flute puts the ogre to sleep")
                                print("You take the opportunity to slay the beast")
                                print("You have defeated the ogre")
                                print()
                                monster = 0
                            else:
                                print("You have attempted to fight the ogre unprepared")
                                print("You are defeated by the ogre")
                                print()
                                print("Game Over")
                                sys.exit()
                        else:
                            print("Please input a valid action")
                if run == True:
                    monster = 0
                    prev_pos = 12
                pos_mon = [position, monster, prev_pos]
                monster = pos_mon[1]            
                position = pos_mon[0]
                prev_pos = pos_mon[2]
                if position != 12 and prev_pos != 12:
                    room[ROOM_DESC] = new_desc
                    room[MONST_CODE] = pos_mon[1]
                elif position == 12:
                    room[MONST_CODE] = pos_mon[1]
                    room[ROOM_DESC] = boss_battle

        while position_curr == position:
            if position == 12:
                print()
                print("You have reached the final room of the dungeon")
                print("If you have the key you will be able to escape")
                print("You can MOVE, LOOT, or ESCAPE")
            else:
                print()
                print("You can MOVE, LOOT, or INVENTORY") #, or USE ITEM
            action = input("What would you like to do: ")
            if action.upper() == "LOOT":
                if loot == 1:
                    print()
                    print("You find five gold pieces")
                    gold = gold + 5
                    inventory[0] = f"Gold: {gold}"
                    print(inventory) 
                    loot = 0
                    room[LOOT] = 0
                elif loot == 2:
                    
                    item = items_spec[position]
                    if item not in inventory:
                        inventory.append(item)
                    else:
                        print()
                        print("No loot in this room. Time to move on")
                    print(inventory)
                    loot = 0
                    room[LOOT] = 0
                else:
                    print()
                    print("No loot in this room. Time to move on")
            #elif action.upper() == "USE ITEM":
            #    print("This is a work in progress feature.")
            #    print("Please pick another option.")
            #    print(inventory)
            #    item = input("Which item would you like to use: ")
            #WIP concept
            elif action.upper() == "MOVE":
                options = directions(position, doors)
                print()
                print(f"You can move {options}")
                direc = input("Which way would you like to go: ")
                if direc.upper() in options:
                    prev_pos = position
                    position = move(position, direc)
                    print()
                    print("You leave the room.")
                else:
                    print()
                    print("Please pick a valid direction.")
            elif action.upper() == "INVENTORY":
                print(inventory)
            elif action.upper() == "ESCAPE" and position == 12:
                if "Key" in inventory:
                    print()
                    print("The key easily slides into the lock and turns with a satisfying click")
                    print("The door opens and you climb the stairs that lead to your freedom")
                    position = 16
                else:
                    print()
                    print("You attempt to open the door but it does not budge")                
            elif action.upper() == "ROOM": #option for testing purposes only 
                print(position)
            elif action.upper() == "KILL":
                print("Goodbye")
                sys.exit()
            else:
                print("Please input a valid action.")

    print()
    print("Congratulations!")
    print('You have escaped the dungeon.')




if __name__ == "__main__":
    main()


    