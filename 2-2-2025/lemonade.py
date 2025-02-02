def LemonadeChange(bills):
    fives = 0
    tens = 0
    twenties = 0
    for transaction in bills:
        if transaction == 5:
            fives += 1
        elif transaction == 10:
            tens += 1
            if fives == 0:
                return False
            else:
                fives -= 1
        else:
            if fives > 0 and tens > 0:
                fives -= 1
                tens -= 1
            elif fives > 3:
                fives -= 3
            else:
                return False

    return True






def _Test():
    nums = [5,5,5,10,20]
    print(LemonadeChange(nums))
    nums = [5,5,10,10,20]
    print(LemonadeChange(nums))

if __name__ == "__main__":
    _Test()