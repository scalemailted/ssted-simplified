from ..events.ContinuousEvent import ContinuousEvent
import math


class DistanceWeightMaintenanceEvent:
    def ex(src, dst):
        return lambda e: (e := math.dist(src,dst))

    class Continuous(ContinuousEvent):
        def __init__(self, uid, startingTime, variable, src, dst):
            super().__init__(uid, startingTime, variable, DistanceWeightMaintenanceEvent.ex(src,dst) )
            variable.bindEvent(uid)

