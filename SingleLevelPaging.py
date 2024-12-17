# Input parameters
logical_address_space = int(input("Enter the total logical address space (in bytes): "))
page_size = int(input("Enter the page size (in bytes): "))
physical_memory_size = int(input("Enter the total physical memory size (in bytes): "))

# Calculating the number of pages and frames
num_pages = logical_address_space // page_size
num_frames = physical_memory_size // page_size

# Page Table: Assume a simple mapping of page numbers to frame numbers for demo
page_table = []
for i in range(num_pages):
    frame_number = i % num_frames  # Simple modulo operation for demo
    page_table.append(frame_number)

# Calculate the page table size
page_table_size = num_pages * 4  # Assume each entry takes 4 bytes

print("\nPaging Information:")
print(f"Total number of pages: {num_pages}")
print(f"Total number of frames: {num_frames}")
print(f"Page Table Size: {page_table_size} bytes")

# Logical to Physical Address Translation
logical_address = int(input("\nEnter a logical address: "))

# Calculate page number and offset
page_number = logical_address // page_size
offset = logical_address % page_size

# Get the frame number from the page table
frame_number = page_table[page_number]

# Calculate the physical address
physical_address = frame_number * page_size + offset

print(f"Logical Address: {logical_address}")
print(f"Page Number: {page_number}")
print(f"Offset: {offset}")
print(f"Frame Number: {frame_number}")
print(f"Physical Address: {physical_address}")
