def lru(num_frames , page_replacement_string):
    page_faults = 0
    frames = []
    for page in page_replacement_string:
        if page in frames:
            frames.remove(page)
            frames.append(page)
        else:
            page_faults += 1
            if len(frames) == num_frames:
                frames.pop(0)
                frames.append(page)
            else:
                frames.append(page)
        print(f"Page : {page} Frames : {frames}")
                
    return page_faults
    
def fifo(num_frames , page_replacement_string):
    page_faults = 0
    frames = []
    for page in page_replacement_string:
        if page in frames:
            pass
        else:
            page_faults += 1
            if len(frames) == num_frames:
                frames.pop(0)
                frames.append(page)
            else:
                frames.append(page)
        print(f"Page : {page} Frames : {frames}")
        
    return page_faults
    
def optimal(num_frames , page_replacement_string):
    frames = []
    page_faults = 0
    
    for i,page in enumerate(page_replacement_string):
        if page in frames:
            print(f"Page : {page} Frames : {frames}")
            continue
        else:
            page_faults += 1
            
            if len(frames) == num_frames:
                furthest_index = -1
                page_to_replace = None
                
                for p in frames :
                    try : 
                        next_index = page_replacement_string[i+1 : ].index(p) + i+1
                    except ValueError:
                        page_to_replace = p
                        break
                    if next_index > furthest_index:
                        furthest_index = next_index
                        page_to_replace = p
                frames.remove(page_to_replace)
            frames.append(page)
            
            print(f"Page : {page} Frames : {frames}")
            
    return page_faults
    
def main():
    num_frames = int(input("Enter the number of frames : "))
    page_replacement_string = input("Enter the page reference string (comma separated) : ").split(',')
    page_replacement_string = [int(page.strip()) for page in page_replacement_string]
    page_faults = fifo(num_frames,page_replacement_string)
    print(f"\nTotal page faults: {page_faults}")
    
main()