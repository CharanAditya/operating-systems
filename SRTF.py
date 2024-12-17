# SRTF (Pre-emptive)
# 22BCE0166

def srtf():
    #Get the required details
    number_of_processes = int(input("\nEnter the number of processes : "))
    processes = []
    arrival_times = []
    burst_times = []

    for i in range(number_of_processes):
        processes.append(i+1)
        arrival_times.append(int(input(f"\n\nEnter the Arrival time for process Process {i+1} : ")))
        burst_times.append(int(input(f"Enter the Burst time for the Process {i+1} : ")))

    #Sort in the order of increasing AT followed by BT
    process_info = list(zip(processes,arrival_times,burst_times))

    #Start the processing
    t = 0
    gantt = []
    completion_times = [0]*number_of_processes
    waiting_times = [0]*number_of_processes
    turnaround_times = [0]*number_of_processes

    #While there are processes that havent yet be completed
    while process_info != []:

        #Prepare the ready Queue
        available = []
        for p in process_info:
            if(p[1] <= t):
                available.append(p)

        if available == []    :
            t += 1
            gantt.append("Idle")
            continue
        else:
            available.sort(key=lambda x : (x[2] , x[1] , x[0]))
            process = list(available[0])
            copy_process = available.pop(0)
            t+=1
            gantt.append(process[0])
            
            #Update the Burst time of the process
            process[2] -= 1
            process_info.remove(copy_process)

            if process[2] == 0:
                completion_times[process[0]-1] = t
                turnaround_times[process[0]-1] = t - arrival_times[process[0] - 1]
                waiting_times[process[0] - 1] = turnaround_times[process[0]-1] - burst_times[process[0]-1]
                continue
            else:
                process_info.append(tuple(process))

            

    # Print the Output to the console
    print("\n\nProcess\t\tA.T\t\tB.T\t\tC.T\t\tTA.T\t\tW.T\n\n")
    for i in range(number_of_processes):
        print(f"P{i+1}\t\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")

    # Calculate the Average Waiting time and Average TurnAround time
    avg_wt = sum(waiting_times)/number_of_processes
    avg_tt = sum(turnaround_times)/number_of_processes
    print(f"\nAverage Waiting time = {avg_wt} units")
    print(f"Average Turn Around time = {avg_tt} units")

    # Display the Gantt chart
    print("\n\nGantt Chart :")
    print(gantt)
    print()

srtf()
