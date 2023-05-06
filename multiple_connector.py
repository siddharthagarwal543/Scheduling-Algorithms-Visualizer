# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import sys 
# from tkinter import * 
# def priority_non_preemptive(data):
#     prior = []
#     indx = 0
#     curr_time = 0
#     for i in data:
#         prior.append([i['pr'], i['at'], i['bt'], indx,i['id']])
#         indx += 1
#     lst=[]
#     prior.sort(reverse=True)
#     for val in prior:
#         curr_time += val[2]
#         data[val[-2]]['ct'] = curr_time
#         lst.append([curr_time,val[-1],val[2]])
#     df=pd.DataFrame(lst)
#     df[0]=df[0]-1
#     print(lst)
#     plt.barh(y=df[1], width=df[2], left=df[0])
#     plt.show() 
#     return lst


# data=[{"id": "a", "at": 0, "bt":4 , "pr": 1, "ct": 8, "tat": 8, "wt": 6,"pr":1},
#   {"id": "b", "at": 1, "bt": 2, "pr": 2, "ct": 12, "tat": 12, "wt": 8,"pr":2}, 
#   {"id": "c", "at": 2, "bt": 1, "pr": 3, "ct": 6, "tat": 6, "wt": 0,"pr":3}]
# # print(shortest_remaining_time(data))
# df=pd.DataFrame(priority_non_preemptive(data))
# df[0]=df[0]-1
# plt.barh(y=df[1], width=1, left=df[0])
# plt.show()


# root = Tk()
# root.title("Detailed Table")
# root.geometry('580x250')
# txt = Text(root) 
# txt.pack() 

# class PrintToTXT(object): 
#  def write(self, s): 
#      txt.insert(END, s)

# sys.stdout = PrintToTXT() 
# print (df)

# mainloop()

from multiple_algorithms import *
import multiple_second_screen
import json
algos = {
    '1': first_come_first_serve,
    '2': shortest_job_first,
    '3': shortest_remaining_time,
    '4': priority_preemptive,
    '5': priority_non_preemptive,
    '6': round_robin
}

def algo_name(num):
    if(num=='1'):
        return "first_come_first_serve"
    elif (num=='2'):
        return "shortest_job_firs"
    elif (num=='3'):
        return "shortest_remaining_time"
    elif (num=='4'):
        return "priority_preemptive"
    elif (num=='5'):
        return "priority_non_preemptive"
    else:
        return "round_robin"
def main():
    with open('data.json', "r") as read_file:
        data = json.load(read_file)
    f = open('fl.txt')
    txt = next(f)
    txt = txt.strip('\n')
    ls=[]
    for i in txt:
        if(int(i)>0):
            ls.append(i)
    # print(ls)
    res=[]
    avg_tat=[]
    avg_wt=[]
    avg={}
    table=[]
    for i in ls:
        print((i))
        if i == '6':
            tq = next(f)
            f.close()
        if i == '6':
            temp=avg_wt_tat(algos[i](data, int(tq)))
        else:
            temp=avg_wt_tat(algos[i](data))
        print(temp)
        avg_tat.append([temp['avg_tat'],algo_name(i)])
        avg_wt.append([temp['avg_wt'],algo_name(i)])
        table.append([algo_name(i),temp['avg_tat'],temp['avg_wt']])
        
    avg_tat.sort()
    avg_wt.sort()
    avg={'avg_tat':avg_tat[0],'avg_wt':avg_wt[0]}
    print(avg_tat[0],avg_wt[0])
    data_f = open('data.json', 'w')
    data_f.write(json.dumps(table))
    data_f.close()
    return avg
