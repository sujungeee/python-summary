# 트리 삽입 후 순회
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
    # 전위 순회: 부모 -> 왼쪽 -> 오른쪽
    def preorder(self):
        def _preorder(curr):
            print(curr.val, end= ' ')
            if curr.left:
                _preorder(curr.left)
            if curr.right:
                _preorder(curr.right)

        _preorder(self.root)

    # 중위 순회: 왼쪽 -> 부모 -> 오른쪽
    def inorder(self):
        def _inorder(curr):
            if curr.left:
                _inorder(curr.left)
            print(curr.val, end= ' ')
            if curr.right:
                _inorder(curr.right)

        _inorder(self.root)


    # 후위 순회: 왼쪽 -> 오른쪽 -> 부모
    def postorder(self):
        def _postorder(curr):
            if curr.left:
                _postorder(curr.left)
            if curr.right:
                _postorder(curr.right)
            print(curr.val, end= ' ')

        _postorder(self.root)

tree= BST()

tree.insert(10)
tree.insert(5)
tree.insert(12)
tree.insert(2)
tree.insert(8)
tree.insert(11)
tree.insert(15)
tree.insert(1)
tree.insert(4)
tree.insert(6)
tree.insert(9)
tree.insert(13)
tree.insert(14)
tree.insert(3)

print('전위 순회 결과 -> ', end= ' ')
tree.preorder()
print()
print('중위 순회 결과 -> ', end= ' ')
tree.inorder()
print()
print('후위 순회 결과 -> ', end= ' ')
tree.postorder()