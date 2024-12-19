allocations = [[2, 0, 0],
               [3, 0, 2],
               [0, 0, 2],
               [0, 1, 0],
               [2, 1, 1]]
max_req = [[3, 2, 2],
           [8, 0, 0],
           [4, 3, 3],
           [7, 5, 3],
           [2, 2, 2]]
available = [1, 3, 2]
n = 5
m = 3

# Calculate the need matrix
need = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        need[i][j] = max_req[i][j] - allocations[i][j]

finished_proc = [0] * n
answer_proc = [0] * n
index = 0

# Process allocation simulation
for k in range(n):
    for i in range(n):
        if finished_proc[i] == 0:
            progress = False
            flag = 0
            for j in range(m):
                if need[i][j] > available[j]:
                    flag = 1
                    break
            if flag == 0:  # If the process can be allocated
                answer_proc[index] = i
                index += 1
                
                # Update available resources
                for y in range(m):
                    available[y] += allocations[i][y]
                
                finished_proc[i] = 1
                progress = True
                
                # Show remaining available resources
                print(f"Process P{answer_proc[index - 1]} finished. Remaining resources: {available}")
    
    if not progress:
        print("Unsafe state")
        break

# Print the safe sequence
print('Safe sequence is: ', end='')
for i in range(index):
    print(f"P{answer_proc[i]} ", end='')
