# Scheduling Algorithms

This module contains implementations of common CPU scheduling algorithms using Python for the Operating System Lab.

All algorithms take input from a common `input.txt` file.



## Input Format

The input is provided through a file named `input.txt`.

Each line represents a process with the following format:

```id="y4k9ds"
PID Arrival_Time Burst_Time Priority
```

### Example

```
1 0 3 2
2 2 1 1
3 3 4 3
```



## Field Description

| Field        | Description                                             |
| ------------ | ------------------------------------------------------- |
| PID          | Process ID                                              |
| Arrival Time | Time at which process arrives                           |
| Burst Time   | CPU execution time required                             |
| Priority     | Priority of the process (lower value = higher priority) |



## Implemented Algorithms

### FCFS (First Come First Serve)

* Non-preemptive
* Processes are executed in order of arrival



### SJF (Shortest Job First)

* Non-preemptive
* Process with the smallest burst time is selected



### SRTF (Shortest Remaining Time First)

* Preemptive version of SJF
* Process with the shortest remaining time is executed



### Round Robin

* Preemptive
* Each process gets a fixed time quantum
* Executes processes in cyclic order



### Priority Scheduling (Preemptive)

* CPU is assigned based on priority
* Higher priority processes can interrupt lower priority ones



### Priority Scheduling (Non-Preemptive)

* Process with the highest priority executes fully once started
* No interruption during execution



## How to Run

1. Create an `input.txt` file in the project directory
2. Add process data following the specified format
3. Run any scheduling algorithm script

Example:

```
python fcfs.py
```



## Notes

* All programs read input from `input.txt`
* Ensure correct spacing between values
* Priority: lower number means higher priority
* Round Robin may require a time quantum (defined in code)
