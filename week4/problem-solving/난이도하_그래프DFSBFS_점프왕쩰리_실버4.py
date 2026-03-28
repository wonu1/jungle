# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
sys.setrecursionlimit(10**5)

N = int(input())

arr = [] * N
for _ in range(N):
    arr.append(list(map(int,(input().split()))))


def jump(i, j):
    if i >= N or j >= N:
        return False
    
    if i == N-1 and j == N-1:
        return True
    
    current = arr[i][j]

    return jump(i + current, j) or jump(i, j+ current)
    


if jump(0, 0):
    print('HaruHaru')
else:
    print('Hing')