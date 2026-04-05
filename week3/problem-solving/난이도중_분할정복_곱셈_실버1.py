# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

A, B, C = map(int, input().split())

def power(A, B):
    if B == 1:
        return A % C
    mid = B // 2
    temp = power(A, mid)
    
    if B % 2 == 0:
        return  temp * temp % C
    else:
        return temp * temp * A % C
    
result = power(A,B)

print(result)
















# pow(A, B)
# for i in range(B):
#     A *= A
#     A %= C

# print( A % C )
