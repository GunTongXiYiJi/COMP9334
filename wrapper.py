'''This is the wrapper file.'''
'''Written by z5106189 for COMP9334 Project, Session 1, 2018.'''

import os, sys
from project import trace, random
def run(seed_value, Tc, time_end):
    cdir = os.getcwd()
    with open(cdir + '/num_tests.txt') as file:
        nt = int(file.read())
        '''nt is num of tests'''
        
    for i in range(1,nt+1):
        with open(cdir + '/mode_' + str(i) + '.txt') as file:
            mode = file.read().strip()
            '''Depending on mode, trace(i) or random(i) will be called'''
            '''They are defined in project.py'''
            if mode == 'trace':
                #trace
                print(mode)###
                mrt,depart_time = trace(i,cdir)
                print('mean response time is',mrt)###      
            else:
                #random
                print(mode)###
                mrt,depart_time = random(i,cdir, seed_value, Tc,time_end)
                print('mean response time is',mrt)###
                
            try:
                name = 'result'
                #name = 'result' + str(Tc)#replication mode
                os.mkdir(name)
            except FileExistsError:
                pass
            
            file1 = open(name + '/mrt_' + str(i) + '.txt', 'w+')
            file1.write('{:.3f}\n'.format(mrt))
            file1.close()
            file = open(name + '/departure_' + str(i) + '.txt', 'w+')
            #file = open(name + '/departure_' + str(seed_value) + '.txt', 'w+')#replication mode
            for e in depart_time:
                file.write('{:.3f}\t{:.3f}\n'.format(e[0],e[1]))
                #file.write('{:.3f}\t{:.3f}\t{:.3f}\n'.format(e[0],e[1],e[2]))
            file.close()
    return mrt  
    

if __name__ == '__main__':
    run(1, -1, -1)
    print('finish, press enter to exit.')
    sys.stdin.readline()
