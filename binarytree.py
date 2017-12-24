class BinaryTree():
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def getLeftChild(self):
		return self.left

	def getRightChild(self):
		return self.right

	def getNodeValue(self):
		return self.data

	def setNodeValue(self, value):
		self.data = value

	def insertRightChild(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			tree = BinaryTree(newNode)
			tree.right = self.right
			self.right = tree

	def insertLeftChild(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			tree = BinaryTree(newNode)
			tree.left = self.left
			self.left = tree


def printTree(tree):
	if tree != None:
		printTree(tree.getLeftChild())
		print(tree.getNodeValue())
		printTree(tree.getRightChild())


def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeftChild("Bob")
    myTree.insertRightChild("Tony")
    myTree.insertRightChild("Steven")
    printTree(myTree)

testTree()