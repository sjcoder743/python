def priority_non_preemptive(processes):
    processes.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival time, then priority
    time, waiting_time, turnaround_time, completion_time = 0, {}, {}, {}

    print("\nProcess\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting")

    for pid, arrival, burst, priority in sorted(processes, key=lambda x: x[3]):  # Sort by priority
        if time < arrival:
            time = arrival  # CPU waits if no process available

        waiting_time[pid] = time - arrival
        completion_time[pid] = time + burst
        turnaround_time[pid] = completion_time[pid] - arrival

        print(f"{pid}\t{arrival}\t{burst}\t{priority}\t\t{completion_time[pid]}\t\t{turnaround_time[pid]}\t\t{waiting_time[pid]}")

        time += burst  # Move time forward

# Example Usage:
processes = [(1, 0, 6, 2), (2, 1, 8, 1), (3, 2, 7, 3), (4, 3, 3, 2)]
priority_non_preemptive(processes)