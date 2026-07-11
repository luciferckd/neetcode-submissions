class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        has = set()
        max_str = 0
        left = 0

        for right in range(len(s)):
            while s[right] in has:
                has.remove(s[left])
                left += 1
            
            has.add(s[right])
            max_str = max(max_str, right - left + 1)
        return max_str



        