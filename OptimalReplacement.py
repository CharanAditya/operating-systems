def optimal_page_replacement(num_frames, page_reference_string):
    frames = []  # List to store pages currently in frames
    page_faults = 0

    for i, page in enumerate(page_reference_string):
        # If page is already in frames, continue to the next page
        if page in frames:
            print(f"Page: {page} -> Frames: {frames} (No page fault)")
            continue

        # Page fault occurs if page is not in frames
        page_faults += 1

        # If frames are full, find the optimal page to replace
        if len(frames) == num_frames:
            furthest_index = -1
            page_to_replace = None

            for p in frames:
                # Try to find the next occurrence of page `p` after the current index `i`
                try:
                    next_index = page_reference_string[i+1:].index(p) + i + 1
                except ValueError:
                    # If `p` does not appear again, we should replace this page
                    page_to_replace = p
                    break
                # Select the page with the farthest next occurrence
                if next_index > furthest_index:
                    furthest_index = next_index
                    page_to_replace = p

            # Remove the selected page from frames
            frames.remove(page_to_replace)

        # Add the current page to frames
        frames.append(page)

        # Print the current state of frames
        print(f"Page: {page} -> Frames: {frames} (Page fault)")

    return page_faults

# Main code to take input and call the function
def main():
    num_frames = int(input("Enter the number of frames: "))
    page_reference_string = input("Enter the page reference string (comma-separated): ").split(',')
    page_reference_string = [int(page.strip()) for page in page_reference_string]
    page_faults = optimal_page_replacement(num_frames, page_reference_string)
    print(f"\nTotal page faults: {page_faults}")

if __name__ == "__main__":
    main()
