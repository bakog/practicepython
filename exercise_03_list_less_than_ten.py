# -*- coding: utf-8 -*-
"""
https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    1. Instead of printing the elements one by one, make a new list that has all the elements
    less than 5 from this list in it and print out this new list.
    Write this in one line of Python.

    2. Ask the user for a number and return a list that contains only
    elements from the original list a that are smaller than that number given by the user.

"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)
# Extra 1
num = [x for x in a if x < 5]
print(num)
print("-"*20)
# Extra 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("Van egy ilyen számokból állo lista. ", a)
szam = int(input("Melyik számnál kisebb értékeket írjam ki? "))
print([x for x in a if x < szam])