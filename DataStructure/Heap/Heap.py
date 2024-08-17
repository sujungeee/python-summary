import heapq

# 1. 최소힙, 최대힙
# 1. heapify, heappush, heappop, nlargest, nsmallest
# 2. 힙 정렬

# 1.
# heapify
hq1= [5, 1, 3, 10, 8]
heapq.heapify(hq1)
print('리스트-> 힙: ', hq1) # [10, 50, 20]

# 최소힙, 최대힙

# 최소힙: 자식 노드가 부모 노드보다 큼(by heappush)
heap= []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
print('최소힙: ', heap) # [10, 50, 20]

# heappop: heappop이 완료된 heap은 남은 원소들로 다시 최소힙을 구성한다.
result= heapq.heappop(heap)
print(result) # 10
print(heap) # [20, 50]
print(heap[0]) # 20

# 최대힙: 부모 노드가 자식 노드보다 큼

heap_items= [1, 3, 5, 7, 9]
max_heap= [] # 최대힙
tmp_heap= [] # 임시 힙
for item in heap_items:
    heapq.heappush(tmp_heap, (-item, item))

for _ in range(len(heap_items)):
    tmp= heapq.heappop(tmp_heap)
    max_heap.append(tmp[1])

print(max_heap) # [9, 7, 5, 3, 1]

# nlargest, nsmallest
heap= [1, 3, 5, 7, 9]
heapq.heapify(heap)
print(heap) # [1, 3, 5, 7, 9]
print(heapq.nlargest(n=2, iterable=heap)) # [9, 7]
print(heapq.nsmallest(n=2, iterable=heap)) # [1, 3]

# 2.
# 힙 정렬- Algorithm-Sorting-힙 정렬.py 참조