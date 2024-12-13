#Move Zeros to the End
#Write a function that moves all zeros in an array to the end without changing the order of non-zero elements. 
#Implement it efficiently in O(n) time complexity and O(1) space.


def move_zeros_to_end(nums):
    non_zero_index = 0  

    for i in range(len(nums)):
        if nums[i] != 0:

            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

    return nums

# input
nums = [0, 1, 0, 3, 12]
result = move_zeros_to_end(nums)
print(f"Array after moving zeros to the end: {result}")
# output = [1, 3, 12, 0, 0]
