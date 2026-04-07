# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

N , limit = map(int,(input().split()))

nums = []

for i in range(N):
    nums.append(tuple(map(int,(input().split()))))

dp = [0] * (limit+1)

for w, v in nums:
    for j in range(limit,w - 1,-1):
        dp[j] = max(dp[j] , dp[j - w] + v)

print(dp[limit])

