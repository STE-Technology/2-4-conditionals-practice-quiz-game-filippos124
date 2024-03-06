"""
File: quiz.py
Author: Filippo
Date: 2024-03-06
Description: 5 question computer quiz
"""
score = 0

print ("Welcome to the Grade 11 Computer Quiz")
print (" ")

# question 1
print ("What does does 'CPU' Stand for?")
print ("A) Computer Prosessing Unit")
print ("B) Central Processing Unit")
print ("C) Central prossesor Understanding")
print ("D) Controller plug-in unit")

# takes user input and gives answer
answer_one = input("> ")
if answer_one == "B" or answer_one == "b":
    print (" ")
    print ("Correct! :D")
    score += 1
else:
    print ("Incorrect. D:")


# question 2
print ("What does does 'GPU' Stand for?")
print ("A) Gaming Processing Unit")
print ("B) Graphical Peripherals Unit")
print ("C) Graphic Processing Unit")
print ("D) Good practical Unit")

# takes user input and gives answer
answer_two = input("> ")
if answer_two == "C" or answer_two == "c":
    print (" ")
    print ("Correct! :D")
    score += 1
else:
    print ("Incorrect. D:")


# question 3
print ("What does does 'RAM' Stand for?")
print ("A) Rotating accout manager")
print ("B) Runaway Man")
print ("C) Random Access Memory")
print ("D) Random Advertisment")

# takes user input and gives answer
answer_three = input("> ")
if answer_three == "C" or answer_three == "c":
    print (" ")
    print ("Correct! :D")
    score += 1
else:
    print ("Incorrect. D:")


# question 4
print ("What does does 'SSD' Stand for?")
print ("A) Solid State Drive")
print ("B) Solid State Driver")
print ("C) Hard Disk Drive")
print ("D) Super speed drive")

# takes user input and gives answer
answer_four = input("> ")
if answer_four == "A" or answer_four == "a":
    print (" ")
    print ("Correct! :D")
    score += 1
else:
    print ("Incorrect. D:")

# question 5
print ("What does does 'PC' Stand for?")
print ("A) Personal Creator")
print ("B) Personal Computer")
print ("C) Power Central")
print ("D) Computer")

# takes user input and gives answer
answer_five = input("> ")
if answer_five == "B" or answer_five == "b":
    print (" ")
    print ("Correct! :D")
    score += 1
else:
    print ("Incorrect. D:")

print ("Thank you for playing!!!")
print ("You Answered " + str(score) + " out of 5 Questions :D")