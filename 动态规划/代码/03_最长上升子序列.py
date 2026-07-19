# -*- coding: utf-8 -*-
"""
3.2 节配套代码：最长上升子序列 (LIS)
==================================
问题：从一串数字里选一些数（不用挨着，但顺序不能乱），
      让它们从左到右严格变大，最长能有多长？

例子：5  3  9  11  4  2  15      答案：4  （比如 5 9 11 15）

核心思想：
    dp[i] = 以第 i 个数"结尾"的最长上升子序列长度
    看看 i 前面有哪些数比 a[i] 小，那些数后面都能接上 a[i]：
        对所有 j < i 且 a[j] < a[i]：dp[i] = max(dp[i], dp[j] + 1)
    初始：每个 dp[i] = 1 （至少能选自己这一个数）
"""


def lis(a):
    """返回 (最长长度, dp数组)"""
    n = len(a)
    dp = [1] * n          # ② 初始化：每个位置至少长度为 1

    for i in range(n):
        for j in range(i):              # 只看 i 左边的
            if a[j] < a[i]:             # 比 a[i] 小才能接上
                # ③ 状态转移
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp), dp


if __name__ == "__main__":
    a = [5, 3, 9, 11, 4, 2, 15]

    print("=" * 40)
    print("📈  最长上升子序列 (LIS)")
    print("=" * 40)
    print("数字序列：", a)
    print()

    ans, dp = lis(a)

    print("位置 i   :", list(range(1, len(a) + 1)))
    print("数字 a[i]:", a)
    print("长度 dp[i]:", dp)
    print()
    print("✅ 最长上升子序列长度 =", ans)   # 应该是 4
