from binary_tree_nodes_reference import BinaryTree
from stack import Stack

def buildParseTree(fpexp):
	fplist = fpexp.split()
	pStack = Stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree
	for i in fpexp:
		if i == '(':
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif i not in ['+','-','*','/',')']:
			currentTree.setRootVal(int(i))
			parent = pStack.pop()
			currentTree = parent
	return currentTree



pt = buildParseTree('((10+5)*3)')

print(pt)
