# First Come First Serve Scheduling Algorithm
# 22BCE0166

# Define the function
def fcfs():
    # Get the number of inputs
    number_of_processes = int(input("\nEnter the number of processes : "))

    # Initialise the required variables
    process_id = []
    arrival_times = []
    burst_times = []

    # Get the input for each of the process
    for i in range(number_of_processes):
        process_id.append(i+1)
        arrival_times.append(int(input(f"\nEnter the Arrival time of the Process {i+1} : ")))
        burst_times.append(int(input(f"Enter the Burst Time of the Process {i+1} : ")))
    

    # Sort the processes according to the Arrival time, in case of same AT then use the process ID
    process_list = list(zip(process_id, arrival_times, burst_times))
    process_list.sort(key=lambda x: (x[1], x[0]))
    process_id,arrival_times,burst_times = zip(*process_list)

    completion_times = [0] * number_of_processes
    waiting_times = [0] * number_of_processes
    turnaround_times = [0] * number_of_processes

    gantt = []
    completed = 0
    t = 0
    current = 0

    # Do this unitl all processes are completed
    while completed < number_of_processes:
        if t < arrival_times[current]:
            gantt.append("Idle")
            t = arrival_times[current]
            continue

        gantt.append(f"P{process_id[current]}")
        t = t + burst_times[current]

        # Calculate the required attributes
        completion_times[current] = t
        turnaround_times[current] = completion_times[current] - arrival_times[current]
        waiting_times[current] = turnaround_times[current] - burst_times[current]
        current += 1
        completed += 1



    # Display the results    
    print("\n\nProcess\t\tA.T\t\tB.T\t\tC.T\t\tTA.T\t\tW.T\n\n")
    for i in range(number_of_processes):
        print(f"P{i+1}\t\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")

    # Calculate and display the Average Waiting time and Turnaround time
    avg_wt = sum(waiting_times) / number_of_processes
    avg_tt = sum(turnaround_times) / number_of_processes
    print(f"\nAverage Waiting time = {avg_wt} units")
    print(f"Average Turn Around time = {avg_tt} units")

    print("\nGantt Chart :")
    print(gantt)
    print()

fcfs()
