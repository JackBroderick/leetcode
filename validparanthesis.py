


def isvalid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in mapping:  # If it's a closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)  # Push opening brackets
    
    return not stack  # Return True if stack is empty (all matched)




def _Test():
    s = "()"
    print(isvalid(s))
    s = "()[{}"
    print(isvalid(s))
    s = "([])"
    print(isvalid(s))
if __name__ == "__main__":
    _Test()