# https://wikidocs.net/197589
# 노드 클래스 정의
class DoubleNode():
    def __init__(self, _data):
        self.data= _data
        self.prev= None
        self.next= None

# 덱 클래스
class Deque:
    def __init__(self):
        self.head= None
        self.tail= None
        self.length= 0

    # 덱 노드 개수
    def __len__(self):
        return self.length

    # 덱 상태 출력
    def __str__(self):
        if self.head is None:
            return 'Empty!'
        res= ''
        node= self.head
        while node.next is not None:
            res += str(node.data) + " <-> "
            node= node.next
        return res + str(node.data)

    # 값 포함되어 있는지의 여부
    def __contains__(self, target):
        if self.head is None:
            return False
        node= self.head
        while node is not None:
            if node.data == target:
                return True
            node= node.next
        return False

# 테스트하기
dq= Deque()
dq.head= dq.tail= DoubleNode(0)
dq.head.next= DoubleNode(1)
dq.head.next.prev= dq.head
dq.tail= dq.head.next

print(dq)
print(len(dq))
for target in (1, 2):
    if target in dq:
        print(f"{target} is in dq.")
    else:
        print(f"{target} is not in dq.")