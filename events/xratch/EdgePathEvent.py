
from ..timeseries.PathEntityEvent import PathEntityEvent
from ..ent.Weight import Weight

class EdgePathEvent:
    class Additive(PathEntityEvent):
        def __init__(self, uid, startingTime, variable, path):
            super().__init__(uid, startingTime, variable, path, lambda ew,seq: ew +seq )
            variable.bindEvent(uid)

    class Absolute(PathEntityEvent):
        def __init__(self, uid, startingTime, variable, path):
            super().__init__(uid,startingTime,variable,path, lambda ex,seq: (ew:=seq))
            variable.bindEvent(uid)


