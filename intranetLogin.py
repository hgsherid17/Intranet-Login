# Hannah Sheridan
# Create a login and menu to a company intranet system
# Login: Username and password
# Menu of Options: Time Reporting, Accounting, IT Helpdesk, Engineering Documents
# Access levels: Admin (all menu items), Employee (limited access), Unauthorized (no access)

# Define access levels
    # 0 - ADMIN
    # 1 - NO ACCESS TO JANITORIAL
    # 2 - NO ACCESS TO ACCOUNTING 
    # -1 - UNAUTHORIZED
accessLvl = 0
userInfo = []
# Index corresponds with
MENU_OPTIONS = ["1", "2", "3", "4", "5"]
CHOICES = [["1", "2", "3", "4", "5"], ["2", "5"], ["3", "5"]]

## Parameters: string filename, string user, string passW
## Returns: integer accessLvl
def authenticate(filename, user, passW):
    try:
        with open(filename, "r") as inFile:
            junk = inFile.readline()
            for line in inFile:
                userInfo = line.split(",")
                if userInfo[0] == user and userInfo[1] == passW:
                    return int(userInfo[2])
    except FileNotFoundError:
        print("Error:", filename, "not found.")
    return -1

## Returns: integer accessLvl
def login():
    filename = "intranetInfo.csv"
    
    print("Intranet Login\n<><><><><><><><><><>")
    
    user = input("Username: ")
    passW = input("Password: ")

    accessLvl = authenticate(filename, user, passW)
    while accessLvl == -1:
        print("Username or password is incorrect. Please try again.")
        user = input("Username: ")
        passW = input("Password: ")
        accessLvl = authenticate(filename, user, passW)
        
    return accessLvl
        
def print_menu():
    print("+--------MENU--------+")
    print("| 1 - Admin          |")
    print("| 2 - Accounting     |")
    print("| 3 - Janitorial     |") 
    print("| 4 - Schedule Edit  |")
    print("| 5 - Exit           |")
    print("+--------------------+")

def back_to_menu(accessLvl):
    back = ""
    back = input("Press enter to go back to the menu: ")
    menu_access(accessLvl)
        
def menu_access(accessLvl):
    print_menu()
    choice = input("Choose a menu option: ")

    # Validate that input is a choice in menu
    while choice not in MENU_OPTIONS:
        print("That choice is not in the menu!")
        choice = input("Choose a menu option: ")

    # Go to area or deny access
    if choice in CHOICES[accessLvl]:
        if choice == "1":
            print("You have entered the admin area")
            back_to_menu(accessLvl)
        elif choice == "2":
            print("You have entered the accounting area")
            back_to_menu(accessLvl)
        elif choice == "3":
            print("You have entered the janitorial area")
            back_to_menu(accessLvl)
        elif choice == "4":
            print("You have entered the schedule area")
            back_to_menu(accessLvl)
        else:
            print("See you soon!")
            return
    else:
        print("XX You do not have access to this menu area! XX")
        back_to_menu(accessLvl)
        

##########
        
accessLvl = login()
menu_access(accessLvl)

    




