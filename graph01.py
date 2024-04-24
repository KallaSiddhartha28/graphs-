def distance(e):
    return e[2]
graph=[(1,2,5),(2,3,4),(3,4,10),(4,5,6),(3,5,8)]
vertexset=set()
td=0
for edge in graph:
    print(edge)
    vertexset.add(edge[0])
    vertexset.add(edge[1])
    td=td+edge[2]
print("total distance of graph is",td)
print("no of vertices=",len(vertexset))
print("no of edge=",len(graph))
graph.sort(key=distance)
print("sorted graph based on distaNCE",graph)
print(graph)
