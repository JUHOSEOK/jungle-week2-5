# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

# 입력
# 1. 입력으로 받을 수의 개수
# 2. 입력한 숫자들
#
# 출력:
# 입력한 세개의 수를 합했을때 존재하는 가장 큰수
#
# 1. 개수 입력받고
# 2. 배열로 숫자 입력받고
# 3. 세수 합치는 함수 만들어 완전탐색으로
# 4. 그리고 for 문 돌려봐 5번 세수 합친거가 set 자료구조에 있냐? 있으면 max(함수에 저장해놔)


# 1. 개수 입력받고
# 2. 배열데가 숫자 입력은거 넣고
# 3. 두개 합친거 set에 넣어놓고
# 4. 배열에있는거 하나 하나 2중for문으로  - set에 있는거 존재하면 max함수 저장

# 5
# 3
# 2
# 5
# 10
# 18

S = int(input())
num = [int(input()) for _ in range(S)]
max_num = 0
left = []

for i in range(S):
    for j in range(S):
        left_port = num[i] + num[j]
        left.append(left_port)
check_set = set(left)

for k in range(S):
    for z in range(S):
        if (num[k] - num[z]) in check_set:
            max_num =  max(num[k], max_num)

print(max_num)

