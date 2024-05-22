import heapq
import random
datas=[]

# 개념
# : 정렬한 자료를 최대 힙이나 최소 힙을 재배열하여 정렬을 하는 방법

# 시간 복잡도
# (최선): O(NlogN)
# (최악): O(NlogN)

# 특징
#   - 안정적인 성능으로 정렬할 수 있음
#   - 데이터를 삽입과 동시에 빠르게 정렬할 수 있음

# 1) 오름차순 정렬
# 1-1. 최소힙을 사용: 하나씩 heappop하면 오름차순 정렬이 됨
# 1-2. 최대힙을 사용: 루트 노드(최댓값)의 값을 배열의 끝으로 이동,
#               남은 힙 재정렬하여 배열의 왼쪽으로(반대 방향으로) 값을 채워가기

# 1-1. 최소힙을 사용한 오름차순 정렬
for _ in range(10):
    datas.append(random.randrange(15))

byMinHeap= []
heapq.heapify(byMinHeap)
result= []

for data in datas: # 우선순위 큐인 byMinHeap에 data들을 다 넣는다.
    heapq.heappush(byMinHeap, data)

for _ in range(len(byMinHeap)): # byMinHeap에서 하나씩 pop하면 가장 작은 요소가 pop되므로 result에 append하기
    result.append(heapq.heappop(byMinHeap))

# 1-3. 최대힙을 사용한 오름차순 정렬(최대힙에서 뽑힌 수가 가장 크므로 배열 가장 끝쪽에 두기)
byMaxHeap= []
heapq.heapify(byMaxHeap)
result= [0 for _ in range(10)]

for data in datas:
    heapq.heappush(byMaxHeap, [-data, data])

cnt= len(byMaxHeap)-1
for _ in range(len(byMaxHeap)):
    tmp= heapq.heappop(byMaxHeap)
    result[cnt]= tmp[1]
    cnt-=1
