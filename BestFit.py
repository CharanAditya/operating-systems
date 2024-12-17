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
    
    # Best fit memory allocation algorithm
    def best_fit(self, process_size):
        current = self.head
        best_block = None

        # Traverse the free list to find the best block
        while current is not None:
            if current.size >= process_size:
                if best_block is None or current.size < best_block.size:
                    best_block = current
                    
            current = current.next
        
        # Allocate memory if a best block is found
        if best_block is not None:
            print(f"Allocating {process_size} units from a block of {best_block.size} units, Block {best_block.position}")
            best_block.size -= process_size
        else:
            print("Allocation failed: No suitable block found")
            return False
    

# Test the implementation
if __name__ == "__main__":
    # Create a free list with some memory blocks
    free_list = LinkedList()
    free_list.add_block(100)  # Add a block of 100 units
    free_list.add_block(500)  # Add a block of 200 units
    free_list.add_block(200)  # Add a block of 50 units
    
    print("Initial Free Memory Blocks:")
    free_list.print_free_list()
    
    # Try to allocate memory using the Next Fit algorithm
    free_list.best_fit(150)     
    free_list.best_fit(40)  
    free_list.best_fit(112)
    free_list.best_fit(426)  
    
    print("\nFree Memory Blocks after allocation:")
    free_list.print_free_list()

