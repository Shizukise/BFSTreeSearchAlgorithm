# making a tree data sctructure with a list of lists

#we will make a function that creates a root node(list) with 2 subsequent child nodes. we could add a parameter to get the input of how many child
#nodes will be made

def BinaryTree(r, number_of_child):                    #this will take the node or value that will be the root of the list, and a number for
    child = [[] for _ in range(number_of_child)]        #how many childs we want to make in this node. we use a list ccomprehension to make the lists
    return [r] + child                                 #and then we return a list with root and concatenate x other lists to it, each of this lists
                                                        #will have a node or value also, and subsequently can have more childs(lists) each one of it


#this is the base concept of creating a tree data structure using lists of lists.

#now we will make a method to add another node at the current child of our list, we will be making the root node to only have 2 childs
#for simplicity of learning

def insertLeft(root,newBranch):    #we take what root we will be adding a child on and the name of the new branch(node)
    t = root.pop(1)               #because our tree is a list of lists, the first index (0) is the root node, so we will take the next one, wich
                                 #if we were to visualize this, it would be on the left, so we take this value with pop(1)
    if len(t) > 1:                      #we check if the node has a value already, and if it does we will replace it and the older value will be    
                                        #a child of the new one, on the left side
        root.insert(1,[newBranch,t,[]])  #we make this by inserting a new list at index 1 and passing the old value to the index (1) of the new list,
                                        #that again, visually would be on the left side

    else:                               #else we simply add the value with no need to replace and change positions of anything else
        root.insert(1,[newBranch, [], []])
    return root                            #and we return the new root list.

treetest1 = BinaryTree("Root",2)

insertLeft(treetest1,"child")
insertLeft(treetest1,"child2")

print(treetest1)

#and we can make one to insert at right side, wich will be index 2,

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

#some straightforward aid methods for this
def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]