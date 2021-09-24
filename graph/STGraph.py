#TODO TED fix: find replacemment library for Scala Graphs. 
#from igraph import *                                #scala: scalax.collection.Graph
#from graphviz import *                              #scala: scalax.collection.io.dot
#> launch /usr/local/Cellar/graph-tool/2.31_1/libexec/bin/python3
#import sys
#sys.path.append('/usr/local/opt/graph-tool/lib/python3.8/site-packages/')
#from graph_tool.all import *

import networkx as nx
from ..timeseries.TimeSeries import TimeSeries
from .STNode import STNode
from .TEdge import TEdge

#  * Specifies a SpatioTemporal graph

class STGraph:
    def __init__(self, stNodes, tEdges, timeSeries):
        self.stgNodes =  set( stNodes )
        self.stgEdges = set( tEdges )
        self.ts = timeSeries
        self.stgNodesMap = {n.uid: n for n in self.stgNodes}
        self.stgEdgesMap = {e.uid: e for e in self.stgEdges}

    
    def clock(self, n=1):
        for i in range (n):
            self.ts.clockEvents()
    
    def getGraph(self):         #Graph[String, WDiEdge]
        nodes = [ stgNode.uid for stgNode in self.stgNodes ]
        edges = [ (stgEdge.src, stgEdge.dst, stgEdge.getWeight().mag) for stgEdge in self.stgEdges ]
        graph = nx.DiGraph()
        graph.add_nodes_from(nodes)
        graph.add_weighted_edges_from(edges)
        return graph


    def removeEdge(self, edgeUID):
        if edgeUID in self.stgEdgesMap:
            edge = self.stgEdgesMap[edgeUID]
            bindings = edge.getWeight().getBindings()
            for event in bindings:
                self.ts.killEvent(event)
            self.stgEdges.remove( self.stgEdgesMap[edgeUID] )
            del self.stgEdgesMap[edgeUID]

    def hasEdge(self, edgeUID):
        return edgeUID in self.stgEdgesMap

    def addEdge(self, edge):
        self.stgEdges.add(edge)
        self.stgEdgesMap[edge.uid] = edge

    def getDot(self):
        nx.drawing.nx_agraph.write_dot(self.getGraph(), str(self.ts.ctr))


    #Do not use this for graphs with high node and edge counts due to performance.
    def __str__(self):
        """
        ret = ""
        for node in self.stgNodes: 
            ret += str(node) + "\n"
        for edge in self.stgEdges:
            ret += str(edge) + "\n"
        return ret
        """
        nodes =  ",".join( map(str,self.stgNodes))
        links =  ",".join( map(str,self.stgEdges))
        return f'{{"nodes": [{nodes}], "links": [{links}]}}'

    def stats(self):
        ret = ""
        nodeBindingCount = 0;
        edgeBindingCount = 0;

        for node in self.stgNodes:
            nodeBindingCount += len(node.getPos().getBindings())
        for edge in self.stgEdges:
            edgeBindingCount += len(edge.getWeight().getBindings())

        ret += "Node bindings: "+nodeBindingCount+"; Edge bindings: "+edgeBindingCount+ "\n"
        ret += self.ts.stats()
        return ret
