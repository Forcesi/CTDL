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
def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild)
inorder(newBT)
