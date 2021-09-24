from ..graph.STNode import STNode 
from ..graph.STGraph import STGraph
from ..ent.Point import Point
from ..events.GaussianMotionEvent import GaussianMotionEvent
from ..events.GlobalEdgeConnectivityEvent import GlobalEdgeConnectivityEvent
from ..timeseries.TimeSeries import TimeSeries

"""
Specifies a Stochastic SpatioTemporal Graph with the given parameters
"""
class SSTGraph:
    def __init__(self, nodeIds, positions, nodeMeans, nodeStdDevs, r, muW, sigmaW):
        self.nodeIds = list(set(nodeIds))
        self.positions = positions
        self.nodeMeans = nodeMeans
        self.nodeStdDevs = nodeStdDevs
        self.r = r
        self.muW = muW
        self.sigmaW = sigmaW

    def getSTGraph(self):
        ts = TimeSeries()
        nodeList = []
        for i in range(0, len(self.nodeIds)):
            pos = Point( *self.positions[i] ) 
            uid = ts.generateNextUID()
            motion = GaussianMotionEvent.Continuous(uid, 0, pos, self.nodeMeans[i], self.nodeStdDevs[i])
            node = STNode(self.nodeIds[i], pos)
            nodeList.append(node)
            ts.addNodeMovementEvent(motion)

        g = STGraph( nodeList, [], ts)
        uid = ts.generateNextUID()
        globalEdgeEvent = GlobalEdgeConnectivityEvent.ContinuousGlobalRadio(uid, 0, g, self.r, self.muW, self.sigmaW)
        ts.addGlobalEvent( globalEdgeEvent )
        return g


