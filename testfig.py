import flowmax, tikzcdexport

flowmax.run("test.fm")
nodes = flowmax.node.nodes

tikzcdexport.makeFig(nodes,"target")