def searchInsert(nums, target):
    length = len(nums)
    for num in range(length):
        if target == nums[num]:
            return num
        elif nums[num] > target:
            return num
    return length
        
        

        


def _Test():
    nums = [1,3,5,6]
    target = 5
    print(searchInsert(nums, target))
    nums = [1,3,5,6]
    target = 2
    print(searchInsert(nums, target))
    nums = [1,3,5,6]
    target = 7
    print(searchInsert(nums, target))
if __name__ == "__main__":
    _Test()