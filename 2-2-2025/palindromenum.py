def isPalindrome(x):
    #can just do return str(x) == str(x)[::-1] but whats the fun in that :P
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed = 0 

    while x > reversed:
        reversed = reversed * 10 + x % 10
        x //= 10
    
    return x == reversed or x == reversed // 10
    


def _Test():
    x = 121
    print(isPalindrome(x))
    x = -121
    print(isPalindrome(x))
    x = 10
    print(isPalindrome(x))
if __name__ == "__main__":
    _Test()
