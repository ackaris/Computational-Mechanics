#-----------BODY CLASS------------
import numpy as np
class body:
    def __init__(self,thickness,l1,l2):
        self.length=l1+l2
        self.thickness=thickness
        self.l1=l1
        self.l2=l2
        self.y=[]
        self.yy=self.pyarray(0)
        for x in range(0,self.length+1):
            self.y.append(x)
            if x!=self.length:
                self.y.append(x+0.5)
    def pcrossection(self,x):# Returns diameter by x location
        pc=0
        if x<self.l1:
            fc=-(25/self.l1)*x+50
            pd=fc*2
        else:
            pd=50
        pc = self.thickness*pd
        return pc
    def pcsmodulus(self,x):
        pcsm=0
        cs=self.pcrossection(x)
        pcsm=(1/6)*(1*cs*cs)
        return pcsm
    def pyarray(self,x):
        h=self.pcrossection(x)/self.thickness
        a=h/2
        b=-h/2
        pyarray=[]
        for x in np.arange(a,b,-0.5):
            pyarray.append(x)
        return pyarray