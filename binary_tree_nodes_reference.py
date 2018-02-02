class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.left_child = None
		self.right_child = None

	def insertLeft(self, new_node):
		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.left_child = self.left_child
			self.left_child = t

	def insertRight(self, new_node):
		if self.right_child == None:
			self.right_child = BinaryTree(new_node)
		else:
			t = BinaryTree(new_node)
			t.right_child = self.right_child
			self.right_child = t


	def getRightChild(self):
		return self.right_child

	def getLeftChild(self):
		return self.left_child

	def setRootVal(self, obj):
		self.key = obj

	def getRootVal(self):
		return self.key

# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())