# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

N = int(input())
result = []
num = []

for i in range(N):
    num.append(int(input()))

for x in range(len(num)):
    for y in range(x, len(num)):
        for z in range(y, len(num)):
            if (num[x] + num[y] + num[z]) in num:
                result.append(num[x] + num[y] + num[z])

print(result[-1])