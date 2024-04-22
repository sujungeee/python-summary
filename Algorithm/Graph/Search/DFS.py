from collections import defaultdict
# 깊이 우선 탐색(DFS)
# : 가장 깊은 노드까지 방문한 후에 더 이상 방문할 노드가 없으면
# 최근 방문한 노드로 돌아온 다음, 해당 노드에서 방문할 노드가 있는지 확인

# 그래프 순회
graph= [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
start= 'A'

# 스택을 이용하여 모든 그래프를 DFS로 순회
def graphSearchByStack(start, graph):
    adj_list= defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    result= []
    stack= [start]

    visited= set()
    visited.add(start)

    while stack:
        node= stack.pop()
        result.append(node)

        adjs= adj_list[node]
        adjs.reverse()
        for adj in adjs:
            if adj not in visited:
                visited.add(adj)
                stack.append(adj)

    return result

print(graphSearchByStack(start, graph))

# 재귀 함수를 이용하여 모든 그래프를 DFS로 순회

def graphSearchByRecursion(start,graph):
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)

    def dfs(node, visited, result):
        visited.add(node)
        result.append(node)

        for adj in adj_list.get(node, []):
            if adj not in visited:
                dfs(adj, visited, result)

    result= []
    visited= set()
    dfs(start, visited, result)
    return result

print(graphSearchByRecursion(start, graph))