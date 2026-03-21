"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""
#
# def dfs(graph, start, visited=None):
#     """
#     깊이 우선 탐색 (재귀)
#
#     Args:
#         graph: 그래프 딕셔너리
#         start: 현재 정점
#         visited: 방문 리스트
#
#     Returns:
#         방문 순서 리스트
#     """
#
#     # 1. 스택생성
#     # 2. 시작노드 생성(append)
#     # 3. 스택에서 꺼냄 (pop)
#     # 4. 꺼낸노드의 자식을 스택에 넣음
#     # 4.1 만약에 자식도느가 스택에 존재하면 안넣음
#     # 5. 꺼낸애 출력 (visited)에 추가?
#
#     # TODO: visited가 None이면 초기화
#     pass
#     if visited is None:
#         visited = []
#     # TODO: 현재 정점 방문
#     pass
#     # 2. 시작 노드 생성
#
#     # 3. 꺼냄
#
#     # 5. 꺼낸에 출력?
#
#     # 4. 자식노드 스택에 넣음
#
#
#
#     # TODO: 인접한 정점들에 대해 재귀
#     ## 방문하지 않은 정점이면 재귀 호출
#     pass
#
#     return visited

def dfs (graph, start):

    stack = [start]

    visited = []

    while stack:

        pop_node = stack.pop()

        if pop_node not in visited:
            visited.append(pop_node)

            for neighbor in reversed(graph[pop_node]):
                stack.append(neighbor)

    return visited


    # 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


