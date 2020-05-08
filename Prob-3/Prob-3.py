# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Matthew Bly

def letterGrade(score):
    if score == 5:
        grade = "A"
    elif score == 4:
        grade = "B"
    elif score == 3:
        grade = "C"
    elif score == 2:
        grade = "D"
    elif score == 1:
        grade = "F"
    elif score == 0:
        grade = "F"
    


    return grade

def unitTest():
    print("grade for score 5:", letterGrade(5))
    print("grade for score 4:", letterGrade(4))
    print("grade for score 3:", letterGrade(3))
    print("grade for score 2:", letterGrade(2))
    print("grade for score 1:", letterGrade(1))
    print("grade for score 0:", letterGrade(0))

if __name__ == "__main__":
    unitTest()