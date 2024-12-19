class Process:
    def __init__(self, pid, priority, burst_time, arrival_time=0):
        self.pid = pid
        self.priority = priority
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.turnaround_time = 0
        self.waiting_time = 0
        self.arrival_time = arrival_time

def non_preemptive_priority(processes):
    time = 0
    gantt_chart = []
    completed_processes = 0
    total_processes = len(processes)

    while completed_processes < total_processes:
        # Filter available processes that have arrived and are not completed
        available_processes = [p for p in processes if p.arrival_time <= time and p.remaining_time > 0]

        if available_processes:
            # Select the process with the highest priority (lowest priority number)
            current_process = min(available_processes, key=lambda p: (p.priority, p.arrival_time))
            gantt_chart.append(current_process.pid)  # Track Gantt chart
            
            # Simulate process execution
            time += current_process.remaining_time  # Complete this process
            current_process.remaining_time = 0  # Mark as completed
            current_process.turnaround_time = time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            
            completed_processes += 1  # Increment completed processes
        else:
            time += 1  # Increment time if no processes are available

    return gantt_chart

def print_gantt_chart(gantt_chart, processes):
    print("\nGantt Chart:")
    for process_id in gantt_chart:
        print(f"| P{process_id} ", end="")
    print("|")

    # Print the time markers
    time = 0
    print(f"{time}", end="")
    for process_id in gantt_chart:
        # Find the corresponding process to get its burst time
        process = next(p for p in processes if p.pid == process_id)
        time += process.burst_time  # Use burst time for time increment
        print(f"{time}", end="")
    print()

def main():
    # Hardcoded processes
    processes = [
        Process(1, 3, 4, 0),  # Process 1: Priority 3, Burst time 4, Arrival time 0
        Process(2, 1, 2, 2),  # Process 2: Priority 1, Burst time 2, Arrival time 2
        Process(3, 4, 1, 1),  # Process 3: Priority 4, Burst time 1, Arrival time 1
        Process(4, 2, 8, 3),  # Process 4: Priority 2, Burst time 8, Arrival time 3
        Process(5, 5, 3, 5)
    ]
    
    gantt_chart = non_preemptive_priority(processes)

    # Output results
    print("\nProcess\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
    total_wait_time = total_turnaround_time = 0

    for process in processes:
        print(f"{process.pid}\t{process.priority}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
        total_wait_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

    print(f"\nAverage waiting time: {total_wait_time / len(processes):.2f}")
    print(f"Average turnaround time: {total_turnaround_time / len(processes):.2f}")

    print_gantt_chart(gantt_chart, processes)

if __name__ == "__main__":
    main()
