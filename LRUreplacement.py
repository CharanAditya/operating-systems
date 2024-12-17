# Function for LRU Page Replacement
def lru_page_replacement(num_frames, page_reference_string):
    frames = []  # List to store pages currently in frames
    page_faults = 0

    for page in page_reference_string:
        # If page is already in frames, mark it as recently used
        if page in frames:
            frames.remove(page)  # Remove the page
            frames.append(page)  # Add it back to the end to mark it as recently used
        else:
            # Page fault occurs if page is not in frames
            page_faults += 1
            # If frames are full, remove the least recently used page (first element)
            if len(frames) == num_frames:
                frames.pop(0)
            # Add the current page to frames
            frames.append(page)

        # Print the current state of frames
        print(f"Page: {page} -> Frames: {frames}")

    return page_faults
    
def main():
    # Input: Number of frames and page reference string
    num_frames = int(input("Enter the number of frames: "))
    page_reference_string = input("Enter the page reference string (comma-separated): ").split(',')
    page_reference_string = [int(page.strip()) for page in page_reference_string]
    page_faults = lru_page_replacement(num_frames, page_reference_string)
    print(f"\nTotal page faults: {page_faults}")

if __name__ == "__main__":
    main()
