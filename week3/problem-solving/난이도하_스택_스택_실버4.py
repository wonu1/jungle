# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828


import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []

for _ in range(N):
    arr = input().split()
    command = arr[0]

    if command == 'push':
        stack.append(arr[1])
    elif command == 'pop':
        if stack:
            result.append(stack.pop())
        else:
            result.append('-1')
    elif command == 'size':
        result.append(str(len(stack)))
    elif command == 'empty':
        result.append('0' if stack else '1')
    elif command == 'top':
        if stack:
            result.append(stack[-1])
        else:
            result.append('-1')

print('\n'.join(result))