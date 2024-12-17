import threading
import time
import random

shared_data = 0
read_count = 0

mutex = threading.Semaphore(1)
write_lock = threading.Semaphore(1)

class Reader(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    
    def run(self):
        global read_count
        i = 1
        while i <= 2:
            # Reader tries to read
            mutex.acquire()
            read_count += 1
            if read_count == 1:
                write_lock.acquire()  # First reader locks the writer
            mutex.release()

            # Critical section (reading)
            print(f"Reader {self.index} is reading the shared data: {shared_data}")
            time.sleep(random.uniform(1, 3))  # Simulate reading time
            i += 1

            # Reader done reading
            mutex.acquire()
            read_count -= 1
            if read_count == 0:
                write_lock.release()  # Last reader unlocks the writer
            mutex.release()

class Writer(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index

    def run(self):
        global shared_data
        i = 1
        while i <= 2:
            write_lock.acquire()  # Writer acquires the lock

            # Critical section (writing)
            shared_data += 1
            print(f"Writer {self.index} is writing to the shared data: {shared_data}")
            time.sleep(random.uniform(1, 3))  # Simulate writing time

            write_lock.release()  # Release the lock
            time.sleep(random.uniform(1, 3))  # Simulate time before the next write
            i += 1

if __name__ == "__main__":
    readers = [Reader(i) for i in range(3)]
    writers = [Writer(i) for i in range(2)]

    for reader in readers:
        reader.start()
    for writer in writers:
        writer.start()
