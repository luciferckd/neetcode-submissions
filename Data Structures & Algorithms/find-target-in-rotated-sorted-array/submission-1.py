class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:
            rotate = (left + right) // 2

            if nums[rotate] == target:
                return rotate
            
            if nums[left] <= nums[rotate]:


                if nums[left] <= target < nums[rotate]:
                    right = rotate-1
                else:
                    left = rotate+1

            else:
                if nums[rotate] < target <= nums[right]:
                    left = rotate + 1
                else:
                    right = rotate - 1
        return -1
        