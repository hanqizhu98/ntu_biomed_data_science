m = 4 #x
n = 4 #y
t = 19

stack = []
path = [1]
x = 0
y = 0
current_reuslt = 0
stack.append(((0,0), 1, 0, 0))

while (True):
    current_position, current_value, seq, direction = stack.pop()
    
    # print("pos:",current_position)
    # print("value:",current_value)
    if (len(path) >= seq):
        path = path[:seq-1]
    if (direction != 0):
        path.append(direction)
    # print(path)

    # print("______________________________")
    
    if (current_value == t and current_position[0] == m-1 and current_position[1] == n-1):
        print("found!")
        print(path)
        break

    if (current_value >= t and (current_position[0] != m-1 or current_position[1] != n-1)):
        continue
    elif (current_position[0] == m-1 and current_position[1] == n-1):
        continue
    if (current_position[0] == m-1):
        stack.append(((current_position[0],current_position[1]+1), current_value+current_position[1]+2, seq + 1,"down"))

    elif (current_position[1] == n-1):
        stack.append(((current_position[0]+1,current_position[1]), current_value+current_position[1]+1, seq + 1,"right"))

    else:
        stack.append(((current_position[0],current_position[1]+1), current_value+current_position[1]+2, seq + 1,"down"))

        stack.append(((current_position[0]+1,current_position[1]), current_value+current_position[1]+1, seq + 1,"right"))
