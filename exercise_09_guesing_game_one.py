# coding=utf-8
"""
 Guessing Game One
Exercise 9 (and Solution)

Generate a random number between 1 and 9 (including 1 and 9).
 Ask the user to guess the number, then tell them whether they guessed too low,
  too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.

Discussion

Concepts for this week:

    Modules
    Random numbers
    User input

Random Numbers (and Modules)

This is your first exposure to using Python code that somebody else wrote. In Python, these formally-distributed code packages are called modules. The thing we want from a module in this exercise is the ability to generate random numbers. This comes from the random module.

To use a module, at the top of your file, type

	import random

This means you are allowing your Python program to use a module called random in the rest of your code.

To use it (and generate a random integer), now type:

	a = random.randint(2, 6)

Once you run this program, the variable a will have a random integer that the computer made for you, between 2 and 6 (including 2 and 6). The specific documentation for this method is here.

There are many ways you can generate random numbers - integers, decimals, and much more. The Python documentation has much more detailed information about what is possible from the random module.

"""
import random
import sys
import os

jatekszam=0
tippszam=0
tovabb = True
tipp=-1
while tovabb:

    if sys.platform == "linux":
        _ = os.system("clear")
    else:
        _ = os.system("cls")

    szam = random.randint(1,9)
    print("""
    Gondoltam egy számra 1 és 9 között.
    Próbáld meg minél kevesebb lehetőségból kitalálni a számot!
    """)
    jatekszam+=1
    while tipp!=szam:
        try:
            tipp =int(input("Melyik számra gondoltam?:"))
            tippszam+=1
        except:
            print('1-9 közé eső egész számot adjon meg!')
            continue
        if tipp>szam:
            print("Kisebb...")
        elif tipp<szam:
            print("Nagyobb")
        else:
            print("Eltaláltad")
    print("{} tipped volt".format(tippszam))
    ujra=input("Akarsz még játszani? i/n [i]")

    if len(ujra)==0 or ujra.lower()=="i":
        tovabb=True
        tippszam=0
    else:
        tovabb=False

print("{} menetet játszottunk, köszi a játékot!".format(jatekszam))

