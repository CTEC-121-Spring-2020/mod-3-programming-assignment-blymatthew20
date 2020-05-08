# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Matthew Bly

'''
Input: Persons name, Persons hourly wage, Persons hours
Process: Calculate persons regular wages, overtime wages, total wages, Tax witholding, Insurance Witholding, and Take Home Pay
OutPut: Return regular wages, overtime wages, total wages, Tax witholding, Insurance Witholding, and Take Home Pay
'''

def main():
    #employee info
    NamePlease = (input("Please Enter your Name:"))
    HourlyWage = float(input("Please Enter your hourly wage:"))
    WorkHours = int(input("Please Enter your work hours:"))
    

    # Regular Wages
    RegularWages = HourlyWage * WorkHours
    print(RegularWages)

    # over time Wages
    OverTimeWages = (WorkHours - 40) * 1.5
    print(OverTimeWages)

    # Total Wages
    TotalWages = RegularWages + OverTimeWages
    print(TotalWages)
    
    # Tax witholding
    Tax = TotalWages * 0.2
    print(Tax)

    # Insurance
    Insurance = TotalWages * 0.1
    print(Insurance)

    # Take Home Pay
    TakeHomePay = TotalWages - Tax - Insurance
    print(TakeHomePay)
    print()

    # PayCheck Into
    print("Employee Name:", NamePlease)
    print("Regular Wages:", RegularWages)
    print("Overtime Wages:", OverTimeWages)
    print("Total Wages:", TotalWages)
    print("Tax Witholding:", Tax)
    print("Insurance Witholding:", Insurance)
    print("Take Home Pay:", TakeHomePay)




main()