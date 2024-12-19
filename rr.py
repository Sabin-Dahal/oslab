from collections import deque

class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.turnaround_time = 0
        self.waiting_time = 0

def round_robin(processes, time_quantum):
    time = 0
    process_queue = deque()
    processes_left = len(processes)
    gantt_chart = []

    # Enqueue processes that have arrived at time 0
    for process in processes:
        if process.arrival_time == 0:
            process_queue.append(process)

    while processes_left > 0:
        if process_queue:
            current_process = process_queue.popleft()
            gantt_chart.append(current_process.process_id)  # Track the Gantt chart
        else:
            time += 1
            continue

        # Calculate execution time
        execution_time = min(time_quantum, current_process.remaining_time)
        current_process.remaining_time -= execution_time
        time += execution_time

        # Add newly arrived processes (after the current process runs)
        for process in processes:
            if time - execution_time < process.arrival_time <= time:
                if process.remaining_time > 0:
                    process_queue.append(process)

        if current_process.remaining_time > 0:
            process_queue.append(current_process)  # Re-add current process if it still has remaining time
        else:
            current_process.turnaround_time = time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            processes_left -= 1  # Process finished

    return gantt_chart

def print_gantt_chart(gantt_chart):
    print("\nGantt Chart:")
    for process_id in gantt_chart:
        print(f"| P{process_id} ", end="")
    print("|")
    
    # Print the time markers
    time = 0
    print(f"{time}", end="")
    for process_id in gantt_chart:
        time += 3  # Each time quantum is 3 units
        print(f"{time}", end="")
    print()

def main():
    # Hardcoded processes
    processes = [
        Process(1, 0, 6),  # Process 1: arrival time 0, burst time 6
        Process(2, 1, 5),  # Process 2: arrival time 1, burst time 5
        Process(3, 3, 4),  # Process 3: arrival time 3, burst time 4
        Process(4, 4, 3),  # Process 4: arrival time 4, burst time 3
        Process(5, 6, 3)   # Process 5: arrival time 6, burst time 3
    ]
    time_quantum = 3  # Hardcoded time quantum
    gantt_chart = round_robin(processes, time_quantum)

    # Output results
    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    total_wait_time = total_turnaround_time = 0

    for process in processes:
        print(f"{process.process_id}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")
        total_wait_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

    print(f"\nAverage waiting time: {total_wait_time / len(processes):.2f}")
    print(f"Average turnaround time: {total_turnaround_time / len(processes):.2f}")

    print_gantt_chart(gantt_chart)

if __name__ == "__main__":
    main()
