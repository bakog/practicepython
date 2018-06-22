# coding=utf-8
"""
 File Overlap
Exercise 23 (and Solution)

Given two .txt files that have lists of numbers in them, f
ind the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000,
 and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number.
 And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
 The explanation is easier with an example, which I will describe below.)
Discussion

You’ll need to stitch together a few ideas of things I’ve previously talked about
 on this blog, so if you need a refresher in any of these topics, now is your chance!
  Of course, there are any number of ways to do this exercise, so these are only suggestions.

Topics:

    Reading a file, in Exercise 21
    Number types and converting to integers from strings, in Exercise 1
    Lists, in Exercise 3 and Exercise 5

"""
primenumbers = []
happynumbers = []
happyprimenumbers = []

with open("primenumbers.txt", "r") as file1:
    for sor in file1:
        szam=sor.split("\n")[0]
        primenumbers.append(int(szam))

with open("happynumbers.txt", "r") as file2:
    for sor in file2:
        szam=sor.split("\n")[0]
        happynumbers.append(int(szam))

for i in happynumbers:
    if i in primenumbers:
        happyprimenumbers.append(i)


print("{} db. olyan szám van, ami mind a két fájlban szerepel.".format(len(happyprimenumbers)))
print("Ezek a következő számok: ", happyprimenumbers)