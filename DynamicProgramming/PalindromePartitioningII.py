 # -*- coding: utf-8 -*-
# @File    : PalindromePartitioningII.py
# @Date    : 2019-12-19
# @Author  : tc
"""
题号 132 分割回文串II
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

参考:https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/

dp[i]：以 s[i] 结尾的字符串分割成若干个回文子串所需要最小分割次数。

"""
class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return 0

        dp = [i for i in range(size)]
        check_palindrome = [[False for _ in range(size)] for _ in range(size)]

        for right in range(size):
            for left in range(right+1):
                if s[left] == s[right] and (right - left <= 2 or check_palindrome[left+1][right - 1]):
                    check_palindrome[left][right] = True

        for i in range(1, size):
            if check_palindrome[0][i]:
                dp[i] = 0
                continue
            # 枚举分割点
            dp[i] = min([dp[j] + 1 for j in range(i) if check_palindrome[j + 1][i]])
        return dp[size - 1]

if __name__ == '__main__':
    s = "aab"
    solution = Solution()
    print(solution.minCut(s))