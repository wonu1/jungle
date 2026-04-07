# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
# import re

# sic = input()

# flag = False
# result = []

# for i in sic:
#     if i == '-':
#         if flag == False:
#             result.append('-')
#             result.append('(')
#             flag = True
#         else:
#             result.append(')')
#             result.append('-')
#             result.append('(')
#             flag = True
#     elif i.isdecimal():
#         result.append(i)
#     elif i == '+':
#         result.append(i)

# if flag:
#     result.append(')')

# result = ''.join(result)
# normalized = re.sub(r'\d+', lambda m: str(int(m.group())), result)

# result = eval(normalized)

# print(result)


sic = input()

s = (sic.split('-'))

result = sum(map(int,(s[0].split('+'))))

for i in s[1:]:
    result -= sum(map(int,(i.split('+'))))

print(result)