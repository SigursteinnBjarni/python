#!/bin/python
import random
 
print 'Welcome to password generator'

def get_rand_number():
    return random.randint(0, 999999)


#Takes a letter and swaps it out for a symbol
def change_char(letter):
 
    #new_letter = letter
    if letter.lower() == 'o' and get_rand_number() % 2 == 0:
        letter = '0'
        return letter
    elif letter.lower() == 'i' and get_rand_number() % 2 == 0 :
        letter = '!'
        return letter
    elif letter.lower() == 's' and get_rand_number() % 2 == 0 :
        letter = '$'
        return letter

    else:
        return letter

file = open('words.txt', 'r')
words = []
for line in file:
    words.append(line.strip())
 
#Get two random words for the array and add them together 
word = words[get_rand_number() % len(words)] + words[get_rand_number() % len(words)]
 
string = ''
#Modify the string for complexity
for letter in word:
    var = random.randint(0, 999)
    if (var % 2) == 0:
        string += change_char(letter).upper()
    else:
        string += change_char(letter)
 
string += str(random.randint(0, 9999))
 
print string

file.close()
