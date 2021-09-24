from ..events.ContinuousEvent import ContinuousEvent
import random


class GaussianEdgeEvent:
    
    def ex(mean, stddev): 
        return lambda e: e+abs( random.normalvariate(0,1) *stddev+mean)
    
    class GaussianContinuous(ContinuousEvent):
        def __init__(self, uid, startingTime, variable, mean= 0.0, stddev=1.0):
            super().__init__(uid, startingTime, variable, GaussianEdgeEvent.ex(mean,stddev) )
            variable.bindEvent(uid)

