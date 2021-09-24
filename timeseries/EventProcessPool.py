#import ent.Entity

class EventProcessPool:
  #TODO: entities are never unbound from singleton events that die.
    def  __init__(self):
        self.pool = {}       #new mutable.HashMap[Int, Option[Iterator[_]]]

    def add(self, event):
        self.pool[event.uid] = event.getIter()

    def kill(self, uid):
        if uid in self.pool:
            del self.pool[uid]

    #TODO TED fix: iterates through all k,v in map, and advances each iterator by one, or removes it from pool.

    def go(self):
        for k,v in list(self.pool.items()):
            if v:
                option = next(v, None) 
            if option is None:
                del self.pool[k]
    
    def stats(self):
        ret = "EventProcessPool total UIDs: " + str(len(self.pool.keys())) + " Events: " + str(len(self.pool.values())) + "\n"
        return ret