'''This file calculates the confidence intervals'''
from math import sqrt
'''rt is all the response times'''
'''vrt is the response times of job #3000+'''
'''mssrt is mean steady state response times'''
for i in range(95,111):
    rt = [] 
    vrt = []
    mssrt = []
    for j in range(1,31):
        with open('result' + str(i/10) + '/departure_' + str(j) + '.txt') as file:
            for line in file:
                l = line.split('\t')
                t = float(l[1]) - float(l[0])
                rt.append(t)
        vrt = rt[3000:]
        mssrt.append(round(sum(vrt)/len(vrt),3))
    T = sum(mssrt)/len(mssrt)
    st = 0
    for k in range(len(mssrt)):
        st += (T - mssrt[k])**2
    S = sqrt(st/(len(mssrt)-1))
    left = round(T - 2.045*(S/sqrt(30)),3)
    right = round(T + 2.045*(S/sqrt(30)),3)
    print('at Tc=',i/10,'confidence interval is [',left,',',right,']')
