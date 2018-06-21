# coding=utf-8
"""
 Password Generator
Exercise 16 (and Solution)

Write a password generator in Python. Be creative with how you generate passwords -
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks
for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

Discussion

There are no new topics this week, but you will need to use Python’s random module, described in this post.
"""
import random

chars = ["q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m"]
nums = [0,1,2,3,4,5,6,7,8,9]
symbols= ["-", "_", "+", "@"]

def egyszeru_jelszo(db, hossz):
    pws = []
    for i in range(db):
        pw = ""
        for j in range(hossz):
            v = random.randint(0,1)
            if v ==0:
                kn=random.randint(0,1)
                if kn==0:
                    pw+=chars[random.randint(0, len(chars)-1)]
                else:
                    pw+=chars[random.randint(0, len(chars)-1)].upper()
            else:
                pw+=str(nums[random.randint(0, len(nums)-1)])
        pws.append(pw)
    return pws

def bonyolult_jelszo(db, hossz):
    pws = []
    for i in range(db):
        pw = ""
        for j in range(hossz):
            v = random.randint(0,2)
            if v ==0:
                kn=random.randint(0,1)
                if kn==0:
                    pw+=chars[random.randint(0, len(chars)-1)]
                else:
                    pw+=chars[random.randint(0, len(chars)-1)].upper()

            elif v==1:
                pw+=str(nums[random.randint(0, len(nums)-1)])
            else:
                pw+=str(symbols[random.randint(0, len(symbols)-1)])

        pws.append(pw)
    return pws

db = int(input("Hány jelszót generáljak? "))
hossz=int(input("Milyen hosszú legyen a jelszó? "))
print("""
a. Egyszerű jelszó (kis-, és nagybetű és számok)
b. Bonyolult jelszó (kis-, és nagybetű, számok és szimbólumok)""")
bonyolultsag = input("Milyen bonyolult legyen a jelszó? a/b [b]")

if bonyolultsag.lower()=="a":
    jelszavak = egyszeru_jelszo(db, hossz)
else:
    jelszavak = bonyolult_jelszo(db, hossz)

print(jelszavak)