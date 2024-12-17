def preemptivePriority():

    number_of_processes = int(input("\nEnter the number of processes : "))

    process_id = []
    arrival_times = []
    burst_times = []
    priority = []
    process_list = []
    for i in range(number_of_processes):
        process_id.append(i+1)
        arrival_times.append(int(input(f"\nEnter the Arrival time of the Process {i+1} : ")))
        burst_times.append(int(input(f"Enter the Burst Time of the Process {i+1} : ")))
        priority.append(int(input(f"Enter the Priority of the Process {i+1} : ")))
        process_list.append([process_id[i],arrival_times[i],burst_times[i],priority[i]])


    gantt = []
    t = 0
    completion_times = [0]*number_of_processes
    waiting_times = [0]*number_of_processes
    turnaround_times = [0]*number_of_processes

    completed = 0
    # Do until the all the processes have completed their execution
    while completed < number_of_processes:
        available_processes = [p for p in process_list if p[1]<=t and p[2]>0]
        if available_processes:
            # Lower the value -> higher the priority
            current_process = min(available_processes, key=lambda x : (x[3] , x[1] , x[0]))
            process_list.remove(current_process)
            gantt.append(current_process[0])
            t+=1
            current_process[2] -= 1

            if current_process[2] == 0:
                completion_times[current_process[0] - 1] = t
                turnaround_times[current_process[0] - 1] = t - current_process[1]
                waiting_times[current_process[0] - 1] = turnaround_times[current_process[0] - 1] - burst_times[current_process[0] - 1]
                completed += 1
            else:
                process_list.append(current_process)
                
        else:
            gantt.append("Idle")
            t+=1


    # Display the table
    print("\n\nProcess\t\tA.T\t\tB.T\t\tC.T\t\tTA.T\t\tW.T\n\n")
    for i in range(number_of_processes):
        print(f"P{i+1}\t\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")

    avg_wt = sum(waiting_times)/number_of_processes
    avg_tt = sum(turnaround_times)/number_of_processes
    print(f"\nAverage Waiting time = {avg_wt} units")
    print(f"Average Turn Around time = {avg_tt} units")

    print("\n\nGantt Chart :")
    print(gantt)
    print()

preemptivePriority()