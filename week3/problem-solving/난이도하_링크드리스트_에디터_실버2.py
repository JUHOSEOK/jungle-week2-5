# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
#
# 입력:
# 1. 문자열
# 2. 명령이 들어올 갯수
#
# 출력:
# 명령어에 의해 수정된 문자열
# #
# 이 문제를 어떻게 링크드 리스트로 푸냐
# 기존에 만들었던 08의 기능에서 왼쪽주소를 참조해 중간에 삽입 가능하게 만들어야 하는데
# l+1 배열을 만들어놓고 배열의 마지막위치를 커서의 위치로 생각?
# L 이 들어오면 커서의 위치하는 공간이 문자열 사이에 있으면 왼쪽의 공간과 오른쪽의 공간(배열)을 두 배열로 쪼개버리기
# ex) [a,b,c,d] , []
# L [a,b,c], [d]
# L [a, b,] , [d, c]
# PX [a, b, X], [d c]
# D [a, b, x, c] [d]
# B [a b x] [d]
#
# 출력
# [a, b, x] + reversed([d])
#
# 1. 리스트로 문자열 받는다
# 2. 갯수 받는다.
# 3. 명령어 개수만큼 받는다.
# 3.1 처음에 받은 문자열은 left_stack에 다 넣고 right_stack은 초기화만해놓는다
# 3.2 만약 L이 들어올때는 left_stack에 마지막 값을 pop하고 right_stack에 추가한다.
# 3.2 만약 D가 들어올때는 right_stack에 마지막 값을 pop하고 그 값을 left_stack에 추가한다.
# 3.3 만약 B가 들어올때는 left_stack에 마지막 값을 pop한다 만약 인덱스 번호가 0이라면 하지안는다.
# 3.3 P가 들어올때는 left_stack에 마지막 위치에 append한다.
# 4 출력할대는 left_stack + reversed(right_stack) 으로 합쳐 출력한다.

# left_stack = [input()]
import sys

input = sys.stdin.readline

left_stack = list(input().rstrip())
command_N = int(input())
right_stack = []

for i in range(command_N):
    command = input().split()

    if command[0] == 'P':
        left_stack.append(command[1])
    # if문을 L, D, B, P 중에 어떤걸 만났을때 제일 앞에 두는게좋을까
    elif command[0] == 'L' and left_stack:
        left = left_stack.pop()
        right_stack.append(left)
    elif command[0] == 'D' and right_stack:
        right = right_stack.pop()
        left_stack.append(right)

    elif command[0] == 'B' and left_stack:
        left_stack.pop()

left_result = "".join(left_stack)
right_stack.reverse()
right_result = "".join(right_stack)


print(left_result + right_result)