'''This file contains two functions, trace() for trace mode; random() for random mode.'''
'''Both of them should be invoked from wrapper.py.'''
'''This file is not supposed to be run directly.'''

from collections import deque
from random import expovariate, seed
from assist import simulation

'''trace() is invoked from wrapper.py'''
def trace(i,cdir):
    #configure part, read in all the files
    '''para_*.txt'''
    para = []
    with open(cdir + '/para_' + str(i) + '.txt') as file:
        for line in file:
            para.append(line.strip())
        
    '''arrival_*.txt''' 
    arrival = []
    with open(cdir + '/arrival_' + str(i) + '.txt') as file:
        for line in file:
            arrival.append(float(line.strip()))

    '''service_*.txt'''   
    service = deque()
    with open(cdir + '/service_' + str(i) + '.txt') as file:
        for line in file:
            service.append(float(line.strip()))
    mode = 'trace'
    Tc = -1
    time_end = '-1'
    depart_time = simulation(para, arrival, service, mode, Tc, time_end)
                
    total = 0
    for i in range(len(arrival)):
        depart_time[i].append(arrival[i])
        depart_time[i].reverse()
        total += depart_time[i][1] -depart_time[i][0]
    mrt = total/len(arrival)
    
    return mrt,depart_time
        
'''random() is invoked from wrapper.py'''
def random(i,cdir, seed_value, Tc, time_end):
    #configure part, read in all the files
    '''para_*.txt'''
    para = []
    with open(cdir + '/para_' + str(i) + '.txt') as file:
        for line in file:
            para.append(line.strip())
        if time_end < 0:
            time_end = float(para[-1])
        
    '''arrival_*.txt''' 
    with open(cdir + '/arrival_' + str(i) + '.txt') as file:
        for line in file:
            lambd = float(line.strip())

    '''service_*.txt'''   
    with open(cdir + '/service_' + str(i) + '.txt') as file:
        for line in file:
            service_para = float(line.strip())

    #generate random arrivals and service times
    seed(seed_value)
    arrival = [0.000]
    while arrival[-1] <= time_end:
        arrival.append(round(arrival[-1] + expovariate(lambd),3))
    arrival.pop()

    seed(seed_value + 30)
    service = deque()
    for i in range(len(arrival)):
        num = 0.000
        for j in range(3):
            num += round(expovariate(service_para),3)
        service.append(num)
    mode = 'random'
    depart_time = simulation(para, arrival, service, mode, Tc, time_end)
    #service1 = service.copy()#######

    total = 0
    for i in range(len(depart_time)):
        depart_time[i].append(arrival[i])
        depart_time[i].reverse()
        total += depart_time[i][1] -depart_time[i][0]
    mrt = total/len(arrival)

##    for i in range(len(service1)):######
##        depart_time[i].append(service1[i])#######
    return mrt,depart_time
    
