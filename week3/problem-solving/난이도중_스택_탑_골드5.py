# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

N = int(input())
arr = list(map(int, input().split()))
print(arr)
stack = []
result = []

for i in range(N):
    stack.append(arr[i])
    test = stack.pop()
    print('test: ', test)

    for j in range(0, i):
        print('arr[i]:',arr[i], 'j:',j,'i:', i)
        # if stack[j] > arr[i]:
        #     result.append(j+1)
        #     break
    else:
        result.append(0)
    
print(result)