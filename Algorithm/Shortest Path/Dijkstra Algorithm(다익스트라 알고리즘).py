# 다익스트라 알고리즘
# : 가중치가 있는 그래프의 최단 경로를 구하는 알고리즘
# , 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것이 핵심 !!

# 필요한 요소
# 1. 시작 노드
# 2. 시작 노드-목적 노드, 가중치
# 3. 방문 여부(visited) -- distance[node] < d로 간접 확인

# 구해야 할 것
# 1. 각 노드까지의 최소 가중치 값
# 2. 시작 노드부터 최소 가중치 값을 가지는 경로


# 전체적인 흐름
# 1. 비용이 가장 작은 노드를 선택하기(by 우선순위 큐)
#        1-1 노드에서 나온 비용이 노드의 최소 비용(distance[node])보다 크면 continue
#           [이유]: 최소 비용은 이미 갱신되고 예전에 heappush했던 [최소 비용, 노드] 가 존재하므로
# 2. 최소 비용을 갖는 노드를 거쳐서 다른 인접 노드들이 최소 가중치 값을 갱신할 수 있는지 확인
#    --> 해당 경유지로 최소 비용을 가질 수 있다면
#        2-1 최소 비용을 갱신(distance)
#        2-2 최단 경로 추가: 현재 path + 인접 노드
# 3. 모든 노드를 방문하면 각 노드의 최소 비용 및 최단 경로를 알 수 있음

import heapq

graph= {
    'A': {'B': 9, 'C': 3},
    'B': {'A': 5},
    'C': {'B': 1}
}

start= 'A'

def dijkstra(graph, start):
    # 1. 각 노드의 최소 가중치 값을 구하기 위함
    distance= {node : float('inf') for node in graph}
    distance[start] = 0

    # 2. 각 노드까지의 최소 가중치 값을 갖는 경로를 구하기 위함
    path= {start: [start]}

    que= []
    heapq.heappush(que, [distance[start], start])

    while que:
        d, node= heapq.heappop(que)
        # node의 거리가 d보다 작다는 것
        # : 힙에 노드가 들어가고 해당 노드가 다른 경유지로 인해 최소 거리가 갱신 됐기 때문
        # , 이미 최소 거리가 d보다 작기 때문에 뛰어 넘음
        if distance[node] < d:
            continue

        # 현재 graph의 최소 거리보다 d+가중치가 더 적으면 현재 node를 경유해서 더 작은 가중치를 가질 수 있다는 뜻이므로 graph를 갱신
        for adj_node, weight in graph[node].items():
            if d + weight < distance[adj_node]:
                # 최소 거리와 최단 경로 갱신
                distance[adj_node]= d + weight
                path[adj_node]= path[node] + [adj_node]
                heapq.heappush(que, [d+weight, adj_node])

    sorted_path= sorted(path.items())

    return [distance, sorted_path]

print(dijkstra(graph, start))