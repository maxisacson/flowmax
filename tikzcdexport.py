import flowmax

#Takes list of nodes defined in flowmax.node and produces a target .tex file containing tikz code
def makeFig(nodes,target):
	with open("template.tex","r") as file:
		figdata = file.readlines()	
	#print figdata

	#Finds where to insert code
	codei = figdata.index("%Code goes here\n")+1

	#Loop through each node and insert tikz code in .tex file
	for n in nodes:
		#Grabbing info about node
		nodei = n.index
		nodenr = n.label
		nodetext = n.text
		nodeshape = n.symbol
		nodeto = n.flowsToByIndex
		nodedist = n.dist

		#Create nodes. Sets text size in querys to tiny (otherwise the diamond will probably become huge).
		if nodeshape == "start" or nodeshape == "stop":
			figdata.insert(codei+nodei,"\\node[start-stop] at (2*"+str(nodedist)+",-2*"+str(nodei)+") ("+str(nodenr)+") {"+nodetext+"};\n")
		elif nodeshape == "query":
			figdata.insert(codei+nodei,"\\node["+nodeshape+"] at (2*"+str(nodedist)+",-2*"+str(nodei)+") ("+str(nodenr)+") {\\tiny{"+nodetext+"}};\n")
		else:
			figdata.insert(codei+nodei,"\\node["+nodeshape+"] at (2*"+str(nodedist)+",-2*"+str(nodei)+") ("+str(nodenr)+") {"+nodetext+"};\n")

		#Create arrows, checks if there is a flow from a node to itsef
		for flowto in nodeto:
			if nodenr == flowto:
				pass
			else:
				figdata.insert(codei+nodei+1,"\\draw[->] ("+str(nodenr)+") -- ("+str(flowto)+");\n")
			

	#Create/append new target file
	tar = open(target+".tex","a")
	tar.close()

	#Write in the target
	with open(target+".tex","w") as file:
		file.writelines(figdata)