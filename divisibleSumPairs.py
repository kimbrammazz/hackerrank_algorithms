def divisibleSumPairs(n, k, ar):
    # Write your code here
    pairs = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                pairs += 1
    return pairs
