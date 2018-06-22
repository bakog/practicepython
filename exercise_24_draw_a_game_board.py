# coding=utf-8
"""

 Draw A Game Board
Exercise 24 (and Solution)

This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---

This one is 3x3 (like in tic tac toe). Obviously, they come in many
other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for
them to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by

  print("Thing to show on screen")

Hint: this requires some use of functions, as were discussed previously
 on this blog and elsewhere on the Internet, like this TutorialsPoint link.
Topics and links for more information

The main topic of this exercise is functions. They are tricky,
 and deserve lots of practice and thought. Here are a few links in case you want some more reading.

    Functions on TutorialsPoint
    Hands-on Python, by Loyola University
    Learn Python the Hard Way
    ZetCode

There are hundreds more out there - read and practice away!
"""
def oddrow(w):
    for i in range(w):
        print(" ---",end="")
    print()

def evenrow(w):
    for i in range(w+1):
        print("|   ", end="")
    print()

def drawtable(h,w):
    for i in range(h):
        oddrow(w)
        evenrow(w)
    oddrow(w)

print("""
Mekkora legyen a játéktér?

1. 3X3 mező (alapértelmezett)
2. 5X5 mező
3. 8X8 mező

Válassz! 1-3 közül [1]
""")
h=3
w=3
try:
    meret=input()
except:
    print("Nem jó számot adott meg, az alapértelmezett pályaméret lesz érvényes.")
    meret=1

if meret==2:
    h=5
    w=5
    drawtable(h,w)
elif meret==3:
    h=8
    w=8
    drawtable(h,w)
else:
    drawtable(h, w)