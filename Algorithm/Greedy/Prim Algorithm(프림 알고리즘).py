from collections import deque
import heapq

# graph= [(1, 2, 1), (1, 5, 3), (2, 4, 2), (4, 5, 5), (2, 3, 6), (3, 5, 4)]
graph= [(1, 2, 1), (1, 3, 8), (1, 4, 3), (3, 4, 4), (2, 4, 2),
        (2, 5, 7), (4, 5, 6), (3, 5, 5)]
# 프림 알고리즘
# - 최소 신장 트리를 구하는 알고리즘(그리디 알고리즘)
# - 노드가 중심!
MST= []

# 과정
# 0. 정점의 개수 구하기
nodes= set()
for g in graph:
    nodes.add(g[0])
    nodes.add(g[1])
N= len(nodes) # 정점의 개수
connected= set() # visited 개념

# 1. 임의의 노드(1번)부터 시작
hq= [] # heapq: (간선 가중치, 1번 노드)
heapq.heapify(hq)
for g in graph: # 1-1. 1번 노드와 연결된 노드를 heapq에 삽입
    if g[0] == 1:
        heapq.heappush(hq, [g[2], g[1]])
    elif g[1] == 1:
        heapq.heappush(hq, [g[2], g[0]])

connected.add(1)
startNode= 1
cnt= 1

# 2. heapq에서 가중치, 노드의 정보를 꺼내(heappop) connected에 있는지 확인한 후,
# 확인 여부에 따라 그래프에 포함시키기 or 다음 정보 확인
while cnt != N:
    weight, node= heapq.heappop(hq)

    # 2-1. 꺼낸 노드가 connected(방문한 노드 set)에 있는지 확인
    if node not in connected: # 꺼낸 노드가 방문한 적 없는 노드이면 그래프에 추가
        connected.add(node) # 방문
        cnt+=1
        MST.append((startNode, node, weight)) # 그래프에 추가
        startNode= node

        # 2-2. 꺼낸 노드와 연결된 노드가 있다면 heapq에 삽입
        for g in graph:  # 1-1. 1번 노드와 연결된 노드를 heapq에 삽입
            if g[0] == node:
                heapq.heappush(hq, [g[2], g[1]])
            elif g[1] == node:
                heapq.heappush(hq, [g[2], g[0]])

print(MST)