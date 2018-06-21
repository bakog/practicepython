# coding=utf-8
"""
 List Ends
Exercise 12 (and Solution)

Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
Concepts to practice

    Lists and properties of lists
    List comprehensions (maybe)
    Functions

"""
import random

def firstandlast(l):
    return [l[0], l[-1]]

alist= []
for i in range(10,20):
    alist.append(random.randint(0,100))

print(alist)

print(firstandlast(alist))
