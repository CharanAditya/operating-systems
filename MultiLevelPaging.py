PAGE_SIZE = 4096  # 4 KB page size
OUTER_TABLE_SIZE = 1024  # 10 bits for outer table
INNER_TABLE_SIZE = 1024  # 10 bits for inner table

outer_page_table = {}
inner_page_tables = {}

# This function splits the logical address into outer page number, inner page number, and offset
def split_address(logical_address):
    outer_page_num = (logical_address >> 22) & 0x3FF  # Use the top 10 bits for outer page number
    inner_page_num = (logical_address >> 12) & 0x3FF  # Use the next 10 bits for inner page number
    offset = logical_address & 0xFFF  # Use the last 12 bits for the offset
    return outer_page_num, inner_page_num, offset

# Populate the outer and inner page tables
for i in range(OUTER_TABLE_SIZE):
    outer_page_table[i] = f"inner_table_{i}"
    inner_page_tables[f"inner_table_{i}"] = {j: f"frame_{i}_{j}" for j in range(INNER_TABLE_SIZE)}

# This function translates the logical address to a physical address using the multi-level page table
def translate_address(logical_address):
    outer_page_num, inner_page_num, offset = split_address(logical_address)

    # Fetch the inner page table name using the outer page number
    inner_table_name = outer_page_table.get(outer_page_num)
    if inner_table_name:
        # Fetch the frame number from the inner page table
        frame = inner_page_tables[inner_table_name].get(inner_page_num)
        if frame:
            # Compute the physical address: frame number * PAGE_SIZE + offset
            physical_address = (int(frame.split('_')[-1]) * PAGE_SIZE) + offset
            return physical_address
        else:
            return "Page Fault: Inner Page not found"
    else:
        return "Page Fault: Outer Page not found"
    
# Function to test the address translation
def test_system():
    logical_address = 0x12345678  # Example logical address
    physical_address = translate_address(logical_address)

    if isinstance(physical_address, int):
        print(f"Logical Address: {hex(logical_address)} -> Physical Address: {hex(physical_address)}")
    else:
        print(physical_address)

# Test the system
test_system()
