from ..ent.Weight import Weight

#Specifies a temporal edge where source and destination are immutable.
class TEdge:
    def __init__(self, uniqueId, source, destination, initialWeight=None):
        self.uid = uniqueId
        self.src = source
        self.dst = destination
        self.weight = initialWeight

    def getWeight(self):
        return self.weight

    def __eq__(self, other):
        if isinstance(other,TEdge) and self.uid == other.uid:
            return True
        return False

    def __hash__(self):
        return hash(self.uid);

    def __str__(self): 
        #return f"{self.uid};({self.src},{self.dst});[{self.weight}];"
        #return f'{{"source": "{self.src}", "target": "{self.dst}", "value": {self.weight}}}'
        return f'{{"source": "{self.src}", "target": "{self.dst}"}}'

