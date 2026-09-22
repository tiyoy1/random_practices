import random

while True:
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    length = int(input("How long do you want your password to be? "))

    pw=""
    for char in range(length) :
        pw += random.choice(characters)

    print("your password is:", pw)