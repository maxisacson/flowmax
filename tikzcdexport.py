import flowmax

#Takes list of nodes defined in flowmax.node and produces a target .tex file containing tikz code
def makeFig(nodes,target):
	with open("template.tex","r") as file:
		figdata = file.readlines()	
	#print figdata

	#Finds where to insert code
	kodindex = figdata.index("%Code goes here\n")+1

	#Loop through each node and insert tikz code in .tex file
	for n in nodes:
		#Grabbing info about node
		i = n.index
		nodenr = n.label
		nodetext = n.text
		nodeshape = n.symbol
		nodeto = n.connectedToByIndex

		#Just for proof of concept
		displacement = str(len(nodeto)-1)

		#Create nodes
		if nodeshape == "start" or nodeshape == "stop":
			figdata.insert(kodindex+i,"\\node[start-stop] at (2*"+displacement+",-2*"+str(i)+") ("+str(nodenr)+") {"+nodetext+"};\n")
		else:
			figdata.insert(kodindex+i,"\\node["+nodeshape+"] at (2*"+displacement+",-2*"+str(i)+") ("+str(nodenr)+") {"+nodetext+"};\n")	

		#Create arrows
		if nodeto == None:
			pass
		else:
			for c in nodeto:
				figdata.insert(kodindex+i+1,"\\draw[->] ("+str(nodenr)+") -- ("+str(c)+");\n")	
			

	#Create/append new target file
	tar = open(target+".tex","a")
	tar.close()

	#Write in the target
	with open(target+".tex","w") as file:
		file.writelines(figdata)
		