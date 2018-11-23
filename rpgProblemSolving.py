import random

# List of two and three letter syllables for use in generating a random name
syllables = ["en ", "da ", "fu ", "el ", "kar ", "tuk ", "ar ", "cha ", "ing ", "ant ", "low "]
# A list of all the different character types
charTypes = ["B", "E", "W", "D", "K"]
# list that will hold all the instances of the character objects
generatedChars = []


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
    def __init__(self, charType, charHealth):
        self.name = rndName()
        self.type = charType
        self.health = charHealth


# A subclass for creating a Barbarian character, inherits the Character class
# and adds the power, sAttackPwr, and speed properties
class barbarian(character):
    def __init__(self, charPower, charSAttackPwr, charSpeed):
        # Getting the properties from the inheritted character Base Class
        character.__init__(self, "B", 100)
        self.power = charPower
        self.sAttackPwr = charSAttackPwr
        self.speed = charSpeed

    # Method for getting and returning all the stats of the character
    def getStats(self):
        # Creating a string to hold all the stats, using concatenation
        stats = "Name: %s, Type: %s, Health: %s, Power: %s, Special Attack Power: %s, Speed: %s" % (self.name, self.type, self.health, self.power, self.sAttackPwr, self.speed)
        # Returns stats to the the function that called
        return stats


# A subclass for creating a Elf character, inherits the Character class
# and adds the power, sAttackPwr, and speed properties
class elf(character):
    def __init__(self, charPower, charSAttackPwr, charSpeed):
        # Getting the properties from the inheritted character Base Class
        character.__init__(self, "E", 100)
        self.power = charPower
        self.sAttackPwr = charSAttackPwr
        self.speed = charSpeed

    # Method for getting and returning all the stats of the character
    def getStats(self):
        # Creating a string to hold all the stats, using concatenation
        stats = "Name: %s, Type: %s, Health: %s, Power: %s, Special Attack Power: %s, Speed: %s" % (self.name, self.type, self.health, self.power, self.sAttackPwr, self.speed)
        # Returns stats to the the function that called
        return stats


# A subclass for creating a Wizard character, inherits the Character class
# and adds the power, sAttackPwr, and speed properties
class wizard(character):
    def __init__(self, CharPower, CharSAttackPwr, CharSpeed):
        # Getting the properties from the inheritted character Base Class
        character.__init__(self, "W", 100)
        self.power = CharPower
        self.sAttackPwr = CharSAttackPwr
        self.speed = CharSpeed

    # Method for getting and returning all the stats of the character
    def getStats(self):
        # Creating a string to hold all the stats, using concatenation
        stats = "Name: %s, Type: %s, Health: %s, Power: %s, Special Attack Power: %s, Speed: %s" % (self.name, self.type, self.health, self.power, self.sAttackPwr, self.speed)
        # Returns stats to the the function that called
        return stats


# A subclass for creating a Dragon character, inherits the Character class
# and adds the power, sAttackPwr, and speed properties
class dragon(character):
    def __init__(self, CharPower, CharSAttackPwr, CharSpeed):
        # Getting the properties from the inheritted character Base Class
        character.__init__(self, "D", 100)
        self.power = CharPower
        self.sAttackPwr = CharSAttackPwr
        self.speed = CharSpeed

    # Method for getting and returning all the stats of the character
    def getStats(self):
        # Creating a string to hold all the stats, using concatenation
        stats = "Name: %s, Type: %s, Health: %s, Power: %s, Special Attack Power: %s, Speed: %s" % (self.name, self.type, self.health, self.power, self.sAttackPwr, self.speed)
        # Returns stats to the the function that called
        return stats


# A subclass for creating a Knight character, inherits the Character class
# and adds the power, sAttackPwr, and speed properties
class knight(character):
    def __init__(self, CharPower, CharSAttackPwr, CharSpeed):
        # Getting the properties from the inheritted character Base Class
        character.__init__(self, "B", 100)
        self.power = CharPower
        self.sAttackPwr = CharSAttackPwr
        self.speed = CharSpeed

    # Method for getting and returning all the stats of the character
    def getStats(self):
        # Creating a string to hold all the stats, using concatenation
        stats = "Name: %s, Type: %s, Health: %s, Power: %s, Special Attack Power: %s, Speed: %s" % (self.name, self.type, self.health, self.power, self.sAttackPwr, self.speed)
        # Returns stats to the the function that called
        return stats


# A function to randomly generate characters, parsing
# a list of the classes
def generateCharacters(classes):
    # Randomly picks a class from the classes list
    choice = random.choice(classes)

    # An IF ELIF statement to choose which type of character to instantiate. A
    # "B" will instantiate an instance of the Barbarian object
    if choice == "B":
        # The new instance is then returned
        return barbarian(70, 20, 50)
    # If the choice selected is an instance of an Elf will be created
    elif choice == "E":
        return elf(30, 60, 10)
    # "W" will instantiate a Wizard
    elif choice == "W":
        return wizard(50, 70, 30)
    # If the choice is a "D" then a Dragon appears
    elif choice == "D":
        return dragon(90, 40, 50)
    # And finally, if a "K" is selected, then a Knight is created
    elif choice == "K":
        return knight(60, 10, 60)


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
        if input("Would you like to save this team? [y or n]: "):
            print("nlergh")
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
        charAns -= 1
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
        # An IF ELIF statement to check which state was needing to change. If
        # the User entered "N", then they wanted to change the Name
        if editAns == "N":
            # The object in y has it's name property changed to whatever the
            # User specified in changeToAns
            y.Name = int(changeToAns)
        # If the User entered a "T", then they wanted to change the character
        # type
        elif editAns == "T":
            # The object in y has it's type property change to the value of
            # changeToAns
            y.type = int(changeToAns)
        # Same again with "H", except this is for health
        elif editAns == "H":
            # The property health has it's value changed to changeToAns
            y.health = int(changeToAns)
        # If the User enters "P", they want the power changed
        elif editAns == "P":
            # y has it's power property changed to changeToAns
            y.Power = int(changeToAns)
        # If the User enters SAP, then the stat to change is the Special Attack
        # Power property
        elif editAns == "SAP":
            # The sAttackPwr property of y is changed to changeToAns
            y.sAttackPwr = int(changeToAns)
        # If the input is "S", the User wants to change the Speed
        elif editAns == "S":
            # The speed property of y is then changed to the value in changeToAns
            y.Speed = int(changeToAns)

        # Finally, we print out a statement showing the User what has happened
        print("%s changed to %s" % (editAns, changeToAns))
        # Then we call the Menu again, and see what the User wants to do next
        menu(gameChars)


def saveCharsToFile():
    


def main():
    # An empty list, that will hold the randomly generated characters
    gameChars = []

    # For loop used to generate 10 random characters and insert them into
    # the gameChars list
    for x in range(10):
        # Generating a new instance of a randomly selected character from
        # the generateCharacters function, parsing a randomly selected type
        y = generateCharacters(charTypes)
        # Adding this newly generated character to gameChars, at position x
        gameChars.insert(x, y)

    # Start of the menu system
    print("Welcome to the RPG Character Simulator")
    print("Here is your randomly generated team: ")
    # For loop for showing the full list of characters
    for z in gameChars:
        print(z.getStats())
    # Calling the menu funtion, and parsing the list of characters in gameChars
    menu(gameChars)


# Calling the main() function
main()
