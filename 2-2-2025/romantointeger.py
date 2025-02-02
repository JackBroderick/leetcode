def romanToInt(s):
    values = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    

    for char in reversed(s):
        curr = values[char]
        if curr < prev:
            total -= curr #subtract if smaller than previous
        else:
            total += curr # add
        prev = curr

    return total


def _Test():
    s = "III"
    print(romanToInt(s))
    s = "LVIII"
    print(romanToInt(s))
    s = "MCMXCIV"
    print(romanToInt(s))

if __name__ == "__main__":
    _Test()
