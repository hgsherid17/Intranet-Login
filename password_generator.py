# Num, lower, upper, special, 8-25 chars
import random


def create_strong_password():
    strong = ""
    for i in range(0, 24):
        val = random.randint(33, 126)
        strong += chr(val)

    if test_password(strong):
        print(strong)
        return strong
    else:
        create_strong_password()


def test_password(password) -> bool:
    valid = 0

    if len(password) < 8 & len(password) > 25:
        return False
    for s in " ~`!@#$%^&*()-_=+{}[]|\\:;\"',<.>/?":
        if s in password:
            valid += 1
            break
    for s in range(65, 90):
        if chr(s) in password:
            valid += 1
            break
    for s in range(97, 122):
        if chr(s) in password:
            valid += 1
            break
    if valid < 3:
        return False
    
    return True





