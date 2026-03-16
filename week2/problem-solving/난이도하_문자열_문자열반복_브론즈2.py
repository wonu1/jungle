# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

T = int(input())

for i in range(T):
    num, str = input().split()
    for j in list(str):
        for k in range(int(num)):
            print(j,end="")
    print()