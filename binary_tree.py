def binaryTree(r):
	return [r, [], []]

def insertLeft(root, new_branch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1, [new_branch, t, []])
	else:
		root.insert(1,[new_branch, [], []])
	return root


def insertRight(root, new_branch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2, [new_branch, [], t])
	else:
		root.insert(2, [new_branch, [], []])
	return root

def  getRootVal(root):
	return root[0]

def setRootVal(root, new_val):
	root[0] = new_val

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

r = binaryTree('a')
insertLeft(r, 'b')
insertLeft(getLeftChild(r), 'd')
insertRight(r, 'c')
insertLeft(getRightChild(r), 'e')
insertRight(getRightChild(r), 'f')

print(r)
