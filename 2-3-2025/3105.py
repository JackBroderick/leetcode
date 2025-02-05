def count_subarrays(nums):
    def count_sequences(nums, increasing=True):
        count = 0
        length = 1
        
        for i in range(1, len(nums)):
            if (increasing and nums[i] > nums[i-1]) or (not increasing and nums[i] < nums[i-1]):
                length += 1
            else:
                length = 1
            
            count += length  # Each element itself is a subarray
        
        return count
    
    increasing_count = count_sequences(nums, increasing=True)
    decreasing_count = count_sequences(nums, increasing=False)
    
    return increasing_count - decreasing_count

# Example usage
nums = [1, 4, 3, 3, 2]
print(count_subarrays(nums))  # Output: 2

def _Test():
    
    nums = [1, 4, 3, 3, 2]
    print(count_subarrays(nums))  

if __name__ == "__main__":
    _Test()