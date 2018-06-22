# coding=utf-8
"""
 Pick Word
Exercise 30 (and Solution)

This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random
word from a list of words from the SOWPODS dictionary. Download this file
and save it in the same directory as your Python code. This file is Peter Norvig’s
compilation of the dictionary of words used in professional Scrabble tournaments.
Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.
Aside: what is SOWPODS

SOWPODS is a word list commonly used in word puzzles and games (like Scrabble for example).
It is the combination of the Scrabble Player’s Dictionary and the Chamber’s Dictionary.
(The history of SOWPODS is quite interesting, I highly recommend reading the Wikipedia article if you are curious.)
Previous exercises with similar concepts

In previous exercises, we have covered all the necessary skills needed to complete this exercise. Check out:

    Exercise 22: read from a file
    Exercise 9: generating a random number
    Exercise 3: accessing an element of a list

Brief concept review
Reading a file

The Python way of reading a file from disk is to use the with construction together with a while loop:

with open('filename.txt', 'r') as f:
  line = f.readline()
  while line:
    # do something to the line, for example
    # saving it to disk
    line = f.readline()

print("The entire file as been read!")

The file filename.txt should be in the same directory as your Python script.

The idea behind the with construction is that it isolates any variables defined
in the with line from the rest of your code. When you are dealing with files,
this means properly opening and closing the files. The open line in the with
statement actually does the opening of the file and saves the file object in
the variable f. The 'r' passed into the open() function tells Python “open
the file for reading”. If the 'w' argument is passed instead, Python will
interpret this as “open the file and allow writing to it.”

After all the code inside the with block is finished, the file f is properly
closed by Python. So by the time the program starts executing the print statement,
the file is already closed.

One thing to remember when reading lines from a file in this way is that a
line contains a \n, or a newline character at the end. So before processing the line,
 it is usually a good idea to use .strip() to remove the newlines and spaces
 from the start and end of the lines, like so:

with open('filename.txt', 'r') as f:
  line = f.readline().strip()
  while line:
    # do something with the 'line' variable
    line = f.readline().strip()

There are many ways of reading lines from files. If for example you want to
read all the lines of the file into a list, you can use the following variant:

with open('filename.txt', 'r') as f:
  lines = f.readlines()

At the end of this code, the variable lines will have all the elements from the file in a Python list.

Here are a few references about opening files, if you would like to read more:

    Learn Python the Hard Way page about reading files
    The Python 3.5 documentation about reading and writing files

Generating a random number

Python’s random library is used to do operations with random numbers.
For a list of the full methods available in the random library, check the Python 3 documentation of the random library.

The two methods that might be useful for this exercise are random.choice()
or random.randint(). The documentation is easy to read, so check out the docs for how these methods work!
"""