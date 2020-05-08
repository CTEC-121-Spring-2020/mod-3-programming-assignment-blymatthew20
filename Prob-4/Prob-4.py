# Module 3
#   Programming Assignment 4
#     Prob-4.py

# Matthew Bly

# Author: Bruce Elgort
# Date: July 12, 2017

"""
The Elgorte coffee shop sells coffee at $16.50 a pound
plus the cost of shipping. Each order ships for $0.76
per pound plus $1.25 fixed cost for overhead. If the
number of pounds of the coffee order exceeds 10, then
the shipping cost is waived. Write a program that
calculates the cost of an order. Name your function
coffeeProcessor()
"""

def coffeeProcessor():

    # define variables
    overHead = 1.25
    priceOfCoffee = 16.50

    # get number of pounds from user

    # Fix number 1 added quotation mark to end of string

    # Fix number 2 changed evaluate to eval

    # Fix number 3 added a second parenthese at the end 

    quantity = eval(input("How many pounds of coffee would you like to order?"))
    
    # Check number of pounds ordered
    # If less than or equal to 10 pounds we must charge for shipping
    if quantity <= 10:
        shippingPerPound = .76

    # Fix number 4 added a colon in front of else
    else:
        shippingPerPound = 0      

    # Calculate cost of order

    # Fix number 5 the second spelling of quantity was fixed to correct spelling
    costOfOrder = (quantity * priceOfCoffee) + (quantity * shippingPerPound) + overHead

    # Print result

    # Fix number 6 put quotation marks in correct place

    print("The cost of the order is:",costOfOrder)

    # start the program

    # Fix number 7 took the word go out 

coffeeProcessor()