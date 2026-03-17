# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

# 입력:
# 1. 숫자개수
# 2. 숫자들
#
# 출력:
# 1. 두수를 연산햇을때 0 의 가장 가까운 두수
# 1. for 문으로 타겟으로 고를값을 정한다.
# 2. 타겟값과 가장 동떨어진값 ex) -2 == +2를 찾는다.
# 3. 없다면 가장 근처값을 찾아 min(함수로 저장한다.)

S = int(input())
arr = list(map(int, input().split()))
arr.sort()

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # 왜 범위가 1개일때는 생각하지 못했을까
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, mid

        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1

    return left, right

min_num = float('inf')

for i in range(S):
    value = int(arr[i])
    target = -value

    left,right = binary_search(arr, target)

    print("왼쪽",left,"오른쪽",right)



#     candidate = []
#
#     if min_num > (abs(arr[output] + value)):
#         ans1 = arr[output]
#         ans2 = value
#         min_num = abs(arr[output] + value)
#
# result_arr = [ans1,ans2]
# result_arr.sort()
# print(" ".join(map(str,result_arr)))









