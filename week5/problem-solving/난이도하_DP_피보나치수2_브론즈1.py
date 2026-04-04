# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

N = int (input())

def fibo(n, memo = None):

    if n == 1 or n == 0:
        return n

    if memo is None:
        memo = {}

    for i in range(n+1):
        if i not in memo.keys():
            memo[i] = fibo(n-1, memo) + fibo(n-2, memo)

    return memo[n]

print(fibo(N))