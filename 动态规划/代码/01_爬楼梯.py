# -*- coding: utf-8 -*-
"""
第 1 章配套代码：爬楼梯（动态规划入门）
======================================
问题：一次能上 1 阶或 2 阶，爬到第 n 阶有多少种走法？

核心思想（状态转移方程）：
    到第 n 阶的走法 = 到第 n-1 阶的走法 + 到第 n-2 阶的走法
    （因为你最后一步要么从 n-1 跨 1 阶，要么从 n-2 跨 2 阶）

这其实就是"斐波那契数列"！
"""


def stairs(n):
    """返回爬到第 n 阶的走法数（动态规划版）"""

    # ② 初始化最前面的状态
    if n == 1:
        return 1
    if n == 2:
        return 2

    # 用两个变量记住"前两阶"和"上一阶"的答案
    prev2 = 1  # 第 1 阶
    prev1 = 2  # 第 2 阶

    # ③ 按方程一步步算到第 n 阶
    for step in range(3, n + 1):
        current = prev1 + prev2   # 当前阶 = 上一阶 + 上上阶
        prev2 = prev1             # 往前"挪一格"
        prev1 = current
    return prev1


def stairs_show_table(n):
    """把每一阶的走法数打印成一张表，方便观察规律"""
    if n >= 1:
        dp = [0] * (n + 1)
        dp[1] = 1
        if n >= 2:
            dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

    print("台阶阶数：", list(range(1, n + 1)))
    print("走法数量：", dp[1:])
    print()


if __name__ == "__main__":
    print("=" * 40)
    print("🪜  爬楼梯走法数")
    print("=" * 40)
    stairs_show_table(8)

    n = 6
    print(f"爬到第 {n} 阶，一共有 {stairs(n)} 种走法！")
    # 第 6 阶应该是 13 种
