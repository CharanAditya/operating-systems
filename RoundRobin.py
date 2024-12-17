# Round Robin Algorithm
# 22BCE0166
# Charan Aditya Ravichandran


# Define the function
def roundRobin():

    # Get the input values
    number_of_processes = int(input("\nEnter the number of processes : "))
    time_quantum = int(input("\nEnter the Time Quantum (units) : "))

    process_id = []
    arrival_times = []
    burst_times = []
    process_list = []
    for i in range(number_of_processes):
        process_id.append(i+1)
        arrival_times.append(int(input(f"\nEnter the Arrival time of the Process {i+1} : ")))
        burst_times.append(int(input(f"Enter the Burst Time of the Process {i+1} : ")))
        process_list.append([process_id[i],arrival_times[i],burst_times[i]])

    gantt = []
    t = 0
    completion_times = [0]*number_of_processes
    waiting_times = [0]*number_of_processes
    turnaround_times = [0]*number_of_processes

    # Sort with respect to the arrival times
    process_list.sort(key=lambda x : (x[1] , x[0]))

    queue = []
    response_given = [0]*number_of_processes
    for p in process_list:
        if p[1] <= t:
            response_given[p[0]-1] = 1
            queue.append(p)

    completed = 0
    context_switches = 1
    # Service the processes
    while completed < number_of_processes:
        if queue == []:
            gantt.append("Idle")
            t=t+1
            for p in process_list:
                if p[1] <= t and response_given[p[0] - 1] == 0:
                    response_given[p[0]-1] = 1
                    queue.append(p)
        else:
            chosen_process = queue.pop(0)
            gantt.append(f"{chosen_process[0]}")

            rem_burst = chosen_process[2]

            if rem_burst <= time_quantum:
                t =t+ rem_burst
                completion_times[chosen_process[0] -1] = t
                turnaround_times[chosen_process[0] -1] = t - chosen_process[1]
                waiting_times[chosen_process[0] -1] = turnaround_times[chosen_process[0] -1] - burst_times[chosen_process[0]-1]
                completed += 1
                for p in process_list:
                    if p[1] <= t and response_given[p[0]-1] == 0:
                        response_given[p[0]-1] = 1
                        queue.append(p)
            else:
                t =t+ time_quantum
                chosen_process[2] = rem_burst-time_quantum
                for p in process_list:
                    if p[1] <= t and response_given[p[0]-1] == 0:
                        response_given[p[0]-1] = 1
                        queue.append(p)
                queue.append(chosen_process)

            if len(queue) > 0:
                context_switches += 1
    # Display the table
    
    print("\n\nProcess\t\tA.T\t\tB.T\t\tC.T\t\tTA.T\t\tW.T\n\n")
    for i in range(number_of_processes):
        print(f"P{i+1}\t\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")

    avg_wt = sum(waiting_times)/number_of_processes
    avg_tt = sum(turnaround_times)/number_of_processes
    print(f"\nAverage Waiting time = {avg_wt} units")
    print(f"Average Turn Around time = {avg_tt} units")
    print(f"No. of context switches : {context_switches}")

    print("\nGantt Chart :")
    print(gantt)
    print()

roundRobin()