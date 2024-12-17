import math

# System constants
PAGE_SIZE = 4096  # 4 KB
PHYSICAL_MEMORY_SIZE = 1024 * 1024 * 1024  # 1 GB
FIRST_LEVEL_ENTRIES = 1024
SECOND_LEVEL_ENTRIES = 1024

# Page table entries
class PageTableEntry:
    def __init__(self, present, frame_number):
        self.present = present
        self.frame_number = frame_number

# Page tables
class PageTable:
    def __init__(self):
        self.entries = [PageTableEntry(False, 0) for _ in range(SECOND_LEVEL_ENTRIES)]

class PageDirectory:
    def __init__(self):
        self.entries = [PageTable() for _ in range(FIRST_LEVEL_ENTRIES)]

# Paging system
class PagingSystem:
    def __init__(self):
        self.page_directory = PageDirectory()
        self.physical_memory = [0] * (PHYSICAL_MEMORY_SIZE // PAGE_SIZE)
        self.page_faults = 0

    def translate_address(self, logical_address):
        # Extract page directory index, page table index, and offset
        pd_index = (logical_address >> 22) & 0x3FF
        pt_index = (logical_address >> 12) & 0x3FF
        offset = logical_address & 0xFFF

        # Combine pd_index and pt_index to form the page number
        page_number = (pd_index << 10) | pt_index

        # Get page table entry
        page_table_entry = self.page_directory.entries[pd_index].entries[pt_index]

        # Check if page is present
        if not page_table_entry.present:
            self.handle_page_fault(pd_index, pt_index)
            page_table_entry = self.page_directory.entries[pd_index].entries[pt_index]

        # Calculate physical address
        physical_address = (page_table_entry.frame_number * PAGE_SIZE) + offset
        return page_number, physical_address

    def handle_page_fault(self, pd_index, pt_index):
        # Find a free frame in physical memory
        for i, frame in enumerate(self.physical_memory):
            if frame == 0:
                break
        else:
            raise Exception("Out of physical memory!")

        # Update page table entry
        self.page_directory.entries[pd_index].entries[pt_index].present = True
        self.page_directory.entries[pd_index].entries[pt_index].frame_number = i
        self.physical_memory[i] = 1

        self.page_faults += 1

def main():
    paging_system = PagingSystem()

    for logical_address in [0x12345678, 0xABCDEF12, 0x98765432]:
        print(f"Logical address: 0x{logical_address:08X}")

        # Translate logical address to physical address
        page_number, physical_address = paging_system.translate_address(logical_address)
        pd_index = (logical_address >> 22) & 0x3FF
        pt_index = (logical_address >> 12) & 0x3FF
        offset = logical_address & 0xFFF

        print(f"  Page directory index: {pd_index}")
        print(f"  Page table index: {pt_index}")
        print(f"  Offset: {offset}")
        print(f"  Page number: {page_number}")
        print(f"  Physical address: 0x{physical_address:08X}")
        print(f"  Page faults: {paging_system.page_faults}")
        print()

if __name__ == "__main__":
    main()
