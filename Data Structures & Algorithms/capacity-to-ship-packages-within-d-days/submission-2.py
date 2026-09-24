class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2

            curr_weight = 0
            req = 1

            for weight in weights:
                if curr_weight + weight > mid:
                    req += 1
                    curr_weight = 0

                curr_weight += weight

            if req <= days:
                right = mid
            else:
                left = mid + 1
        return left
