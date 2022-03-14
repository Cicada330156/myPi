def calcPi(calcTo):
    pi = 1
    index = 3
    while index <= calcTo:
        if (index % 2) == 1:
            if ((index + 1) / 2 % 2) == 1:
                pi += (1/index)
            else:# ((index + 1) / 2 % 2) == 1:
                pi -= (1/index)
        index += 1
    print(pi * 4)
