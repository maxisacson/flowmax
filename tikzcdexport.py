import flowmax

#Takes list of nodes defined in flowmax.node and produces a target .tex file containing tikz code
def makeFig(nodes,target):
	with open("template.tex","r") as file:
		figdata = file.readlines()	
	#print figdata

	#Finds where to insert code
	kodindex = figdata.index("%Code goes here\n")+1

	#Loop through each node and insert tikz code in .tex file
	for i in xrange(0,len(nodes)):
		nodenr = nodes[i][0]
		nodetext = nodes[i][1]
		nodeshape = nodes[i][2]
		nodeto = nodes[i][3]

		#Create nodes
		if nodeshape == "start" or nodeshape == "stop":
			figdata.insert(kodindex+i,"\\node[start-stop] at (0,-2*"+str(i)+") ("+str(nodenr)+") {"+nodetext+"};\n")
		elif nodeshape == "query":
			figdata.insert(kodindex+i,"\\node[query=1.6] at (0,-2*"+str(i)+") ("+str(nodenr)+") {"+nodetext+"};\n")
		else:
			figdata.insert(kodindex+i,"\\node["+nodeshape+"] at (0,-2*"+str(i)+") ("+str(nodenr)+") {"+nodetext+"};\n")
		#Create arrows
		if nodeto == None:
			pass
		else:
			figdata.insert(kodindex+i+1,"\\draw[->] ("+str(nodenr)+") -- ("+str(nodeto[0])+");\n")

	#Create/append new target file
	tar = open(target+".tex","a")
	tar.close()

	#Write in the target
	with open(target+".tex","w") as file:
		file.writelines(figdata)

