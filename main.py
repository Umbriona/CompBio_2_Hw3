import numpy as np
import matplotlib.pyplot as plt
import Exercises as ex
import scipy.special
import math

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
    listTimeA = np.asarray(listTimeA)
    listTimeB = np.asarray(listTimeB)
    meanTimeA = np.mean(listTimeA)
    meanTimeB = np.mean(listTimeB)
    mean2TimeA = np.mean(listTimeA**2)
    mean2TimeB = np.mean(listTimeB**2)

    fig, axes = plt.subplots(nrows=2, ncols=1)
    ax0, ax1 = axes.flatten()
    #n_binsA = len(set(listTimeA))
    #n_binsB = len(set(listTimeB))
    def analytT(x):
        recombinationRate = 0
        coalescentRate = scipy.special.comb(2, 2)
        Lambda = recombinationRate + coalescentRate
        return Lambda * np.exp(-Lambda*x)
    x = np.linspace(0,17,100)
    meanTime = np.mean(analytT(x))
    mean2Time = np.mean(analytT(x) ** 2)
    print('<Ta>', meanTimeA, '\n<Tb>', meanTimeB, '\n<Ta^2', mean2TimeA, '\n<Tb^2', mean2TimeB,'\n<T>',meanTime,'\n<T^2>',mean2Time)
    ax0.hist(listTimeA, bins=100,density = True, histtype = 'bar', facecolor='red',label='Simulation')
    ax0.plot(x,analytT(x),label='Analytical',color='blue')
    ax0.set_title('T_a R = 1')
    ax0.legend(loc='upper center', shadow=True, fontsize='x-large')

    ax1.hist(listTimeB, bins=100, density = True , facecolor='red',label='Simulation')
    ax1.plot(x, analytT(x),label='Analytical',color='blue')
    ax1.legend(loc='upper center', shadow=True, fontsize='x-large')

    ax1.set_title('T_b R = 1')
    plt.show()

    R = np.array([0,10**-5,10**-4,10**-3,10**-2,0.1,1,10])
    n = np.array([2,4,8,16])
    R_a = np.linspace(0,10,100)
    analyt = lambda x: (x+18)/(x**2+13*x+18)
    numberOfRepeats = 10000
    fig, axes = plt.subplots(nrows=2, ncols=2)
    ax = axes.flatten()
    for k in range(len(n)):
        Pab = []
        for j in R:
            listTimeA = []
            listTimeB = []
            for i in range(numberOfRepeats):
                timeA, timeB = ex.Question2(n[k], j)
                listTimeA.append(timeA)
                listTimeB.append(timeB)
            listTimeA = np.asarray(listTimeA)
            listTimeB = np.asarray(listTimeB)
            meanTimeA = np.mean(listTimeA)
            meanTimeB = np.mean(listTimeB)
            meanTimeAB = np.mean(listTimeA*listTimeB)
            varTimeA = np.var(listTimeA)
            varTimeB = np.var(listTimeB)
            Pab.append((meanTimeAB-meanTimeA*meanTimeB)/(varTimeA*varTimeB))

        ax[k].set_xscale('log')
        ax[k].plot(R,Pab,'*',label='sim')
        ax[k].plot(R, analyt(R),label='analytic')
        ax[k].set_ylabel('Pab')
        ax[k].set_xlabel('R')
        ax[k].legend(loc='upper right', shadow=True)
        ax[k].set_title('N = '+str(n[k]))
    plt.show()


if __name__ == '__main__':
    main()