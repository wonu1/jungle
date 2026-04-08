# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971


N = int(input())
cost = [0] * N

for i in range(N):
    cost[i] = list(map(int,input().split()))

result = 999

def travel(route):
    global result
    if(len(route) == N):
        if(result > sum(route)):
            result = sum(route)
            print(result)
        return

    for i in cost:
        for j in i:
            if(j == 0 or j in route):
                continue
            route.append(j)
            print("route:",route)
            travel(route)
            route.pop()

travel([])

print(cost)
"""
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
"""

