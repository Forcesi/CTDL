class treenode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addchild(self, treenode):
        self.children.append(treenode)
tree = treenode("drink",[])
cold = treenode("cold",[])
hot = treenode("hot",[])
tree.addchild(cold)
tree.addchild(hot)
tea =treenode("tea",[])
coffee = treenode("coffee",[])
cola = treenode("cola",[])
fanta = treenode("fanta",[])
cola.addchild(cola)
cola.addchild(fanta)
hot.addchild(tea)
hot.addchild(coffee)
print(tree)
