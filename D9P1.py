def expand(data: str) -> list[str, int]:
    """Expands a string of integers into its corresponding hard drive memory space visualization

    Args:
        data (str): raw string of integers to be expanded

    Returns:
        list[str, int]: a list of either integers that represent a file ID or dots that represent free space
    """
    expanded = []

    curr_ID = 0
    for i in range(len(data)):
        if i % 2 == 0:
            new = [curr_ID for i in range(int(data[i]))]
            curr_ID += 1
        elif i % 2 == 1:
            new = ["." for i in range(int(data[i]))]
        
        expanded.extend(new)
    
    return expanded

def move_to_front(expanded: list[str, int]) -> list[str, int]:
    """Transfers files one byte at a time to defragment disk space

    Args:
        expanded (list[str, int]): a list of either integers that represent a file ID or dots that represent free space

    Returns:
        list[str, int]: the defragmented drive space visualization
    """
    isSolved = False
    i = -1
    while not isSolved:
        space = expanded.index(".")
        if len(expanded) - 1 + i < space:
            isSolved = True
            break
        if type(expanded[i]) == str:
            i -= 1
            continue
        to_move = expanded[i]
        expanded[i] = "."
        expanded[space] = to_move
        i -= 1
    
    return expanded

def checksum(finished: list[str, int]) -> int:
    """Calculates checksum for hard drive by multiplying disk position by file ID and summing

    Args:
        finished (list[str, int]): the defragmented disk space visualization

    Returns:
        int: the checksum for the hard drive
    """
    products = []

    position = 0
    for i in range(len(finished)):
        if type(finished[i]) == str:
            break
        product = position * finished[i]
        products.append(product)
        position += 1
    
    return sum(products)

def main():
    """Reads file, calls functions, and prints results
    """
    with open("files/test9.txt", "r") as f:
        data = f.read()
    
    expanded = expand(data.strip())
    finished = move_to_front(expanded)
    check_sum = checksum(finished)

    print(check_sum)


if __name__ == "__main__":
    main()