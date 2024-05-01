# [다익스트라]
# 1. 하나의 정점에서 다른 모든 정점까지의 최단 거리를 구하는 알고리즘
# 2. 그리디 알고리즘
# [플로이드-워셜]
# 1. 한 번 실행하여 **(모든 노드)** 간 최단 경로를 구하는 알고리즘
# 2. 음의 가중치도 가능
# 3. 다이나믹 프로그래밍(점화식)

# 점화식: D_ab= min(D_ab, D_ak+D_kb)
# 노드가 k 일때, k를 제외한 두 노드 a,b 가 k를 거쳐서 더 작은 거리가 나오면
# 그 값으로 a와 b 사이의 거리를 갱신
# 따라서, 2차원 리스트가 필요

# 전체 과정
# 1. 2차원 리스트를 초기화한다.
#   1-1. 각 노드에서 노드까지 가중치가 있으면 그 값으로 초기화
#   1-2. 가중치가 없으면 float('inf')
#   1-3. 자신의 노드로부터의 값은 0으로 초기화

# 2. 총 노드의 개수가 N개일 때, N번의 단계만큼 수행한다.
#   2-1. k 노드(<=N) 를 제외한 모든 노드들 중에서 2개를 선택한다(순서 의미 있음, 즉 ab와 ba는 다른 순서)
#   2-2. 선택한 2개의 노드에 대해 중간에 k를 거쳐서 더 작은 값이 나온다면,
#        그 값으로 2차원 리스트를 갱신한다.
#   2-3. 모든 k Permutation 2 에 대해서 2-1과 2-2를 수행한다. (Permutation: 순열)


n= int(input()) # 노드의 개수
m= int(input()) # 간선의 개수

# 1. 2차원 리스트를 초기화한다.
# 1-2. 가중치가 없으면 float('inf')
graph= [[float('inf')]*(n+1) for _ in range(n+1)]
# 1-3. 자신의 노드로부터의 값을 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j]= 0
# 1-1. 각 노드에서 노드까지 가중치가 있으면 그 값으로 초기화
for _ in range(m):
    a, b, w= map(int, input().split())
    graph[a][b]= w

# 2. 총 노드의 개수가 n개일 때, n번의 단계만큼 수행한다.
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]= min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]== float('inf'):
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()