"""
    This program defines menu options and access levels for an intranet system. It
    contains a function that returns true if a user has access to a given menu option.

    Author: Hannah Sheridan
"""
# Define access levels
MENU_OPTIONS = {"1" : "Time Reporting",
                "2" : "Accounting",
                "3" : "Engineering Documents",
                "4" : "HR Documents",
                "5" : "IT Helpdesk",
                "6" : "User Management",
                "7" : "Security Settings"}
MENU_ACCESS = [["1", "2", "3", "4", "5", "6", "7"], ["1", "2", "3", "5"], ["1", "4", "5"]]
# USER_DATA = "intranetInfo.csv"
# accessLvl = 0


def menu_access(accesslvl, option):
    """ Checks if user has access to a given menu item """
    if option in MENU_ACCESS[int(accesslvl)]:
        return True
    else:
        return False



