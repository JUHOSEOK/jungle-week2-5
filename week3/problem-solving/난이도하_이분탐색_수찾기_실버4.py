# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
#
# 입력:
# 1.탐색할원소 개수
# 2.기준원소리스트
# 1.탐색할원소 개수
# 2.원소리스트
#
# 출력:
# 1. 원소리스트에서 기준원소리스트가 있으면 1, 없으면 0

def binary_search(arr, target):

    left = 0
    right = len(arr) - 1


    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True

        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1

    return False

s = int(input())
N = [int(x) for x in input().split()]

N.sort()

s2 = int(input())
N2 = [int(x) for x in input().split()]



for i in range(s2):
    if binary_search(N, N2[i]) :

        print(1)
    else:

        print(0)

# sort 써야댐