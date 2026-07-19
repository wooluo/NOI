# -*- coding: utf-8 -*-
"""
5.1 节配套代码：石子合并（区间动规）
==================================
问题：一排石子堆，每次只能合并【相邻】的两堆，
      得分 = 合并后这堆的石子数。合并到只剩 1 堆，求最小总得分。

例子：石子堆 a = [5, 3, 3, 5]      答案：32

核心思想（区间动规）：
    dp[i][j] = 把第 i 堆到第 j 堆合并成一堆的最小得分

    最后一步一定是把区间 [i..j] 切成左右两半分别合并好，再合到一起。
    不管怎么切，最后一次大合并的代价都 = 这段区间的石子总和。

    所以枚举切点 k（i <= k < j）：
        dp[i][j] = min( dp[i][k] + dp[k+1][j] + 区间[i..j]的总和 )

    要点：【按区间长度从小到大算】——先算所有长度2的，再长度3……最后整个。
"""


def stone_merge(a):
    """返回 (最小得分, dp表格, 前缀和数组)"""
    n = len(a)

    # 前缀和：快速求任意区间 [i..j] 的石子总和
    # prefix[k] = a[0]+a[1]+...+a[k-1]，所以 区间和 = prefix[j+1]-prefix[i]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]

    def region_sum(i, j):
        """返回第 i 堆到第 j 堆（含两端）的石子总和"""
        return prefix[j + 1] - prefix[i]

    # dp[i][j]：i==j 时（只有一堆）不用合并，得分为 0（初始化）
    dp = [[0] * n for _ in range(n)]

    # 按区间长度 length 从小到大算（长度1已经是0，从2开始）
    for length in range(2, n + 1):           # 遍历区间长度
        for i in range(n - length + 1):      # 遍历区间起点
            j = i + length - 1               # 计算区间终点
            dp[i][j] = float("inf")
            # 枚举切点 k
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + region_sum(i, j)
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1], dp, prefix


if __name__ == "__main__":
    a = [5, 3, 3, 5]

    print("=" * 40)
    print("🪨  石子合并（区间动规）")
    print("=" * 40)
    print(f"石子堆：{a}")
    print()

    ans, dp, _ = stone_merge(a)
    n = len(a)

    print("dp 表格（dp[i][j] = 第i~j堆合并的最小得分）：")
    header = "i＼j | " + " ".join(f"{j+1:>3d}" for j in range(n))
    print(header)
    print("-" * len(header))
    for i in range(n):
        row = []
        for j in range(n):
            if j < i:
                row.append("   .")          # 下三角无意义
            else:
                row.append(f"{dp[i][j]:>4d}")
        print(f" {i+1}  |" + " ".join(row))
    print()

    print(f"✅ 把全部 {n} 堆合并成一堆的最小得分 = {ans}")   # 32
