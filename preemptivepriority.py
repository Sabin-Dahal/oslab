# process = id, arrival, burst, priority
processes = [
    [1, 0, 6, 5],
    [2, 1, 5, 2],
    [3, 3, 4, 4],
    [4, 4, 3, 1],
    [5, 6, 3, 3]
]

waitingTime = [0 for i in range(len(processes))]
turnaroundTime = [0 for i in range(len(processes))]
queue = []
currentTime = 0   # oi kati bajyo?
while sum(process[2] for process in processes) != 0:    # sabbai process executed?
    # naya process ayo vanne thapdyu queue ma
    for process in processes:
        if process[0] not in queue and process[1] <= currentTime and process[2] != 0:
            queue.append(process[0])    # append process id
    # determine which process to run
    index = -1
    for processID in queue:
        for i, process in enumerate(processes):
            if process[0] == processID:         # process with this processID is in queue to run (select the one with highest priority (lowest value))
                waitingTime[i]+=1               # assume this process is not the chosen one
                if index==-1 or process[3] < processes[index][3]:
                    index = i                   # possible chosen one
    currentTime += 1    # time badyo tww
    if index == -1: continue    # oppse not process found
    waitingTime[index]-=1       # we assumed this is waiting but it isn't so correct it
    processes[index][2] -= 1    # reduce 1 timeframe from burst time
    # process completed case
    if processes[index][2] == 0:
        queue.remove(processes[index][0])   # remove from queue
        turnaroundTime[index] = currentTime - processes[index][1]   # calculate turnaround time


print("ID | arrival |priotity| burst | turnaround | waiting")
for i, process in enumerate(processes):
    # yeta burst time harako le we do turnaround - waiting
    print(f"{process[0]:<3}| {process[1]:<8}|{process[-1]:<8}|{turnaroundTime[i]-waitingTime[i]:<7}| {turnaroundTime[i]:<11}| {waitingTime[i]}")
# print turnaround and waiting
print(f"Average Turnaround= {sum(turnaroundTime)/len(processes)}ms")
print(f"Average Waiting= {sum(waitingTime)/len(processes)}ms")