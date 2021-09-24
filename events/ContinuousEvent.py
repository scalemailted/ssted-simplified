class ContinuousEvent:
    def __init__(self, uid, startingTime, startingValue, model):
        self.uid = uid
        self.startTime = startingTime
        self.startValue = startingValue
        self.model = model

    def getIter(self):
        return self.iterator(self.startValue, self.model)
        
    class iterator:
        def __init__(self, startValue, model):
            self.current = startValue
            self.model = model
        def __next__(self):
            self.model(self.current)
            return self.current

