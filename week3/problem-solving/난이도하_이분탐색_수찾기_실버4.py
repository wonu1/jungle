N = int(input())
number_list = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

number_list.sort()
result = []

for target in target_list:
    left = 0
    right = len(number_list) - 1

    while left<=right:
        mid = (left + right)//2

        if target == number_list[mid]:
            result.append('1')
            break
        elif target < number_list[mid]:
            right = mid -1
        else :
            left = mid +1
    else:
        result.append('0')

print('\n'.join(result))