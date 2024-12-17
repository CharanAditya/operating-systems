import math
def calculate_paging(logical_address_space , page_size, physical_memory_size):
    num_pages = logical_address_space//page_size
    num_frames = physical_memory_size//page_size
    page_table_size = num_pages * math.log2(num_frames)
    
    print(f"Number of Pages : {num_pages}")
    print(f"Number of Frames : {num_frames}")
    print(f"Page Table size : {page_table_size} bits")

    return num_pages , num_frames

def translate_logical_to_physical_address(logical_address, page_size, page_table):
    page_number = logical_address // page_size
    offset = logical_address%page_size
    frame_number = page_table.get(page_number,None)

    if frame_number is None:
        print(f"Error : Page Number {page_number} not found in the table")
        return None
    
    physical_address = frame_number*page_size + offset
    print(f"\nLogical Address : {logical_address}")
    print(f"Page Number : {page_number}")
    print(f"Offset : {offset}")
    print(f"Frame Number : {frame_number}")
    print(f"Physical Address : {physical_address}")

    return physical_address

def main():
    logical_address_space = int(input("Enter the Logical Address Space in B : "))
    page_size = int(input("Enter the page size (B): "))
    physical_memory_size = int(input("Enter thr Physical Memory Size (B): "))

    num_pages, num_frames = calculate_paging(logical_address_space, page_size,physical_memory_size)
    page_table = {}

    print("\nEnter the Page Table Mapping (Page Number to Frame NNumber) : ")
    for i in range(num_pages):
        page_number = i
        frame_number = int(input(f"Enter the frame number for page {page_number}: "))
        page_table[page_number] = frame_number
    logical_address = int(input("Enter Logical Address to be translated : "))
    translate_logical_to_physical_address(logical_address,page_size,page_table)

if __name__ == "__main__":
    main()
    