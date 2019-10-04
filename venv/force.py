#----------FORCCE CLASS------------
from body import body
class force:
    def __init__ (self,f,body): #DETERMINING FORCE OBJECT
        self.magnitude = f*(body.l2/1000)
        self.f=f
        self.starts = body.l1
        self.ends = body.l1+body.l2
        self.location = (self.starts+self.ends)/2
    def magcalc(self,body,x): #FROM ADJUSTABLE FUNCTION OF THE DISTRUBUTED LOAD, CALCULATES TOTAL FORCE
        magnitude=self.f*((x/1000)-(body.l1/1000))
        return magnitude