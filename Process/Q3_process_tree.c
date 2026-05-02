// Question 3-Process
// Create two child processes from one parent process and display the process tree.
// Command: pstree -p 
//          pstree -p [process_id]

#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid1, pid2;

    printf("Parent process started. PID = %d\n", getpid());

    pid1 = fork();  // first child

    if (pid1 < 0) {
        printf("Fork failed!\n");
        return 1;
    }

    if (pid1 == 0) {
        // First child
        printf("Child 1: PID = %d, PPID = %d, PID2 = %d\n", getpid(), getppid(), pid2);
    }
    else {
        // Only parent executes this

        pid2 = fork();  // second child

        if (pid2 < 0) {
            printf("Second fork failed!\n");
            return 1;
        }

        if (pid2 == 0) {
            // Second child
            printf("Child 2: PID = %d, PPID = %d, PID1 = %d\n", getpid(), getppid(), pid1);
        }
        else {
            // Parent
            printf("Parent: PID = %d, Child1 PID = %d, Child2 PID = %d\n",
                   getpid(), pid1, pid2);
        }

    }
    while(1);
    return 0;
}