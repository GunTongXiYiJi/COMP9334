from collections import deque
def search_DEOFF(servers):
    p = []
    for e in servers:
        if e[0] == 'DEOFF':
            p.append(e)
    if p:
        p.sort(key = lambda x:x[1])
        return servers.index(p[-1])
    else:
        return -1
       
def search_SETUP(servers):
    p = []
    for e in servers:
        if e[0] == 'SETUP':
            p.append(e)
    if p:
        p.sort(key = lambda x:x[1])
        return servers.index(p[-1])
    else:
        print('Fatal error in search_SETUP(servers)')

def search_unmarked(dispatcher):
    for e in dispatcher:
        if e[2] == 'unmarked':
            return dispatcher.index(e)
    return -1

def event_del(event, index, state):
    for e in event:
        if len(e) == 4:
            if e[2] == index and e[3] == state:
                return event.index(e)

def simulation(para, arrival, service, mode, Tc, time_end):
    if mode == 'trace':
        m, setup_time, Tc = int(para[0]),float(para[1]),float(para[2])
    else:
        m, setup_time = int(para[0]),float(para[1])
        if Tc < 0:
            Tc = float(para[2])
    #simulation part
    '''initial state'''
    master_clock, dispatcher = 0.0, deque()
    '''server [state, time]'''
    servers = [['OFF',0] for _ in range(m)]
    '''record departure times'''
    depart_time = []
    job_index = 0
    event = deque()
    for e in arrival:
        event.append(['a', e])
        
    while event:
        try:
            if master_clock >= time_end:
                break
        except TypeError:
            pass
        e = event.popleft()
        #print(master_clock,servers)####
        #print(e)###
        #job arrival event
        if e[0] == 'a':
            job_index += 1
            master_clock = e[1]#######
            '''if we have a deoff server'''
            index = search_DEOFF(servers)####
            if index > -1:
                t = master_clock + service.popleft()
                servers[index] = ['BUSY', t]
                event.append(['s', t, index, 'BUSY'])
                event = deque(sorted(event, key = lambda x:x[1]))
                edel = event_del(event, index, 'DEOFF')####
                del(event[edel])
                depart_time.append([t])
                continue
            '''if we have a off server'''
            if ['OFF',0] in servers:
                marking = 'marked'
                index = servers.index(['OFF',0])
                servers[index] = ['SETUP',setup_time+master_clock]
                event.append(['s', setup_time+master_clock, index, 'SETUP'])
                event = deque(sorted(event, key = lambda x:x[1]))
            else:
                marking = 'unmarked'
            dispatcher.append([arrival[0],service[0],marking,job_index])
            service.popleft()
        #server event
        elif e[0] == 's':
            master_clock = e[1]####
            if servers[e[2]][0] == 'SETUP':
                try:
                    job = dispatcher.popleft()
                    servers[e[2]] = ['BUSY', master_clock + job[1]]
                    event.append(['s', master_clock + job[1], e[2], 'BUSY'])
                    event = deque(sorted(event, key = lambda x:x[1]))
                    depart_time.append([master_clock + job[1]])
                except IndexError:
                    print('Fatal error, setup to empty dispatcher')
            elif servers[e[2]][0] == 'BUSY':
                try:
                    '''try taking another job'''
                    job = dispatcher.popleft()
                    servers[e[2]] = ['BUSY', master_clock + job[1]]
                    event.append(['s', master_clock + job[1], e[2], 'BUSY'])
                    event = deque(sorted(event, key = lambda x:x[1]))
                    depart_time.append([master_clock + job[1]])
                    if job[2] == 'marked':
                        index = search_unmarked(dispatcher)###
                        if index > -1:
                            '''If there is at least a UNMARKED job'''
                            dispatcher[index][2] = 'marked'
                        else:
                            '''we need to turn off a SETUP server'''
                            index = search_SETUP(servers)###
                            servers[index] = ['OFF', 0]
                            edel = event_del(event, index, 'SETUP')
                            del(event[edel])
                except IndexError:
                    servers[e[2]] = ['DEOFF', master_clock + Tc]
                    event.append(['s', master_clock + Tc, e[2], 'DEOFF'])
                    event = deque(sorted(event, key = lambda x:x[1]))
            elif servers[e[2]][0] == 'DEOFF':
                servers[e[2]] = ['OFF', 0]
    print('simulation stops at',depart_time[-1][0],'s\nserver states are\n',servers)####
    
    return depart_time


            
