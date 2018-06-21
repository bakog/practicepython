# coding=utf-8

"""Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except with
the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
Discussion

Concepts for this week:

    More string things

More string things

Python has a lot of interesting things you can do with strings.
I will show a few here, but you can see many more methods that
may or may not be useful at the official Python documentation about the string format.

Remember that strings are lists.
Splitting strings

You can “split” or tear apart strings based on a given set of characters. For example:

  teststring = "this is a test"
  result = teststring.split("t")

And at the end, result will contain the list:

  ['', 'his is a ', 'es', '']

Instead of "t", you can write any character you want.
If you do not include any character, it means “split on all whitespace”:

  teststring = "  this      has a lot    of   spaces and    tabs"
  result = testring.split()

Then result contains:

  ['this', 'has', 'a', 'lot', 'of', 'spaces', 'and', 'tabs']

Joining strings

You can also relatively easily “join” or “smush” strings together:

  listofstrings = ['a', 'b', 'c']
  result = "**".join(listofstrings)

Then result will contain the string:

  a**b**c

"""

def szofordito(l):
    for i in range(len(l)-1, -1 ,-1):
        print(l[i], end=" ")

mondat = input("Adjon meg egy töb szóból álló mondatot!")

szavak = mondat.split(" ")
print(szavak)

szofordito(szavak)
