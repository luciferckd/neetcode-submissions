class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # first is intalized for brute force apply i get is ok now answer
        # is correct but time and space complexity is large for is come that rate limit o(n2) is so many time is get that

        # now i refrom the time and space complexity for o(n), o(n)

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # nums.sort()

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False







        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False