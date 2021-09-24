from ..ent.Point import Point


"""
  * Specifies a SpatioTemporal Node
"""
class STNode:
    def __init__(self, uniqueId, initialPosition=None):
        self.uid = uniqueId
        self.position = initialPosition
        self.group = 1

    def getPos(self):
        return self.position

    def __eq__(self, other):
        if isinstance(other, STNode) and other.uid == self.uid:
            return True
        return False

    def __hash__(self):
        return hash(self.uid)

    def __str__(self):
        #return f"{self.uid};[List{self.position}];"
        pos_str = f' "fx": {self.position.mags[0]}, "fy": {self.position.mags[1]},' if self.position else ""
        return f'{{"id": "{self.uid}",{pos_str} "group": {self.group}}}'


#######################################
#######        2021-08-10       #######
#######################################
'''
#Models a STNode
class STNode:
    def __init__(self, uid,x,y):
        self.uid = uid
        self.position_x = x 
        self.position_y = y 
        self.velocity_x = 0 
        self.velocity_y = 0 
        self.broadcast_range = 0
        self.broadcast_bandwidth = 0
        self.broadcast_duration = 0
        self.isActive = False
        self.prior_states = []
        self.dynamics = None
        self.group = 1
        self.gravity = 0
'''

class Node:
    def __init__(self, uid, loc, body, emitter):
        self.uid = uid
        self.location = loc
        self.body = body
        self.emitter = emitter
        self.reciever = receiver
        self.prior_states = []


    def inRange(self, other):
        return None
    
    def __eq__(self, other):
        if isinstance(other, Node) and other.uid == self.uid:
            return True
        return False

    def __hash__(self):
        return hash(self.uid)

    def __str__(self):
        pos_str = f' "fx": {self.location.x}, "fy": {self.location.y},' if self.location else ""
        return f'{{"id": "{self.uid}",{pos_str} "group": {self.location.group}}}'

class Emitter:
    def __init__(self):
        self.broadcast_range = 0
        self.broadcast_bandwidth = 0
        self.broadcast_duration = 0
        self.isActive = False

class Reciever:
    def __init__(self):
        self.reception_range = float('inf')
        self.reception_bandwidth = float('inf')
        self.reception_duration = float('inf')
        self.reception_group = True
        self.isActive = True 

class Location:
    def __init__(self):
        self.group = 1
        self.x = 0
        self.y = 0

class Body:
    def __init__(self, pos):
        self.velocity = None
        self.gravity = 0
        self.dynamics = None
        self.speed = 0
        self.terminal = 0






