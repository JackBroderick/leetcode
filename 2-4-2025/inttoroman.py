def intToRoman(num):
    map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    roman_numeral = ""

    for value, symbol in map:
        while num > value:
            roman_numeral += symbol
            num -=value
    return roman_numeral
            

def _Test():
    num  = 58
    print(intToRoman(num))
    num = 1994
    print(intToRoman(num))

if __name__ == "__main__":
    _Test()