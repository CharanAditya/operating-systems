# Function for FIFO Page Replacement
def fifo_page_replacement(num_frames, page_reference_string):
    frames = ['-']*num_frames # Queue with fixed size for the frames
    page_faults = 0
    pos = 0

    for page in page_reference_string:
        if page not in frames:
            page_faults += 1
            frames[pos] = page
            pos = (pos+1)%num_frames
        print(f"Page: {page} -> Frames: {frames}")

    return page_faults

def main():
    num_frames = int(input("Enter the number of frames: "))
    page_reference_string = input("Enter the page reference string (comma-separated): ").split(',')
    page_reference_string = [int(page.strip()) for page in page_reference_string]
    page_faults = fifo_page_replacement(num_frames, page_reference_string)
    print(f"\nTotal page faults: {page_faults}")

if __name__ == "__main__":
    main()
