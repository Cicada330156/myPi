from decimal import *
getcontext().prec = 69

def calcPi(calcTo):
    pi = Decimal(1)
    index = 3
    while index <= calcTo:
        if (index % 2) == 1:
            if ((index + 1) / 2 % 2) == 1:
                pi += (Decimal(1)/Decimal(index))
            else:# ((index + 1) / 2 % 2) == 1:
                pi -= (Decimal(1)/Decimal(index))
                #check every other time if results are no longer being made more accurate. Checking every 4 times saves considerable computing power.
                if (Decimal(1) + Decimal(1) / Decimal(index) == 1):
                    print("Reached maximum accuracy for the precision at " + str(index) + ". pi is:")
                    print(pi)
                    return
        index += 1
    print(pi * (4))
