'''
Created on 9/20/2023
@author:   James Barbi
Pledge:    I pledge my Honor that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
from functools import reduce
#from dict import *
# Be sure to submit as hw2.py.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(40000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo', 'spam', 'spammy', 'zzyzva']


# Implement your functions here.
def letterScore(letter, scoreList):
    """
    takes as input a single letter string called letter and a list where each element in that list is itself a list of the form
    [character, value] where character is a single letter and value is a number associated with that letter

    returns a single number, namely the value associated with the given letter
    """
    for x in scoreList:
        if x[0] == letter[0]:
            return x[1]

def wordScore(S, scoreList):
    """
    takes as input a string S which will have only lowercase letters and a scorelist
    
    return as output the scrabble score of that string
    """
    if S == "":
        return 0
    else:
        counter = letterScore(S[0], scoreList)
    return counter + wordScore(S[1::], scoreList)


def ind(e, L):
    """
    takes as input a character and a string/list

    return the index at which e is first found in L(string or list)
    """
    if L == "" or L == []:
        return 0
    elif L[0] == e:
        return 0
    return 1 + ind(e, L[1::])


def check_letters(word, Rack):
    """
    takes as input a string and a Rack which is a list of lower-case leters

    returns true if the string can be made using the letters in the rack and false if it cannot
    """
    if word == "":
        return True
    else:
        if word[0] in Rack:
            x = ind(word[0], Rack)
            return check_letters(word[1:], Rack[0:x] + Rack[x+1:])
        return False
    
def myFilter(R, D):
    """
    takes a Rack which is a list of lower-case letters and list as input
    
    returns the list for which all the words in the dictionary can be made with the given rack
    """
    if D == []:
        return D
    if check_letters(D[0], R) == True:
        return [D[0]] + myFilter(R, D[1:])
    return myFilter(R, D[1:])
    

def scoreList(Rack):
    """
    takes as input a Rack which is a list of lower-case letters
    
    returns a list of all of the words in the global Dictionary that can be made from those letters and the score for each one
    """
    final_result = []

    all_words = myFilter(Rack, Dictionary)
    for word in all_words:
        final_result.append([word, wordScore(word, scrabbleScores)])

    return final_result

def helper(x, y):
    """
    takes as input two lists

    returns the list with the larger value at index 1
    """
    if x[1] >= y[1]:
        return x
    if x[1] < y[1]:
        return y

def bestWord(Rack):
    """
    takes as input a Rack which is a list of lower-case letters
    
    returns a list with two elements: the highest possible scoring word from that Rack followed by its score. If there are ties, they can be broken arbitrarily
    """
    options = scoreList(Rack)
    if options == []:
        options.append(['', 0])
    return list(reduce(helper, options))