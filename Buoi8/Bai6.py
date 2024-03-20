class treenode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
newBT = treenode("drink")
leftchild = treenode("hot")
rightchild = treenode("cold")
newBT.leftchild = leftchild
newBT.rightchild = rightchild
def levelorder (rootnode):
    if not rootnode:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootnode)
        while not (customqueue.isempty()):
            root = customqueue.dequeue()
            print(root.value.data)
            if (root.value.leftchild is not None):
                customqueue.enqueue( root.value.leftchild)
            if (root.value.rightchild is not None):
                customqueue.enqueue ( root.value.rightchild)
levelorder(newBT)
