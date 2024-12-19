queue = [128, 79, 184, 90, 230, 199, 198, 59]
headStart = 57
limit = 200
headMovement = 0
for i in queue:
    move = abs(i-headStart)
    headMovement += move
    headStart = i

print("running Queue =", queue)
print("headMovement =", headMovement)