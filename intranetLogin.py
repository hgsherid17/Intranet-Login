# Hannah Sheridan
# Create a login and menu to a company intranet system
# Login: Username and password
# Menu of Options: Time Reporting, Accounting, IT Helpdesk, Engineering Documents
# Access levels: Admin (all menu items), Employee (limited access), Unauthorized (no access)

import sys

# Define access levels
MENU_OPTIONS = {"1" : "Time Reporting",
                "2" : "Accounting",
                "3" : "Engineering Documents",
                "4" : "HR Documents",
                "5" : "IT Helpdesk",
                "6" : "User Management",
                "7" : "Security Settings",
                "8" : "Exit"}
MENU_ACCESS = [["1", "2", "3", "4", "5", "6", "7", "8"], ["1", "2", "3", "5", "8"], ["1", "4", "5", "8"]]
USER_DATA = "intranetInfo.csv"
accessLvl = 0

## Authenticate function takes in a filename, username, and password,
## then searches the file for the username and password. The function
## returns an access level 0-2 if the username and password match one
## in the file. Returns -1 if the information is not found.
def authenticate(filename, user, passW):
    userInfo = []
    try:
        with open(filename, "r") as inFile:
            junk = inFile.readline()
            for line in inFile:
                userInfo = line.split(",")
                if userInfo[0] == user and userInfo[1] == passW:
                    return int(userInfo[2])
    except FileNotFoundError:
        print("Error:", filename, "not found. Please review the file and try again.")
        sys.exit()
    return -1


## Login function prompts the user to enter their username and password,
## then calls the authenticate function to verify the information.
## Continues to prompt the user if incorrect information is given.
def login():
    valid = False;
    print("Intranet Login\n<><><><><><><><><><>")

    while valid == False:
        user = input("Username: ")
        while user == "":
            valid == False
            print("No input detected. Please try again.")
            user = input("Username: ")
            
        passW = input("Password: ")
        while passW == "":
            valid = False
            print("No input detected. Please try again.")
            passW = input("Password: ")
            
        accessLvl = authenticate(USER_DATA, user, passW)
        if accessLvl == -1:
            valid = False
            print("Username or password is incorrect. Please try again.")
            #accessLvl = authenticate(USER_DATA, user, passW)
        else:
            
            valid = True
        
    return accessLvl

## Print_menu function prints the MENU_OPTIONS dict
def print_menu():
    print("+--------MENU--------+")
    for key, value in MENU_OPTIONS.items():
        print(" ", key, "-", value)
    print("+--------------------+")

## Back_to_menu takes in an access level, then prompts the user
## To return to the main menu
def back_to_menu(accessLvl):
    back = ""
    back = input("Press enter to go back to the menu: ")
    menu_access(accessLvl)

## Menu access takes in an access level and prompts the user to
## choose an option. Based on the access level, the function grants
## or denies access to the chosen menu item.
def menu_access(accessLvl):
    print_menu()
    choice = input("Choose a menu option: ")

    # Validate that input is a choice in menu
    while choice not in MENU_ACCESS[0]:
        print("That choice is not in the menu!")
        choice = input("Choose a menu option: ")

    # Go to area or deny access
    if choice in MENU_ACCESS[accessLvl] and choice != "8":
        print("You have now accessed the", MENU_OPTIONS[choice], "area.")
        back_to_menu(accessLvl)
    elif choice == "8":
        print("See you soon!")
        return
    else:
        print("XX You do not have access to this menu area! XX")
        back_to_menu(accessLvl)
        

##########

accessLvl = login()

menu_access(accessLvl)




#### TESTING

    




