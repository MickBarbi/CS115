# James Barbi
# I pledge my Honor that I have abided by the Stevens Honor System.

# https://www.geeksforgeeks.org/python-program-convert-string-list/
import math
from functools import reduce
import time
import os

running = True

def multiply(x, y): #takes two inputs and returns the first multiplied by the second
    return x * y

def add(x, y): #takes two inputs and returns the first added with the second
    return x + y

def convert_to_float(string): #takes a string input and returns it as a float
    return float(string)

def factorial(x): #taking the input of integer x, returns the factorial by making a list, and reducing the list through multiplication
    return reduce(multiply, range(1, x + 1))

def convert_string_to_list(string): #takes a string input and converts it to a list of individual strings and then a list of floats
    li = list(string.split(", "))
    li = (list(map(convert_to_float, li)))
    return li

def mean(L): #takes a list input and returns the mean by adding all the values and dividing by the total number of values
    return (reduce(add, L) / len(L))

while running:
    #clear the console for better looking program
    os.system('cls')
    #display menu for different operations
    print("This application can be used to find the factorial of a number or to find the mean of a list. Which would you like to do?")
    print("1. Factorial")
    print("2. Mean of List")
    print("3. Exit Program")
    choice = input("")
    
    #if else list for what the user picked
    if choice == '1':
        os.system('cls')
        #input the number to take the factorial of
        factnumber = int(input("Plese input the number you would like to take the factorial of: "))
        #print the output of the 'factorial' function
        print("The factorial of the number you entered is: " + str(factorial(factnumber)))
        #go back to the menu
        input("Hit Enter to continue")
    elif choice == '2':
        os.system('cls')
        #take list of numbers for the mean list
        mean_list = input("Please list the numbers you would like to take the mean of. Enter the numbers using a comma and space to separate them (i.e. #, #, #). Hit enter when done:\n")
        #converts the string to a list of floats
        mean_list = convert_string_to_list(mean_list)
        #print the output of the 'mean' function
        print("The mean of the numbers you entered is: " + str(mean(mean_list)))
        #go back to menu
        input("Hit Enter to continue")
    elif choice == '3':
        os.system('cls')
        #thank the user for using the program
        print("Thank you for using our program, hope we can be of service sometime again soon!")
        #wait 3 seconds before exiting
        time.sleep(3)
        #set running to false so the while loop ends and the program ends
        running = False