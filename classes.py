#Node class so that we can store values in the form of a node data structure

class Node:

    def __init__(self,value):
        self.value = value
        self.next_node = None                                       #simple as this, for now it will do.

    def get_value(self):
        return self.value
    
    def set_next_node(self,next_node):
        self.next_node = next_node
    
    def __repr__(self) -> str:
        return "{0}".format(self.value)


class Tree:

    def __init__(self,root_node):
        self.root = root_node
        self.children = []

    def add_child(self,child):                            
        self.children.append(Node(child))                                             #simple as this, for now it will do.

    def remove_child(self,rchild):
        new_child_nodes = []
        for child in self.child:
            if child != rchild:
                new_child_nodes.append(child)
        self.children = new_child_nodes

    def __repr__(self) -> str:
        pass

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self,node):
        self.queue.append(node)

                                                                        #for now it will do. :P
    def dequeue(self):
        item_out = self.queue.pop(0)
        print("removing {0}".format(item_out))
        self.queue = [node for node in self.queue if node != item_out]

    def peek(self):
        return self.queue[0]
        


    
