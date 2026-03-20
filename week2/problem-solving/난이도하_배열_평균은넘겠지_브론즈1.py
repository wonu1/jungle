# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

    
nums = []
C = int(input())
for i in range(C):
    sum = 0
    average = 0
    success = 0
    
    nums = list(map(int, input().split()))

    for j in range(1, len(nums)):
        sum += nums[j]

    average = sum / nums[0]

    for j in nums[1:]:
        if(j > average):
            success +=1
    
    result = success / nums[0] * 100

    print(f"{result:.3f}"+"%")