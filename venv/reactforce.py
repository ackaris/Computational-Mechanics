#--------REACTİON FORCE CLASS-----------
from force import force
class reactforce:
    def __init__(self,f): #DEFİNES REACTION FORCE
        forcem = f.magnitude
        forces = f.starts
        forcee = f.ends
        self.magnitude = -forcem
        self.locx=0
        self.locy=0
        self.moment=-forcem*(((forcee-forces)/2)+forces)

    
