# -*- coding: utf-8 -*-
"""
4.3 节配套代码：完全背包
=======================
问题：每种物品有【无限件】，想拿几件拿几件，让总价值最高。

例子：
    重量 w = [2, 3, 7, 4]
    价值 v = [1, 3, 9, 5]
    载重 W = 10
    答案：12

和 0/1 背包的【唯一区别】：
    "拿"的时候，看的不是上一行 dp[i-1][...]，而是【本行】dp[i][...]！
    因为拿完一件还能再拿同一件。

    dp[i][j] = max( dp[i-1][j] ,  dp[i][j-w[i]] + v[i] )
                 不拿           拿（看"本行"，可以再拿）

一维数组版：载重 j 要【从小到大】（正序）遍历！
    正序遍历能让"本行"的新值被读到，从而支持"同一物品拿多件"。
    （对比 0/1 背包是逆序 —— 这是两兄弟最容易搞混的地方！）
"""


def knapsack_complete(w, v, W):
    """二维数组版。返回 (最大价值, dp表格)"""
    n = len(w)
    dp = [[0] * (W + 1) for _ in range(n + 1)]   # ② 初始化全 0

    for i in range(1, n + 1):
        for j in range(W + 1):
            # 不拿第 i 件
            dp[i][j] = dp[i - 1][j]
            # 拿第 i 件：注意这里是 dp[i][...]（本行），不是 dp[i-1][...]
            if j >= w[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i][j - w[i - 1]] + v[i - 1])

    return dp[n][W], dp


def knapsack_complete_1d(w, v, W):
    """一维数组省空间版。
    关键：载重 j 要【从小到大】（正序）遍历！
    """
    n = len(w)
    dp = [0] * (W + 1)

    for i in range(n):
        for j in range(w[i], W + 1):   # ⚠️ 正序！从小到大
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    return dp[W]


if __name__ == "__main__":
    w = [2, 3, 7, 4]
    v = [1, 3, 9, 5]
    W = 10

    print("=" * 40)
    print("🎒♻️  完全背包（物品无限件）")
    print("=" * 40)
    print(f"重量 w = {w}")
    print(f"价值 v = {v}")
    print(f"载重 W = {W}")
    print()

    ans, dp = knapsack_complete(w, v, W)

    print("dp 表格（行=物品，列=载重 0~10）：")
    header = "物品(重,值) | " + " ".join(f"{j:2d}" for j in range(W + 1))
    print(header)
    print("-" * len(header))
    for i in range(1, len(w) + 1):
        row = " ".join(f"{dp[i][j]:2d}" for j in range(W + 1))
        print(f"  ④({w[i-1]},{v[i-1]})  | {row}")
    print()

    print("✅ 二维数组结果 =", ans)                       # 12
    print("✅ 一维数组结果 =", knapsack_complete_1d(w, v, W))  # 12

    print()
    print("💡 对比记忆：")
    print("   0/1 背包一维  →  j 逆序（大到小）")
    print("   完全背包一维  →  j 正序（小到大）")
