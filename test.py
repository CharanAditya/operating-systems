n = int(input("Enter number of processes : "))
m = int(input("Enter number of resources : "))

max_per_resource = []
for i in range(m):
    max_per_resource.append(int(input(f"Enter max for R{chr(65+i)} : ")))

allocation_per_process = []
resources_allocated = [0]*m
for i in range(n):
    l1 = []
    for j in range(m):
        l1.append(int(input(f"P{i} R{chr(65+j)} aloocated : ")))
        resources_allocated[j] += l1[j]
    allocation_per_process.append(l1)

max_required_per_process = []
for i in range(n):
    l1 = []
    for j in range(m):
        l1.append(int(input(f"P{i} , R{chr(65+j)} max needed : ")))
    max_required_per_process.append(l1)

print("The Resource allocation matrix : ")
for i in range(n):
    for j in range(m):
        print(*allocation_per_process[i])
    print()

print("The Max Need matrix : ")
for i in range(n):
    for j in range(m):
        print(*max_required_per_process[i])
    print()

def safetyCheck(requestedProcess = -1, requestedResources = [0]*m):
    need = []
    for i in range(n):
        l1 = []
        for j in range(m):
            if i == requestedProcess:
                l1.append(max_required_per_process[i][j] - allocation_per_process[i][j] - requestedResources[j])
            else:
                l1.append(max_required_per_process[i][j] - allocation_per_process[i][j])
        need.append(l1)

    available = max_per_resource.copy()
    for i in range(m):
        available[i] -= resources_allocated[i] - requestedResources[i]

    completed = 0
    safeSequence = []
    while completed < n:
        changed = False

        for i in range(n):
            flag = 0
            if i in safeSequence:
                continue

            for j in range(m):
                if need[i][j] > available[j]:
                    flag = 1

            if flag == 0:
                completed += 1
                safeSequence.append(i)
                for j in range(m):
                    available[j] += allocation_per_process[i][j]
                    if i == requestedProcess:
                        available[j]+=requestedResources[j]
                changed = True
        if changed == False:
            break

    if completed == n:
        print("The system is in a safe state.")
        print(f"Safe sequence : {safeSequence}")
    else:
        print("Danger")
        print(f"Safe sequence : {safeSequence}")

def resourceRequest():
    choice = int(input("Request any resource (0/1) : "))
    if choice == 0:
        return
    requestedProcess = int(input("Enter requesting process : "))
    requestedResource = []
    for i in range(m):
        requestedResource.append(int(input(f"R{chr(65+i)} : ")))
    
    allowed = 1
    available = max_per_resource.copy()
    for i in range(m):
        available[i] -= resources_allocated[i]
        if requestedResource[i] > available[i]:
            allowed = 0

    need = []
    for i in range(n):
        l1 = []
        for j in range(m):
            l1.append(max_required_per_process[i][j] - allocation_per_process[i][j])
        need.append(l1)
    
    for i in range(m):
        if requestedResource[i] > need[requestedProcess][i]:
            allowed = 0
    
    if allowed == 0:
        print("Cannot grant !")
    else :
        safetyCheck(requestedProcess, requestedResource)

safetyCheck()
resourceRequest()
    
