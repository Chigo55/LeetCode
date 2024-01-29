class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        l, r = 0, len(height) -1
        l_max, r_max = height[l], height[r]

        while l < r:
            l_max, r_max = max(height[l], l_max), max(height[r], r_max)

            if l_max <= r_max:
                volume += l_max - height[l]
                l += 1
            else:
                volume += r_max - height[r]
                r -= 1
        return volume