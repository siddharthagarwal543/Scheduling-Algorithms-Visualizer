def avg_wt_tat(data):
    for dct in data:
        dct['tat'] = dct['ct'] - dct['at']
        dct['wt'] = dct['tat'] - dct['bt']
    tot_wt = tot_tat = 0
    for dct in data:
        tot_wt += dct['wt']
        tot_tat += dct['tat']
    ln = len(data)
    return {'avg_tat': tot_tat/ln, 'avg_wt': tot_wt/ln}


def first_come_first_serve(data):
    arrival_time = []
    indx = 0
    for i in data:
        arrival_time.append([i['at'], i['id'], indx,i['id']])
        indx += 1
    arrival_time.sort()
    curr_time = 0
    lst=[]
    for val in arrival_time:
        if data[val[2]]['at'] > curr_time:
            curr_time += data[val[2]]['at'] - curr_time
        curr_time += data[val[2]]['bt']
        data[val[2]]['ct'] = curr_time
        lst.append([curr_time,val[3]])
    cht = "|"
    tm = "0"
    for i in lst:
        cht += i[0]//2*'_' + str(i[1]) + i[0]//2*'_' + '|'  #i[0]=current slice completion time,i[1]=id of current slice process
        tm += " "*(i[0]+len(i[1])) + str(i[0])
    print(cht)
    print(tm)  
    return data


data = [{'id': '1', 'at': 0, 'bt': 3},
        {'id': '2', 'at': 1, 'bt': 6}, {
    'id': '3', 'at': 4, 'bt': 4},
    {'id': '4', 'at': 6, 'bt': 2}]


def round_robin(data, tq):
    rr = []
    indx = 0
    curr_time = 0
    flag = True

    for dct in data:
        rr.append([dct['at'], dct['bt'], indx,dct['id']])
        indx += 1
    count=0
    lst=[]#Gantt chart
    while count!=len(data):
        for i in range(len(rr)):
            bt = rr[i][1]
            if bt != 0 and rr[i][0] <= curr_time or curr_time == 0:
                temp=[]#details of current slice
                if bt > tq:
                    rr[i][1] -= tq
                    curr_time += tq
                else:
                    rr[i][1] = 0
                    curr_time += bt
                    data[rr[i][2]]['ct'] = curr_time
                    count+=1
                temp.append(curr_time)
                temp.append(rr[i][3]) #taking id of current process
                lst.append(temp)
            if count==len(data):
                break
    cht = "|"
    tm = "0"
    for i in lst:
        cht += i[0]//2*'_' + str(i[1]) + i[0]//2*'_' + '|'  #i[0]=current slice completion time,i[1]=id of current slice process
        tm += " "*(i[0]+len(i[1])) + str(i[0])
    print(cht)
    print(tm)  
    return data


def shortest_job_first(data):
    sjf = []
    indx = 0
    curr_time = 0
    for dct in data:
        sjf.append([dct['bt'], dct['at'], indx,dct['id']])
        indx += 1
    sjf.sort()
    lst=[]#gantt chart, format [CT,ID]
    while sjf:
        for val in sjf:
            if val[1] <= curr_time:
                curr_time += data[val[2]]['bt']
                data[val[2]]['ct'] = curr_time
                sjf.remove(val) 
                lst.append([curr_time,val[3]])
    cht = "|"
    tm = "0"
    for i in lst:
        cht += i[0]//2*'_' + str(i[1]) + i[0]//2*'_' + '|'  #i[0]=current slice completion time,i[1]=id of current slice process
        tm += " "*(i[0]+len(i[1])) + str(i[0])
    print(cht)
    print(tm)  
    return data


def shortest_remaining_time(data):
    def find_min_rt_arrived(curr_time, lst):
        lst.sort(key=lambda x: x[1])
        for i in lst:
            if curr_time >= i[0]:
                return i[2], True

    def all_done(lst):
        for i in lst:
            if i[1] != 0:
                return False
        return True

    def reduce_bt(indx, lst):
        for i in range(len(lst)):
            if lst[i][2] == indx:
                lst[i][1] -= 1
                if lst[i][1] == 0:
                    del lst[i]
                    return lst, True
        return lst, False
    srtf = []
    indx = 0
    curr_time = 0
    for dct in data:
        srtf.append([dct['at'], dct['bt'], indx,dct['id']])
        indx += 1
    srtf.sort()
    lst=[]
    while not all_done(srtf):
        index, has_arrived = find_min_rt_arrived(curr_time, srtf)
        if has_arrived:
            curr_time += 1
            srtf, is_done = reduce_bt(index, srtf)
            if is_done:
                data[index]['ct'] = curr_time
            lst.append([curr_time,data[index]['id']])
    cht = "|"
    tm = "0"
    for i in lst:
        cht += i[0]//2*'_' + str(i[1]) + i[0]//2*'_' + '|'  #i[0]=current slice completion time,i[1]=id of current slice process
        tm += " "*(i[0]+len(i[1])) + str(i[0])
    print(cht)
    print(tm)  
    return data

#AT not working
def priority_non_preemptive(data):
    prior = []
    indx = 0
    curr_time = 0
    for i in data:
        prior.append([i['pr'], i['at'], i['bt'], indx,i['id']])
        indx += 1
    lst=[]
    prior.sort(reverse=True)
    for val in prior:
        curr_time += val[2]
        data[val[-2]]['ct'] = curr_time
        lst.append([curr_time,val[-1]])
    cht = "|"
    tm = "0"
    for i in lst:
        cht += i[0]//2*'_' + str(i[1]) + i[0]//2*'_' + '|'  #i[0]=current slice completion time,i[1]=id of current slice process
        tm += " "*(i[0]+len(i[1])) + str(i[0])
    print(cht)
    print(tm) 
    return data


def priority_preemptive(data):
    def find_max_prior_arrived(curr_time, lst):
        lst.sort(reverse=True)
        for i in lst:
            if curr_time >= i[1]:
                return i[3], True

    def all_done(lst):
        for i in lst:
            if i[2] != 0:
                return False
        return True

    def reduce_bt(indx, lst):
        for i in range(len(lst)):
            if lst[i][3] == indx:
                lst[i][2] -= 1
                if lst[i][2] == 0:
                    del lst[i]
                    return lst, True
        return lst, False
    prior = []
    indx = 0
    curr_time = 0
    for i in data:
        prior.append([i['pr'], i['at'], i['bt'], indx,i['id']])
        indx += 1
    lst=[]
    prior.sort(reverse=True)
    while not all_done(prior):
        index, has_arrived = find_max_prior_arrived(curr_time, prior)
        if has_arrived:
            curr_time += 1
            prior, is_done = reduce_bt(index, prior)
            if is_done:
                data[index]['ct'] = curr_time
        lst.append([curr_time,data[index]['id']])
    cht = "|"
    tm = "0"
    for i in lst:
        cht += i[0]//2*'_' + str(i[1]) + i[0]//2*'_' + '|'  #i[0]=current slice completion time,i[1]=id of current slice process
        tm += " "*(i[0]+len(i[1])) + str(i[0])
    print(cht)
    print(tm) 
    return data
