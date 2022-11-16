MAX_QSIZE = 10
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class CircularLinkedQueue:
    def __init__(self):
        self.tail = None #front = self.tail.link
        
    def isEmpty(self): return self.tail == None
    def clear(self): self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
        
    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
            
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def size(self):
        if self.isEmpty(): return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                count += 1
                node = node.link
            return count

    def display(self, msg="CircularLinkedQueue: "):
        print(msg, end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end=' ')
                node = node.link
            print(node.data, end=' ')
            print()


class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        

def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)    #recursion은 None일 경우 종료하고 다시 돌아온다
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root):
    queue = CircularLinkedQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    return max(calc_height(n.left), calc_height(n.right)) + 1


g = TNode('G', None, None)
h = TNode('H', None, None)
e = TNode('E', g, h)
f = TNode('F', None, None)
c = TNode('C', e, f)
d = TNode('D', None, None)
b = TNode('B', d, None)
root = TNode('A', b, c)

print('\n    In-Order : ', end='')
inorder(root)
print('\n   Pre-Order : ', end='')
preorder(root)
print('\n  Post-Order : ', end='')
postorder(root)
print('\n Level-Order : ', end='')
levelorder(root)
print()

print(" 노드의 개수 = %d개"% count_node(root))
print(" 단말의 개수 = %d개"% count_leaf(root))
print(" 트리의 높이 = %d"% calc_height(root))

a = TNode('A', None, None)
b = TNode('B', None, None)
div = TNode('/', a, b)
c = TNode('C', None, None)
mul = TNode('*', div, c)
d = TNode('D', None, None)
mul2 = TNode('*', mul, d)
e = TNode('E', None, None)
root = TNode('*', mul2, e)

print('\n    In-Order : ', end='')
inorder(root)
print('\n   Pre-Order : ', end='')
preorder(root)
print('\n  Post-Order : ', end='')
postorder(root)
print('\n Level-Order : ', end='')
levelorder(root)
print()

print(" 노드의 개수 = %d개"% count_node(root))
print(" 단말의 개수 = %d개"% count_leaf(root))
print(" 트리의 높이 = %d"% calc_height(root))

