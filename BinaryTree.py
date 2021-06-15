
class Node:
    def __init__ (self, data):
        self.left = None
        self.right = None
        self.data = data

    def printTree(self):
        if self is None:
            return
        if self.left != None:
            self.left.printTree()
        print(self.data)
        if self.right != None:
            self.right.printTree()

    def insert(self, data):
        if self is None:
            self = Node(data)
        if self.data > data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def delete(self, parent, data):
        if self.data > data:
            if self.left is None:
                print("Cannot find the node to delete!!!")
            else:
                self.left.delete(self, data)
        elif self.data < data:
            if self.right is None:
                print("Cannot rind the node to delete!!!")
            else:
                self.right.delete(self, data)
        else:
            if self == parent:
                if self.left is None and self.right is None:
                    self = None
                elif self.left is not None:
                    tmpNode = self.left
                    while tmpNode.right is not None:
                        tmpNode = tmpNode.right
                    value = tmpNode.data
                    self.delete(self, tmpNode.data)
                    self.data = value
                else:
                    tmpNode = self.right
                    while tmpNode.left is not None:
                        tmpNode = tmpNode.left
                    value = tmpNode.data
                    self.delete(self, tmpNode.data)
                    self.data = value
            elif self.left is None and self.right is None:
                if self is parent.left:
                    parent.left = None
                elif self is parent.right:
                    parent.right = None
                self = None
            elif self.left is not None:
                if self is parent.left:
                    parent.left = self.left
                else:
                    parent.right = self.left
                self = None
            elif self.right is not None:
                if self is parent.left:
                    parent.left = self.right
                else:
                    parent.right = self.right
                self = None
            else:
                tmpNode = self.left
                while tmpNode.right is not None:
                    tmpNode = tmpNode.right
                self.value = tmpNode.data
                tmpNode = None

        return

root = Node(10)
root.insert(1)
root.insert(2)
root.insert(15)
root.insert(12)
root.printTree()
root.delete(root, 1)
root.delete(root, 3)
root.delete(root, 10)
root.delete(root, 15)
root.delete(root, 12)
root.delete(root, 2)
print("============ after delete")
root.printTree()
