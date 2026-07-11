

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        total_product = 1

        # Build hash map and product of non-zero elements
        for num in nums:
            freq[num] += 1
            if num != 0:
                total_product *= num

        result = []

        for num in nums:
            if freq[0] > 1:
                result.append(0)
            elif freq[0] == 1:
                # Only the zero index gets the product
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)
            else:
                # No zeros → safe to divide
                result.append(total_product // num)

        return result
