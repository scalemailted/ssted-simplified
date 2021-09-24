class SingleEvent:
    def __init__(self, uid, time, value, model):
        self.uid = uid
        self.time = time
        self.value = value
        self.model = model
    
    def getIter(self):
        return self.iterator(1, self.value, self.model)

    class iterator:
        def __init__(self, count, value, model):
            self.count = count
            self.current = value
            self.model = model
        def __next__(self):
            if self.count > 0:
                self.count -= 1
                return self.model(self.current)
            else:
                return None
