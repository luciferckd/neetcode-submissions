class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        arr = sorted(nums)
        n = len(nums)

        mid = (n + 1) // 2

        small = mid - 1
        large = n - 1

        for i in range(n):
            if i % 2 == 0:
                nums[i] = arr[small]
                small -= 1

            else:
                nums[i] = arr[large]
                large -= 1
