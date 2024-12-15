def expand(data: str) -> list[str]:
    """Expands a string of integers into its corresponding hard drive memory space visualization

    Args:
        data (str): raw string of integers to be expanded

    Returns:
        list[str]: represents either dots as groups of free space or integers separated by commas as files grouped by file ID
    """
    expanded = []

    curr_ID = 0
    for i in range(len(data)):
        if i % 2 == 0:
            new = (str(curr_ID) + ",") * int(data[i])
            curr_ID += 1
        elif i % 2 == 1:
            new = str("." * int(data[i]))
        
        if new != "":
                expanded.append(new)
    
    return expanded

def move_to_front(expanded: list[str]) -> list[str]:
    """Transfers files at once, one at a time, towards front to defragment disk space

    Args:
        expanded (list[str]): represents either dots as groups of free space or integers separated by commas as files grouped by file ID

    Returns:
        list[str]: the defragmented drive space visualization
    """
    isSolved = False
    i = -1
    while len(expanded) + i > 0:
        curr = expanded[i]
        id_ = curr.split(",")
        
        if "." in curr:
            i -= 1
            continue

        try:
            id_.remove("")
        except ValueError:
            pass

        empty_space = "." * len(id_)
        for j in range(len(expanded) + i + 1):
            if empty_space in expanded[j]:
                break
        if empty_space not in expanded[j]:
            i -= 1
            continue
        
        new = "." * (len(expanded[j]) - len(empty_space))
        if new != "":
            expanded[j] = new
        else:
            expanded.remove(empty_space)
        expanded.insert(j, curr)
        expanded[i] = empty_space
        i -= 1

    return expanded

def checksum(finished: list[str]) -> int:
    """Calculates checksum for hard drive by multiplying disk position by file ID and summing

    Args:
        finished (list[str]): the defragmented disk space visualization

    Returns:
        int: the checksum for the hard drive
    """
    products = []

    position = 0
    for i in range(len(finished)):
        if "." in finished[i]:
            position += len(finished[i])
            continue
        
        ids = finished[i].split(",")
        try:
            ids.remove("")
        except ValueError:
            pass
        curr_ID = int(ids[0])
        diff = len(ids)
        
        for j in range(diff):
            product = position * curr_ID
            products.append(product)
            position += 1
    
    return sum(products)

def main():
    """Reads file, calls functions, and prints results
    """
    with open("files/D9.txt", "r") as f:
        data = f.read()
    
    expanded= expand(data.strip())
    finished = move_to_front(expanded)
    check_sum = checksum(finished)

    print(check_sum)


if __name__ == "__main__":
    main()