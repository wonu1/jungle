# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

N = int(input())

nums = list(map(int,input().split()))
nums.sort()
result = []
min = 2000000000

for i in range(len(nums)):
    target = -(nums[i])

    left = i+1
    right = len(nums) - 1

    while left <= right:
        mid = (left + right)//2

        if target == nums[mid]:
            result.append(nums[i])
            result.append(nums[mid])
            break
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    else:
        if left < len(nums):
            result.append(nums[i])
            result.append(nums[left])
        if right > i:
            result.append(nums[i])
            result.append(nums[right])
        

for i in range(0,len(result),2):
    if min > abs(result[i] + result[i+1]):
        min = abs(result[i] + result[i+1])
        end = i

if result[end]< result[end+1]:
    print(result[end], result[end+1])
else:
    print(result[end+1], result[end])
