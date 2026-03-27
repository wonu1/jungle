# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
from collections import deque


computer = int(input())
edge = int(input())
edges = []

for i in range(edge):
    edges.append(list(input().split()))

queue = deque('1')
visited = set()

while queue:
    current = queue.popleft()
    visited.add(current)

    for u, v in edges:
        if v == current and u not in visited:
            queue.append(u)
        if u == current and v not in visited:
            queue.append(v)

print(len(visited)-1)


