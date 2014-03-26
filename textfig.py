import flowmax, tikzcdexport

flowmax.run("test.fm")
nodes = flowmax.container

tikzcdexport.makeFig(nodes,"target")