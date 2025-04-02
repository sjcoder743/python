

# FCFS CPU Scheduling Algorithm Simulation

def find_turnaround_time(processes, n, bt, wt, tat):
    # Calculate Turnaround Time
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def find_waiting_time(processes, n, bt, wt):
    # Calculate Waiting Time
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def find_average_time(processes, n, bt):
    wt = [0] * n
    tat = [0] * n

    # Find Waiting Time and Turnaround Time
    find_waiting_time(processes, n, bt, wt)
    find_turnaround_time(processes, n, bt, wt, tat)

    total_wt = sum(wt)
    total_tat = sum(tat)

    # Find average waiting time and turnaround time
    avg_wt = total_wt / n
    avg_tat = total_tat / n

    print("Process | Burst Time | Waiting Time | Turnaround Time")
    for i in range(n):
        print(f"  {processes[i]}    |     {bt[i]}     |      {wt[i]}     |      {tat[i]}")

    print(f"\Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

if __name__ == "__main__":
    # Input processes and burst time
    processes = [1, 2, 3, 4]  # Example processes (P1, P2, P3, P4)
    burst_time = [6, 8, 7, 3]  # Burst time for each process
    n = len(processes)

    # Call function to calculate and print average times
    find_average_time(processes, n, burst_time)