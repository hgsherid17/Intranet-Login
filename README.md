# Intranet Login System
This Python program represents an Intranet login and menu system for a company. The user is prompted to login, then choose options from a menu. Usernames, passwords, and access levels are stored in a CSV file. Based on the user's access level, they are either granted or denied access to a certain menu option.
## Features
### Variables
**MENU_OPTIONS:** key-value pairs representing menu options and their corresponding numbers

**MENU_ACCESS:** a 2d array in which index corresponds to accessLvl and the arrays list accessible menu options

**USER_DATA:** a string, the title of the desired CSV file

**accessLvl:** an integer value representing the status of the user

### Functions
| Name | Parameters | Returns | About |
| --- | --- | --- | --- |
| authenticate | string filename, string user, string pass | integer accessLvl | searches file for desired username and password. returns accessLvl if found, -1 if not |
| print_menu | N/A | N/A | displays MENU_OPTIONS to console |
| back_to_menu | integer accessLvl | N/A | prompts user to go back to the main menu |
| menu_access | integer accessLvl | N/A | prompts user to choose an option from the menu, then displays whether or not they have access to the menu area |


## Menu
### Access Levels
0 - Admin access; user can choose any menu option

1 - Employee access; user can access Time Reporting, Accounting, Engineering Documents, and IT Helpdesk

2 - HR access; user can access Time Reporting, HR Documents, and IT Helpdesk

### Options
| Menu Option | Accessible by |
| --- | --- |
| Time Reporting | Everyone |
| Accounting | 0, 1 |
| Engineering Documents | 0, 1 |
| HR Documents | 0, 2 |
| IT Helpdesk | Everyone |
| User Management | 0 |
| Security Settings | 0 |
| Exit | Everyone |

## Testing Instructions
1. Create or obtain a CSV file in the format: username, password, accessLvl
3. **Scenario 1:** Admin Access
- Log into an account with access level 0
- Test accessing every menu option to ensure you are granted access to all of them
- Choose menu option 8 to exit the program
4. **Scenario 2:** Employee Access
- Log into an account with access level 1
- Test accessing every menu option
- User should be denied access to:
  - HR Documents
  - User Management
  - Security Settings
5. **Scenario 3:** HR Access
- Log into an account with access level 2
- Test accessing every menu option
- User should be denied access to:
  - Accounting
  - Engineering Documents
  - User Management
  - Security Settings
6. **Scenario 4:** Unauthorized Access
- Log into an account not listed on the CSV file
- Ensure that program reprompts user after incorrect username and password are entered
7. Input Validation
- Change "USER_DATA" to a nonexistent file to ensure program exits gracefully
- Test varying login credentials
  - No username
  - No password
  - Incorrect username and password
  - Incorrect username and correct password
  - Correct username and incorrect password
  - Correct username and password
- Attempt to choose non-existent menu options (e.g. -1, 'hello', 9)
