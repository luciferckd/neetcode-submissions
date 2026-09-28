class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        paries =  {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in paries.values():
                stack.append(char)

            else:
                if not stack or stack.pop() != paries[char]:
                    return False
        return not stack

            