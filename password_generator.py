"""
    Password Authenticator and Generator

    This program contains functions for creating strong passwords and testing password strength

    Author: Hannah Sheridan
"""

import random


def create_strong_password():
    """ Generates a random strong password """
    strong = ""
    for i in range(0, 24):
        val = random.randint(33, 126)
        strong += chr(val)

    # Ensure password meets requirements
    if test_password(strong):
        return strong
    else:
        create_strong_password()


def test_password(password) -> bool:
    """ Tests the strength of a given password """
    length = False
    special = False
    upper = False
    lower = False

    # Password length must be between 8-25 characters
    if 8 <= len(password) <= 25:
        length = True

    # Password must include at least one special character
    for s in " ~`!@#$%^&*()-_=+{}[]|\\:;\"',<.>/?":
        if s in password:
            special = True

    # Password must include at least one upper case character
    for s in range(65, 90):
        if chr(s) in password:
            upper = True

    # Password must include at least one lowercase character
    for s in range(97, 122):
        if chr(s) in password:
            lower = True

    if special and upper and lower and length:
        return True
    else:
        return False





