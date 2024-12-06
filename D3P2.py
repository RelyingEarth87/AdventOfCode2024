def find_mul(raw: str, last_inst: str) -> list[str]:
    """Finds any instructions to multiply 2 numbers (mul(int, int)), and whether or not to "do()" them or not, returns only positive instructions

    Args:
        raw (str): the raw stream of data and chars to search in
        last_inst (str): the last instruction of either "do()" or "don't()", initially set to "do()"

    Returns:
        list[str]: a list of instructions to multiply two numbers together (mul(int, int)
    """
    import re
    mults: list[str] = []
    dos = [last_inst]
    data = re.split(r"do\(\)|don[']*t\(\)", raw)
    dos.extend(re.findall(r"do\(\)|don[']*t\(\)", raw))

    for i in range(len(data)):
        if "do()" == dos[i]:
            mult = re.findall(r"mul\([0-9]+,[0-9]+\)", data[i])
            mults.extend(mult)

    return mults, dos[-1]


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

    mults = []
    inst = "do()"
    for i in data:
        mult, inst = find_mul(i, inst)
        mults.extend(mult)

    products = []
    for i in mults:
        product = parse_mult(i)
        products.append(product)
    
    print(sum(products))
    

if __name__ == '__main__':
    main()