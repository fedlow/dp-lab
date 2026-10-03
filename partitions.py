def count_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for part in range(1, n + 1):
        for total in range(part, n + 1):
            dp[total] += dp[total - part]

    return dp[n]