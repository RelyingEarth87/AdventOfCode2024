from copy import deepcopy

def pathing(guard: list[str]) -> tuple[set[tuple[int]], tuple[int]]:
    """Determines a guard's patrol path through a room, as indicated by chars: 
    . (free spaces)
    # (obstacles)
    ^ (a guard's starting position)

    Args:
        guard (list[str]): a grid system showing the confines of the room, the guard's starting position, and any obstacles

    Returns:
        set[tuple[int]]: the coordinates of the distinct positions the guard's path will have crossed
        tuple[int]: the coordinates of the guard's starting position
    """
    for i in range(len(guard)):
        if "^" in guard[i]:
            x = guard[i].find("^")
            y = i
            break
    
    start = (x, y)
    pos = start
    next_ = (x, y-1)
    order = ["up", "right", "down", "left"]

    steps = [start]
    directions = ["up"]

    i = 0
    starting_direction = order[i]
    direction = starting_direction
    finished = False
    while not finished:
        try:
            if guard[next_[1]][next_[0]] == "#":
                i += 1
                direction = order[i]
            else:
                pos = next_
        except IndexError:
            finished = True
            break
        
        if direction == "up":
            next_ = (pos[0], pos[1]-1)
        elif direction == "right":
            next_ = (pos[0]+1, pos[1])
        elif direction == "down":
            next_ = (pos[0], pos[1]+1)
        elif direction == "left":
            next_ = (pos[0]-1, pos[1])
            i = -1

        steps.append(pos)
        directions.append(direction)

        if next_[0] < 0 or next_[1] < 0:
            finished = True
            break
        elif next_ in steps:
            index = steps.index(next_)
            if direction == directions[index]:
                return -1
    
    steps = set((steps))

    return steps, start

def new_obstacle(guard: list[str], steps: set, start: tuple) -> int:
    """Determines how many paths will end in loops if one obstacle is added

    Args:
        guard (list[str]): a grid system showing the confines of the room, the guard's starting position, and any obstacles
        steps (set): the coordinates of the distinct positions the guard's path will have crossed
        start (tuple): the coordinates of the guard's starting position

    Returns:
        int: the number of total paths that will end in loops
    """
    counter = 0

    steps = list(steps)
    steps.remove(start)

    for i in range(len(steps)):
        guard1 = deepcopy(guard)
        guard1[steps[i][1]] = guard[steps[i][1]][0:steps[i][0]] + "#" + guard[steps[i][1]][steps[i][0]+1:]
        result = pathing(guard1)
        if result == -1:
            counter += 1
    
    return counter

def main():
    """Reads the file, prepares the data, calls the functions, and prints the results
    """
    with open("files/D6.txt", "r") as f:
        lines = f.readlines()
    
    lines = [i.strip() for i in lines]
    
    steps, start = pathing(lines)

    num_loops = new_obstacle(lines, steps, start)

    print(num_loops)
    

if __name__ == "__main__":
    main()