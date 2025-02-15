import time
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins
from memory_profiler import memory_usage


def test_time(amount, func):
    start_time = time.perf_counter()
    mem_usage_before = memory_usage()[0]
    result = func(amount)
    mem_usage_after = memory_usage()[0]
    end_time = time.perf_counter()

    print(f"{func.__name__} result for {amount}: {result}")
    print(f"{func.__name__} algorithm took {end_time - start_time:.8f} seconds")
    print(
        f"{func.__name__} memory usage: {mem_usage_after - mem_usage_before:.2f} MiB\n"
    )


if __name__ == "__main__":
    amount = 137_113_34

    test_time(amount, find_coins_greedy)
    test_time(amount, find_min_coins)
