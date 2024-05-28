from collections import deque
# 개념
# : 방향성이 있는 그래프에서 차수가 0인 정점부터 정렬하는 알고리즘

# 시간 복잡도
# (최선): O(V+E)
# (최악): O(V+E)

# 특징
#   - 작업의 순서가 존재할 때 사용되는 알고리즘

n, m= map(int, input().split()) # n: 정점의 개수, m: 간선의 개수

indegree= [0 for _ in range(n+1)]
graph= [[] for _ in range(n+1)]

for _ in range(m):
    start, end= map(int, input().split())
    graph[start].append(end)
    indegree[end]+=1

def topology_sort(graph, indegree):
    result= []
    queue= deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        current= queue.popleft()
        result.append(current)

        for i in graph[current]:
            indegree[i]-=1
            if indegree[i] == 0:
                queue.append(i)

    return result

print(topology_sort(graph, indegree))