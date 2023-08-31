from classes import *

nodeA = Node("A")


treeTest1 = Tree("A")


treeTest1.add_child("B1")
treeTest1.add_child("B2")
treeTest1.add_child("B3")
treeTest1.add_child("B4")

treeTest1.children.add_child("C1")

print(treeTest1.children)

treeTest1.children