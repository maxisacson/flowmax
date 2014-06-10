import flowmax
import os
xsize = 4
ysize = 2


def findHeight(lay, ind):
	# First check whether ind lies in the list or not
	try:
		return lay.index(ind)
	except ValueError:
		pass

	for i in range(0, len(lay)):
		try:
			lay[i].index(ind)
		except ValueError:
			pass
		else:
			return [i, lay[i].index(ind)]


def getxy(nodes):
	x = []
	y = []
	# Loop through each node
	for n in nodes:
		# Grab some info about each node
		nodei = n.index
		nodepos = findHeight(flowmax.layers, nodei)
		x.append(xsize*nodepos[1])
		y.append(-ysize*nodepos[0])
	return [x, y]


def layerSize(layers):
	sizes = []
	for l in layers:
		sizes.append(len(l))
	return sizes


# Takes list of nodes defined in flowmax.node and produces
# a target .tex filecontaining tikz code
def makeFig(nodes, target):
	__dir__ = os.path.dirname(os.path.abspath(__file__))
	__dir__ = __dir__[:-4]
	filepath = os.path.join(__dir__, "template/template.tex")
	with open(filepath, "r") as file:
		figdata = file.readlines()

	#Finds where to insert nodes and arrows (arrows must succeed the nodes)
	nodecodei = figdata.index("%Nodes goes here\n")+1
	arri = figdata.index("%Arrows goes here\n")+1

	xy = getxy(nodes)
	#Loop through each node
	for n in nodes:

		#Grab info about each node
		nodetot = len(nodes)
		nodei = n.index
		nodelbl = n.label
		nodetext = n.text
		nodeshape = n.symbol
		nodeto = n.flowsToByLabel
		nodearrowlabel = n.routeLabels
		# Create nodes
		figdata.insert(nodecodei + nodei,
						"\\node[" + nodeshape + "] at (" + str(xy[0][nodelbl]) +
						"," + str(xy[1][nodelbl]) + ") (" + str(nodelbl) +
						") {" + nodetext + "};\n")
		arlabelstrings = ['']*nodetot

		if len(nodearrowlabel) > 0:
			for i in range(0, len(nodearrowlabel)):
				arlabelstrings.insert(nodeto[i], nodearrowlabel[i])

		# Create arrows
		for flw in nodeto:
			diffx = xy[0][nodelbl]-xy[0][flw]
			diffy = xy[1][nodelbl]-xy[1][flw]
			#Sets a value of the fill, and determine which arrows have labels
			if arlabelstrings[flw] != '':
				fillstring = "fill=white,"
			else:
				fillstring = ""

			if nodelbl != flw:
				if (abs(diffy) == ysize or abs(diffx) == xsize):
					figdata.insert(arri + nodei + 1,
									"\\draw[->] (" + str(nodelbl) +
									") -- (" + str(flw) +
									") node [midway," + fillstring +
									",tiny] {" + arlabelstrings[flw] +
									"} ;\n")
				elif diffy != 0:
					if diffx == 0:
						figdata.insert(arri + nodei + 1,
										"\\draw[->,rounded corners] (" + str(nodelbl) +
										") -- (" + str(xy[0][nodelbl]) +
										"-" + str(ysize) + "," + str(xy[1][nodelbl]) +
										") -- (" + str(xy[0][nodelbl]) +
										"-" + str(ysize) + "," + str(xy[1][nodelbl]) +
										"-" + str(diffy) + ") node [midway," + fillstring +
										",tiny] {" + arlabelstrings[flw] +
										"} -- (" + str(flw) + ");\n")
					elif diffx > 0:
						figdata.insert(arri + nodei + 1,
										"\\draw[->,rounded corners] (" + str(nodelbl) +
										") -- (" + str(xy[0][nodelbl]) +
										"," + str(xy[1][nodelbl]) +
										"-" + str(diffy) + ") node [midway," + fillstring +
										",tiny] {" + arlabelstrings[flw] +
										"} -- (" + str(flw) + ");\n")
					else:
						figdata.insert(arri + nodei + 1,
										"\\draw[->,rounded corners] (" + str(nodelbl) +
											") -- (" + str(xy[0][nodelbl]) +
											"," + str(xy[1][nodelbl]) +
											"-" + str(diffy) + ") node [midway," + fillstring +
											",tiny] {" + arlabelstrings[flw] +
											"} -- (" + str(flw) + ");\n")
	#Create/append new target file
	tar = open(target + ".tex", "a")
	tar.close()

	#Write in the target
	with open(target + ".tex", "w") as file:
		file.writelines(figdata)
		print(target + ".tex written!")
	try:
		os.system("xelatex -interaction=nonstopmode " + target + ".tex")
		os.system("rm *.log *.aux *.tex")
	except Exception:
		os.system("pdflatex -interaction=nonstopmode " + target + ".tex")
		os.system("rm *.log *.aux *.tex")


