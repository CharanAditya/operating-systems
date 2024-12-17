def lfu_page_replacement(num_frames, page_reference_string):
    frames = []  # List to store pages currently in frames
    frequency_count = {}  # Dictionary to track the frequency of each page
    page_faults = 0

    for page in page_reference_string:
        # If page is already in frames, increment its frequency count
        if page in frames:
            frequency_count[page] += 1
            print(f"Page: {page} -> Frames: {frames} (No page fault, Frequency: {frequency_count[page]})")
            continue

        # Page fault occurs if page is not in frames
        page_faults += 1

        # If frames are full, find the least frequently used page to replace
        if len(frames) == num_frames:
            # Find the least frequent page
            least_frequent_page = frames[0]
            min_frequency = frequency_count[least_frequent_page]
            
            # Identify the page with the lowest frequency
            for p in frames:
                if (frequency_count[p] < min_frequency) or \
                   (frequency_count[p] == min_frequency and frames.index(p) < frames.index(least_frequent_page)):
                    least_frequent_page = p
                    min_frequency = frequency_count[p]
            
            # Remove the least frequent page from frames and frequency count
            frames.remove(least_frequent_page)
            del frequency_count[least_frequent_page]

        # Add the new page to frames and set its frequency count to 1
        frames.append(page)
        frequency_count[page] = 1

        # Print the current state of frames
        print(f"Page: {page} -> Frames: {frames} (Page fault, Frequency: {frequency_count[page]})")

    return page_faults

def main():
    # Input: Number of frames and page reference string
    num_frames = int(input("Enter the number of frames: "))
    page_reference_string = input("Enter the page reference string (comma-separated): ").split(',')
    page_reference_string = [int(page.strip()) for page in page_reference_string]
    page_faults = lfu_page_replacement(num_frames, page_reference_string)
    print(f"\nTotal page faults: {page_faults}")

if __name__ == "__main__":
    main()
