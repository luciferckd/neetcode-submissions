class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) -1

        while left <= right:
            total = (left + right) // 2

            if nums[total] == target:
                return total
            
            elif nums[total] < target:
                left += 1
            else:
                right -= 1
        return -1
        