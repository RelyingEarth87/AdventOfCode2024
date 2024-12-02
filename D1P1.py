def sorter(data: list[str]) -> tuple[list[int], list[int]]:
    """Parses and sorts the data into lists and sorts them

    Args:
        data (list[str]): a list of lines from a document with 2 numbers separated by white space

    Returns:
        tuple[list[int], list[int]]: 2 lists of sorted integers
    """
    left = []
    right = []

    for i in data:
        line = i.split()
        left.append(int(line[0]))
        right.append(int(line[1]))
    
    left.sort()
    right.sort()
    
    return left, right


def pairer(left: list, right: list) -> list[int]:
    """Pairs the two lists together and finds the differences between each side

    Args:
        left (list): a sorted list of integers
        right (list): a sorte list of integers

    Returns:
        list[int]: a list of the differences between the data in each list
    """
    differences = []
    for i in range(len(left)):
        differences.append(abs(left[i] - right[i]))
    
    return differences

def main():
    """Imports files, calls functions, and prints the sum of the differences to present the data
    """
    with open('files/D1.txt', 'r') as f:
        lines = f.readlines()
    
    left, right = sorter(lines)
    differences = pairer(left, right)

    print(sum(differences))

if __name__ == "__main__":
    main()
