# 우선순위 큐 by heapq
import heapq

# 작은 값일수록 우선 순위가 높을 때

hq1= [5, 1, 3, 10, 8]
heapq.heapify(hq1)
result= []
for _ in range(len(hq1)):
    result.append(heapq.heappop(hq1))

print(result)

# 큰 값일수록 우선 순위가 높을 때
class MaxHeap:
    def __init__(self):
        self.heap= []
        self.num= 0

    def push(self, value):
        heapq.heappush(self.heap, -value)
        self.num+=1

    def pop(self):
        return -heapq.heappop(self.heap)



max_heap= MaxHeap()
max_heap.push(5)
max_heap.push(1)
max_heap.push(3)
max_heap.push(10)
max_heap.push(8)

result= []
for _ in range(max_heap.num):
    result.append(max_heap.pop())

print(result)
