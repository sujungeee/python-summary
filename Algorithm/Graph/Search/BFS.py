from collections import defaultdict, deque
# 너비 우선 탐색(BFS)
# : 시작 노드와 가장 가까운 노드를 우선하여 방문하는 방식의 알고리즘

# 그래프 순회
graph=[(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)]
start= 1

# 큐를 이용하여 BFS 순회
def graphSearchByQueue(graph, start):
    adj_list= defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    def bfs(start):
        visited= set()

        que= deque([start])
        result.append(start)
        visited.add(start)

        while que:
            node= que.popleft()

            for adj in adj_list.get(node, []):
                if adj not in visited:
                    que.append(adj)
                    result.append(adj)
                    visited.add(adj)

    result= []
    bfs(start)
    return result

print(graphSearchByQueue(graph, start))