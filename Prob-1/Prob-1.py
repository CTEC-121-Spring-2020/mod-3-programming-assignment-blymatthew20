# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Matthew Bly

def shippingCost(orderSubTotal):
    shippingCost = 2.99
    if orderSubTotal >= 10:
        shippingCost = 0.0


    return shippingCost

def unitTest():
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(9.99))
    print("Shipping cost if subtotal < 10.00:\t", shippingCost(10.0))
    


if __name__ == "__main__":
    unitTest()