import flowmax, tikzexport

flowmax.run("test.fm")
nodes = flowmax.node.nodes

tikzexport.makeFig(nodes,"target")