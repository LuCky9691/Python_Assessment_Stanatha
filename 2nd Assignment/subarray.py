#Subarray with Given Sum
#Given an array of integers and a target sum, find a subarray (continuous part of the array) whose sum equals the target sum. 
#Implement an efficient solution using a sliding window or hashmap to find the subarray in O(n) time.


def subarray_with_given_sum(nums, target):
    prefix_sum = 0
    prefix_map = {}

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum == target:
            return nums[:i + 1]

        if (prefix_sum - target) in prefix_map:
            start_index = prefix_map[prefix_sum - target] + 1
            return nums[start_index:i + 1]

        prefix_map[prefix_sum] = i

    return []

#input
nums = [1, 2, 3, 7, 5]
target = 12
result = subarray_with_given_sum(nums, target)
print(f"Subarray with the given sum {target}: {result}")
#output = [2,3,7]
