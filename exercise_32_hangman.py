# coding=utf-8
"""
 Hangman
Exercise 32 (and Solution)

This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.

You can start your Python journey anywhere, but to finish this exercise
you will have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).

In this exercise, we will finish building Hangman. In the game of Hangman,
 the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it.
In Part 2, we wrote the logic for guessing the letter and displaying
that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

    Only let the user guess 6 times, and tell the user how many guesses they have left.
    Keep track of the letters the user guessed. If the user guesses a
    letter they already guessed, don’t penalize them - let them guess again.

Optional additions:

    When the player wins or loses, let them start a new game.
    Rather than telling the user "You have 4 incorrect guesses left",
    display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!

Your solution will be a lot cleaner if you make use of functions to help you!
Concepts

    Sets
    Code organization

Sets

We already discussed sets in Exercise 14, but here is a brief summary:

    Sets, like lists, store a collection of items
    The collection of items in a set are unique. There cannot be any repeated elements.

The only “gotcha” is that you cannot have a set of lists - each element in the set must
be hashable. Basically this means you can’t have elements that can change in a set,
 so the objects in your set should be integers or strings. The reason and distinction
 are not super important; the most important thing to know is that sets are most useful
  when you want a set of integers or strings, rather than a set of lists.

In Python:

>>> my_list = [1, 1, 2, 2, 3, 3, 5, 5, 8]
>>> print(my_list)
[1, 1, 2, 2, 3, 3, 5, 5, 8]
>>> my_set = {1, 1, 2, 2, 3, 3, 5, 5, 8}
>>> print(my_set)
{1, 2, 3, 5, 8}

To add elements to a set, use the .add() method:

>>> my_set = set()  # makes an empty set
>>> my_set.add(5)  # adds the number 5
>>> print(my_set)
{5}
>>> my_set.add("Michele")
>>> print(my_set)
{5, "Michele"}
>>> my_set.add(5)
>>> print(my_set)
{5, "Michele"}

The advantage of sets is that all the elements in it are unique.
This makes it very easy to check whether an element is already in the set.
All you need to do is ask elem in my_set:

>>> my_set = {1, 2, 3, 5}
>>> 1 in my_set
True
>>> 4 in my_set
False

And this check is very fast - much faster than doing the same in check with a list.
(The reason it is fast is a concept called hashing, which you can read about in detail in this StackOverflow post.)
Code organization

We briefly discussed some tips on working with lots of code in Exercise 29, and I’ll add a few more here:

    If you don’t like your code from Parts 1 and 2, just take any of the code
    from the solution to Part 1 or the solution to Part 2 to start.
    Just because you wrote some code before, doesn’t mean you are locked in forever!
    Any piece of your code that is used more than once, put it into a function.
    We did a long discussion of functions in Exercise 11, if you want a review.
    Your functions should be small and easy to understand - think of it as a 3-year-old child;
    if you ask a 3-year-old to do too many things, they will get confused and not do exactly what you asked.

If you have any other code organization tips, leave them in the comments, would love to get a good discussion going.
"""