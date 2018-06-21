# -*- coding: utf-8 -*-
"""
https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and
    one number to divide by (check). If check divides evenly into num,
    tell that to the user. If not, print a different appropriate message.

"""

szam = int(input("Adjon meg egy számot! "))
if szam % 2 == 0:
    print("Páros")
    if szam % 4 == 0:
        print("Néggyel is osztható!")
else:
    print("Páratlan")

szam2 = int(input("Adjon meg egy másik számot! "))
szam3 = int(input("Adjon meg egy újabb számot, amivel osztani akarja az előbbit!"))
if szam2 % szam3 == 0:
    print(szam3, " osztója ", szam2, "-nek")
else:
    print("Nem osztója")