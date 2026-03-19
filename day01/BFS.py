from collections import deque

# BFS(시작 노드):
#     큐에 시작 노드 넣기
#     방문 표시

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

#   큐가 비어있지 않는 동안:
#         현재 = 큐에서 꺼내기
#         현재 노드 처리

    while queue:
        node = queue.popleft()
        order.append(node)

#       현재의 이웃들에 대해:
#           방문하지 않았으면:
#               방문 표시
#               큐에 넣기

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order
