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

def login(user, passW):
    ######## account for missing text file!
    ######## pass in file?????
    with open("intranetInfo.csv", "r") as inFile:
        junk = inFile.readline()
        for line in inFile:
            userInfo = line.split(",")
            if userInfo[0] == user and userInfo[1] == passW:
                return int(userInfo[2])
    return -1

def print_menu():
    print("<><>MENU<><>")
    print("1 - Admin")
    print("2 - Accounting")
    print("3 - Janitorial") 
    print("4 - Schedule Edit")
    print("5 - Exit")

def back_to_menu(accessLvl):
    back = ""
    back = input("Press enter to go back to the menu: ")
    menu_access(accessLvl)
        
def menu_access(accessLvl):
    print_menu()
    choice = input("Choose an option: ")
    if choice == "1" or choice == "4":
        if accessLvl == 0:
            if choice == "1":
                print("You have entered the admin area")
                back_to_menu(accessLvl)
            else:
                print("You have entered the schedule area")
                back_to_menu(accessLvl)
        else:
            print("You are not authorized to enter this area")
            back_to_menu(accessLvl)
    elif choice == "2":
        if accessLvl == 0 or accessLvl == 1:
            print("You have entered the accounting area")
            back_to_menu(accessLvl)
        else:
            print("You are not authorized to enter this area")
            back_to_menu(accessLvl)
            
    elif choice == "3":
        if accessLvl == 0 or accessLvl == 2:
            print("You have entered the janitorial area")
            back_to_menu(accessLvl)
        else:
            print("You are not authorized to enter this area")
            back_to_menu(accessLvl)
    else:
        print("Thank you!")

##########
print("Intranet Login System")
user = input("Username: ")
passW = input("Password: ")

accessLvl = login(user, passW)
while accessLvl == -1:
    user = input("Username: ")
    passW = input("Password: ")
    accessLvl = login(user, passW)


menu_access(accessLvl)

    




