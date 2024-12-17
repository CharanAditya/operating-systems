class DiskScheduling:
    def __init__(self, requests, head, disk_size=200):
        self.requests = requests
        self.initial_head = head
        self.disk_size = disk_size

    def calculate_seek_time(self, sequence):
        seek_time = 0
        current_position = self.initial_head
        for track in sequence:
            seek_time += abs(track - current_position)
            current_position = track
        return seek_time

    def fcfs(self):
        # FCFS serves requests in the original order
        sequence = self.requests
        seek_time = self.calculate_seek_time(sequence)
        return [self.initial_head] + sequence, seek_time

    def scan(self):
        # Sort requests into two lists based on the initial head position
        left = sorted([req for req in self.requests if req < self.initial_head])
        right = sorted([req for req in self.requests if req >= self.initial_head])

        # SCAN goes toward the end and reverses
        # Move right first to the end, then reverse to the left end
        sequence = right + [self.disk_size - 1] + left[::-1]
        seek_time = self.calculate_seek_time(sequence)
        return [self.initial_head] + sequence, seek_time

    def c_scan(self):
        # Sort requests into two lists based on the initial head position
        left = sorted([req for req in self.requests if req < self.initial_head])
        right = sorted([req for req in self.requests if req >= self.initial_head])

        # C-SCAN goes in one direction to the end, wraps to the beginning, then continues
        sequence = right + [self.disk_size - 1, 0] + left
        seek_time = self.calculate_seek_time(sequence)
        return [self.initial_head] + sequence, seek_time

    def look(self):
        # LOOK only goes as far as the furthest request in each direction
        left = sorted([req for req in self.requests if req < self.initial_head])
        right = sorted([req for req in self.requests if req >= self.initial_head])

        # LOOK moves toward the last request on each side and reverses
        sequence = right + left[::-1]
        seek_time = self.calculate_seek_time(sequence)
        return [self.initial_head] + sequence, seek_time

    def c_look(self):
        # C-LOOK goes toward the last request in one direction, wraps to the beginning, then continues
        left = sorted([req for req in self.requests if req < self.initial_head])
        right = sorted([req for req in self.requests if req >= self.initial_head])

        sequence = right + left  # C-LOOK wraps around to the first request on the opposite side
        seek_time = self.calculate_seek_time(sequence)
        return [self.initial_head] + sequence, seek_time

    def plot_movements(self, algorithms):
        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 6))
        for name, (sequence, _) in algorithms.items():
            plt.plot(sequence, label=name, marker='o')
        plt.xlabel("Step")
        plt.ylabel("Track Position")
        plt.title("Disk Head Movement for Different Scheduling Algorithms")
        plt.legend()
        plt.show()

# Initialize variables
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 50
disk_scheduler = DiskScheduling(requests, head)

# Run algorithms and gather results
algorithms = {
    'FCFS': disk_scheduler.fcfs(),
    'SCAN': disk_scheduler.scan(),
    'C-SCAN': disk_scheduler.c_scan(),
    'LOOK': disk_scheduler.look(),
    'C-LOOK': disk_scheduler.c_look()
}

# Print results and plot movements
for algo_name, (sequence, seek_time) in algorithms.items():
    print(f"{algo_name} Sequence: {sequence}")
    print(f"{algo_name} Total Seek Time: {seek_time}\n")

# Plot results
disk_scheduler.plot_movements(algorithms)
