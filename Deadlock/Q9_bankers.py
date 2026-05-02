# Question 9 — Banker’s Algorithm
# Write a program to implement the Banker’s Algorithm for deadlock avoidance.
# The program should:
# •	take Allocation, Maximum, and Available matrices as input 
# •	determine whether the system is in a safe state 
# •	display the safe sequence

import numpy as np

def safety(allocation, available, max):
    need = max - allocation
    work = available.copy()

    n = allocation.shape[0]
    safe_sequence = []

    finish = np.zeros(n, dtype="bool")

    for k in range(n):
        for i in range(n):
            if not finish[i]  and np.all(need[i] <= work):
                work += allocation[i]
                finish[i] = True
                safe_sequence.append(i+1)
    
    if np.sum(finish) == n:
        return True, safe_sequence
    else:
        return False, []


# Resource allocation

def res_alloc(allocation, available, max, request, pid):
    need = max - allocation
    n = allocation.shape[0]

    if np.all(request <= need[pid]) and np.all(request <= available):
        allocation[pid] += request
        need[pid] -= request
        available -= request
        flag ,sequence = safety(allocation, available, max)

        if flag:
            return flag, sequence
        else:
            # Roll back
            allocation[pid] -= request
            need[pid] += request
            available += request
            return flag, []


available = np.array([2, 3, 2])
max = np.array([[7, 6, 3],
                [3, 2, 2], 
                [8, 0, 2],
                [2, 1, 2],
                [5, 2, 3]])
allocation = np.array([[0, 0, 1], 
                [3, 0, 0], 
                [1, 0, 1], 
                [2, 3, 2],
                [0, 0, 3]])

flag , seq = safety(allocation,available,max)
print(flag, seq)