# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

num = []
for i in range(9):
    num.append(int(input()))

print(max(num))
print(num.index(max(num))+1)