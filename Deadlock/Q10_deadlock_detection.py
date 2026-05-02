# Question 10 — Deadlock Detection
# Write a program to detect deadlock in a system using:
# •	Allocation matrix 
# •	Request matrix 
# •	Available resources

import numpy as np

def detect(allocation, available, request):
   
    work = available.copy()

    n = allocation.shape[0]
    sf = []

    finish = np.zeros(n, dtype="bool")

    for i in range(n):
        if np.all(allocation[i] == 0):
            finish[i] = True



    for k in range(n):
        for i in range(n):
            if not finish[i]  and np.all(request[i] <= work):
                work += allocation[i]
                finish[i] = True
                sf.append(i+1)
    
    if np.sum(finish) == n:
        return True, sf
    else:
        return False, finish
    
allocation = np.array([
    [0,1,0],
    [2,0,0],
    [3,0,2],
    [2,1,1],
    [0,0,2]
])

request = np.array([
    [0,0,0],
    [2,0,2],
    [0,0,0],
    [1,0,0],
    [0,0,2]
])

available = np.array([0,0,0])

safe, res = detect(allocation, available, request)

if safe:
    print("No deadlock, safe sequence:", res)
else:
    print("Deadlock detected, processes:", res)