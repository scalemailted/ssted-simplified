from ..ent.Weight import Weight
from ..graph.STGraph import STGraph
from ..graph.TEdge import TEdge
from ..index.kdtree import KDTree  #import *
from ..events.ContinuousEvent import ContinuousEvent
from .DistanceWeightMaintenanceEvent import DistanceWeightMaintenanceEvent
from .GaussianEvent import GaussianEvent

from random import random
import math


class GlobalEdgeConnectivityEvent:

    class ContinuousGlobalRadio (ContinuousEvent):
        def __init__(self, uid, startingTime, graph, r, muW, sigmaW):
            super().__init__(uid, startingTime, graph, lambda g:GlobalEdgeConnectivityEvent.updateEdges(r, muW, sigmaW, g))


    def getRandomInRange(min, max): 
        return random() * (max-min) + min

    def updateEdges(r, muW, sigmaW, g): 
        sgraph = g.getGraph()
        bbNodesTree = KDTree.build(0, g.stgNodes)

        nearbyNodesMap = {}
        for n in g.stgNodes:
            min = list( map(lambda x:x-r, n.getPos().mags ))
            max = list( map(lambda x:x+r, n.getPos().mags ))
            nearbyNodesMap[n] = bbNodesTree.rangeQuery(min,max)

        for src in g.stgNodes:
            bbNodes = set(nearbyNodesMap[src])

            #Find edges that are not in the neighborhood and remove them.
            for currentNeighborUID in sgraph.successors(src.uid):
                currentNeighborEdgeUID = src.uid + ":" + currentNeighborUID
                if not g.stgNodesMap[currentNeighborUID] in list(bbNodes) and g.hasEdge(currentNeighborEdgeUID):
                    g.removeEdge(currentNeighborEdgeUID) #//Side Effect

            #For all neighborhood nodes
            for dst in bbNodes.difference({src}):
                if isinstance(dst, tuple):
                    continue
                distance = math.dist(src.getPos().mags, dst.getPos().mags)
                edgeUID = str(src.uid)+":"+str(dst.uid)

                if distance > r and g.hasEdge(edgeUID):         #//The dest node is out of range.  Remove it.
                    g.removeEdge(edgeUID)                       #//Side effect
                elif distance <= r and not g.hasEdge(edgeUID):  #//A new node is in range.  Add an edge.
                    w = Weight(distance)
                    e = TEdge(edgeUID, src.uid, dst.uid, w)
                    #//Notice the g.ts.ctr.  It is OK to insert these events at the current time because global events
                    #// get processed before maintenance and weight events (but after move events).
                    m = DistanceWeightMaintenanceEvent.Continuous(g.ts.generateNextUID(), g.ts.ctr, w, src.getPos(), dst.getPos())
                    ev = GaussianEvent.Continuous(g.ts.generateNextUID(), g.ts.ctr, w, GlobalEdgeConnectivityEvent.getRandomInRange(muW[0], muW[1]), GlobalEdgeConnectivityEvent.getRandomInRange(sigmaW[0], sigmaW[1]))

                    g.addEdge(e)                    #//Side effects
                    g.ts.addMaintenance(m)          #//Side effects
                    g.ts.addEdgeWeightEvent(ev)     #//Side effects

        return g

