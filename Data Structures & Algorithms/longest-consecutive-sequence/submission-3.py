class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in nSet:
                length = 0
                while (n+length) in nSet:
                    length += 1
                longest = max(length, longest)
        return longest
        