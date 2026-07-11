class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0
        l, r = 0, len(height)-1 # let chexk the two side of pointer 
        left_max, right_max = height[l], height[r] # find the max left and max right
        water = 0  # how many water to calculate

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l]) # to increase the pointer to check the max value of height in left
                water += left_max - height[l] # water increase for image to count left

            else:
                r -= 1  # other wise to decrement the right side
                right_max = max(right_max, height[r]) # let to increase the pointer to check the max value height right
                water += right_max - height[r] # water increase for image to count right
        return water 

        