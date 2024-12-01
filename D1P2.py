import numpy as np

def sorter(data: list[str]):
    left = []
    right = []

    for i in data:
        line = i.split()
        left.append(int(line[0]))
        right.append(int(line[1]))
    
    arr = np.array([left, right])
    
    return np.sort(arr)

def pairer(arr: list[int]):
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

def multiplier(left, counts):
    similarity = 0
    for i in range(len(left)):
        addend = left[i] * counts[i]
        similarity += addend

    return similarity

def main():
    with open('files/D1.txt', 'r') as f:
        lines = f.readlines()
    
    arr = sorter(lines)
    left, counts = pairer(arr)
    print(multiplier(left, counts))

if __name__ == "__main__":
    main()