# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

N = int(input())
nums = []
for i in range(N):
    nums.append(list(map(int, input().split())))
    print(nums[i])

mid = int((len(nums[0])+1) / 2)
print(mid)

for i in range(mid):
    print(nums[i][0 : mid])
    