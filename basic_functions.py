#Each basic keyword function for the dungeon crawler game
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




def combat(monster, inventory, previous_position, position):
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
                    position = previous_position
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
        previous_position = 12

    new_values = [position, monster, previous_position]

    return new_values
                  

    