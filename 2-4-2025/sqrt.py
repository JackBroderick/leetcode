def mySqrt(x):
    if x < 2:
        return x  # Return x itself for 0 and 1
    
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid  # Perfect square
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right 
def _Test():
    x = 4
    print(mySqrt(x))
    x = 8
    print(mySqrt(x))


if __name__ == "__main__":
    _Test()