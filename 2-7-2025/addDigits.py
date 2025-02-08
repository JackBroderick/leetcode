def addDigits(num):
    return 1 + (num - 1) % 9 if num else 0

def _Test():
    num = 38
    print(addDigits(num))
    num = 112
    print(addDigits(num))
    
if __name__ == "__main__":
    _Test()