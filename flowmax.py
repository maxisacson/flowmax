


class node(object):
	"""basic node for flowchart"""
	nNodes = 0
	nodes = []
	width = 0
	height = 0
	connectedTo = [];
	def __init__(self, text, x = 0, y = 0):
		self.text = text
		self.x = x
		self.y = y
		self.index = node.nNodes
		node.nNodes+=1
		node.nodes.append(self)

	def getIndex(self):
		return self.index
	
	def connectTo(self, other):
		self.connectedTo.append(other.getIndex())
