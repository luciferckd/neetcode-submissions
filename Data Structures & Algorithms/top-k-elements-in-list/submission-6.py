class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return sorted(count, key=count.get, reverse=True)[:k]
        