# Intranet Login System
This Python program represents the login and menu of a company intranet system. The user is prompted to log in using a valid username and password, then choose options from a menu. If 
the user does not have an account, they can create an account on the signup page. 
Each user has an access level that grants them permission to certain menu items; based on this, they are either granted or denied access to a particular menu option. All user information is stored in an SQL database.

## Table of Contents

- [Programs](#programs)
- [Features](#features)
- [Testing Instructions](#testing-instructions)

## Programs
**werk.py:** Main script that powers the intranet system web application using Flask

**config.py:** Contains configuration settings for the intranet system

**app.py:** Flask web application for the intranet system

**authentication.py:** Contains functions for user authentication and password hashing

**database.py:** SQLite database operations for user account management

**password_generator.py:** Contains functions for generating strong passwords and testing password strength

**intranetLogin.py:** Defines user access levels and menu options. Contains a function that ensures user is granted access to a given menu option.
## Features

- User authentication with password hashing
- Account creation and management
- Access control based on user roles
- Password strength enforcement during account creation
- Generates suggested strong passwords

### Access Levels
0 - Admin access; user can choose any menu option

1 - Employee access; user can access Time Reporting, Accounting, Engineering Documents, and IT Helpdesk

2 - HR access; user can access Time Reporting, HR Documents, and IT Helpdesk

### Menu
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

### Existing Accounts
| Username | Password | Access Level |
| --- | --- |
| wwhite | Skyler51! | 0 |
| hschrader | Marie307$ | 1 |
| walterjr | BreAkfAst17%! | 2 |

## Installation Instructions
1. Install SQLite: https://www.sqlite.org/download.html
2. Install Flask:
  ```angular2html
pip install flask
```
3. Download all program files
4. Create database using the `create_db()` function in `database.py`

    NOTE: `werk.py` does this for you when running the flask application
## Testing Instructions
1. Run the Flask app using `werk.py` and confirm that it runs successfully
2. Test User Authentication
- Navigate to the login page
- **Scenario 1:** Successful Login
  - Enter a valid username and password
  - Ensure that the system logs you in successfully and displays the correct username and access level
- **Scenario 2:** Unsuccessful Login
  - Enter invalid credentials
  - Ensure that the system does not allow login
3. Test Account Creation
- Navigate to the signup page
- Ensure that the 'generate password' button generates strong passwords
- **Scenario 1:** Invalid password
  - Attempt to create an account with invalid password credentials
  - Ensure the system reprompts the user
- **Scenario 2:** Taken username
  - Attempt to create an account with an already existing username
  - Ensure the system reprompts the user
- **Scenario 3:** Passwords don't match
  - Attempt to create an account with two different passwords
  - Ensure the system reprompts the user
- **Scenario 4:** Valid credentials
  - Create an account with a valid username and password
  - Ensure the system redirects to the login page
4. Test Access Control
- **Scenario 1:** Admin Access
  - Log into an account with access level 0
  - Test accessing every menu option to ensure you are granted access to all of them
  - Choose menu option 8 to return to menu
- **Scenario 2:** Employee Access
  - Log into an account with access level 1
  - Test accessing every menu option
  - User should be denied access to:
    - HR Documents
    - User Management
    - Security Settings
  - Choose menu option 8 to return to menu
- **Scenario 3:** HR Access 
  - Log into an account with access level 2
  - Test accessing every menu option
  - User should be denied access to:
    - Accounting
    - Engineering Documents
    - User Management
    - Security Settings
  - Choose menu option 8 to return to menu