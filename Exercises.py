import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import random as rand
import math

def initiateSamle(sampleSize):
    sampleSize = int(sampleSize)
    sample = np.ones([sampleSize,2])
    return sample

def PoissonEvent(sample,R,sampleSize):
    count = 0
    for i in range(len(sample[:,0])-1):
        if((sample[i,0]!= 0 and sample[i,1]!= 0 ) and (sample[i,0]!= sampleSize and sample[i,1]!= sampleSize )):
            count += 1
    recombinationRate = count*R/2
    coalescentRate = scipy.special.comb(sampleSize,2)
    coalescentTime = -math.log(1.0 - rand.random()) / coalescentRate
    if(recombinationRate != 0):
        recombinationTime = -math.log(1.0 - rand.random()) / recombinationRate
    else:
        recombinationTime = coalescentTime+1
    if(recombinationTime<coalescentTime):
        Event = 'Recombination'
        Time = recombinationTime
    else:
        Event = 'Coalescent'
        Time = coalescentTime
    return [Event, Time]

def CoalescentEvent(sample):
    individual1 = rand.randint(0,len(sample[:,1])-1)
    individual2 = individual1
    while (individual1 == individual2):
        individual2 = rand.randint(0,len(sample[:,1])-1)
    temp = sample[individual1,:]+sample[individual2,:]
    return [individual1,individual2,temp]

def Recombination(sample,sampleSize):
    randi =  rand.randint(0, len(sample[:,0])-1)
    tempBol1 = sample[randi, 1] == 0 or sample[randi, 1] == sampleSize
    tempBol2 =   sample[randi, 0] == 0 or sample[randi, 0] == sampleSize

    while(tempBol1 or tempBol2):
        randi = rand.randint(0, len(sample[:,0])-1)
        tempBol1 = sample[randi, 1] == 0 or sample[randi, 1] == sampleSize
        tempBol2 = sample[randi, 0] == 0 or sample[randi, 0] == sampleSize
    individual = sample[:,randi]
    temp1 = np.transpose([0,individual[1]])
    temp0 = np.transpose([individual[0],0])
    sample = np.transpose(sample)
    np.random.shuffle(sample)
    sample = np.transpose(sample)
    return [temp0, temp1, randi]
def Question1(populationSize):

    def f11(x, populationSize):
        return (117-53*x)/populationSize
    def f21(x, populationSize):
        return (114+53*x)/populationSize
    def f12(x, populationSize):
        return (85+53*x)/populationSize
    def f22(x, populationSize):
        return (58-53*x)/populationSize


    listF = [f11, f21, f12, f22]

    p1 = 202/populationSize
    p2 = 172/populationSize
    q1 = 231/populationSize
    q2 = 143/populationSize
    listPQ = [p1*q1, p2*q1, p1*q2, p2*q2]

    def X(x,populationSize):
        return populationSize*((f11(x,populationSize)-listPQ[0])**2/listPQ[0]+ (f21(x,populationSize)-listPQ[1])**2/listPQ[1]+(f12(x,populationSize)-listPQ[2])**2/listPQ[2]+(f22(x,populationSize)-listPQ[3])**2/listPQ[3])

    x = np.linspace(0,1,100)
    flag = True
    i=1
    reject = ((X(x[0],populationSize)-7.81)**2)
    while flag:

        if((X(x[i],populationSize)-7.81)**2>reject):
            break
        else:
            reject = ((X(x[i],populationSize) - 7.81) ** 2)
        i += 1
    markX95 = x[i]
    markY95 = X(x[i],populationSize)
    markXList95 =  np.linspace(markX95,markX95,100)
    markYList95 = np.linspace(0, markY95, 100)
    chi95 = np.linspace(7.81,7.81,100)

    flag = True
    i=1
    reject = ((X(x[0],populationSize)-11.34)**2)
    while flag:

        if((X(x[i],populationSize)-11.34)**2>reject):
            break
        else:
            reject = ((X(x[i],populationSize) - 11.34) ** 2)
        i += 1
    markX99 = x[i]
    markY99 = X(x[i],populationSize)
    markXList99 =  np.linspace(markX99,markX99,100)
    markYList99 = np.linspace(0, markY99, 100)
    chi99= np.linspace(11.34,11.34,100)
    print('mark 95', markX95, '\nmark 99 ', markX99)

    plt.plot(x,X(x,populationSize),x,chi95,x,chi99,markXList95,markYList95,markXList99,markYList99)
    plt.axis([0, 1, 0, 175])
    plt.ylabel('X^2')
    plt.xlabel('x')
    plt.legend(['X^2','Chi 95: 3 degree of freedom ','Chi 99: 3 degree of freedom '])
    plt.show()

def Question2(sampleSize,R):
    timeA = 0
    timeB = 0
    flagA = True
    flagB = True
    sample = initiateSamle(sampleSize)
    #print(event,time)
    while (len(sample[:,0])>1):
        event,time = PoissonEvent(sample,R,sampleSize)
        if(event == 'Coalescent'):
            individual1, individual2, temp = CoalescentEvent(sample)
            sample = np.insert(sample,0,temp,axis=0)
            sample = np.delete(sample, individual1+1,axis=0)
            if (individual1 > individual2 ):
                sample = np.delete(sample, individual2+1, axis=0)
            else:
                sample = np.delete(sample, individual2, axis=0)
            if(sample is None):
                sample = temp

            np.random.shuffle(sample)


        elif(event == 'Recombination'):
            temp = Recombination(sample,sampleSize)
            sample = np.insert(sample, 0, temp[0], axis=0)
            sample = np.insert(sample, 0, temp[1], axis=0)
            sample = np.delete(sample,temp[2]+2,axis=0)
            np.random.shuffle(sample)
        if(np.amax(sample[:, 0]) < sampleSize or flagA == True):
            timeA += time
            if(True):
                flagA = False
        if(np.amax(sample[:, 1]) < sampleSize or flagB == True):
            timeB += time
            if(True):
                flagB = False
    return [timeA, timeB]
