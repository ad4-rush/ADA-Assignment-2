import random
import time
import sys

sys.setrecursionlimit(10**6)  # Set the recursion limit to a higher value


def ding(k):
    if k < 0:
        return 0
    elif Ding[k] != 0:
        return Ding[k]
    else:
        a1 = large_input[k] if k >= 0 else 0
        a2 = large_input[k - 1] if k - 1 >= 0 else 0
        a3 = large_input[k - 2] if k - 2 >= 0 else 0
        a4 = large_input[k - 3] if k - 3 >= 0 else 0
        a5 = large_input[k - 4] if k - 4 >= 0 else 0

        m = max(
            (ding(k - 5) + a5 + a4 + a3 - a2 - a1),
            (ding(k - 4) + a4 + a3 - a2 - a1),
            (ding(k - 4) + a4 + a3 + a2 - a1),
            (ding(k - 3) + a3 + a2 - a1),
            (ding(k - 3) + a3 - a2 - a1),
            (ring(k - 3) - a3 - a2 - a1),
            (ring(k - 4) - a4 - a3 + a2 - a1),
            (ring(k - 5) - a5 - a4 - a3 + a2 - a1),
            (ring(k - 3) - a3 + a2 - a1)
        )
        Ding[k] = m
        return m

def ring(k):
    if k < 0:
        return 0
    elif Ring[k] != 0:
        return Ring[k]
    else:
        a1 = large_input[k] if k >= 0 else 0
        a2 = large_input[k - 1] if k - 1 >= 0 else 0
        a3 = large_input[k - 2] if k - 2 >= 0 else 0
        a4 = large_input[k - 3] if k - 3 >= 0 else 0
        a5 = large_input[k - 4] if k - 4 >= 0 else 0

        m = max(
            (ring(k - 5) - a5 - a4 - a3 + a2 + a1),
            (ring(k - 4) - a4 - a3 + a2 + a1),
            (ring(k - 4) - a4 - a3 - a2 + a1),
            (ring(k - 3) - a3 - a2 + a1),
            (ring(k - 3) - a3 + a2 + a1),
            (ding(k - 3) + a3 + a2 + a1),
            (ding(k - 4) + a4 + a3 - a2 + a1),
            (ding(k - 5) + a5 + a4 + a3 - a2 + a1),
            (ding(k - 3) + a3 - a2 + a1)
        )
        Ring[k] = m
        return m


def bootforce(k, ringcounter, dingcounter):
    if ringcounter >= 4 or dingcounter >= 4:
        return -2147483646
    if k < 0:
        return 0
    return max(
        bootforce(k - 1, ringcounter + 1, 0) + large_input[k],
        bootforce(k - 1, 0, dingcounter + 1) - large_input[k]
    )

# Dynamic programming solution
start_time = time.time()
# Generate a list of 10,000 random integers between -100 and 100
large_input = [random.randint(-100, 100) for _ in range(30)]
# Memoization arrays for caching results
Ring = [0] * len(large_input)
Ding = [0] * len(large_input)
dp_time = time.time() - start_time
print("Array Time:", dp_time)
start_time = time.time()
ring_list = [ring(i) for i in range(len(large_input))]
dp_result = max(ring_list[len(large_input) - 1], ding(len(large_input) - 1))
dp_time = time.time() - start_time

# Compare the results and time taken
print("Dynamic Programming Result:", dp_result)
print("Dynamic Programming Time:", dp_time)
# Brute-force solution
start_time = time.time()
bf_result = bootforce(len(large_input) - 1,0,0)
bf_time = time.time() - start_time


print("\nBrute-Force Result:", bf_result)
print("Brute-Force Time:", bf_time)