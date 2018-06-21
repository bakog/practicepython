# -*- coding: utf-8 -*-
"""
https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
Create a program that asks the user to enter their name and their age. Print out a
message addressed to them that tells them the year that they will turn 100 years old.

Hozzon létre egy olyan programot, amely kéri a felhasználót, hogy írja be a nevét és az életkorát.
Írja ki neki a nevét (köszöntse) és az évet, amikor 100 évesek lesznek.
"""
import datetime
nev = input ("Adja meg a nevét: ")
kor = int(input ("Adja meg a korát: "))
mostani_ev = datetime.datetime.now().year
#print ("Mostani év: ", mostani_ev)
print ("Hello ", nev, ", ",100-kor, " év múlva leszel száz éves! (", mostani_ev+100-kor, ")" )