def find_min_coins(amount, coins=None):
    if coins is None:
        coins = [50, 25, 10, 5, 2, 1]

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    coin_choice = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0 and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                coin_choice[i] = c

    result = {}
    current = amount
    while current > 0:
        c = coin_choice[current]
        if c == -1:

            return {}
        result[c] = result.get(c, 0) + 1
        current -= c

    return dict(sorted(result.items()))


if __name__ == "__main__":
    amount = 113
    dp_result = find_min_coins(amount)
    print(f"DP result for {amount}:", dp_result)
