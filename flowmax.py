import sys

validSymbols = ['start', 'query', 'action', 'stop']

def connect(n1, n2):
	n1.connectTo(n2)
	n2.connectTo(n1)

def isConnected(n1,n2):
	if (n1.isConnectedTo(n2) and n2.isConnectedTo(n1)):
		return True
	else:
		return False

def getNodeByIndex(i):
	for n in node.nodes:
		if (n.index == i):
			return n

def readFrom(template):
	validIdentifiers = ['node', '{', '}', 'symbol', 'connect']
	container = []
	ind = 0
	buf = 4
	endOfLine = False
	endOfFile = False
	iter1 = 0
	while True:
		iter1+=1
		print "iter1 = " + str(iter1)
		tempString = ''
		if (endOfLine):
			container.append([uIndex, text, symb, cnct])
			endOfLine = False
		while True:
			byte = template.read(1)
	#		print template.tell()
			if (byte == ''):
				endOfFile = True
				break;
			if (byte.isspace()):
				pass
			else:
				tempString += byte
			if (tempString in validIdentifiers):
				print tempString
				break
		if (endOfFile):
			break
		#print tempString
		if (tempString == 'node'):
		#	print tempString
			tmpIndex = ''
			while True:
				byte = template.read(1)
			#	print template.tell()
				if (byte.isspace() and tmpIndex == ''):
					pass
				elif (byte.isspace()):
					break
				else:
					tmpIndex += byte
			uIndex = int(tmpIndex)
		elif (tempString == '{'):
			#print tempString
			text = ''
			while True:
				byte = template.read(1)
			#	print template.tell()
				if (byte == '}'):
					#print byte
					break
				text += byte
		elif (tempString == 'symbol'):
			#print tempString
			symb = ''
			while True:
				byte = template.read(1)
			#	print template.tell()
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
			#print tempString
			cnct = []
			tmpCnct = ''
			while True:
				byte = template.read(1)
			#	print template.tell()
				if (byte == ';'):
					cnct.append(int(tmpCnct))
					endOfLine = True
					tmpCnct = ''
					#print endOfLine
					break
				elif (byte == ','):
					cnct.append(int(tmpCnct))
					tmpCnct = ''
				elif (byte.isspace()):
					pass
				else:
					tmpCnct += byte	
	#		print cnct
	#		elif (endOfLine):
	#		print uIndex
	#		container.append([uIndex, text, symb, cnct])
	#		print container
			#tempString = ''
		elif (tempString == ''):
			break
	for x in container:
		print x

def run(_file):
	#try:
		template = open(_file, 'r')
		print 'Running over ' + template.name
		readFrom(template)
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
	def __init__(self, text = '', symbol = 'action', x = 0, y = 0):
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
