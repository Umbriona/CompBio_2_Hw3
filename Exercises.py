import numpy as np

def Question1(populationSize):

    f11 = lambda x: (117-53*x)/populationSize
    f21 = lambda x: (114+53*x)/populationSize
    f12 = lambda x: (85+53*x)/populationSize
    f22 = lambda x: (58-53*x)/populationSize
    listF = [f11, f21, f12, f22]

    p1 = 202/populationSize
    p2 = 172/populationSize
    q1 = 231/populationSize
    q2 = 143/populationSize
    listPQ = [p1, p2, q1, q2]

    for