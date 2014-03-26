import sys

validSymbols = ['start', 'query', 'action', 'stop']

def connectByLabel(n1, n2):
	n1.connectToByLabel(n2)
	n2.connectToByLabel(n1)

def connectByIndex(n1, n2):
	n1.connectToByIndex(n2)
	n2.connectToByIndex(n1)

def connect(n1,n2):
	connectByLabel(n1,n2)
	connectByIndex(n1,n2)

def isConnectedByLabel(n1,n2):
	if (n1.isConnectedToByLabel(n2) and n2.isConnectedToByLabel(n1)):
		return True
	else:
		return False

def isConnectedByIndex(n1,n2):
	if (n1.isConnectedToByIndex(n2) and n2.isConnectedToByIndex(n1)):
		return True
	else:
		return False

def getNodeByLabel(i):
	for n in node.nodes:
		if (n.label == i):
			return n

def getNodeByIndex(i):
	for n in node.nodes:
		if (n.index == i):
			return n

def createNodes(container):
	for c in container:
		node(c[0], c[1], c[2])
	for n in node.nodes:
		if container[n.index][3] is not None:
			for l in container[n.index][3]:
				connect(n, getNodeByLabel(l))

def readFrom(template):
	validIdentifiers = ['node', '{', '}', 'symbol', 'connect', ';']
	container = []
	endOfLine = False
	endOfFile = False
	while True:
		tempString = ''
		if (endOfLine):
			container.append([uIndex, text, symb, cnct])
			endOfLine = False
			uIndex = None
			text = None
			symb = None
			cnct = None
		while True:
			byte = template.read(1)
			if (byte == ''):
				endOfFile = True
				break;
			if (byte.isspace()):
				pass
			else:
				tempString += byte
			if (tempString in validIdentifiers):
				break
		if (endOfFile):
			break
		if (tempString == 'node'):
			tmpIndex = ''
			while True:
				byte = template.read(1)
				if (byte.isspace() and tmpIndex == ''):
					pass
				elif (byte.isspace()):
					break
				else:
					tmpIndex += byte
			uIndex = int(tmpIndex)
		elif (tempString == '{'):
			text = ''
			while True:
				byte = template.read(1)
				if (byte == '}'):
					break
				text += byte
		elif (tempString == 'symbol'):
			symb = ''
			while True:
				byte = template.read(1)
				if (byte.isspace() and symb == ''):
					pass
				elif (byte.isspace()):
					break
				else:
					symb += byte
				if (symb in validSymbols):
					break
			if (symb == 'stop'):
				endOfLine = True
				endOfFile = True
		elif (tempString == 'connect'):
			cnct = []
			tmpCnct = ''
			while True:
				byte = template.read(1)
				if (byte == ';'):
					cnct.append(int(tmpCnct))
					endOfLine = True
					tmpCnct = ''
					break
				elif (byte == ','):
					cnct.append(int(tmpCnct))
					tmpCnct = ''
				elif (byte.isspace()):
					pass
				else:
					tmpCnct += byte	
		elif (tempString == ''):
			break
		elif (tempString == ';'):
			endOfLine = True
	return container

def printNodes():
	for n in node.nodes:
		print "Node " + str(n.label) + " with content '" + n.text + "' of type '" + n.symbol + "' is connected to " + str(n.connectedToByLabel)

def run(_file):
	#try:
		template = open(_file, 'r')
		print 'Running over ' + template.name
		container = readFrom(template)
		createNodes(container)
		printNodes()
	#except IOError as e:
	#	print 'I/O Error({0}): {1}'.format(e.errno, e.strerror)
	#except:
	#	print 'Unexpected error:', sys.exc_info()[0]
	#else:
		template.close()

class node(object):
	"""basic node for flowchart"""
	nNodes	=	0
	nodes		=	[]
	def __init__(self, label, text = '', symbol = 'action', x = 0, y = 0):
		self.label	=	label
		self.text	=	text
		if (symbol in validSymbols):
			self.symbol = symbol
		else:
			print "*** Symbol '" + symbol + "' is NOT a valid symbol!"
			exit(-1)
		self.x						=	x
		self.y						=	y
		self.height					=	0
		self.width					=	0
		self.connectedToByIndex	=	[]
		self.connectedToByLabel	=	[]
		self.index					=	node.nNodes
		node.nNodes					+=	1
		node.nodes.append(self)

	def isConnectedToByLabel(self, other):
		if (other.label in self.connectedToByLabel):
			return True
		else:
			return False

	def isConnectedToByIndex(self, other):
		if (other.index in self.connectedToByIndex):
			return True
		else:
			return False

	def connectToByLabel(self, other):
		if (not self.isConnectedToByLabel(other)):
			self.connectedToByLabel.append(other.label)
		else:
			pass

	def connectToByIndex(self, other):
		if (not self.isConnectedToByIndex(other)):
			self.connectedToByIndex.append(other.index)
		else:
			pass
