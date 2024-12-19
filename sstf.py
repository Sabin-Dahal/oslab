queue = [128, 79, 184, 90, 230, 199, 198, 59]
headStart = 57
headMovement = 0
limit = 200
runQueue = []

def solve(queue, start):
    if not len(queue): return 0
    a = min(queue, key=lambda a: abs(a-start))
    runQueue.append(a)
    queue.remove(a)
    return abs(start-a)+solve(queue, a)
    

headMovement = solve(queue, headStart)

print("running Queue =", runQueue)
print("headMovement =", headMovement)