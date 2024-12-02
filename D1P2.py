import numpy as np

def sorter(data: list[str]) -> np.array:
    """Parses and sorts the data into lists and a sorted numpy array

    Args:
        data (list[str]): a list of lines from a document with 2 numbers separated by white space

    Returns:
        np.array: A 2D numpy array with 2 columns of integers sorted from low to high values
    """
    left = []
    right = []

    for i in data:
        line = i.split()
        left.append(int(line[0]))
        right.append(int(line[1]))
    
    arr = np.array([left, right])
    
    return np.sort(arr)

def pairer(arr: np.array) -> tuple[list[int], list[int]]:
    """Pairs the data from the right an left columns of data and uses a filtered numpy array to get the counts of each data point from the left column in the right column

    Args:
        arr (np.array[int]): A 2D numpy array with 2 columns of integers sorted from low to high values

    Returns:
        tuple[list[int], list[int]]: a list of the left column of data and a list of the amount of times each integer appears in the right column
    """
    left = arr[0]
    right = arr[1]
    counts = []
    for i in range(len(left)):
        num = left[i]
        try:
            tf = right == num
            filtered = arr[1][tf]   
            counts.append(len(filtered))
        except IndexError:
            counts.append(0)
    
    return left, counts

def multiplier(left: list[int], counts: list[int]) -> int:
    """Takes a list of data and the amount of times each piece of data appears and multiplies them together to get a similarity score

    Args:
        left (list[int]): a list of data
        counts (list[int]): the amount of times each number appears in a set of data

    Returns:
        int: a similarity score  calculated using the sum of each number in the list, times the amount it appears
    """
    similarity = 0
    for i in range(len(left)):
        addend = left[i] * counts[i]
        similarity += addend

    return similarity

def main():
    """A main funcion to handle calling other functions and presenting data
    """
    with open('files/D1.txt', 'r') as f:
        lines = f.readlines()
    
    arr = sorter(lines)
    left, counts = pairer(arr)
    print(multiplier(left, counts))

if __name__ == "__main__":
    main()
