from collections import deque
# graph= [(1, 2, 1), (1, 5, 3), (2, 4, 2), (4, 5, 5), (2, 3, 6), (3, 5, 4)]
graph= [(1, 2, 1), (1, 4, 2), (2, 4, 2),(2, 3, 3), (3, 4, 4)]
# 크루스칼 알고리즘
# - 최소 신장 트리를 구하는 알고리즘(그리디 알고리즘)
# - 간선이 중심!

# 과정
# 0. 정점의 개수 구하기
nodes= set()
for g in graph:
    nodes.add(g[0])
    nodes.add(g[1])
N= len(nodes) # 정점의 개수

# 1. 노드 사이의 가중치에 대해 오름차순 정렬
graph.sort(key= lambda x: x[2]) # [(1, 2, 1), (2, 4, 2), (1, 5, 3), (3, 5, 4), (4, 5, 5), (2, 3, 6)]
graph= deque(graph)

# 2. 부모 자식 관계로 루트 노드를 확인하기 위한 CPR
CPR= [i for i in range(6)]

# 3. 가중치가 가장 작은 노드를 최소 신장 트리에 추가
MST= []
minInfo= graph.popleft()
MST.append(minInfo)
CPR[minInfo[1]]= minInfo[0]
cnt= 1 # 간선의 개수

# 4. 그 다음 가중치부터 사이클을 형성하는지 확인하고, 사이클이 없으면 그래프에 추가
while graph:
    if cnt==N-1:
        break

    # 4-1 사이클 형성하는지 확인
    isCycle= False
    start, end= graph[0][0], graph[0][1]
    while CPR[start]!= start:
        start= CPR[start]
    while CPR[end]!= end:
        end= CPR[end]
    if start == end:
        isCycle= True

    # 4-2 사이클이 없으면 그래프에 추가
    minInfo= graph.popleft()
    if isCycle == False:
        MST.append(minInfo)
        CPR[minInfo[1]]= minInfo[0]
        cnt+=1

print(MST)