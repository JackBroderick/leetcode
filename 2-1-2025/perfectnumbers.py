def checkperfect(num):
    allnums = range(1, num)
    divisible = []
    for i in allnums:
        if num % i == 0:
            divisible += [i]
    if sum(divisible) == num:
        return True
    return False



def _Test():
    num  = 28
    print(checkperfect(num))
    num  = 7
    print(checkperfect(num))
if __name__ == "__main__":
    _Test()