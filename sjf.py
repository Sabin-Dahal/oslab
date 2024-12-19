arrival_time_unsorted = {
    "P1": [0, 6],  # First index is the arrival time, second index is the burst time
    "P2": [1, 5],
    "P3": [4, 3],
    "P4": [3, 4],
    "P5": [6, 3]
}

# Sort by arrival time first
arrival_time_sorted = {key: val for key, val in sorted(arrival_time_unsorted.items(), key=lambda ele: ele[1][0])}

# Now sort by burst time for processes that have arrived by the current time
waiting = []
turnaround = []
finishtime = []
gantchart = []
val_fin = 0
completed_processes = []

while len(completed_processes) < len(arrival_time_sorted):
    # Filter processes that have arrived by the current time (val_fin)
    available_processes = {key: val for key, val in arrival_time_sorted.items() if val[0] <= val_fin and key not in completed_processes}
    
    # If there are no available processes, move time forward to the next process's arrival
    if not available_processes:
        val_fin = min([val[0] for key, val in arrival_time_sorted.items() if key not in completed_processes])
        continue
    
    # Select the process with the shortest burst time
    current_process = min(available_processes, key=lambda key: arrival_time_sorted[key][1])
    
    # Update Gantt chart, finish time, turnaround time, and waiting time
    val_fin += arrival_time_sorted[current_process][1]
    finishtime.append(val_fin)
    trntime = val_fin - arrival_time_sorted[current_process][0]
    turnaround.append(trntime)
    gantchart.append(current_process)
    wtime = trntime - arrival_time_sorted[current_process][1]
    waiting.append(wtime)
    
    # Mark process as completed
    completed_processes.append(current_process)

# Display results
print(f"Execution Order  Finish Time   Turnaround Time   Waiting Time")
# print("Task will be scheduled as: (represented with finish time, turnaround time, and waiting time as columns respectively)")
for i in range(len(gantchart)):
    print(f"{gantchart[i]:<18}{finishtime[i]:<15}{turnaround[i]:<16}{waiting[i]:<12}")
 
print(f"Average waiting time is {sum(waiting)/len(waiting):.2f}")
print(f"Average turnaround time is {sum(turnaround)/len(turnaround):.2f}")
