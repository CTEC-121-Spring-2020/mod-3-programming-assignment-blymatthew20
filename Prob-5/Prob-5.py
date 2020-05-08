# Module 3
#   Programming Assignment 4
#     Prob-5.py

# Matthew Bly

def main():
    try:
     x = eval(2)
     print("x:", x)
    except TypeError:
        print("\nThere was a type error. \nExiting.")
        exit
main()