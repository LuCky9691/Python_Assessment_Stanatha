def kth_largest_element(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

    return min_heap[0]

#input
nums = [3, 2, 1, 5, 6, 4]
k = 2
result = kth_largest_element(nums, k)
print(f"The {k}th largest element is: {result}") #output = 5
