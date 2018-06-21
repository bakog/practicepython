# -*- coding: utf-8 -*-
"""
 List Comprehensions
Exercise 7 (and Solution)

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new
list that has only the even elements of this list in it.
Discussion

Concepts for this week:

    List comprehensions

List comprehensions

The idea of a list comprehension is to make code more compact to
accomplish tasks involving lists. Take for example this code:

  years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = []
  for year in years_of_birth:
    ages.append(2014 - year)

And at the end, the variable ages has the list [24, 23, 24, 24, 22, 23].
What this code did was translate the years of birth into ages, and it took
 us a for loop and an append statement to a new list to do that.

Compare to this piece of code:

  years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = [2014 - year for year in years_of_birth]

The second line here - the line with ages is a list comprehension.

It accomplishes the same thing as the first code sample - at the end,
the ages variable has a list containing [24, 23, 24, 24, 22, 23], the ages
corresponding to all the birthdates.

The idea of the list comprehension is to condense the for loop and the
list appending into one simple line. Notice that the for loop just shifted to
the end of the list comprehension, and the part before the for keyword is the
thing to append to the end of the new list.

You can also embed if statements into the list comprehension - check out
this reference to help you out. There are many examples and a better explanation
than I can ever give.
"""
import random
a = []
for i in range(1,20):
    a.append(random.randint(0,100))
print("Az eredeti lista (sorba rendezve):")
a.sort()
print(a)

#lista alkalmazásával
print("Páros számok:")
b= [x for x in a if x%2==0]
b.sort()
print(b)

print("-"*20)
#lista, majd set alkalmazásával egyszerűbb alakban kiszűrve a duplikált értékeket.
print("Páros számok:")
d= set([x for x in a if x%2==0])

print(sorted(d))

