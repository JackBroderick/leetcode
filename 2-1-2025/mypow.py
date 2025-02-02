def myPow(x, n): #x to the power of n
    if n == 0:
        return 1
        
    isnegative = n < 0
    n = abs(n)

    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *=x
        n //=2

    return 1 / result if isnegative else result

def _Test():
    x = 2.0000
    n = 10
    print(myPow(x, n))

    x = 2.1000
    n = 3
    print(myPow(x, n))

    x = 2.0000
    n = -2
    print(myPow(x, n))

if __name__ == "__main__":
    _Test()
    