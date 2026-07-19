# -*- coding: utf-8 -*-
"""
4.1 节配套代码：最长公共子序列 (LCS)
==================================
问题：找两个序列都拥有的最长子序列（不用连续，顺序不能乱）。

例子：s1 = "abcbdab"
      s2 = "bdcaba"
      答案：4  （比如 "bcba" 或 "bdab"）

核心思想（画一张二维表格 dp[i][j]）：
    dp[i][j] = s1前i个字符 和 s2前j个字符 的最长公共子序列长度

    ① s1[i] == s2[j] （两个字符相同）：
        dp[i][j] = dp[i-1][j-1] + 1        # 对角线 + 1
    ② s1[i] != s2[j] （两个字符不同）：
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])   # 上方、左方取较大

    第 0 行、第 0 列全是 0 （空序列和谁比都是 0）。
"""


def lcs(s1, s2):
    """返回 (最长长度, dp表格)"""
    m, n = len(s1), len(s2)

    # ② 初始化：多开一行一列，全是 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 注意：dp 的下标比字符串大 1，所以要减 1
            if s1[i - 1] == s2[j - 1]:
                # ③ 情况①：字符相同，对角线 +1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # ③ 情况②：字符不同，取上、左较大
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n], dp


def print_table(s1, s2, dp):
    """漂亮地打印 dp 表格"""
    print("        ", "  ".join(s2))
    print("       ", "  ".join(str(j) for j in range(1, len(s2) + 1)))
    for i in range(1, len(s1) + 1):
        row = [f"{dp[i][j]}" for j in range(1, len(s2) + 1)]
        print(f"  {s1[i-1]}({i}):", "  ".join(row))


if __name__ == "__main__":
    s1 = "abcbdab"
    s2 = "bdcaba"

    print("=" * 40)
    print("🤝  最长公共子序列 (LCS)")
    print("=" * 40)
    print(f"s1 = {s1}")
    print(f"s2 = {s2}")
    print()

    ans, dp = lcs(s1, s2)

    print("dp 表格：")
    print_table(s1, s2, dp)
    print()
    print("✅ 最长公共子序列长度 =", ans)   # 应该是 4
