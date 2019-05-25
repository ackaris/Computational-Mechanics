#----------FORCCE CLASS------------
from body import body
class force:
    def __init__ (self,f,body):
        self.magnitude = f*(body.l2/1000)
        self.f=f
        self.starts = body.l1
        self.ends = body.l1+body.l2
        self.location = (self.starts+self.ends)/2
    def magcalc(self,body,x):
        magnitude=self.f*((x/1000)-(body.l1/1000))
        return magnitude