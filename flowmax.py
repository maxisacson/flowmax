validSymbols = ['start', 'query', 'q', 'action', 'a', 'stop']

def connect(n1, n2):
	n1.connectTo(n2)
	n2.connectTo(n1)

def isConnected(n1,n2):
	if (n1.isConnectedTo(n2) and n2.isConnectedTo(n1)):
		return True
	else:
		return False

class node(object):
	"""basic node for flowchart"""
	nNodes	=	0
	nodes		=	[]
	def __init__(self, text, symbol, x = 0, y = 0):
		self.text = text
		if (symbol in validSymbols):
			if (symbol == 'a'):
				self.symbol = 'action'
			elif (symbol == 'q'):
				self.symbol = 'query'
			else:
				self.symbol = symbol
		else:
			print "*** Symbol '" + symbol + "' is NOT a valid symbol!"
			exit(-1)
		self.x				=	x
		self.y				=	y
		self.height			=	0
		self.width			=	0
		self.connectedTo	=	[]
		self.index			=	node.nNodes
		node.nNodes			+=	1
		node.nodes.append(self)
	
	def isConnectedTo(self, other):
		if (other.index in self.connectedTo):
			return True
		else:
			return False

	def connectTo(self, other):
		if (not self.isConnectedTo(other)):
			self.connectedTo.append(other.index)
		else:
			pass
