def containsDuplicate(nums):
    numset = set(nums)
    return len(numset) == len(nums)




def _Test():
    nums = [1,2,3,1]
    print(containsDuplicate(nums))

    nums = [1,2,3,4]
    print(containsDuplicate(nums))

    nums = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(nums))
if __name__ == "__main__":
    _Test()
