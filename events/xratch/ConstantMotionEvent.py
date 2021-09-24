from ..timeseries.ContinuousEntityEvent import ContinuousEntityEvent
from ..ent.Point import Point

class ConstantMotionEvent:
    class Linear(ContinuousEntityEvent):
        def __init__(self, uid, startingTime, startingValue, velocity):
            super().__init__(uid, startingTime, startingValue, lambda x: x+velocity)
            startingValue.bindEvent(uid)

