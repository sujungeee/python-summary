# 이진트리 구현: 삽입, 탐색, 삭제

# 삭제 참고 링크(1): https://doing7.tistory.com/92
# 삭제 참고 링크(2): https://velog.io/@seanlion/bstimplementation

class Node:
    def __init__(self, key):
        self.left= None
        self.right= None
        self.val= key

class BST:
    def __init__(self):
        self.root= None

    # 삽입
    def insert(self, key):
        if not self.root:
            self.root= Node(key)
        else:
            curr= self.root

            while True:
                if key < curr.val:
                    if curr.left:
                        curr= curr.left
                    else:
                        curr.left= Node(key)
                        break
                else:
                    if curr.right:
                        curr= curr.right
                    else:
                        curr.right= Node(key)
                        break

    # 탐색
    def search(self, key):
        curr= self.root

        while True:
            if curr is None:
                return -1
            if key == curr.val:
                return curr.val
            elif key < curr.val:
                curr= curr.left
            else:
                curr= curr.right

    # 삭제
    def delete(self, key):
        curr= self.root
        parent= None

        while True:
            if curr is None:
                return -1
            if key == curr.val: # 삭제할 노드
                break
            else:
                parent= curr
                if key < curr.val:
                    curr= curr.left
                else:
                    curr= curr.right

        # case 1: leaf node 삭제
        if curr.left == None and curr.right == None:
            if key <  parent.val:
                parent.left= None
            else:
                parent.right= None

        # case 2: 자식 노드가 1개인 node 삭제
        elif curr.left != None and curr.right == None:
            # 2-1: 왼쪽 자식 노드만 가지고 있을 때
            if key < parent.val:
                parent.left= curr.left
            else:
                parent.right= curr.left
        elif curr.left == None and curr.right != None:
            # 2-2: 오른쪽 자식 노드만 가지고 있을 때
            if key < parent.val:
                parent.left= curr.right
            else:
                parent.right= curr.right

        # case 3: 자식 노드가 2개인 node 삭제
        if curr.left != None and curr.right != None:
            change_node = curr.right
            change_node_parent = curr.right

            # 삭제할 노드의 오른쪽 자식 노드 중에서 가장 작은 노드를 찾는다.
            while change_node.left != None:
                change_node_parent = change_node
                change_node = change_node.left

            # 가장 작은 노드가 오른쪽 자식을 가지는 경우
            if change_node.right != None:
                change_node_parent.left = change_node.right
            else:  # 가장 작은 노드가 오른쪽 자식을 가지지 않는 경우
                change_node_parent.left = None

            # 3-1: 삭제할 노드가 부모 노드의 왼쪽에 있을 때
            if key < parent.val:
                # 삭제 노드 위치에 change_node(삭제 노드의 오른쪽 서브 트리에서 가장 작은 값을 가지는 노드)를 넣기
                parent.left= change_node
            # 3-2: 삭제할 노드가 부모 노드의 오른쪽에 있을 때
            else:
                parent.right= change_node

            change_node.right = curr.right
            change_node.left = curr.left
