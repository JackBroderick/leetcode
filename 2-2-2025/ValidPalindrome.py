import re

def isPalindrome(s):
    string = s.upper()
    cleaned_string = re.sub(r'[^a-zA-Z0-9]','',string)
    return cleaned_string == cleaned_string[::-1]

def _Test():
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))

    s = "race a car"
    print(isPalindrome(s))

    S = ""
    print(isPalindrome(s))
if __name__ == "__main__":
    _Test()

