# Question 4 — FCFS Scheduling
# Write a program to implement First Come First Serve (FCFS) CPU scheduling algorithm and calculate:
# •	Waiting Time 
# •	Turnaround Time 
# •	Average Waiting Time 
# •	Average Turnaround Time

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

def read_input(filename = "input.txt"):
    processes = []

    with open(filename, 'r') as f:
        for line in f:
            pid, at, bt, pr = map(int, line.strip().split())
            processes.append(Process(pid, at, bt, pr))
    return processes

def calculate_metrics(processes: List[Process], start_times):

    for p in processes:
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst
        p.response = start_times[p.pid] - p.arrival


class Segment:
    def __init__(self, pid, start, end):
        self.pid = pid
        self.start = start
        self.end = end

def fcfs(processes: List[Process]):
    time = 0
    start_times = {}
    n = len(processes)

    processes.sort(key=lambda p: p.arrival, reverse=False)
    segments = []
    for p in processes:
        if(p.arrival > time):
            time = p.arrival
        start_times[p.pid] = time
        time += p.burst
        p.completion = time
        segments.append(Segment(p.pid, start_times[p.pid], time))

    calculate_metrics(processes, start_times)
    plot(segments)

def print_result(processes):
    print(f"{'PID':<5}{'Arrival':<10}{'Burst':<8}{'Waiting':<10}{'Turnaround':<12}{'Response':<10}")
    print("-" * 55)

    for p in processes:
        print(f"{p.pid:<5}{p.arrival:<10}{p.burst:<8}{p.waiting:<10}{p.turnaround:<12}{p.response:<10}")
    if processes:
        avg_turnaround = sum(p.turnaround for p in processes) / len(processes)
        print(f"{avg_turnaround:.4}")
        avg_waiting = sum(p.waiting for p in processes) / len(processes)
        print(f"{avg_waiting:.4}")
        avg_response = sum(p.response for p in processes) / len(processes)
        print(f"{avg_response:.4}")
    else:
        print("No processes")


# def plot(segments: List[Segment]):
#     times = [0] + [p.end for p in segments]
#     plt.stem(times, [2]*len(times))
#     for i, s in enumerate(segments):
#         mid = (times[i] + times[i+1]) / 2
#         plt.text(mid, 1, "P"+str(s.pid))
#     plt.show()

import matplotlib.pyplot as plt

def plot(s):
    for i, x in enumerate(s):
        plt.barh(0, x.end-x.start, left=x.start)
        plt.text((x.start+x.end)/2, 0, f"P{x.pid}", ha='center')
    plt.xticks(range(min(x.start for x in s), max(x.end for x in s)+1))
    plt.yticks([])
    plt.show()

processes = read_input()
fcfs(processes)
print_result(processes)




        