import numpy as np
import matplotlib.pyplot as plt
import Exercises as ex

def main():
    populationSize = 2*187
    ex.Question1(populationSize)

    N = 1000
    r = 0.01
    R =1
    listTimeA = []
    listTimeB = []
    numberOfRepeats = 100000
    for i in range(numberOfRepeats):
        timeA,timeB = ex.Question2(2,R)
        listTimeA.append(timeA)
        listTimeB.append(timeB)
    plt.hist(listTimeA, bins=100, normed=1, facecolor='red')
    plt.hist(listTimeB, bins=100, normed=1, facecolor='blue')
    plt.show()

if __name__ == '__main__':
    main()