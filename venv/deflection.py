#---------DEFLECTİON---------
from scipy.integrate import simps
from body import body
from force import force
from reactforce import reactforce
from moment import moment
import numpy as np

class deflection: #CALCULATION OF THE DEFLECTION
    def __init__(self,rf,body,moment):
        self.magnitude=[]
        self.slope=[]
        i=0
        for a in body.y:
            PD1 =simps(moment.defstress[:i+1], body.y[:i+1], 0.0001)
            self.slope.append(PD1)
            PD=simps(self.slope,body.y[:i+1],0.0001)/(300000)
            self.magnitude.append(PD)
            i=i+1


