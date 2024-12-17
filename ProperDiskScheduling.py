import matplotlib.pyplot as plt

class DiskScheduling:
    def __init__(self,requests,initial_head , disk_size=200):
        self.initial_head = initial_head
        self.disk_size = disk_size
        self.requests = requests
        
    def calculate_seek_time(self,sequence):
        count = 0
        current = self.initial_head
        for track in sequence:
            count += abs(current - track)
            current = track
        return count
        
    def fcfs(self):
        seek_time = self.calculate_seek_time(self.requests)
        return [self.initial_head]+self.requests , seek_time
        
    def scan(self):
        left = sorted([request for request in self.requests if request < self.initial_head ])
        right = sorted([request for request in self.requests if request >= self.initial_head])
        sequence = right + [self.disk_size-1] + left[::-1]
        seek_time =self.calculate_seek_time(self.requests)
        
        return [self.initial_head]+sequence , seek_time
        
    def sstf(self):
        sequence = []
        requests_copy = self.requests[:]
        current_head = self.initial_head
        while requests_copy:
            closest_request = min(requests_copy, key=lambda x: abs(current_head - x))
            sequence.append(closest_request)
            requests_copy.remove(closest_request)
            current_head = closest_request
        
        seek_time = self.calculate_seek_time(sequence)
        return [self.initial_head] + sequence, seek_time
        
    def plot_movements(self, algorithms):
        plt.figure(figsize=(10,6))
        for name , (sequence , _) in algorithms.items():
            plt.plot(sequence , label=name , marker='o')
        plt.xlabel("Step")
        plt.ylabel("Track")
        plt.title("Disk Head Movement")
        plt.legend()
        plt.show()
        
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 50
disk_scheduler = DiskScheduling(requests, head)

algorithms = {
    'FCFS': disk_scheduler.fcfs(),
    'SCAN': disk_scheduler.scan(),
    'SSTF': disk_scheduler.sstf()
}

for algo , (sequence , seek_time) in algorithms.items():
    print(f"{algo} Sequence: {sequence}")
    print(f"{algo} Total Seek Time: {seek_time}\n")
    
disk_scheduler.plot_movements(algorithms)