# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

# 아이디어: 위성정렬을 통해 순서를 정하고 그 배열의 숫자에 저장해놓은 시간 배열에 인덱스접근해 시간을 더한다?
# queue를 통해 빼면서 가장큰값을 시간 업데이트

import sys
from collections import deque

input = sys.stdin.readline  # 백준 시간초과 방지용!

v = int(input())

# 1. 시간 배열 (1번부터 v번까지 편하게 쓰려고 인덱스를 v+1개 만듭니다)
time = [0] * (v + 1)

# 2. 그래프 (선행 작업 -> 다음 작업)
graph = {i: [] for i in range(1, v + 1)}

# 3. 진입차수 배열 (나를 가리키는 화살표 개수)
in_degree = [0] * (v + 1)

# 1번 작업부터 v번 작업까지 차례대로 입력을 받습니다.
for i in range(1, v + 1):
    # 한 줄을 읽어서 정수들의 리스트로 바꿉니다. (예: [6, 1, 1])
    data = list(map(int, input().split()))

    # 첫 번째 숫자(인덱스 0)는 걸리는 시간!
    time[i] = data[0]

    # 세 번째 숫자(인덱스 2)부터 끝까지가 모두 선행 작업들의 번호입니다.
    # data[2:] 를 하면 [1] 만 쏙 빠져나옵니다.
    for pre_work in data[2:]:
        # 선행 작업(pre_work)이 끝나면 현재 작업(i)을 하러 가야 하니까 이렇게 연결!
        graph[pre_work].append(i)

        # 현재 작업(i)을 가리키는 화살표가 하나 생겼으니 진입차수 +1
        in_degree[i] += 1


queue = deque()

for i in range(1, v + 1):
    if in_degree[i] == 0:
        queue.append(i)
result_time = time[:]
cnt = 0
while queue:
    work_node = queue.popleft()


    for next_time in graph[work_node]:
        in_degree[next_time] -= 1

        result_time[next_time] = max(result_time[next_time], time[next_time] + result_time[work_node])



        if in_degree[next_time] == 0:
            queue.append(next_time)



print(max(result_time))

