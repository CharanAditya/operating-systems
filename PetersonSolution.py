import threading
import time

# These are the shared variables for the Peterson's Solution
flag = [False, False]   # Flag array
turn = 0                # Turn variable - Decides whose turn it is to enter the critical section

# Number of iterations each process will execute
NUM_ITERATIONS = 5

# Critical Section
def critical_section(process_id):
    print(f"Process {process_id} is entering the critical section.")
    time.sleep(1) # To simulate the work of a CS
    print(f"Process {process_id} is leaving the critical section.")

# Peterson's Solution for Process 0
def process_0():
    global flag, turn
    for _ in range(NUM_ITERATIONS):
        # Entry Section
        flag[0] = True
        turn = 1
        while flag[1] and turn == 1:
            pass # Busy Wait

        # Critical Section
        critical_section(0)

        # Exit Section
        flag[0] = False

# Peterson's Solution for Process 1
def process_1():
    global flag, turn
    for _ in range(NUM_ITERATIONS):
         # Entry Section
        flag[1] = True
        turn = 0
        while flag[0] and turn == 0:
            pass # Busy Wait

        # Critical Section
        critical_section(1)

        # Exit Section
        flag[1] = False

# Main function to create threads and execute Peterson's Soltion
def main():
    thread_0 = threading.Thread(target=process_0)
    thread_1 = threading.Thread(target=process_1)

    thread_0.start()
    thread_1.start()

    thread_0.join()
    thread_1.join()

    print("Both processes have finished execution.")

if __name__ == "__main__":
    main()