class treenode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
newBT = treenode("drink")
leftchild = treenode("hot")
tea = treenode("tea")
coffee = treenode("coffee")
leftchild.leftchild = tea
leftchild.rightchild = coffee
rightchild = treenode("cold")
newBT.leftchild = leftchild
newBT.rightchild = rightchild
def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.leftchild)
    postorder(rootnode.rightchild)
    print(rootnode.data)
postorder(newBT)