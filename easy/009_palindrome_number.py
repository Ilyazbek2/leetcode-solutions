```python
# 9. Palindrome Number
# Problem: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original, reversed_num = x, 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return original == reversed_num


if __name__ == "__main__":
    print(Solution().isPalindrome(121))   # True
    print(Solution().isPalindrome(-121))  # False
    print(Solution().isPalindrome(10))    # False
