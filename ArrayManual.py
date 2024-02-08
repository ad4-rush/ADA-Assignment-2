A = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,-1 ,-2 ,-3 ,-4 ,-5 ,-6 ,-7, -8]
# A = [i for i in range(1,11)]
n = len(A)

# Memoization arrays for caching results
Ring = [0] * n
Ding = [0] * n

def ding(k):
    if k < 0:
        return 0
    elif Ding[k] != 0:
        return Ding[k]
    else:
        a1 = A[k] if k >= 0 else 0
        a2 = A[k - 1] if k - 1 >= 0 else 0
        a3 = A[k - 2] if k - 2 >= 0 else 0
        a4 = A[k - 3] if k - 3 >= 0 else 0
        a5 = A[k - 4] if k - 4 >= 0 else 0

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
        a1 = A[k] if k >= 0 else 0
        a2 = A[k - 1] if k - 1 >= 0 else 0
        a3 = A[k - 2] if k - 2 >= 0 else 0
        a4 = A[k - 3] if k - 3 >= 0 else 0
        a5 = A[k - 4] if k - 4 >= 0 else 0

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

# Uncomment the following lines to print the result
# ring_list = [ring(i) for i in range(n)]
result = max(ring(n - 1), ding(n - 1))
print(result)
def bootforce(k,ringcounter,dingcounter):
    if ringcounter>=4 or dingcounter>=4:
        return -2147483646
    if k < 0:
        return 0
    return max(bootforce(k-1,ringcounter+1,0)+A[k],bootforce(k-1,0,dingcounter+1)-A[k])
result = bootforce(n-1,0,0)
print(result)