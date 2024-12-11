def find_frequencies(grid: list[str]) -> dict[str, tuple[int, int]]:
    """finds the different frequencies of antennae in the city grid

    Args:
        grid (list[str]): a grid representing a city

    Returns:
        dict[str, tuple[int, int]]: positions of radio antennae with respect to each frequency
    """
    positions = {}

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                try:
                    positions[grid[i][j]] = positions[grid[i][j]] + [(j, i)]
                except KeyError:
                    positions[grid[i][j]] = [(j, i)]

    return positions

def find_antinodes(grid: list[str], nodes: dict[str, tuple[int, int]]) -> int:
    """Finds the antinodes where the frequencies cause an effect

    Args:
        grid (list[str]): a grid representing a city
        nodes (dict[str, tuple[int, int]]): positions of radio antennae with respect to each frequency

    Returns:
        int: number of antinodes created given the positions of the frequencies
    """
    frequencies = list(nodes.keys())
    antinodes = []

    gridy = len(grid)
    gridx = len(grid[0])

    for i in range(len(frequencies)):
        positions = nodes[frequencies[i]]
        antinodes.extend(positions)

        for j in range(len(positions) - 1):
            for k in range(1, len(positions)):
                vector = (positions[k][0] - positions[j][0], positions[k][1] - positions[j][1])

                new_point1 = (positions[j][0] - vector[0], positions[j][1] - vector[1])
                new_point2 = (positions[k][0] + vector[0], positions[k][1] + vector[1])

                if gridx > new_point1[0] >= 0 and gridy > new_point1[1] >= 0:
                    antinodes.append(new_point1)
                if gridx > new_point2[0] >= 0 and gridy > new_point2[1] >= 0:
                    antinodes.append(new_point2)

                if vector == (0, 0):
                    continue

                while gridx > new_point1[0] >= 0 and gridy > new_point1[1] >= 0:
                    new_point1 = (new_point1[0] - vector[0], new_point1[1] - vector[1])

                    if gridx > new_point1[0] >= 0 and gridy > new_point1[1] >= 0:
                        antinodes.append(new_point1)
            
                while gridx > new_point2[0] >= 0 and gridy > new_point2[1] >= 0:
                    new_point2 = (new_point2[0] + vector[0], new_point2[1] + vector[1])

                    if gridx > new_point2[0] >= 0 and gridy > new_point2[1] >= 0:
                        antinodes.append(new_point2)
            
    return set(antinodes)


def main():
    """Reads file, calls functions, and prints results
    """
    with open("files/D8.txt", "r") as f:
        data = f.readlines()
    
    data = [i.strip() for i in data]

    frequencies = find_frequencies(data)
    antinodes = find_antinodes(data, frequencies)
    print(len(antinodes))

if __name__ == '__main__':
    main()