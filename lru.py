nofault = 0
page = []
listp = [1, 2, 3, 4, 5, 3, 4, 4, 3, 9, 0, 11]

for el in listp:
    if el not in page:  # Page fault occurs
        if len(page) < 3:  # If there's space in the page frame
            page.append(el)
        else:  # Replace the least recently used page
            page.pop(0)  # Remove the least recently used page (first in the list)
            page.append(el)
    else:  # Page is already in the frame
        nofault += 1
        # Move the accessed page to the end to mark it as recently used
        page.remove(el)
        page.append(el)

    print(page)

# Calculate faults and fault ratio
fault = len(listp) - nofault
print("Pages: ", end = '')
print(listp)
print("Number of faults: " + str(fault))
print(f'Fault Ratio: {fault} / {len(listp)}')
