# 이진트리_구현 by 배열
# https://wikidocs.net/193817
# 부모 노드의 인덱스: n
# 왼쪽 자식 노드의 인덱스: 2n+1
# 오른쪽 자식 노드의 인덱스: 2n+2

tree= [1, 4, 8, 3, 5, 7, None, 2, None, None, None, 6, None, None, None]

# 자식 노드 찾기
print('자식 노드 찾기')
i= 0
n= len(tree)

while i<n:
    if tree[i]:
        print(f"Parent: {tree[i]}", end= ', ')
        left= 2*i + 1
        right= 2*i + 2
        if left<n and tree[left] is not None:
            print(f"Left: {tree[left]}", end= ', ')
        if right<n and tree[right] is not None:
            print(f"Right: {tree[right]}", end=', ')
        print()
    i+=1


# 부모 노드 찾기
print('부모 노드 찾기')
i=n-1 # 14
while i>0: # 0은 루트 노드여서 부모 노드가 없다.
    if tree[i]:
        print(f"Parent of {tree[i]} -> {tree[(i-1)//2]}")
    i-= 1