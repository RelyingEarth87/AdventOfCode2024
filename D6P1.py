def pathing(guard: list[str]) -> int:
    """Determines a guard's patrol path through a room, as indicated by chars: 
    . (free spaces)
    # (obstacles)
    ^ (a guard's starting position)

    Args:
        guard (list[str]): a grid system showing the confines of the room, the guard's starting position, and any obstacles

    Returns:
        int: the number of distinct positions the guard's path will have crossed
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

    steps = [start, next_]
    counter = 2
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

        if next_ == start and direction == starting_direction:
            finished = True
            break
        elif next_[0] < 0 or next_[1] < 0:
            finished = True
            break
    
    steps = set((steps))

    return len(steps)

def main():
    """Reads the file, prepares the data, calls the functions, and prints the results
    """
    with open("files/D6.txt", "r") as f:
        lines = f.readlines()
    
    lines = [i.strip() for i in lines]
    
    num_steps = pathing(lines)

    print(num_steps)

if __name__ == "__main__":
    main()