#Import Dependencies
from tracemalloc import start
import menus
import creds
import re
from getpass import getpass

#Implements a guild member
class guildMember:

    def __init__(self, charName, classType, mainhandAP, awakeningAP, defensePower, rank):
        self.name = charName
        self.classtype = classType
        self.mainhandAP = mainhandAP
        self.awakeningAP = awakeningAP
        self.defensePower = defensePower

    def activate(self):
        #database gets self.name()
        pass
    
    def deactivate(self):
        #removes themselves from the db
        pass
    def banned(self):
        #adds guild member to ban list
        pass

    

#Handles all validation requirements for actions
class validation:
    def __init__(self):
        pass
    
    def emailCreateValidation(input):
        """
        emailCreateValidation function works by checking if first what is passed is an email such that it contains an chars + @ + chars + . + chars.
        If it does, then it will check to see if the email exists already in the databases or not, and return True/False accordingly.
        """
        # Got regex code from here: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.fullmatch(regex,input):
            if creds.userInfo.find_one({"Email": input}):
                print("ERROR: Email already exists!\n")
                return False
            else:
                return True
        else:
            print("Error: Not an email!\n")
            return False
    
    def userValidation(user, password):
        """
        Takes user email + password, verifies if they are correct, returns data accordingly.
        Else returns false, using this separate method so that should someone put in false information, they are not notified what is false (safety reasons).
        """
        if creds.userInfo.find_one({"Email": user, "Password": password}): 
            infoDict = creds.userInfo.find_one({"Email": user, "Password": password})
            if creds.charInfo.find_one({"_id": infoDict["_id"]}):
                charDict = creds.charInfo.find_one({"_id": infoDict["_id"]})
                validation.rankValidation(charDict) 
            else:
                print("No character found")
        else:
            print("ERROR: Wrong credentials!")
            startup()
    
    def rankValidation(dict):
        """
        Takes in a dictionary containing all of the character information. 
        We will verify here their in game "ranking" and push that information to the main screen accordingly.
        """
        #TODO: PICK UP FROM HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        rank = dict["Rank:"]
        pass


def menuPrinter(x):
    """
    Prints all menu options.
    """
    for key, value in x.items():
        print("{}:{}".format(key,value))
    return None

def logIn():
    """
    If credentials are verified, logs in user according to information passed back.
    """
    user = input(menus.registerMenu[1])
    password = getpass(menus.registerMenu[2])    
    validation.userValidation(user, password)

    return None

def register():
    """
    Register function will take an email and username, send a verification call, 
    and as long as email does not exist will register a new user in the database.
    """
    user = input(menus.registerMenu[1])
    if validation.emailCreateValidation(user):
        password = getpass(menus.registerMenu[2])
        creds.userInfo.insert_one({"Email": user, "Password": password})
        startup()
    else:
        startup()
    return None


def startup():
    """
    Start up function essentially displays the starting page the user will first encounter, 
    it has been separated as a standalone so that it can be called at any point (e.g. failed registration, logging out, etc.)
    this will also help in the future when building the front end as well as keeping our main call clean.
    """
    menuPrinter(menus.logInMenu)
    inp = input()
    if inp not in menus.logInMenu:
        print("ERROR: Wrong Input!\n")
        startup()
    elif inp == "1":
        logIn()
    else:
        register()
    return None

# TODO: 
# 1)members add/removed 2)war attendance 3)growth history / attendance history
# Initialize new guild + give GM/Officer rights to do activate / deactivate / ban
# implement a database backend + website front end

if __name__ == "__main__":
    startup()
