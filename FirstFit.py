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
        self.last = None
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
    
    # First Fit algorithm for memory allocation
    def first_fit(self, process_size):
        current = self.head
        
        # Traverse the list to find the first block that fits
        while current:
            if current.size >= process_size:
                print(f"Allocating {process_size} units from a block of {current.size} units belongs to Block {current.position}")
                # Allocate memory by updating the block size
                current.size -= process_size                
                return True  # Allocation successful
            current = current.next
            
        
        print(f"Failed to allocate {process_size} memory")
        return False  # Allocation failed

'''
# Test the implementation
if __name__ == "__main__":
    # Create a free list with some memory blocks
    free_list = LinkedList()
    free_list.add_block(100)  # Add a block of 100 units
    free_list.add_block(200)  # Add a block of 200 units
    free_list.add_block(50)   # Add a block of 50 units
    
    print("Initial Free Memory Blocks:")
    free_list.print_free_list()
    
    # Try to allocate memory using the First Fit algorithm
    free_list.first_fit(75)   # Allocating 75 units
    free_list.first_fit(150)  # Allocating 150 units
    
    print("\nFree Memory Blocks after allocation:")
    free_list.print_free_list()
'''

# Test the implementation
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

