from ..events.ContinuousEvent import ContinuousEvent
import random


class GaussianEvent:

    def ex(mean, stddev):
        return lambda x: x + (random.normalvariate(0,1) * stddev + mean)

    class Continuous(ContinuousEvent):
        def __init__(self, uid, startingTime, startingValue, mean=0.0, stddev=1.0):
            super().__init__(uid, startingTime, startingValue, GaussianEvent.ex(mean, stddev) )
            startingValue.bindEvent(uid)
  


