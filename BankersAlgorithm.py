import threading

# Banker's Algorithm Class
class BankersAlgorithm:
    def __init__(self, available, max_demand, allocation):
        self.available = available  # Available resources
        self.max = max_demand       # Maximum demand matrix
        self.allocation = allocation  # Current allocation matrix
        self.need = [[self.max[i][j] - self.allocation[i][j] for j in range(len(self.max[0]))] for i in range(len(self.max))]  # Need matrix
        self.num_processes = len(self.allocation)
        self.num_resources = len(self.available)
        self.lock = threading.Lock()  # To simulate multithreading safely

    # Function to check if system is in safe state
    def is_safe(self):
        work = self.available[:]
        finish = [False] * self.num_processes
        safe_sequence = []

        while len(safe_sequence) < self.num_processes:
            progress = False
            for i in range(self.num_processes):
                if not finish[i]:
                    # Check if needs can be satisfied with available resources
                    if all(self.need[i][j] <= work[j] for j in range(self.num_resources)):
                        # Allocate the resources
                        for j in range(self.num_resources):
                            work[j] += self.allocation[i][j]
                        safe_sequence.append(i)
                        finish[i] = True
                        progress = True
            if not progress:
                break
            
        if len(safe_sequence) == self.num_processes :
            print(safe_sequence)
        return len(safe_sequence) == self.num_processes, safe_sequence

    # Request resources for a process
    def request_resources(self, process_id, request):
        self.lock.acquire()

        # Check if the request is valid
        if all(request[j] <= self.need[process_id][j] for j in range(self.num_resources)):
            if all(request[j] <= self.available[j] for j in range(self.num_resources)):
                # Temporarily allocate resources
                temp_available = self.available[:]
                temp_allocation = [row[:] for row in self.allocation]
                temp_need = [row[:] for row in self.need]

                # Pretend to allocate resources
                for j in range(self.num_resources):
                    temp_available[j] -= request[j]
                    temp_allocation[process_id][j] += request[j]
                    temp_need[process_id][j] -= request[j]

                # Check if system is in a safe state
                banker_sim = BankersAlgorithm(temp_available, self.max, temp_allocation)
                is_safe, _ = banker_sim.is_safe()

                if is_safe:
                    # Commit the resource allocation if safe
                    for j in range(self.num_resources):
                        self.available[j] -= request[j]
                        self.allocation[process_id][j] += request[j]
                        self.need[process_id][j] -= request[j]
                    print(f"Request by P{process_id} granted.")
                else:
                    print(f"Request by P{process_id} cannot be granted. Unsafe state detected.")
            else:
                print(f"Request by P{process_id} exceeds available resources.")
        else:
            print(f"Request by P{process_id} exceeds its maximum need.")

        self.lock.release()

# Test function to simulate multiple processes making resource requests
def simulate_bankers_algorithm():
    # Define available resources
    available = [3, 3, 2]

    # Maximum resource demand of each process
    max_demand = [
        [7, 5, 3],  # P0
        [3, 2, 2],  # P1
        [9, 0, 2],  # P2
        [2, 2, 2],  # P3
        [4, 3, 3],  # P4
    ]

    # Currently allocated resources
    allocation = [
        [0, 1, 0],  # P0
        [2, 0, 0],  # P1
        [3, 0, 2],  # P2
        [2, 1, 1],  # P3
        [0, 0, 2],  # P4
    ]

    banker = BankersAlgorithm(available, max_demand, allocation)

    # Start multiple threads to simulate processes making requests
    threads = []

    def process_request(process_id, request):
        banker.request_resources(process_id, request)

    # Test different requests, some will be safe and some will not
    requests = [
        (0, [0, 2, 0]),  # P0 requests 0, 2, 0
        (1, [1, 0, 2]),  # P1 requests 1, 0, 2
        (4, [3, 3, 0]),  # P4 requests 3, 3, 0 
        (3, [0, 2, 0]),  # P3 requests 0, 2, 0
    ]

    for process_id, req in requests:
        t = threading.Thread(target=process_request, args=(process_id, req))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print()
    # Final safety check after all requests
    safe, sequence = banker.is_safe()
    if safe:
        print(f"System is in a safe state. Safe sequence: {sequence}")
    else:
        print("System is in an unsafe state.")

if __name__ == "__main__":
    simulate_bankers_algorithm()