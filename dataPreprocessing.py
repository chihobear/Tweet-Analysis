class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def s(root):
    if not root:
        print(0)
        return
    q = [root]
    max_ = 1
    while q:
        temp = []
        
        while q:
            t = q.pop(0)
            if not t:
                temp.append(None)
                temp.append(None)
            else:
                if t.left:
                    temp.append(t.left)
                else:
                    temp.append(None)
                if t.right:
                    temp.append(t.right)
                else:
                    temp.append(None)

               
        index = 0
        index_l = 0
        for i in range(len(temp)):
            if temp[i] != None:
                index = i
        for j in range(len(temp)):
            if temp[i] != None:
                index_l = j
                break
            
        if index == 0:
            break
        if index + 1 - index_l > max_:
            max_ = index + 1 - index_l
        q = temp
    print(max_)
root = Node(5)
root.left = Node(6)
root.right = Node(7)
root.left.left = Node(1)
root.right.left = Node(2)
s(root)
