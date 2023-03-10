split_line = lambda: map(int, input().split())


if __name__ == '__main__':
    n, m = split_line()
    w_v = [(0, 0)]

    for _ in range(m):
        w, p = split_line()
        v = w * p
        w_v.append((w, v))

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        w, v = w_v[i]

        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]

            if j - w >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)

    print(dp[m][n])
