# Question 7 — Round Robin Scheduling
# Implement Round Robin Scheduling using a user-defined time quantum.
# Display:
# •	Gantt Chart 
# •	Waiting Time 
# •	Turnaround Time

from typing import List
import matplotlib.pyplot as plt
from collections import deque
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
        self.remaining = burst


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

# def plot(segment: List[GanttSegment]):
#     times = [s.start for s in segment] + [s.end for s in segment] 
#     times.sort()
#     plt.stem(times, [2] * len(times))
#     for s in segment:
#         mid = (s.start + s.end)/2
#         plt.text(mid,1,s.pid)
#     plt.xticks(range(int(min(times)), int(max(times)) + 1))
#     plt.show()

import matplotlib.pyplot as plt

def plot(s):
    c = {}
    for x in s:
        c.setdefault(x.pid, plt.cm.tab10(len(c)))
        plt.barh(0, x.end-x.start, left=x.start, color=c[x.pid])
        plt.text((x.start+x.end)/2,0,f"P{x.pid}",ha='center',va='center')
    plt.xticks(range(s[0].start, s[-1].end+1))
    plt.show()

def round_robin(processes: List[Process], tt = 2):
    n = len(processes)
    processes.sort(key= lambda p: p.arrival)
    
    start_times = {}
    segments = []
    time = 0
    completed = 0
    tmp = deque()
    i = 0
    while(i<n or tmp):
        
        while i< n and processes[i].arrival <= time:
            tmp.append(processes[i])
            i += 1

        if not tmp:
            time = processes[i].arrival
            continue

        a = tmp.popleft()
        run = min(tt, a.remaining)
        if a.pid not in start_times:
            start_times[a.pid] = time
        time += run
        segments.append(GanttSegment(a.pid,time-run, time))

        while i < n and processes[i].arrival <= time:
            tmp.append(processes[i])
            i += 1
        
        a.remaining -= run
        if (a.remaining <= 0):
            a.completion = time
        else:
            tmp.append(a)

    calculate_metrics(processes, start_times)
    return segments

p = read_input()
s = round_robin(p, 4)
print_result(p)
plot(s)
        


