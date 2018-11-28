import random
import json

# List of two and three letter syllables for use in generating a random name
syllables = ["en ", "da ", "fu ", "el ", "kar ", "tuk ", "ar ", "cha ", "ing ", "ant ", "low "]
# A list of all the different character types
charTypes = ["B", "E", "W", "D", "K"]


# Function for generating a random name using three syllables
def rndName():
    # Creating an empty string for use in the For Loop
    rndName = ""
    # For Loop that iterates 3 times to concatenate three of the syllables
    # together
    for x in range(3):
        # Using random.choice to pick a pseudorandom item from the syllables
        # list. It does this by concatenating the rndName to the new choice
        rndName = rndName + random.choice(syllables)
    # rndName is then returned
    return rndName


# Base Class for creating an RPG character
class character:
    # __init__ method, creates the name, type, health properties
    def __init__(self, charName, charType, charHealth):
        self.name = charName
        self.type = charType
        self.health = charHealth


class characterClass(character):
    # __init__ method for setting the object properties, both for the
    # characterClass obkect and character object
    def __init__(self, charName, charType, charHealth, charPower, charSAttackPwr, charSpeed):
        character.__init__(self, charName, charType, charHealth)
        self.power = charPower
        self.sAttackPwr = charSAttackPwr
        self.speed = charSpeed

    # Method for getting and returning all the stats of the character
    def getStats(self):
        # Creating a string to hold all the stats, using concatenation
        stats = "Name: %s, Type: %s, Health: %s, Power: %s, Special Attack Power: %s, Speed: %s" % (self.name, self.type, self.health, self.power, self.sAttackPwr, self.speed)
        # Returns stats to the the function that called
        return stats

    def setStats(self, statToChange, statVal):
        if statToChange == "N" or statToChange == "n":
            self.name = statVal
        elif statToChange == "T" or statToChange == "t":
            self.type = statVal
        elif statToChange == "H" or statToChange == "h":
            self.health = statVal
        elif statToChange == "P" or statToChange == "p":
            self.power = statVal
        elif statToChange == "SAP" or statToChange == "sap":
            self.sAttackPwr = statVal
        elif statToChange == "S" or statToChange == "s":
            self.speed = statVal


# A function to randomly generate characters, parsing
# a list of the classes
def generateCharacters(classes):
    # Randomly picks a class from the classes list
    choice = random.choice(classes)

    # An IF ELIF statement to choose which type of character to instantiate. A
    # "B" will instantiate an instance of the Barbarian object
    if choice == "B":
        # The new instance is then returned
        return characterClass(rndName(), "Barbarian", 100, 70, 20, 50)
    # If the choice selected is an instance of an Elf will be created
    elif choice == "E":
        return characterClass(rndName(), "Elf", 100, 30, 60, 10)
    # "W" will instantiate a Wizard
    elif choice == "W":
        return characterClass(rndName(), "Wizard", 100, 50, 70, 30)
    # If the choice is a "D" then a Dragon appears
    elif choice == "D":
        return characterClass(rndName(), "Dragon", 100, 90, 40, 50)
    # And finally, if a "K" is selected, then a Knight is created
    elif choice == "K":
        return characterClass(rndName(), "Knight", 100, 60, 10, 60)


# Menu function for allowing the user to save and edit the characters
def menu(gameChars):
    # Formatting and asking the user for an input
    print("")
    ans = input("Are you happy with this team? [y or n]: ")
    # IF statement using the ans variable to determine if the User is happy
    # with the randomly generated characters
    if ans == "Y" or ans == "y":
        # If the answer is "Y" or "y", then the User is asked if they want to
        # save the generated characters to a file for later
        if input("Would you like to save this team? [y or n]: ") == "y":
            saveCharsToFile(gameChars)
    elif ans == "N" or ans == "n":
        # If the answer is no, the User is then prompted for if they want to
        # add or remove a character from the list
        ans = input("Would you like to add [1], delete [2] a character or edit a character[3]?: ")
        # This then gets parsed, along with the gameChars list to the charEdit
        # function
        charEdit(ans, gameChars)


# Function for editing the character list, with ans, an answer variable, and
# the gameChars list of characters
def charEdit(ans, gameChars):
    # If the answer variable parsed to charEdit is equal to 1, then the User
    # wishs to add a character to the list
    if ans == "1":
        # We get the current length of the gameChars List
        leng = len(gameChars)
        # A second variable that takes the list length and adds 1  to it, so
        # that the new character is added to the end of the list
        lengList = leng + 1
        # Inserting a new, rnadomly generated number into the location
        # specified by the lengList variable
        gameChars.insert(lengList, generateCharacters(charTypes))
        # Telling the user where the new character is located
        print("A new character, number " + str(lengList))
        # And asking for a new user input, on whether this wish to just see the
        # new character, or the whole team again
        ans2 = input("Would you like to see your whole team[1] or just the new character[2]?: ")
        if ans2 == "1":
            # If they answer "1", the program prints out the whole team again
            # using a for loop, and calling the getStats method
            for x in gameChars:
                print(x.getStats())

            # Then calling the menu, parsing the character list
            menu(gameChars)

        elif ans2 == "2":
            # If the User answers "2", then we take the length of the gameChars
            # list, and subtract 1. This gives us the list location of the
            # character to show
            x = len(gameChars) - 1
            # Then we get the character (object) at position x,
            y = gameChars[x]
            # and print it out using the getStats method
            print(y.getStats())
            # Finally, we return to the menu, parsing the list of characters
            menu(gameChars)
    elif ans == "2":
        # If the User answers "2", then they wish to delete a character. The
        # print statement is used for formatting
        print("")
        # We then ask the User which character number they wish to delete
        ans = input("Please enter the number for the character you wish to delete: ")
        # And then we ask again, confirming they want to delete that Character
        ans3 = input("Are you sure you want to delete " + ans + "?[y or n]: ")
        if ans3 == "y" or ans3 == "Y":
            # If they answer "Y" or "y", then we use the del function to delete
            # the object at location ans in the gameChars list - 1
            del gameChars[int(ans) - 1]
            # The first print is for formatting
            print("")
            # Then we print out the character list again, using a for loop
            print("Here is the new character list: ")
            for x in gameChars:
                print(x.getStats())
            # And finally, we call the Menu back, to start from the top
            menu(gameChars)

    # If the User inputs "3", then they wish to edit a characters stats
    elif ans == "3":
        # A print for formatting, to skip a line
        print("")
        # Asking the User for the character number they wish to edit from them
        # gameChars list
        charAns = input("Please enter the number for the character you wish to edit: ")
        # Subtracting 1 from the uer input, because arrays start from 0
        charAns = int(charAns) - 1
        # We then get the User to tell us what stat they want to edit, using
        # a single, or short set of characters, instead of the full description
        editAns = input("Which Stat would you like to edit?[N, T, H, P, SAP, S]: ")
        # The User is then asked to enter what the new value of that new stat
        # should be
        changeToAns = input("What would you like to change the stat too?: ")
        # We fetch the character (object) that the User specified, and put it
        # into the variable y. This is only for convenience, so I didn't use
        # a proper name
        y = gameChars[int(charAns)]
        # Calling the setStats Method of the characterClass to change the stats
        # of the editAns variable to whatever is in changeToAns
        y.setStats(editAns, changeToAns)

        # Using a FOR loop to display the gameChars list
        for z in gameChars:
            # Printing the output of the getStats method
            print(z.getStats())
        # Calling the menu function, and parsing it the gameChars list
        menu(gameChars)


def saveCharsToFile(gameChars):
    # Using a WITH operator for easy readability. creating and opening a file
    # in write mode
    with open("characterFile.json", "w") as write_file:
        # using the json.dump function to take the objects in the gameChars
        # list and serialise it into JSON
        json.dump([x.__dict__ for x in gameChars], write_file, sort_keys=True, indent=4)
    # Tells the User that the file has been written
    print("File 'characterFile.json' has been written to...")
    # Calling the menu function with the game characters parsed to it
    menu(gameChars)


def openCharsToFile(gameChars):
    # Pretty formatting for telling the User we are loading a file
    print("Loading File...")
    # Using a WHILE loop to infintely check that the User has enetered a "1"
    # indicating that the file is in the correct place
    while True:
        # Using an input to Prompt the User to check that a file called
        # characterFile.json sits in the root directory of this program
        ans = input("Please ensure the file is called 'characterFile.json', then press [1]...")
        # If the User has entered "1", then use the WITH keyword to open the
        # JSON file "characterFile"
        if ans == "1":
            # Opening the file, referring to the created object as "read_file"
            with open("characterFile.json") as read_file:
                # Using the JSON module to load the contents of "read_file"
                # into the ImportedChars list
                ImportChars = json.load(read_file)
                # Using a FOR loop, we take the list-of-lists in ImportedChars
                for character in ImportChars:
                    # and insert them into the gameChars list using the append
                    # method to insert them at the newest index
                    gameChars.append(characterClass(character['name'], character['type'], character['health'], character['power'], character['sAttackPwr'], character['speed']))

            # We then print out the list of gameChars to the User
            for x in gameChars:
                # We use the character's getStats() method
                print(x.getStats())

            # Calling the menu fucntion, parsing it the gameChars list
            menu(gameChars)


def main():
    # An empty list, that will hold the randomly generated characters
    gameChars = []
    # Start of the menu system
    print("Welcome to the RPG Character Simulator")
    # Asking the User if they want to generate new characters or load them from
    # a file
    ans = input("Would you like to generate 10 random characters [1] or load them from a file[2]?: ")
    # If the User inputs "1", then they wish to generate 10 random characters
    if ans == "1":
        # For loop used to generate 10 random characters and insert them into
        # the gameChars list
        for x in range(10):
            # Generating a new instance of a randomly selected character from
            # the generateCharacters function, parsing a randomly selected type
            y = generateCharacters(charTypes)
            # Adding this newly generated character to gameChars, at position x
            gameChars.insert(x, y)
        # Showing the User their randomly generated characters
        print("Here is your randomly generated team: ")
        # For loop for showing the full list of characters
        for z in gameChars:
            print(z.getStats())
        # Calling the menu funtion, and parsing the list of characters in
        # gameChars
        menu(gameChars)
    # If the User enters a "2", then they wish to open characters from a file
    elif ans == "2":
        # Calling the openCharsToFile function, and parsing it the empty
        # gameChars list
        openCharsToFile(gameChars)


# Calling the main() function
main()
