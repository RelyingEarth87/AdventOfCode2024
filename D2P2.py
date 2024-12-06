def parser(data: list[str]) -> list[list[str]]:
    """Parses the raw data from the imported document and returns a 2D array with each line as a list inside the overaching list

    Args:
        data (list[str]): the raw lines of the imported document

    Returns:
        list[list[str]]: a 2D array where each line is a list of its data
    """
    reports = []

    for i in data:
        report = i.split()
        reports.append(report)
    
    return reports


def isSafe(report: list[str]) -> bool:
    """Checks if the given report is safe (the differences between each report number are constantly increasing/decreasing and not greater than 3 per item)

    Args:
        report (list[str]): a list of numbers that constitute a safety report

    Returns:
        bool: True if the given report is safe, False if unsafe
    """
    differences = []
    abs_diff = []

    for i in range(len(report) - 1):
        num = int(report[i])
        next_num = int(report[i + 1])
        difference = num - next_num
        differences.append(difference)
        abs_diff.append(abs(difference))
    
    if 0 in differences:
        return False
    elif max(abs_diff) > 3:
        return False
    
    diff_sum = sum(differences)
    abs_sum = sum(abs_diff)

    if abs(diff_sum) != abs_sum:
        return False
    
    return True

def dampener(report: list[str]) -> bool:
    """Allows the report to be safe if the report only has 1 outlier to stop it from being safe

    Args:
        report (list[str]): a list of numbers that constitute a safety report

    Returns:
        bool: True if report is safe without one of its values; False if still unsafe
    """
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if isSafe(modified_report):
            return True
    return False

def main():
    """Imports the document, calls the other functions, and sums up how many safe reports there are
    """
    with open("files/D2.txt", "r") as f:
        data = f.readlines()
    
    reports = parser(data)

    status = []
    for report in reports:
        if isSafe(report):
            status.append(True)
        else:
            status.append(dampener(report))

    print(sum(status))

if __name__ == "__main__":
    main()