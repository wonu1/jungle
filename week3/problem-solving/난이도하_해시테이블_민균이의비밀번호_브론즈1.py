# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

N = int(input())
str_list = []
found = False
for i in range(N):
    str = input()
    str_list.append(str)

for i in str_list:
    for j in str_list:
        if i == j[::-1]:
            print(len(i), i[len(i)//2])
            found = True
            break
    if(found == True):
        break