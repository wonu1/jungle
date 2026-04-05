# # 링크드리스트 - 철도 공사 (백준 골드4)
# # 문제 링크: https://www.acmicpc.net/problem/23309

# N, M = map(int,(input().split()))

# stations = []
# stations = list(map(int,(input().split())))

# prev = [0] *1000001
# next = [0] *1000001

# for i in range(N):
#     current = stations[i]
#     prv = stations[i - 1]
#     nxt = stations[(i + 1) % N]

#     prev[current] = prv
#     next[current] = nxt

# for i in range(M):
#     parts = input().split()
#     command = parts[0]

#     if command == 'BN' or command == 'BP':
#         index = int(parts[1])
#         new_index = int(parts[2])
#     else:
#         index = int(parts[1])

#     match command:
#         case 'BN':
#             temp = next[index]
#             print(temp)

#             next[index] = new_index
#             prev[new_index] = index
#             next[new_index] = temp
#             prev[temp] = new_index

#         case 'BP':
#             temp = prev[index]
#             print(temp)

#             prev[index] = new_index
#             next[new_index] = index
#             prev[new_index] = temp
#             next[temp] = new_index

#         case 'CN':
#             temp = next[index]
#             print(temp)

#             nxt = next[temp]
#             next[index] = nxt
#             prev[nxt] = index

#         case 'CP':
#             temp = prev[index]
#             print(temp)

#             prv = prev[temp]
#             prev[index] = prv
#             next[prv] = index








import sys
input = sys.stdin.readline

N, M = map(int, input().split())

stations = list(map(int, input().split()))

prev = [0] * 1000001
next = [0] * 1000001

for i in range(N):
    current = stations[i]
    prv = stations[i - 1]
    nxt = stations[(i + 1) % N]

    prev[current] = prv
    next[current] = nxt

result = []

for _ in range(M):
    parts = input().split()
    command = parts[0]

    if command == 'BN' or command == 'BP':
        index = int(parts[1])
        new_index = int(parts[2])
    else:
        index = int(parts[1])

    match command:
        case 'BN':
            temp = next[index]
            result.append(str(temp))

            next[index] = new_index
            prev[new_index] = index
            next[new_index] = temp
            prev[temp] = new_index

        case 'BP':
            temp = prev[index]
            result.append(str(temp))

            prev[index] = new_index
            next[new_index] = index
            prev[new_index] = temp
            next[temp] = new_index

        case 'CN':
            temp = next[index]
            result.append(str(temp))

            nxt = next[temp]
            next[index] = nxt
            prev[nxt] = index

        case 'CP':
            temp = prev[index]
            result.append(str(temp))

            prv = prev[temp]
            prev[index] = prv
            next[prv] = index

print('\n'.join(result))


import sys
input = sys.stdin.readline  # 입력이 많으므로 빠른 입력 사용

# N: 처음 역의 개수
# M: 명령의 개수
N, M = map(int, input().split())

# 처음 주어지는 역 번호들
stations = list(map(int, input().split()))

# prev[x] : x번 역의 이전 역 번호
# next[x] : x번 역의 다음 역 번호
# 역 번호는 최대 1,000,000까지 올 수 있으므로 그 크기만큼 배열 생성
prev = [0] * 1000001
next = [0] * 1000001

# 처음 역들을 원형 이중 연결 리스트 형태로 연결
for i in range(N):
    current = stations[i]              # 현재 역
    prv = stations[i - 1]              # 현재 역의 이전 역
    nxt = stations[(i + 1) % N]        # 현재 역의 다음 역 (원형이므로 % N 사용)

    prev[current] = prv                # 현재 역의 이전 역 저장
    next[current] = nxt                # 현재 역의 다음 역 저장

# 출력이 많으므로 바로 print하지 않고 결과를 모아둠
result = []

# 명령 처리
for _ in range(M):
    parts = input().split()            # 명령 한 줄을 공백 기준으로 분리
    command = parts[0]                 # 명령어 종류: BN, BP, CN, CP

    # BN, BP는 역 번호 2개(i, j)를 받음
    if command == 'BN' or command == 'BP':
        index = int(parts[1])          # 기준 역 번호 i
        new_index = int(parts[2])      # 새로 삽입할 역 번호 j
    # CN, CP는 역 번호 1개(i)만 받음
    else:
        index = int(parts[1])          # 기준 역 번호 i

    match command:
        case 'BN':
            # BN i j
            # i의 다음 역 번호를 출력하고,
            # i와 그 다음 역 사이에 j를 삽입

            temp = next[index]         # 원래 i의 다음 역
            result.append(str(temp))   # 출력값 저장

            # index <-> temp 사이에 new_index 삽입
            next[index] = new_index
            prev[new_index] = index
            next[new_index] = temp
            prev[temp] = new_index

        case 'BP':
            # BP i j
            # i의 이전 역 번호를 출력하고,
            # i의 이전 역과 i 사이에 j를 삽입

            temp = prev[index]         # 원래 i의 이전 역
            result.append(str(temp))   # 출력값 저장

            # temp <-> index 사이에 new_index 삽입
            prev[index] = new_index
            next[new_index] = index
            prev[new_index] = temp
            next[temp] = new_index

        case 'CN':
            # CN i
            # i의 다음 역 번호를 출력하고,
            # 그 다음 역을 삭제

            temp = next[index]         # 삭제할 역 = i의 다음 역
            result.append(str(temp))   # 출력값 저장

            nxt = next[temp]           # 삭제할 역의 다음 역
            next[index] = nxt          # i의 다음 역을 nxt로 변경
            prev[nxt] = index          # nxt의 이전 역을 i로 변경

        case 'CP':
            # CP i
            # i의 이전 역 번호를 출력하고,
            # 그 이전 역을 삭제

            temp = prev[index]         # 삭제할 역 = i의 이전 역
            result.append(str(temp))   # 출력값 저장

            prv = prev[temp]           # 삭제할 역의 이전 역
            prev[index] = prv          # i의 이전 역을 prv로 변경
            next[prv] = index          # prv의 다음 역을 i로 변경

# 모아둔 결과를 한 번에 출력
print('\n'.join(result))