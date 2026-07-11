class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_T, count_s = {},{}

        for i in range(len(t)):
            count_T[t[i]] = 1 + count_T.get(t[i], 0)
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
        return count_T == count_s

        