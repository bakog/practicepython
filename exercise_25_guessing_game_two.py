# coding=utf-8
"""
 Guessing Game Two
Exercise 25 (and Solution)

In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user,
will have in your head a number between 0 and 100. The program will guess a number,
 and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess.
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.)
 until you hit the number. But that’s not an optimal guessing strategy.
 An alternate strategy might be to guess 50 (right in the middle of the range),
 and then increase / decrease by 1 as needed. After you’ve written the program,
 try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)
Topics and links for more information

This exercise doesn’t need any functions, but it does need extensive use of variables, math, and user input.

You can refer to this exercise on user input, this one on rock paper scissors, and many others.

If you want to implement the optimal solution without thinking about it first,
you can read this Wikipedia article on binary search.
"""

def kisebb_vagy_nagyobb(tipp, prev_tipp):
    print("Én a {} számra tippelek.\n".format(tipp))
    print("""
    Válassz a következők közül:
    
    1. Az általad gondolt szám az én tippemnél kisebb...
    2. Az általad gondolt szám az én tippemnél nagyobb...
    3. Eltaláltam a számot :-)
    
    """)
    valasz = input()
    if valasz =='1':
        k=abs(tipp-prev_tipp)//2
        next_tipp=tipp-k
    elif valasz=="2":
        k=abs((tipp-prev_tipp)//2)
        next_tipp= tipp+k
    else:
        next_tipp=-1
    return next_tipp


print("""
Gondolj egy számra 1-100 között és én megpróbálom kitalálni...
""")
tippszam= 0
hibas_tipp = True
tipp=50
prevtipp=100
while True:
    tippszam+=1
    tmp=tipp
    tipp=kisebb_vagy_nagyobb(tipp,prevtipp)
    prevtipp=tmp
    if tipp==-1:
        break

print("{} tippból sikerült kitalálnom a számot ({})".format(tippszam, prevtipp))
