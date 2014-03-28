import flowmax

def findHeight(lay,ind):
	#First check whether ind lies in the list or not
	try:
		return lay.index(ind)
	except ValueError:
		pass

	for i in xrange(0,len(lay)):
		try:
			lay[i].index(ind)
		except ValueError:
			pass
		else:
			return [i,lay[i].index(ind)]


def getxy(nodes):
	x = []
	y = []
	#Loop through each node
	for n in nodes:
		#Grab some info about each node
		nodelbl = n.label
		nodepos = findHeight(flowmax.layers,nodelbl)
		x.append(3*nodepos[1])
		y.append(-2*nodepos[0])

	return [x,y]

#Takes list of nodes defined in flowmax.node and produces a target .tex file containing tikz code
def makeFig(nodes,target):
	with open("template.tex","r") as file:
		figdata = file.readlines()	
	#print figdata

	#Finds where to insert code
	codei = figdata.index("%Code goes here\n")+1
	#Loop through each node
	for n in nodes:
		#Grab info about each node
		nodei = n.index
		nodelbl = n.label
		nodetext = n.text
		nodeshape = n.symbol
		nodeto = n.flowsToByLabel
		xy = getxy(nodes)

		#Create nodes
		figdata.insert(codei+nodei,"\\node["+nodeshape+"] at ("+str(xy[0][nodelbl])+","+str(xy[1][nodelbl])+") ("+str(nodelbl)+") {"+nodetext+"};\n")


		#Create arrows
		for flw in nodeto:
			diffx = xy[0][nodelbl]-xy[0][flw]
			diffy = xy[1][nodelbl]-xy[1][flw]
			if nodelbl != flw:
				if (abs(diffy) == 2 or abs(diffx) == 3):
					figdata.insert(codei+nodelbl+1,"\\draw[->] ("+str(nodelbl)+") -- ("+str(flw)+");\n")
				elif diffy != 0:
					if diffx == 0:
						figdata.insert(codei+nodelbl+1,"\\draw[->,rounded corners] ("+str(nodelbl)+") -- ("+str(xy[0][nodelbl])+"-2,"+str(xy[1][nodelbl])+") -- ("+str(xy[0][nodelbl])+"-2,"+str(xy[1][nodelbl])+"-"+str(diffy)+") -- ("+str(flw)+");\n")
					elif diffx > 0:
						figdata.insert(codei+nodelbl+1,"\\draw[->,rounded corners] ("+str(nodelbl)+") -- ("+str(xy[0][nodelbl])+","+str(xy[1][nodelbl])+"-"+str(diffy)+") -- ("+str(flw)+");\n")
					else:
						figdata.insert(codei+nodelbl+1,"\\draw[->,rounded corners] ("+str(nodelbl)+") -- ("+str(xy[0][nodelbl])+","+str(xy[1][nodelbl])+"-"+str(diffy)+") -- ("+str(flw)+");\n")


	#Create/append new target file
	tar = open(target+".tex","a")
	tar.close()

	#Write in the target
	with open(target+".tex","w") as file:
		file.writelines(figdata)