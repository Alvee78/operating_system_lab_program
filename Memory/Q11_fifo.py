# Question 11 — FIFO Page Replacement
# Write a program to implement the First-In First-Out (FIFO) page replacement algorithm.
# The program should:
# •	accept page reference string 
# •	accept number of frames 
# •	count page faults and page hits

from collections import deque

def fifo(pages, frames):
    q = deque()
    s = set()

    hits = faults = 0

    for p in pages:
        if p in s:
            hits += 1
        else:
            faults += 1

            if len(q) == frames:
                old = q.popleft()
                s.remove(old)

            q.append(p)
            s.add(p)

    print("Page Hits:", hits)
    print("Page Faults:", faults)

pages = [7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1]
frames = 3

fifo(pages, frames)