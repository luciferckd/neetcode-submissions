class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                si, st = stack.pop()
                ans[st] = i - st

            stack.append((t, i))
        return ans
        