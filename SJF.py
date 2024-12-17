# SJF (Non pre-emptive)
# 22BCE0166


def sjf():
    #Get the required details
    number_of_processes = int(input("\nEnter the number of processes : "))
    processes = []
    arrival_times = []
    burst_times = []

    for i in range(number_of_processes):
        processes.append(i+1)
        arrival_times.append(int(input(f"\n\nEnter the arrival time for process Process {i+1} : ")))
        burst_times.append(int(input(f"Enter the Burst time for the Process {i+1} : ")))

    #Sort in the order of increasing AT followed by BT
    process_info = list(zip(processes,arrival_times,burst_times))

    #Start the processing
    t = 0
    gantt = []
    completion_times = [0]*number_of_processes
    waiting_times = [0]*number_of_processes
    turnaround_times = [0]*number_of_processes

    while process_info != []:
        available = []
        for p in process_info:
            #Check if the arrival time is less than or equal to the current time
            if p[1] <= t:
                available.append(p)
        
        if available == []:
            t+=1
            gantt.append("Idle")
            continue
        else:
            #Sort the available processees depending on their Burst Time, and if same then 
            #by their Arrival Time if that is also same, then by their ProcessID
            available.sort(key=lambda x : (x[2] , x[1] , x[0]))

            #Choose the appropriate service that has least Burst Time
            process = available[0]

            #Service the process
            burst_time = process[2]
            pid = process[0]
            arrival_time = process[1]
            
            #Since non pre-emptive run it for the entire burst time
            t += burst_time
            gantt.append(pid)

            completion_times[pid-1] = t
            turnaround_times[pid-1] = t - arrival_time
            waiting_times[pid-1] = turnaround_times[pid-1] - burst_time
            
            process_info.remove(process)

    
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

sjf()
