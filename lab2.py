############################################################
# Name: James Barbi
# Pledge: I pledge my Honor that I have abided by the Stevens Honor System.
# CS115 Lab 2
#
############################################################

def dot(L, K): #output the dot product of the lists L and K
    if L == []:
        return 0
    return L[0] * K[0] + dot(L[1::], K[1::])


def explode(S): #take a string S as input and return a list of the characters (each of which is a string of length 1) in that string
    if S == "":
        return []
    return [S[0]] + explode(S[1:])


def ind(e, L): #return the index at which e is first found in L(string or list)
    if L == "" or L == []:
        return 0
    elif L[0] == e:
        return 0
    return 1 + ind(e, L[1::])


def removeAll(e, L): #return another list that is identical to L except that all elements identical to e have been removed
    if L == []:
        return L
    if L[0] == e:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1::])


def myFilter(function, L): #takes a function and list as input and returns the list for which all elements are true for the function
    if L == []:
        return L
    if function(L[0]) == True:
        return [L[0]] + myFilter(function, L[1:])
    else:
        return myFilter(function, L[1:])

    
def deepReverse(L): #returns the reversal of the list where, additionally, any element that is a list is also reversed
    if L == []:
        return L
    if isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]