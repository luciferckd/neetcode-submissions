class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2

            curr_weights = 0
            req = 1

            for weight in weights:
                if curr_weights + weight > mid:
                    req += 1
                    curr_weights = 0
                curr_weights += weight

            if req <= days:
                right = mid

            else:
                left = mid + 1
        return left
