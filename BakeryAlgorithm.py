import threading

class BackeryLock:
    def __init__(self,n):
        self.n = n
        self.flag = [False]*n
        self.label = [0]*n

    def lock(self, thread_id):
        self.flag[thread_id] = True
        self.label[thread_id] = max(self.label) + 1
        while any(self.flag[j] and (self.label[j],j) < (self.label[thread_id],thread_id) for j in range(self.n) if j!= thread_id):
            pass

    def unlock(self, thread_id):
        self.flag[thread_id] = False

counter = 0
lock = BackeryLock(3)
execution_order = []

def critical_section(thread_id):
    global counter
    lock.lock(thread_id)
    execution_order.append(thread_id)
    print(f"Thread {thread_id} is executing...")
    counter+=1
    lock.unlock(thread_id)

threads = []
for i in range(3):
    t = threading.Thread(target=critical_section, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nFinal counter value : ",counter)
print("Process execution order : ",execution_order)