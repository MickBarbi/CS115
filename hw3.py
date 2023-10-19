'''
Created on 10/4/2023
@author: James Barbi
Pledge: I pledge my Honor that I have abided by the Stevens Honor System.
CS115 - Hw 3
'''
# Be sure to submit hw3.py. Remove the '_template' from the file name.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:'''
def giveChange(amount, coins):
    """
    inputs a positive integer amount and a list coins containing integers representing different coin values

    returns an integer that represents how many coins from the list it takes to add up to the given amount, with infinity being impossible
    """
    if amount == 0:
        return [0, []]
    if coins == []:
        return [float("inf"), []]
    if amount < 0:
        return [float("inf"), []]
    used = giveChange(amount - coins[-1], coins)
    use_it = [1 + used[0], [coins[-1]] + used[1]]
    lose_it = giveChange(amount, coins[:-1])
    if use_it > lose_it:
        return lose_it
    else:
        return use_it
''' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
[ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
'spam', 'spammy', 'zzyzva']
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
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

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.
    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    if scores == []:
        return []
    if dct[0] == '':
        return wordsWithScore(dct[1:], scores)
    return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0:
        return []
    if L == []:
        return []
    return [L[0]] + take(n-1, L[1:])
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n == 0:
        return L
    if L == []:
        return []
    return drop(n-1, L[1:])

print(giveChange(19, [1, 5, 10, 25]))