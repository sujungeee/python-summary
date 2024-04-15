from collections import deque

dq= deque()

# append(x), appendleft(x)
print('append(x), appendleft(x): ')
dq.append(1) # deque([1])
dq.append(2) # deque([1, 2])
dq.appendleft(3) # deque([3, 1, 2])
dq.appendleft(4) # deque([4, 3, 1, 2])

print(dq) # deque([4, 3, 1, 2])
print()

# pop(), popleft()
print('pop(), popleft(): ')
dq.pop() # deque([4, 3, 1])
dq.popleft() # deque([3, 1])

print(dq) # deque([3, 1])
print()

# insert(i, x)
print('insert(i, x): ')
dq.insert(1, 2)

print(dq) # deque([3, 2, 1])
print()

# extend(array), extendleft(array)
print('extend(array), extendleft(array): ')
dq.extend([0,3]) # deque([3, 2, 1, 0, 3])
dq.extendleft([10, 6]) # deque([6, 10, 3, 2, 1, 0, 3])

print(dq) # deque([6, 10, 3, 2, 1, 0, 3])
print()

# remove(value)
print('remove(value): ')
dq.remove(3) # deque([6, 10, 2, 1, 0, 3])

print(dq) # deque([6, 10, 2, 1, 0, 3])
print()

# reverse()
print('reverse(): ')
dq.reverse() # deque([3, 0, 1, 2, 10, 6])

print(dq)
print() # deque([3, 0, 1, 2, 10, 6])

# 길이, 요소 접근
print(len(dq)) # 6
print(dq[0]) # 3