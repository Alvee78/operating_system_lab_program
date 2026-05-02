// Question 2-Process
// Write a program where:
// •	parent prints numbers 1–5 
// •	child prints numbers 6–10 
// Observe execution order.


#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h> 

int main() {
    pid_t pid;

    pid = fork();  // create child process

    if (pid < 0) {
        printf("Fork failed!\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process prints 6–10
        printf("Child Process:\n");
        for (int i = 6; i <= 10; i++) {
            printf("%d\n", i);
        }
    }
    else {
        // Parent process prints 1–5
        printf("Parent Process:\n");
        for (int i = 1; i <= 5; i++) {
            printf("%d\n", i);
        }
    }

    return 0;
}