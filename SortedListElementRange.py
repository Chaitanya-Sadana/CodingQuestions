class Solution:
    def getRange(self, arr, target):
        first = self.binarySearchIterative(arr, 0, len(arr) - 1, target, True)
        last = self.binarySearchIterative(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binarySearchIterative(self, arr, low, high, target, find):
        while True:
            if high < low:
                return -1
            mid = low + (high - low) // 2
            if find:
                if(mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                    return mid
                elif target < arr[mid]:
                    high = mid -1 
                else:
                    low = mid + 1

arr = [1,3,3,5,7,8,9,9,9,15]
x = 9

print(Solution().getRange(arr, 9))
