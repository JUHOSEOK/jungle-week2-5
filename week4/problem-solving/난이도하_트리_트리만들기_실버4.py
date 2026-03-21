# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

# 아이디어 : 정점의 개수만큼 2중 반복문을 돌려 간선이 되는 모든 경우의 수를 계산해 간선이 되면 배열에 추가하여 출력한다.

# 시간 복잡도

# 아이디어 : 정점의 개수만큼 반복문을 돌려


# 1. n, m 입력 받기
# 2. 0 1 은 먼저 출력하기

import sys

input = sys.stdin.readline

tree = list(map(int,input().split()))
n= tree[0]
m = tree[1]

print(0, 1)
for i in range(2, n):
    if i <= m:
        # i가 m 이하일 때는 1번(허브)에 붙이기
        print(1, i)
    else:
        # m을 넘어가면 기차처럼 줄기 늘리기
        print(i-1, i)