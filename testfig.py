import flowmax, tikzexport

flowmax.run("test3.fm")
nodes = flowmax.node.nodes

tikzexport.makeFig(nodes,"target")