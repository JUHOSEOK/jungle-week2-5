# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
from collections import deque
# 입력:
# 숫자의 개수
# ex) 6
# 123456
# 출력:
# 마지막에 남게되는 숫자
# ex)
# 1버리면 34562
# 3버리면 5624
# 5버리면 246
# 2버리면 64
# 6버리면 4
#
# 1. 숫자의개수를 받고 1부터 N까지 리스트에 저장?
# 2. popleft로 맨위에 숫자버리고 다음숫자를 popleft 해서 변수에 저장해서 저장한걸 다시 popappend한다
# 3. 숫자 하나 남을때까지 반복? While True로 한다음에 if 숫자하나면 break이게 맞나 아니면 while 숫자길이 > 1 이게맞나
S = int(input())
card_num_arr = [i + 1 for i in range(0,S)]

card_deque = deque(card_num_arr)

while len(card_deque) > 1:
    card_deque.popleft()
    num_second = card_deque.popleft()
    card_deque.append(num_second)
    # print(card_deque)

print(card_deque[0])