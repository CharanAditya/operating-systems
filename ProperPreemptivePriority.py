def preemptivePriority():
    n = int(input("Enter the number of processes : "))
    process_id = []
    arrival_time = []
    burst_time = []
    priority = []
    process_list = []
    for i in range(n):
        process_id.append(i)
        arrival_time.append(int(input(f"Enter the A.T for P{i} : ")))
        burst_time.append(int(input(f"Enter the B.T for P{i} : ")))
        priority.append(int(input(f"Enter the Priority for P{i} : ")))
        process_list.append([process_id[i] , arrival_time[i] , burst_time[i] , priority[i]])
    
    completion_time = [0]*n
    turnaround_time = [0]*n
    waiting_time = [0]*n

    t = 0
    gantt = []

    while process_list != []:
        queue = []
        for p in process_list:
            if p[1] <= t:
                queue.append(p)

        if queue == []:
            t+=1
            gantt.append("Idle")
            continue

        queue.sort(key = lambda x : (x[3],x[1],x[0]))
        chosenp = queue.pop(0)
        process_list.remove(chosenp)
        gantt.append(f"P{chosenp[0]}")

        t+=1
        chosenp[2]-=1
        if chosenp[2] == 0:
            completion_time[chosenp[0]] = t
            turnaround_time[chosenp[0]] = t-arrival_time[chosenp[0]]
            waiting_time[chosenp[0]] = turnaround_time[chosenp[0]] - burst_time[chosenp[0]]
            continue
        else:
            process_list.append(chosenp)

    print(f"P.Id\t\tA.T\t\tB.T\t\tC.T\t\tTAT\t\tWT")
    for i in range(n):
        print(f"{i}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")
        
    avg_tat = sum(turnaround_time)/n
    avg_wat = sum(waiting_time)/n
    print()
    
    print(f"Average waiting time : {avg_wat}")
    print(f"Average turnaround time : {avg_tat}")
    print()
    print(gantt)

preemptivePriority()