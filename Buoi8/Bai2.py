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
def ducphuc (rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    ducphuc(rootnode.leftchild)
    ducphuc(rootnode.rightchild)
ducphuc(newBT)