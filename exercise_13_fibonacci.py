# coding=utf-8
"""
 Fibonacci
Exercise 13 (and Solution)

Write a program that asks the user how many Fibonnaci numbers
to generate and then generates them. Take this opportunity
to think about how you can use functions. Make sure to ask
the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is
the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
import time
szam = int(input("Meddig írjam ki a Fibonacci sorozat elemeit? "))

f = []


def fibonacci(a,b):
    global  f
    global szam

    if len(f)<2:
        f.append(a)
        f.append(b)
    else:
        f.append(b)
    #print("a és b értéke: ", a, b)
    c=b
    b=a+b
    a=c
    #print("a és b értéke: ", a, b)
    #time.sleep(3)
    if len(f)<szam:
        fibonacci(a,b)

fibonacci(0,1)
print(f)
print(sum(f))

