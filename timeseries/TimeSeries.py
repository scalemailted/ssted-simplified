from ..timeseries.EventPool import EventPool
from ..timeseries.EventProcessPool import EventProcessPool


class TimeSeries:
    def __init__(self):
        self.nodeMovementEventIndex = EventPool()         
        self.nodeMovementIterPool = EventProcessPool()   
        self.globalEventIndex = EventPool()              
        self.globalIterPool = EventProcessPool()         
        self.maintenanceIndex = EventPool()              
        self.maintenanceIterPool = EventProcessPool()  
        self.edgeWeightEventIndex = EventPool()         
        self.edgeWeightIterPool = EventProcessPool()   
        self.uIDMap = {}
        self.ctr = 0
        self.nextUID = 0

    def generateNextUID(self): 
        self.nextUID += 1
        return self.nextUID

    def killEvent(self, uid):
        #Has the event started?
        if (self.uIDMap[uid].startTime < self.ctr):      #Kill the event iterator
            self.nodeMovementIterPool.kill(uid)
            self.globalIterPool.kill(uid)
            self.maintenanceIterPool.kill(uid)
            self.edgeWeightIterPool.kill(uid)
        else:                                       #Kill the event in the index
            self.nodeMovementEventIndex.kill(uid)
            self.globalEventIndex.kill(uid)
            self.maintenanceIndex.kill(uid)
            self.edgeWeightEventIndex.kill(uid)
            
        del self.uIDMap[uid]


    def clock(self, events, processes):
        eventSet = events.get(self.ctr)
        if eventSet:
            for e in eventSet:
                processes.add(e)
        processes.go()

    #renamed from clock to clockEvents, as no overloading
    def clockEvents(self):
        print("Beginning Clocking")
        print("Node Movement")
        self.clock(self.nodeMovementEventIndex, self.nodeMovementIterPool)
        print("Global Event")
        self.clock(self.globalEventIndex, self.globalIterPool)
        print("Maintenance Event")
        self.clock(self.maintenanceIndex, self.maintenanceIterPool)
        print("Edge-weight Event")
        self.clock(self.edgeWeightEventIndex, self.edgeWeightIterPool)
        print("Done with clocking")
        self.ctr += 1

    def addNodeMovementEvent(self, event):
        self.nodeMovementEventIndex.add(event)
        self.uIDMap[event.uid] = event

    def addMaintenance(self,event):
        self.maintenanceIndex.add(event)
        self.uIDMap[event.uid] = event

    def addEdgeWeightEvent(self, event):
        self.edgeWeightEventIndex.add(event)
        self.uIDMap[event.uid] = event

    def addGlobalEvent(self, event):
        self.globalEventIndex.add(event)
        self.uIDMap[event.uid] = event

    def __str__(self):
        ret = ""
        ret += "MOVPL: "+ str( len(self.nodeMovementEventIndex.pool)) + ";" + str(len(self.nodeMovementIterPool.pool)) + "\n"
        ret += "GLOPL: "+ str( len(self.globalEventIndex.pool)) + ";" + str(len(self.globalIterPool.pool)) + "\n"
        ret += "MNTPL: "+ str( len(self.maintenanceIndex.pool)) + ";" + str(len(self.maintenanceIterPool.pool)) + "\n"
        ret += "EDGPL: "+ str( len(self.edgeWeightEventIndex.pool)) + ";" + str(len(self.edgeWeightIterPool.pool)) + "\n"
        ret += "UIDCT: "+ str( len(self.uIDMap)) + "\n"
        return ret

    def stats(self):
        ret = ""
        ret += "Node Movement\n"
        ret += self.nodeMovementEventIndex.stats()
        ret += self.nodeMovementIterPool.stats()
        ret += "Global\n"
        ret += self.globalEventIndex.stats()
        ret += self.globalIterPool.stats()
        ret += "Maintenance\n"
        ret += self.maintenanceIndex.stats()
        ret += self.maintenanceIterPool.stats()
        ret += "Edge\n"
        ret += self.edgeWeightEventIndex.stats()
        ret += self.edgeWeightIterPool.stats()
        return ret

