def find_mul(data: list[str]) -> list[str]:
    """Finds all instances of "mul(int, int)" in the given data

    Args:
        data (list[str]): a list of data with instructions on numbers to multiply along with some random characters

    Returns:
        list[str]: a list of strings with instructions to multiply two given numbers together
    """
    import re
    mults: list[str] = []
    for i in data:
        mult = re.findall(r"mul\([0-9]+,[0-9]+\)", i)
        mults.extend(mult)

    return mults


def parse_mult(mults: str) -> int:
    """Parses strings with "mul(int, int)" and returns the two integers multiplied together

    Args:
        mults (str): a string with the instruction multiply (mul) and two integers

    Returns:
        int: a product of two integers
    """
    raw = mults.strip("mul()")
    nums = raw.split(",")

    return int(nums[0]) * int(nums[1])

def main():
    """Reads the file, calls other functions, and prints the results
    """
    with open("files/D3.txt", "r") as f:
        data = f.readlines()
    
    mults = find_mul(data)

    products = []
    for i in mults:
        product = parse_mult(i)
        products.append(product)
    
    print(sum(products))
    

if __name__ == '__main__':
    main()