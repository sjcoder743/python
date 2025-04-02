def round_robin(processes, time_quantum):
    n = len(processes)
    remaining_time = {pid: burst for pid, _, burst in processes}  # Remaining burst time
    time, waiting_time, turnaround_time, completion_time = 0, {}, {}, {}

    queue = [p for p in processes]  # Copy process list
    print("\nProcess\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")

    while queue:
        pid, arrival, burst = queue.pop(0)

        if remaining_time[pid] > time_quantum:
            time += time_quantum
            remaining_time[pid] -= time_quantum
            queue.append((pid, arrival, burst))  # Add back to queue
        else:
            time += remaining_time[pid]
            remaining_time[pid] = 0
            completion_time[pid] = time
            turnaround_time[pid] = completion_time[pid] - arrival
            waiting_time[pid] = turnaround_time[pid] - burst

    for pid, arrival, burst in processes:
        print(f"{pid}\t{arrival}\t{burst}\t{completion_time[pid]}\t\t{turnaround_time[pid]}\t\t{waiting_time[pid]}")

# Example Usage
processes = [(1, 0, 6), (2, 1, 8), (3, 2, 7), (4, 3, 3)]
time_quantum = 3
round_robin(processes, time_quantum)