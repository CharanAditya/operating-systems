class Node:
    count = 0
    def __init__(self,size):
        self.next = None
        self.size = size
        Node.count += 1
        self.position = Node.count
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.last_allocated = None
        self.n = 0
        
    def add_block(self, process_size):
        node = Node(process_size)
        if self.head == None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.n += 1
        
    def print_free_list(self):
        current = self.head
        while current:
            print(f"Block size : {current.size} ")
            current = current.next
        print()
        
    def best_fit(self, process_size):
        current = self.head
        best_block = None
        
        while current:
            if current.size > process_size:
                if best_block == None or current.size < best_block.size : 
                    best_block = current
                    
            current = current.next
            
        
        if best_block is not None :
            print(f"Allocating {process_size} units from a block of {best_block.size} units, Block {current.position}")
            best_block.size -= process_size
        else:
            print("Allocation failed, required memory not present!")
        return
    
    def worst_fit(self,process_size):
        current = self.head
        worst_block = None
        
        while current:
            if current.size > process_size:
                if worst_block == None or current.size > worst_block.size:
                    worst_block = current
            current = current.next
        
        if worst_block is not None:
            print(f"Allocating {process_size} units from a block of {worst_block.size} units, Block {current.position}")
            worst_block.size -= process_size
        else:
            print("Allocation failed, required memory not present!")
        return 
    
    def next_fit(self,process_size):
        if not self.last_allocated:
            self.last_allocated = self.head
            
        current = self.last_allocated
        start = current
        
        while True:
            if current.size >= process_size:
                print(f"Allocating {process_size} units from a block of {current.size} units, Block {current.position}")
                current.size -= process_size
                self.last_allocated = current
                
                return True
                
            current = current.next if current.next else self.head
            
            if current == start:
                break
            
        print("Allocation failed, required memory not present!")
        
    def first_fit(self,process_size):
        current = self.head
        while current : 
            if current.size > process_size:
                print(f"Allocating {process_size} units from a block of {current.size} units, Block {current.position}")
                current.size -= process_size
                self.last_allocated = current
                return True
            
            current = current.next
        print("Allocation failed, required memory not present!")
        
if __name__ == "__main__":
    # Create a free list with some memory blocks
    free_list = LinkedList()
    free_list.add_block(100)  # Add a block of 100 units
    free_list.add_block(500)  # Add a block of 500 units
    free_list.add_block(200)  # Add a block of 200 units
    free_list.add_block(300)  # Add a block of 300 units
    free_list.add_block(600)  # Add a block of 600 units
    
    print("Initial Free Memory Blocks:")
    free_list.print_free_list()
    
    # Try to allocate memory using the First Fit algorithm
    free_list.first_fit(212)   # Allocating 212 units
    free_list.first_fit(417)  # Allocating 417 units
    free_list.first_fit(112)  # Allocating 112 units
    free_list.first_fit(426)  # Allocating 426 units
    
    print("\nFree Memory Blocks after allocation:")
    free_list.print_free_list()
     