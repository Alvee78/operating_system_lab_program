// Question 1-Process
// Write a C program that creates a child process using fork(). Print:
// •	Parent PID 
// •	Child PID 
// •	Parent Process ID (PPID) of child



#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;
    printf("Hello\n");
    pid = fork();  // create child process

    if (pid < 0) {
        // fork failed
        printf("Fork failed!\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process
        printf("Child Process:\n");
        printf("Child PID: %d\n", getpid());
        printf("Parent PID (PPID of child): %d\n", getppid());
    }
    else {
        // Parent process
        printf("Parent Process:\n");
        printf("Parent PID: %d\n", getpid());
        printf("Child PID: %d\n", pid);
    }
    return 0;
}