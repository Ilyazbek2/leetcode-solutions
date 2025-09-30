# 11. Container With Most Water
# Problem: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))  # 49
    print(Solution().maxArea([1,1]))  # 1
