"""
[퀵 정렬 구현]

문제 설명:
- 퀵 정렬(Quick Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 피벗(pivot)을 기준으로 작은 값과 큰 값을 분할하여 재귀적으로 정렬합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [10, 7, 8, 9, 1, 5]
출력: [1, 5, 7, 8, 9, 10]

힌트:
- 피벗 선택 (일반적으로 마지막 원소)
- 피벗보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 분할
- 재귀적으로 왼쪽과 오른쪽 부분 정렬
"""

def partition(arr, start, end):
    """
    배열을 피벗 기준으로 분할하는 함수
    
    Args:
        arr: 배열
        low: 시작 인덱스
        high: 끝 인덱스
    
    Returns:
        피벗의 최종 위치 인덱스
    """
    # TODO: 피벗을 선택 (일반적으로 마지막 원소)
    mid = (start + end) // 2
    bibot = arr[mid]
    # 피벗을 선택 (중간값)
    # while 시작점이 끜지점보다 같거나 작을때만  {
    # while {왼쪽부터 차례로 선택값이 피벗보다크면 선택값이 피벗값보다 작으면 멈춰짐  } start 를 ++
    # while {오른쪽부터 차례로 피벗보다 작으면 선택값이 피벗보다 크면 멈춰짐 }  end 를 --
    # 만약에 지나치지 않았으면 {
    #     변경한 시작값하고 변경한끝에 값을 바꾸고
    #     start ++
    #     end --
    # }
    # }

    # 기준점으로 삼을 피벗을 선택
    # 재귀에서 피벗과 비교해서 앞과 뒤로 왼쪽과 뒤로 나눈후에 가운데에 피벗을 넣어둔다.

    while start <= end:
        while arr[start] < bibot:
            start += 1
        while arr[end] > bibot:
            end -= 1
        if start <= end:
            arr[end], arr[start] = arr[start], arr[end]
            start += 1
            end -= 1

    return start


    # TODO: i는 작은 원소들의 마지막 인덱스를 추적
    pass

    # TODO: low부터 high-1까지 순회하면서
    ## 현재 원소가 피벗보다 작거나 같으면:
    ##   1. i를 1 증가
    ##   2. arr[i]와 arr[j]를 교환
    pass

    # TODO: 피벗을 올바른 위치(i+1)에 배치
    pass

    return i + 1

def quick_sort_helper(arr, low, high):
    """
    퀵 정렬 재귀 함수
    
    Args:
        arr: 배열
        low: 시작 인덱스
        high: 끝 인덱스
    """
    # TODO: base case - low가 high보다 작을 때만 정렬
    if low >= high:
        return

    ## 파티션 분할하기
    part2 = partition(arr, low, high)
    ## 파티션 왼쪽 부분 재귀 정렬
    if low < part2-1:
        quick_sort_helper(arr, low, part2-1)
        # print(f"low:{low}, high{part2-1}")
    ## 파티션 오른쪽 부분 재귀 정렬
    if part2 < high:
        quick_sort_helper(arr, part2, high)
        # print(f"low{part2}, high{high}")

    return arr

    ## 피벗 오른쪽 부분 재귀 정렬
#
# def quick_sort(arr):
#     """
#     퀵 정렬 메인 함수
#
#     Args:
#         arr: 정렬할 배열
#
#     Returns:
#         정렬된 배열
#     """
#     quick_sort_helper(arr, 0, len(arr) - 1)
#     return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [10, 7, 8, 9, 1, 5]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = quick_sort_helper(arr1, 0, len(arr1)-1)
    print(f"정렬 후: {result1}")
    print()
    #
    # 테스트 케이스 2
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = quick_sort_helper(arr2, 0, len(arr2)-1)
    print(f"정렬 후: {result2}")
    print()

    # 테스트 케이스 3: 중복 원소
    arr3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("=== 테스트 케이스 3: 중복 원소 ===")
    print(f"정렬 전: {arr3}")
    result3 = quick_sort_helper(arr3, 0, len(arr3)-1)
    print(f"정렬 후: {result3}")
    print()

    # 테스트 케이스 4: 이미 정렬된 배열
    arr4 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 4: 이미 정렬됨 ===")
    print(f"정렬 전: {arr4}")
    result4 = quick_sort_helper(arr4, 0, len(arr4)-1)
    print(f"정렬 후: {result4}")
    print("이미 정렬된 경우 O(n²) 시간 소요 (최악의 경우)")

#
# arr1 = []
# quick_sort_helper(arr1, 0, len(arr1)-1)
#
# print(arr1)