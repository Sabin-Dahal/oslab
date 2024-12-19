queue = [128, 79, 184, 90, 190, 199, 198, 50]
headStart = 57
headMovement = 0
limit = 200
runQueue = []
queue.sort()
for i,j in enumerate(queue):
    if j>headStart:
        runQueue = queue[i:]+queue[:i]
        break

for i in runQueue:
    move = i-headStart
    if move < 0:
        move = (limit - headStart) + i + limit
    headMovement += move
    headStart = i

print("running Queue =", runQueue)
print("headMovement =", headMovement)