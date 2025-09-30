# 8. String to Integer (atoi)
# Problem: https://leetcode.com/problems/string-to-integer-atoi/
# Difficulty: Medium

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign, i = 1, 0
        if s[0] in ["-", "+"]:
            if s[0] == "-":
                sign = -1
            i += 1

        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(min(result, INT_MAX), INT_MIN)


if __name__ == "__main__":
    print(Solution().myAtoi("42"))          # 42
    print(Solution().myAtoi("   -042"))     # -42
    print(Solution().myAtoi("1337c0d3"))    # 1337
    print(Solution().myAtoi("0-1"))         # 0
    print(Solution().myAtoi("words 987"))   # 0
