# Input details
n = int(input("\nEnter the number of processes : "))
m = int(input("Enter the number of different resource types : "))

# Maximum resources available for each type
max_resources = []
# available = []

print()
for i in range(m):  
    max_resources.append(int(input(f"Enter the maximum available resources of type {chr(65+i)} : ")))
    # available.append(max_resources[i])

# Resources that have been completely allocated till now per process
allocation_per_process = []
resource_allocated_per_type = [0]*m
print("\nEnter the allocation of the resources for each process : ")
for i in range(n):
    l1 = []
    print()
    for j in range(m):
        l1.append(int(input(f"Allocation of Resource {chr(65+j)} for P{i} : ")))
        resource_allocated_per_type[j] += l1[j]
    allocation_per_process.append(l1)

# Total resources needed per process
max_resources_needed = []
print("\nEnter the total maximum resources of each type required per Process : ")
for i in range(n):
    l1 = []
    print()
    for j in range(m):
        l1.append(int(input(f"Maximum resource of type {chr(65+j)} needed for for P{i} : ")))
    max_resources_needed.append(l1)

# Print the configuration after getting the input
# Print the allocated matrix
print("The resource allocation matrix")
for i in range(n):
    print(*allocation_per_process[i])
print()

# Print the Maximum requirement matrix
print("Maximum Resources needed matrix")
for i in range(n):
    print(*max_resources_needed[i])    
print()

# Function for safety check
def safetyCheck(requested_process = -1, requested_resource = [0]*m):
    # Total resources that are still needed per process
    need_to_be_satisfied = []
    for i in range(len(max_resources_needed)):
        row = []
        for j in range(len(max_resources_needed[0])):
            if i == requested_process:
                row.append(max_resources_needed[i][j] - allocation_per_process[i][j] - requested_resource[j])
            else:
                row.append(max_resources_needed[i][j] - allocation_per_process[i][j])
        need_to_be_satisfied.append(row)

    # Formulating the available resources
    available = max_resources.copy()
    for resource in range(m):
        available[resource] = available[resource] - resource_allocated_per_type[resource] - requested_resource[resource]
    print()

    # For debugging -
    # print(max_resources)
    # print(allocation_per_process)
    # print(max_resources_needed)
    # print(need_to_be_satisfied)
    # print(resource_allocated_per_type)
    # print(available)
    # print(requested_resource)

    completed = 0
    process = 0
    safe_sequeuce = []

    while completed<n:
        changed = False
        for process in range(n):
            flag = 0
            # If the process is already completed, the continue
            if process in safe_sequeuce:
                continue
            
            # Check if the current requirements are greater than available
            # If more, then cannot satify
            for i in range(m):
                if(need_to_be_satisfied[process][i] > available[i]):
                    flag = 1
            
            # flag = 0, indicates, we can satisfy the process
            if flag == 0:
                safe_sequeuce.append(process)
                completed += 1
                changed = True
                for i in range(m):
                    available[i] = available[i] + allocation_per_process[process][i]
                    if requested_process == process:
                        available[i] += requested_resource[i]

            # process = (process + 1)%n

        if changed == False:
            break

    if completed == n:
        print("\nThere is a safe sequence :")
        print(safe_sequeuce)
    else:
        print("Danger! There is a chance of danger")
        print(safe_sequeuce)


# The resource request function
def resourceRequest():
    requested_resources = []
    proceed = int(input("\nDo you want to request any resources ? (1/0) :"))
    if proceed == 0:
        return
    
    process = int(input("Enter the process for which the resources are needed : "))
    print()
    for i in range(m):
        requested_resources.append(int(input(f"Enter the amount of resource of type {chr(65+i)} required : ")))
    checkAvailability = 1
    available = max_resources.copy()
    for resource in range(m):
        available[resource] = available[resource] - resource_allocated_per_type[resource]
        if requested_resources[resource] > available[resource]:
            checkAvailability = 0
    
    # If the required amount is not avilable then terminate
    if checkAvailability == 0:
        print("Requested resources cannot be provisioned")
        return

    safetyCheck(process , requested_resources)


safetyCheck()
resourceRequest()