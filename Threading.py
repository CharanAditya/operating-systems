import os

pid = os.fork()

if pid > 0:
    # Parent process
    print(f"Hello from Parent [PID : {os.getpid()}]")
else:
    # Child process
    print(f"Hello from Child [PID : {os.getpid()}]")