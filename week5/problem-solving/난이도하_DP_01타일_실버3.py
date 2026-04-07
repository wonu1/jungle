# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

N = int(input())

def fibo(n, memo = None):

    if n == 1 :
        return 1
    
    if memo is None:
        memo = [0] * (n+1)
        memo[0] = 1
        memo[1] = 1

    for i in range(2,n+1):
        memo[i] = (memo[i-1]% 15746 + memo[i-2]% 15746)% 15746
    
    return memo[n]

print(fibo(N))