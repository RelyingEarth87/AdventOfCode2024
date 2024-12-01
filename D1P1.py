def sorter(data: list[str]) -> tuple[list[int], list[int]]:
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
    differences = []
    for i in range(len(left)):
        differences.append(abs(left[i] - right[i]))
    
    return differences

def main():
    with open('files/D1.txt', 'r') as f:
        lines = f.readlines()
    
    left, right = sorter(lines)
    differences = pairer(left, right)

    print(sum(differences))

if __name__ == "__main__":
    main()