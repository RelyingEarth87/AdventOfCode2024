def parse_positions(data: list[str]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    """parses apart the current positions and velocities in the raw data

    Args:
        data (list[str]): the raw data from a file

    Returns:
        tuple[list[tuple[int, int]], list[tuple[int, int]]]: the positions and velocities respective of each other
    """
    ps = []
    vs = []

    for i in data:
        i = i.strip()
        splt = i.split()
        p = splt[0].strip("p=").split(",")
        p = (int(p[0]), int(p[1]))
        v = splt[1].strip("v=").split(",")
        v = (int(v[0]), int(v[1]))
        ps.append(p)
        vs.append(v)
    
    return ps, vs

def curr_position(p: tuple[int, int], v: tuple[int, int], xlen: int, ylen: int) -> tuple[int, int]:
    """Determines the new position after each second of the simulation

    Args:
        p (tuple[int, int]): current position of the robot
        v (tuple[int, int]): current velocity of the robot
        xlen (int): width of the grid
        ylen (int): height of the grid

    Returns:
        tuple[int, int]: new position of the robot after 1 second of travel
    """
    px, py = p
    vx, vy = v

    px = (px + vx) % (xlen)
    py = (py + vy) % (ylen)

    return (px, py)
def safety_factor(ps: list[tuple[int, int]], xlen: int, ylen: int) -> int:
    """Determines the safety factor of the grid by multiplying the number of robots in each quadrant of the grid

    Args:
        ps (list[tuple[int, int]]): ending positions of all the robots
        xlen (int): width of the grid
        ylen (int): height of the grid

    Returns:
        int: safety factor of the grid, determined by multiplying the number of robots in each quadrant
    """
    mid_x = (xlen - 1) / 2
    mid_y = (ylen - 1) / 2

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for p in ps:
        px, py = p
        if px < mid_x and py < mid_y:
            q1 += 1
        elif px > mid_x and py < mid_y:
            q2 += 1
        elif px < mid_x and py > mid_y:
            q3 += 1
        elif px > mid_x and py > mid_y:
            q4 += 1
    
    print(q1, q2, q3, q4)
    
    return q1 * q2 * q3 * q4


def main():
    """Reads file, calls functions, and prints results
    """
    with open("files/D14.txt") as f:
        data = f.readlines()
    
    ps, vs = parse_positions(data)
    xlen = 101
    ylen = 103

    for i in range(100):
        for j in range(len(ps)):
            ps[j] = curr_position(ps[j], vs[j], xlen, ylen)
    print(ps)
    
    factor = safety_factor(ps, xlen, ylen)
    print(factor)

if __name__ == "__main__":
    main()