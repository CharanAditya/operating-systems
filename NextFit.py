class Node:
    count = 0
    def __init__(self, size):
        self.size = size  # Size of the memory block
        self.next = None  # Pointer to the next block
        Node.count+=1
        self.position = Node.count

class LinkedList:
    def __init__(self):
        self.head = None  # Head of the free list
        self.last_allocated = None  # Keeps track of the last allocated block
        self.n = 0
    
    # Function to add a new free block to the list
    def add_block(self, size):
        new_block = Node(size)
        if self.n == 0:
            self.head = new_block
            self.last = new_block
        else:
            self.last.next = new_block
            self.last = new_block
        self.n+=1

    # Function to print the free memory blocks
    def print_free_list(self):
        current = self.head
        while current:
            print(f"Block Size: {current.size}")
            current = current.next
        print()
    
    # Next Fit algorithm for memory allocation
    def next_fit(self, process_size):
        if not self.last_allocated:
            self.last_allocated = self.head

        current = self.last_allocated
        start_point = current
        
        # Traverse the list starting from the last allocated block
        while True:
            if current.size >= process_size:
                print(f"Allocating {process_size} units from a block of {current.size} units, Block {current.position}")
                
                # Allocate memory by updating the block size
                current.size -= process_size
                
                # Update last allocated block
                self.last_allocated = current
                return True  # Allocation successful
            
            current = current.next if current.next else self.head  # Wrap around to head if end of list is reached
            
            # Stop if we’ve checked all the blocks and found none
            if current == start_point:
                break
        
        print(f"Failed to allocate {process_size} memory")
        return False  # Allocation failed

# Test the implementation
if __name__ == "__main__":
    # Create a free list with some memory blocks
    free_list = LinkedList()
    free_list.add_block(5)  # Add a block of 100 units
    free_list.add_block(10)  # Add a block of 200 units
    free_list.add_block(20)  # Add a block of 50 units
    
    print("Initial Free Memory Blocks:")
    free_list.print_free_list()
    
    # Try to allocate memory using the Next Fit algorithm
    free_list.next_fit(10)   
    free_list.next_fit(5)  
    free_list.next_fit(30)  
    
    print("\nFree Memory Blocks after allocation:")
    free_list.print_free_list()

