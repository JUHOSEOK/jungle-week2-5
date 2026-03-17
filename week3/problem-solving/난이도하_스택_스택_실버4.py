# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

# 입력:
# 1. 명령할 개수 ex)14
# 2. 명령어들 ex) push x, top, size, pop, empty
from collections import deque
# 출력:
# 1. pop, size, empty, top 에 따른 출력
#
# 1. 명령할 개수를 입력 받는다.
# 2.먄약에 push, top, size, empty, top, 이 들어올때의 로직을 구현한다.
# 3.5가지 명령의 순서가 중요할거같은데
#
# 14번 반복하는데
#   if push 라면?
#     리스트에 추가
#   elif pop이면 :
#     가장위에 있는 정수빼기? popleft
#   if size 라면:
#       len(arr) 한거 프린트
#   if empty라면 ?:
#       if len(arr) == 0 확인후 맞으면 1
#       else : 0
#   if top 이라면?
#     if popleft한거 있으면 꺼내오고
#     else 없으면 0-1

command_num = int(input())
arr = []
result = []

for i in range(command_num):
    command = input().split()

    if command[0] == "push":
        arr.append(command[1])
    elif command[0] == "pop":
        if len(arr) == 0:
            result.append(-1)
        else:
            result.append(arr.pop())

    elif command[0] == "size":
        # print(len(arr))
        result.append(len(arr))
    elif command[0] == "empty":
        if len(arr) == 0:
            result.append(1)
        else:
            # print(0)
            result.append(0)
    elif command[0] == "top":
        if len(arr) != 0:
            # print(arr.pop())
            result.append(arr[-1])
        else:
            # print(-1)
            result.append(-1)


for i in result:
    print(i)



