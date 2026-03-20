# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978


import math

N = int(input())
nums = list(map(int, input().split()))
count = 0
if 1 in nums:
    count += 1

for i in nums:
    for j in range(2,int(math.sqrt(i))+1):
        if (i % j == 0 and i !=2 and i != 3):
            count += 1
            break


print(N-count)