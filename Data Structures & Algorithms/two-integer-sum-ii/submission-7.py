class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index1, index2 = 0, len(numbers)-1

        while index1 < index2:
            total = numbers[index1] + numbers[index2]

            if total == target:
                return [index1+ 1, index2+ 1]

            elif total < target:
                index1 += 1
            else:
                index2 -= 1

       
        