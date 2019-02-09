import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)

def PRINTPERCEPTRON():
    x_list = np.array(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ]
    )
    for x in x_list:
        print('AND(' + str(x[0]) + ', ' + str(x[1]) + '): ' + str(AND(x[0], x[1])))
    for x in x_list:
        print('NAND(' + str(x[0]) + ', ' + str(x[1]) + '): ' + str(NAND(x[0], x[1])))
    for x in x_list:
        print('OR(' + str(x[0]) + ', ' + str(x[1]) + '): ' + str(OR(x[0], x[1])))
    for x in x_list:
        print('XOR(' + str(x[0]) + ', ' + str(x[1]) + '): ' + str(XOR(x[0], x[1])))

PRINTPERCEPTRON()
