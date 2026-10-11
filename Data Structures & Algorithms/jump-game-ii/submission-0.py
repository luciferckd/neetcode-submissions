class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        curr = 0
        max_val = 0

        for i in range(len(nums) -1):
            max_val = max(max_val, i + nums[i])

            if i == curr:
                jumps += 1
                curr = max_val
        return jumps
        