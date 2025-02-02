def plus_one(nums):

    length = len(nums)

    for num in range(length - 1, -1, -1):
        if 0 < nums[num] < 9:
            nums[num] += 1
            return nums
        nums[num] = 0
    
    return [1] + nums

def _Tests():
    nums = [1,2,3]
    print(plus_one(nums))

    nums = [4,3,2,1]
    print(plus_one(nums))

    nums = [9]
    print(plus_one(nums))

if __name__ == "__main__":
    _Tests()



