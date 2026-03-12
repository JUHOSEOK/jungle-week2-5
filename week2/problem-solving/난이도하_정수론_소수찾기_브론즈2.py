# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

# 입력 : 주어지는 수의개수 n, 주어지는 수들 check []
# n = 4
# check = 1 3 5 7

# 출력 : 소수의 개수
# 3

# 1. 문자의 개수를 받고
# 2. 개수에 만큼 for문 돌려서 배열에 넣고
# 3.또 for문 돌려서 sosu함수 하나씩 넣어보기
import math

def sosu(n):
    n = int(n)

    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    # for i in range(2, int(math.sqrt(n)) + 1):
    #     if n % i == 0:
    #         return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


lenth = int(input())
result = 0
# check = []

# check.append(input().split(" "))
check = input().split(" ")

for i in range(lenth):
    if sosu( check[i] ):
        result += 1

print(result)
