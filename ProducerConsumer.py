import threading
import time
import random

class Producer(threading.Thread):
    def __init__(self,buffer,empty,full,mutex):
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.empty = empty
        self.full = full
        self.mutex = mutex

    def run(self):
        i = 1
        while i<=5:
            item = random.randint(1,100)
            self.empty.acquire()
            self.mutex.acquire()
            self.buffer.append(item)
            print(f"Producer produced : {item}")
            self.mutex.release()
            self.full.release()
            time.sleep(random.uniform(1,3))
            i+=1


class Consumer(threading.Thread):
    def __init__(self,buffer,empty,full,mutex):
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.empty = empty
        self.full  =full
        self.mutex = mutex

    def run(self):
        i = 1
        while i<= 5:
            self.full.acquire()
            self.mutex.acquire()
            item = self.buffer.pop(0)
            print(f"Consumer consumed : {item}")
            self.mutex.release()
            self.empty.release()
            time.sleep(random.uniform(1,3))
            i+=1

if __name__ == "__main__":
    buffer = []
    buffer_size = 5
    empty = threading.Semaphore(buffer_size)
    full = threading.Semaphore(0)
    mutex = threading.Semaphore(1)

    producer = Producer(buffer,empty,full,mutex)
    consumer = Consumer(buffer,empty,full,mutex)

    producer.start()
    consumer.start()