# Time, Space O(n) O(n)

def sortNums(nums):
    counts = {}
    for n in nums:
        counts[n] = counts.get(n,0) + 1
    return ([1] * counts.get(1,0) +
            [2] * counts.get(2,0) +
            [4] * counts.get(4,0))

# Time, Space O(n), O(1)

def sortNums2(nums):
    firstIndex = 0
    lastIndex = len(nums) - 1
    index = 0
    while index <= lastIndex:
        if nums[index] == 1:
            nums[index], nums[firstIndex] = nums[firstIndex], nums[index]
            firstIndex += 1
            index += 1
        elif nums[index] == 2:
            index += 1
        elif nums[index] == 4:
            nums[index], nums[lastIndex] = nums[lastIndex], nums[index]
            lastIndex -= 1
    return nums

print(sortNums2([4,4,2,2,1,1,4,4,2,2,4,4,4,4,4,1,1,2,2,2,2,4,4,4,4,2,2,2,2,1,1,1,1]))