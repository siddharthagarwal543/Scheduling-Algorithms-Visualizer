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


data=[{"id": "a", "at": 0, "bt":4 , "pr": 1, "ct": 8, "tat": 8, "wt": 6,"pr":1},
  {"id": "b", "at": 1, "bt": 2, "pr": 2, "ct": 12, "tat": 12, "wt": 8,"pr":2}, 
  {"id": "c", "at": 2, "bt": 1, "pr": 3, "ct": 6, "tat": 6, "wt": 0,"pr":3}]
print(shortest_remaining_time(data))