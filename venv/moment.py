#----------MOMENT---------
from body import body
from force import force
from reactforce import reactforce

class moment:
    def __init__(self,body,rf,f):
        self.magnitude=[]
        self.defstress=[]
        for x in body.y:
            defstress=0
            if x<body.l1:
                magnitude=+rf.magnitude*x-rf.moment
                self.magnitude.append(magnitude)
                defstress=(magnitude/body.pcsmodulus(x))
            else:
                magnitude=rf.magnitude*x+f.magcalc(body,x)*((x-body.l1)/2)-rf.moment
                self.magnitude.append(magnitude)
                defstress=magnitude/body.pcsmodulus(x)
            self.defstress.append(defstress)
    def stressarray(self,body,x):
        pyarray=body.pyarray(x)
        i=body.y.index(x)
        stressarray=[]
        defstress=self.defstress[i]
        for a in pyarray:
            stressarray.append(-defstress*a)
        return stressarray


    