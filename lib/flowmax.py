"""FlowMax. A python library to generate latex code for flowcharts.
Copyright (C) 2014  Max Isacson, max.isacson@cern.ch

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""
import sys

validSymbols = ['start', 'query', 'action', 'stop']
layers = []


def connectByLabel(n1, n2):
	n1.connectToByLabel(n2)
	n2.connectToByLabel(n1)


def connectByIndex(n1, n2):
	n1.connectToByIndex(n2)
	n2.connectToByIndex(n1)


def connect(n1, n2):
	connectByLabel(n1, n2)
	connectByIndex(n1, n2)


def isConnectedByLabel(n1, n2):
	if (n1.isConnectedToByLabel(n2) and n2.isConnectedToByLabel(n1)):
		return True
	else:
		return False


def isConnectedByIndex(n1, n2):
	if (n1.isConnectedToByIndex(n2) and n2.isConnectedToByIndex(n1)):
		return True
	else:
		return False


def flowByLabel(n1, n2):
	n1.flowToByLabel(n2)


def flowByIndex(n1, n2):
	n1.flowToByIndex(n2)


def flow(n1, n2):
	flowByLabel(n1, n2)
	flowByIndex(n1, n2)


def isFlowsToByLabel(n1, n2):
	if (n1.isFlowsToByLabel(n2)):
		return True
	else:
		return False


def isFlowsToByIndex(n1, n2):
	if (n1.isFlowsToByIndex(n2)):
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
		node(c[0], c[1], c[2], c[4])
	for n in node.nodes:
		if container[n.index][3] is not None:
			for l in container[n.index][3]:
				connect(n, getNodeByLabel(l))
				flow(n, getNodeByLabel(l))


def initLayers():
	maxDepth = -1
	for n in node.nodes:
		if n.dist > maxDepth:
			maxDepth = n.dist
	for i in range(maxDepth + 1):
		layers.append([])
	for n in node.nodes:
		if not n.symbol == 'stop':
			layers[n.dist].append(n.label)
		elif n.symbol == 'stop':
			layers.append([n.label])


def printLayers():
	for l in layers:
		print(l)


def djikstra():
	unvisited = []
	current = 0
	for n in node.nodes:
		unvisited.append(n.index)
		if n.symbol == 'start':
			n.setDist(0)
			current = n.index
	while True:
		n = getNodeByIndex(current)
		if n.index in unvisited:
			for i in n.flowsToByIndex:
				m = getNodeByIndex(i)
				if n.dist + 1 < m.dist:
					m.setDist(n.dist + 1)
			unvisited.remove(n.index)
		if len(unvisited) == 0:
			break
		for i in unvisited:
			minDist = float('inf')
			n = getNodeByIndex(i)
			if (n.dist < minDist):
					current = n.index
					minDist = n.dist


def readFrom(template):
	validIdentifiers = ['node', '{', '}', 'symbol', 'connect', ';']
	container = []
	endOfLine = False
	endOfFile = False
	uIndex = None
	text = None
	symb = None
	cnct = None
	routeLabels = []
	while True:
		tempString = ''
		if endOfLine:
			container.append([uIndex, text, symb, cnct, routeLabels])
			endOfLine = False
			uIndex = None
			text = None
			symb = None
			cnct = None
			routeLabels = []
		while True:
			byte = template.read(1)
			if byte == '':
				endOfFile = True
				break
			if byte.isspace():
				pass
			else:
				tempString += byte
			if tempString in validIdentifiers:
				break
		if endOfFile:
			break
		if tempString == 'node':
			tmpIndex = ''
			while True:
				byte = template.read(1)
				if byte.isspace() and tmpIndex == '':
					pass
				elif byte.isspace():
					break
				else:
					tmpIndex += byte
			uIndex = int(tmpIndex)
		elif tempString == '{' and symb is None:
			text = ''
			while True:
				byte = template.read(1)
				if byte == '}':
					break
				text += byte
		elif tempString == 'symbol':
			symb = ''
			while True:
				byte = template.read(1)
				if byte.isspace() and symb == '':
					pass
				elif byte.isspace():
					break
				else:
					symb += byte
				if symb in validSymbols:
					break
			if symb == 'stop':
				endOfLine = True
				endOfFile = True
		elif tempString == '{' and symb == 'query':
			tempRouteLabel = ''
			while True:
				byte = template.read(1)
				if byte == '}':
					routeLabels.append(tempRouteLabel)
					break
				tempRouteLabel += byte
		elif tempString == 'connect':
			cnct = []
			tmpCnct = ''
			while True:
				byte = template.read(1)
				if byte == ';':
					cnct.append(int(tmpCnct))
					endOfLine = True
					tmpCnct = ''
					break
				elif byte == ',':
					cnct.append(int(tmpCnct))
					tmpCnct = ''
				elif byte.isspace():
					pass
				else:
					tmpCnct += byte
		elif tempString == '':
			break
		elif tempString == ';':
			endOfLine = True
	return container


def printNodes():
	for n in node.nodes:
		print("Node " + str(n.label) + " with content '" + n.text +
				"' of type '" + n.symbol + "' is connected to node(s) " +
				str(n.connectedToByLabel) + " and flows to node(s) " +
				str(n.flowsToByLabel) + " (" + str(n.routeLabels) + ") with distance " +
				str(n.dist) + " from start.")


def run(_file):
	template = open(_file, 'r')
	print('Running over ' + template.name)
	container = readFrom(template)
	createNodes(container)
	djikstra()
	initLayers()
	printNodes()
	print("\nLayers")
	printLayers()
	template.close()


class node(object):
	"""basic node for flowchart"""
	nNodes = 0
	nodes = []

	def __init__(self, label, text='', symbol='action', routeLabels=[], x=0, y=0):
		super(node, self).__init__()
		self.label = label
		self.text = text
		if (symbol in validSymbols):
			self.symbol = symbol
		else:
			print("*** Symbol '" + symbol + "' is NOT a valid symbol!")
			sys.exit()
		self.x = x
		self.y = y
		self.height = 0
		self.width = 0
		self.connectedToByIndex = []
		self.connectedToByLabel = []
		self.flowsToByIndex = []
		self.flowsToByLabel = []
		self.index = node.nNodes
		self.dist = float('inf')
		self.routeLabels = routeLabels
		node.nNodes += 1
		node.nodes.append(self)

	def isConnectedToByLabel(self, other):
		if other.label in self.connectedToByLabel:
			return True
		else:
			return False

	def isConnectedToByIndex(self, other):
		if other.index in self.connectedToByIndex:
			return True
		else:
			return False

	def isFlowsToByIndex(self, other):
		if other.index in self.flowsToByIndex:
			return True
		else:
			return False

	def isFlowsToByLabel(self, other):
		if other.label in self.flowsToByLabel:
			return True
		else:
			return False

	def flowToByLabel(self, other):
		if not self.isFlowsToByLabel(other):
			self.flowsToByLabel.append(other.label)

	def flowToByIndex(self, other):
		if not self.isFlowsToByIndex(other):
			self.flowsToByIndex.append(other.index)

	def connectToByLabel(self, other):
		if not self.isConnectedToByLabel(other):
			self.connectedToByLabel.append(other.label)

	def connectToByIndex(self, other):
		if not self.isConnectedToByIndex(other):
			self.connectedToByIndex.append(other.index)

	def getDist(self):
		return self.dist

	def setDist(self, d):
		self.dist = d
