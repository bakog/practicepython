# -*- coding: utf-8 -*-
"""
Create a program that asks the user for a number and then 
prints out a list of all the divisors of that number. (If you don’t know
 what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

The topics that you need for this exercise combine lists, 
conditionals, and user input. 
There is a new concept of creating lists.

There is an easy way to programmatically create lists of numbers in Python.

To create a list of numbers from 2 to 10, just use the following code:

  x = range(2, 11)

Then the variable x will contain the list [2, 3, 4, 5, 6, 7, 8, 9, 10]. 
Note that the second number in the range() function is not included 
in the original list.

Now that x is a list of numbers, the same for loop can be
 used with the list:
  for elem in x: 
    print elem

Will yield the result:

  2
  3
  4
  5
  6
  7
  8
  9
  10
"""
from timeit import default_timer as timer
t1, t2, t3  = [],[], []
N=1000
szam=int(input("Adjon meg egy számot! "))
#Az adott számot osztjuk 2-vel, mert ennél csak kisebbek lehetnek az osztói, kivéve saját maga...
fel=int(szam/2)
#print(fel)
#lista alkalmazása nélküli megoldás
start1 = timer()
for i in range(N):
    print ("-"*20)
    print("A szám osztói:")
    for x in range (1,fel+1):
        if szam%x==0:
            print(x)
    print(szam)
end1 = timer()
#print("Idő: ", end-start)


#lista alkalmazásával felezve a számot
start2 = timer()
for i in range(N):
    print ("-"*20)
    print("A szám osztói:")
    lista = [x for x in range(1,fel+1) if szam%x==0]
    lista.append(szam)
    print(lista)
end2 = timer()
#print("Idő: ", end-start)


#lista alkalmazásával 

start3 = timer()

for i in range(N):
    print ("-"*20)
    print("A szám osztói:")
    lista = [x for x in range(1,szam+1) if szam%x==0]
    print(lista)
end3 = timer()
print("Idő1: ", end1-start1)
print("Idő2: ", end2-start2)
print("Idő3: ", end3-start3)