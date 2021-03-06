# -*- coding: utf-8 -*-
# @File    : CoinChange2.py
# @Date    : 2020-03-02
# @Author  : tc
"""
题号 518. 零钱兑换II
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1


注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数

参考：https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-ii-by-leetcode/

"""
from typing import List

class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]


    # 回溯(超时)
    def change2(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        size = len(coins)
        res = []

        def traceback(i, tmp_sum, tmp_list):
            if tmp_sum == amount:
                res.append(tmp_list)
            for j in range(i, size):
                if tmp_sum + coins[j] > amount:  # amount至少大于0
                    break
                traceback(j, tmp_sum + coins[j], tmp_list + [coins[j]])

        traceback(0, 0, [])
        print(res)
        return len(res)


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    solution = Solution()
    print(solution.change(amount,coins))


