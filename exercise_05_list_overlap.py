# -*- coding: utf-8 -*-
"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure
    this out at this point - we’ll get to it soon)

List properties

In other words, “things you can do with lists.”

One of the interesting things you can do with lists in Python is
figure out whether something is inside the list or not. For example:

  >>> a = [5, 10, 15, 20]
  >>> 10 in a
  True
  >>> 3 in a
  False

You can of course use this in loops, conditionals, and any other
programming constructs.

  list_of_students = ["Michele", "Sara", "Cassie"]

  name = input("Type name to check: ")
  if name in list_of_students:
    print("This student is enrolled.")
"""
import random

alist = []
blist = []
kozos = []
for i in range(random.randint(1, 15)):
    alist.append(random.randint(0, 20))
for i in range(random.randint(1, 10)):
    blist.append(random.randint(0, 20))
alist.sort()
blist.sort()
print(alist)
print(blist)
print("-" * 20)
for i in range(len(alist)):
    if alist[i] in blist:
        kozos.append(alist[i])

print(kozos)
# set segítségével csak az egyedi előfordulásokat írja ki, nincs duplikálás

k=set(kozos)
print(k)
#vagy másként
print(set(alist) & set(blist))
