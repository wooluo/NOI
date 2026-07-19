# -*- coding: utf-8 -*-
"""
3.1 节配套代码：最大子段和
========================
问题：从一串数字里挑出"连续的一段"，让它们的和最大。

例子：1  -2  5  3  -4  5      答案：9  （选 5 3 -4 5）

核心思想：
    dp[i] = 以第 i 个数"结尾"的最大子段和
    第 i 个数要么接着前面那段，要么自己单独开一段：
        dp[i] = max( dp[i-1] + a[i] ,  a[i] )
    初始：dp[0] = a[0]
    最终答案：所有 dp[i] 里最大的那个。
"""


def max_subarray(a):
    """返回 (最大子段和, dp数组)"""
    n = len(a)
    dp = [0] * n
    dp[0] = a[0]          # ② 初始化
    ans = dp[0]

    for i in range(1, n):
        # ③ 状态转移：接着前面，或自己开段，取较大的
        dp[i] = max(dp[i - 1] + a[i], a[i])
        ans = max(ans, dp[i])     # 随时记录最大值

    return ans, dp


if __name__ == "__main__":
    a = [1, -2, 5, 3, -4, 5]

    print("=" * 40)
    print("➕  最大子段和")
    print("=" * 40)
    print("数字序列：", a)
    print()

    ans, dp = max_subarray(a)

    # 打印每一步的计算过程
    print("位置 i   :", list(range(len(a))))
    print("数字 a[i]:", a)
    print("dp[i]    :", dp)
    print()
    print("✅ 最大子段和 =", ans)   # 应该是 9
