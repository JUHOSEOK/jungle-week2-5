# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

# 문제 : 선위순위 트리 값들 주어지면 그걸로 후위순위 트리 값으로 출력하기
# 아이디어: 루트(start 값)찾고 왼쪽 서브트리 end값 찾고 오른쪽 루트(start)찾고 end값 찾아서 제귀호출?
import sys

sys.setrecursionlimit(10 ** 5)
# 입력 전체를 한 번에 읽어와서 정수 리스트로 변환합니다.
tree = [int(x) for x in sys.stdin.readlines()]





def postorder(nums):
    # 1. 종료 조건: 넘어온 리스트가 비어있다면 탐색할 것이 없으므로 종료!
    if len(nums) == 0:
        return

    # 2. 현재 트리의 루트는? 항상 전위 순회(preorder) 리스트의 첫 번째 값!
    root = nums[0]

    left_subtree = []
    right_subtree = []

    # 3. 루트 다음 값들(인덱스 1부터 끝까지)을 보면서 왼쪽/오른쪽 나누기
    for i in range(1, len(nums)):
        if nums[i] < root:
            left_subtree.append(nums[i])
        else:
            right_subtree.append(nums[i])

    postorder(left_subtree)
    postorder(right_subtree)
    print(root)

postorder(tree)
