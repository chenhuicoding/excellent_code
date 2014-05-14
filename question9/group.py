class Node:
    def __init__(self, key="", value="", parent=0):
        self.key = key
        self.value = value
        self.children = []
        self.parent = parent

    def addChild(self, child):
        self.children.append(child)
    
    def __str__(self):
        return self.key + " " + self.value

class Group:
    def __init__(self):
        self.root = Node("root", "")
    
    def add(self, parent, child):
        parent.addChild(child)
    
    def get(self, parent):
        children = parent.children
        return children

    def get_root(self):
        return self.root

if __name__ == '__main__':
    group = Group()
    newNode1 = Node("c1", "c1g")
    newNode11 = Node("c11", "c11g")
    newNode2 = Node("c2", "c2g")
    group.add(group.get_root(), newNode1)
    group.add(group.get_root(), newNode2)
    group.add(newNode1, newNode11)
    children1 = group.get(group.get_root())
    
    for child in children1:
        print child
    
    children2 = group.get(newNode1)
    for child in children2:
        print child
