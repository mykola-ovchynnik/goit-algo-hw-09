def find_coins_greedy(amount, coins=None):
    if coins is None:
        coins = [50, 25, 10, 5, 2, 1]

    result = {}
    remaining = amount

    for coin in coins:
        if remaining <= 0:
            break
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= coin * count

    return result


if __name__ == "__main__":
    amount = 113
    greedy_result = find_coins_greedy(amount)
    print(f"Greedy result for {amount}:", greedy_result)
