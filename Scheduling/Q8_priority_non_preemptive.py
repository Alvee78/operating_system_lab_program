# Question 8 — Priority Scheduling
# Write a program to implement:
# •	Non-preemptive priority scheduling
# Calculate:
# •	Completion Time 
# •	Waiting Time 
# •	Turnaround Time

from typing import List
import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority

        # these will be computed later
        self.completion = 0
        self.turnaround = 0
        self.waiting = 0
        self.response = -1  # first time CPU gets it


def read_input(filename="input.txt"):
    processes = []

    with open(filename, "r") as f:
        for line in f:
            pid, at, bt, pr = map(int, line.strip().split())
            processes.append(Process(pid, at, bt, pr))

    return processes

def calculate_metrics(processes, start_times):
    """
    start_times: dictionary {pid: first_time_process_started}
    """

    for p in processes:
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst
        p.response = start_times[p.pid] - p.arrival

class GanttSegment:
    def __init__(self, pid, start, end):
        self.pid = pid
        self.start = start
        self.end = end

def print_result(processes):
    print("\nPID  AT  BT  CT  TAT  WT  RT")

    total_wt = total_tat = total_rt = 0

    for p in processes:
        total_wt += p.waiting
        total_tat += p.turnaround
        total_rt += p.response

        print(f"{p.pid:3} {p.arrival:3} {p.burst:3} "
              f"{p.completion:3} {p.turnaround:4} {p.waiting:4} {p.response:4}")

    n = len(processes)
    print("\nAvg Waiting Time   :", total_wt / n)
    print("Avg Turnaround Time:", total_tat / n)
    print("Avg Response Time  :", total_rt / n)



def pnp(processes: List[Process]):
    n = len(processes)
    processes.sort(key=lambda p: p.arrival)
    start_times = {}
    segment = []

    time = 0;
    tmp = processes.copy()
    
    while tmp:
        pq = []
        for idx , p in enumerate(tmp):
            if p.arrival <= time:
                pq.append((p.priority,p.arrival, idx, p))
        if not pq:
            time = min(p.arrival for p in tmp)
            continue
        
        pq.sort()

        _,_,idx,p = pq[0]

        tmp.pop(idx)

        start_times[p.pid] = time
        time += p.burst
        p.completion = time
        segment.append(GanttSegment(p.pid, start_times[p.pid], time))
    calculate_metrics(processes, start_times)
    return segment

def plot(segment: List[GanttSegment]):
    times = [s.start for s in segment] + [s.end for s in segment] 
    times.sort()
    plt.stem(times, [2] * len(times))
    for s in segment:
        mid = (s.start + s.end)/2
        plt.text(mid,1,s.pid)
    plt.xticks(range(int(min(times)), int(max(times)) + 1))
    plt.show()


content = read_input()
segment = pnp(content)
print_result(content)
plot(segment)

