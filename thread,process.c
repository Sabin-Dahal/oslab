Source Code:
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/wait.h&gt;
int main()
{
printf(“Lab: 2(a) Name: Kalpashree Sharma Roll no./Section: 01 ‘A’\n”);
pid_t pid;
pid = fork(); // create a child process
if (pid == -1)
{ // check for errors
perror(&quot;fork&quot;);
exit(EXIT_FAILURE);
}
if (pid == 0)
{ // child process
printf(&quot;Child process with PID %d has been created\n&quot;, getpid());
sleep(2); // sleep for 2 seconds
printf(&quot;Child process with PID %d is now terminating\n&quot;, getpid());
exit(EXIT_SUCCESS);
}
else
{ // parent process
printf(&quot;Parent process with PID %d has created a child with PID %d\n&quot;, getpid(), pid);
int status;
wait(&amp;status); // wait for child process to terminate
printf(&quot;Child process with PID %d has terminated with status %d\n&quot;, pid,
WEXITSTATUS(status));
}
return 0;
}

Output:

LAB 3. Thread Creation and Termination

WAP in C to demonstrate the thread creation and termination in Linux.
Theory: The function pthread_create is used to create a new thread, and a thread to terminate
itself uses the function pthread_exit. Each thread creation involves the creation of a new stack
where the new thread function will allocate its local variables or the local variables of the
functions it calls
Source Code:
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;pthread.h&gt;
void *thread_function(void *arg)
{
printf(&quot;Child thread executing...\n&quot;);
pthread_exit(NULL);
}
int main()
{
printf(“Lab: 2(a) Name: Kalpashree Sharma Roll no./Section: 01 ‘A’\n”);
pthread_t thread;
int thread_create_result;
int thread_join_result;
// Create a new thread
thread_create_result = pthread_create(&amp;thread, NULL, thread_function, NULL);
if (thread_create_result != 0)
{
printf(&quot;Error: Thread creation failed\n&quot;);
exit(EXIT_FAILURE);
}
printf(&quot;Main thread waiting for child thread to finish...\n&quot;);

// Wait for the thread to finish executing
thread_join_result = pthread_join(thread, NULL);
if (thread_join_result != 0)
{
printf(&quot;Error: Thread join failed\n&quot;);
exit(EXIT_FAILURE);
}
printf(&quot;Child thread has finished executing and has been joined with the main thread\n&quot;);
return 0;
}