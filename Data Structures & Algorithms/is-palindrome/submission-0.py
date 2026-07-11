class Solution:
    def isPalindrome(self, s: str) -> bool:
        name = ''
        for c in s:
            if c.isalnum():
                name += c.lower()
        return name == name[::-1]
        