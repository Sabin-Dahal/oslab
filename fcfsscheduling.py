import math as mt
arrival_time_unsorted = {
    "P1": [0,6],   #here first index for list value for key is arrival time while the second index is burst time
    "P2": [1,5],
    "P3": [4,3],
    "P4": [3,4],
    "P5": [6,3]
}
arrival_time = {key: val for key, val in sorted(arrival_time_unsorted.items(), key = lambda ele: ele[1])}
print(f"Execution Order  Finish Time   Turnaround Time   Waiting Time")
# print("Task will be scheduled as: (represented with finish time, turnaround time and waiting time as columns respectively)")


waiting = []
turnaround = []
finishtime = []
gantchart =[]
val_fin = 0
for keys in arrival_time:
    val_fin += arrival_time[keys][1]
    finishtime.append(val_fin)
    trntime = val_fin - arrival_time[keys][0]
    turnaround.append(trntime)
    gantchart.append(keys)
    wtime = trntime - arrival_time[keys][1]
    waiting.append(wtime)
   
# for _ in range (len(arrival_time_unsorted)):
for i in range(len(arrival_time)):
    print(f"{gantchart[i]:<18}{finishtime[i]:<15}{turnaround[i]:<16}{waiting[i]:<12}")
 
print(f"Average waiting time is {sum(waiting)/len(waiting)}")
print(f"Average turnaround time is {sum(turnaround)/len(turnaround)}")




   






