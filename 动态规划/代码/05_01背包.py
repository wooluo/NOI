# -*- coding: utf-8 -*-
"""
4.2 节配套代码：0/1 背包
=======================
问题：有几种物品，每种只有 1 件，背包装载有限。
      每件物品"拿(1)"或"不拿(0)"，让总价值最高。

例子：
    重量 w = [2, 3, 7, 4]
    价值 v = [1, 3, 9, 5]
    载重 W = 10
    答案：12  （拿第2、3件：重量 3+7=10，价值 3+9=12）

核心思想（二维表格 dp[i][j]）：
    dp[i][j] = 前 i 种物品、载重 j 时的最大价值

    当 j < w[i]   （装不下）：dp[i][j] = dp[i-1][j]
    当 j >= w[i]  （装得下）：
        dp[i][j] = max( dp[i-1][j] ,  dp[i-1][j-w[i]] + v[i] )
                      不拿           拿（看"上一行"）
"""


def knapsack_01(w, v, W):
    """二维数组版。返回 (最大价值, dp表格)"""
    n = len(w)
    dp = [[0] * (W + 1) for _ in range(n + 1)]   # ② 初始化全 0

    for i in range(1, n + 1):          # 遍历每种物品
        for j in range(W + 1):         # 遍历每种载重
            # 不拿第 i 件
            dp[i][j] = dp[i - 1][j]
            # 拿第 i 件（前提是装得下）
            if j >= w[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i - 1]] + v[i - 1])

    return dp[n][W], dp


def knapsack_01_1d(w, v, W):
    """一维数组省空间版。
    关键：载重 j 要【从大到小】（逆序）遍历！
    为什么？因为"拿"的时候要看上一行的旧值，逆序能保证读到的是旧值。
    如果正序，同一件物品就可能被"拿很多次"，那就变成完全背包了。
    """
    n = len(w)
    dp = [0] * (W + 1)

    for i in range(n):                 # 遍历每种物品
        for j in range(W, w[i] - 1, -1):   # ⚠️ 逆序！从大到小
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    return dp[W]


if __name__ == "__main__":
    w = [2, 3, 7, 4]
    v = [1, 3, 9, 5]
    W = 10

    print("=" * 40)
    print("🎒  0/1 背包")
    print("=" * 40)
    print(f"重量 w = {w}")
    print(f"价值 v = {v}")
    print(f"载重 W = {W}")
    print()

    ans, dp = knapsack_01(w, v, W)

    # 打印表格（去掉第 0 行，只看每种物品）
    print("dp 表格（行=物品，列=载重 0~10）：")
    header = "物品(重,值) | " + " ".join(f"{j:2d}" for j in range(W + 1))
    print(header)
    print("-" * len(header))
    for i in range(1, len(w) + 1):
        row = " ".join(f"{dp[i][j]:2d}" for j in range(W + 1))
        print(f"  ④({w[i-1]},{v[i-1]})  | {row}")
    print()

    print("✅ 二维数组结果 =", ans)              # 12
    print("✅ 一维数组结果 =", knapsack_01_1d(w, v, W))   # 12
