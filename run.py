import matplotlib.pyplot as plt
from numpy import linspace
import sys
from wrapper import run

print('random mode only')
print('single simulation mode')
seed_value = int(input('input seed_value(positive integer, -1 for replication mode):'))
if seed_value > 0:
    Tc = float(input('input Tc(positive float point, -1 to use defaut value):'))
    time_end = float(input('input time_end(positive float point,-1 to use defaut value):'))
    run(seed_value, Tc, time_end)
    print('finish, press enter to exit.')
    sys.stdin.readline()
else:
    print('replication mode.')
    for j in range(95,111):
        Tc = j/10
        print(Tc)
        for i in range(30):
            run(i+1, Tc, 30000)
##    x=linspace(1,30)
##    y=[run(i, 10, 10000) for i in x]
##    plt.title('mrt with Tc increasing')
##    plt.xlabel('Tc')
##    plt.ylabel('mrt')
##    plt.plot(x,y)
##    plt.show()


##    seed_value = int(input('input seed_value(positive integer):'))
##    Tc = float(input('input Tc(positive float point, -1 to use defaut value):'))
##    time_end = float(input('input time_end(positive float point,-1 to use defaut value):'))
    
    
