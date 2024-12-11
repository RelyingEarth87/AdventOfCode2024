def pair_up(data: list[str]) -> list[tuple[str,str]]:
    """Finds the pairs of page numbers and returns them in order

    Args:
        data (list[str]): the raw data with page numbers

    Returns:
        list[tuple[str, str]]: a list of page numbers in order
    """
    pairs = []

    for i in data:
        pair = i.split("|")
        pairs.append((pair[0], pair[1]))
    
    return pairs

def ordered_correct(pairs: list[tuple[str,str]], update: list[str]) -> bool:
    """Determines if the pairs are in the correct order in each update

    Args:
        pairs (list[str]): pairs of page numbers in the order they need to be in
        update (list[str]): an update to a repair manual

    Returns:
        bool: _description_
    """
    for i in pairs:
        try:
            index1 = update.index(i[0])
            index2 = update.index(i[1])

            if index2 < index1:
                return False
        except ValueError:
            pass
        
    return True

def middle_vals(updates: list[str], correct: list[bool]) -> int:
    """Finds and sums the values in the middle of each correct update

    Args:
        updates (list[str]): an update to a repair manual
        correct (list[bool]): a list containing whether or not the updates are correct or not

    Returns:
        int: _description_
    """
    pagesum = 0
    for i in range(len(updates)):
        if correct[i]:
            pagesum += int(updates[i][int(len(updates[i])/2)])
    
    return pagesum

def main():

    with open("files/D5.txt", "r") as f:
        data = f.readlines()
    index = data.index("\n")

    raw_pairs = [i.strip() for i in data[:index]]
    raw_updates = [i.strip().split(",") for i in data[index+1:]]

    pairs = pair_up(raw_pairs)

    correct = []
    for i in raw_updates:
        true = ordered_correct(pairs, i)
        correct.append(true)


    pagesum = middle_vals(raw_updates, correct)
    print(pagesum)

if __name__ == '__main__':
    main()