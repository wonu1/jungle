# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157


s = input()
low_s = s.lower()
dup = []
count_list = []

for i in range(len(low_s)):
    if low_s[i] not in dup:
        dup.append(low_s[i])

for i in dup:
    count_list.append(low_s.count(i))

max_val = max(count_list)

if count_list.count(max_val) == 1:
    print(dup[count_list.index(max_val)].upper())
else:
    print("?")
    

