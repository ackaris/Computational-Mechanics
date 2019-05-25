#---------VON MİSES CLASS----------
from shear_stress import shear_stress
from moment import moment
from body import body
import math
class vonmiises:
    def __init__(self,body,moment,shear):
        self.stress = []
        self.x=[]
        self.y=[]
        for x in body.y:
            i = 0
            temp=[]
            pyarray=body.pyarray(x)
            pmoment=moment.stressarray(body,x)
            pshear=shear.stressarray(body,x)
            for y in body.yy:
                if i!=body.yy[len(body.yy)-1]:
                    if y<pyarray[0] and y>-pyarray[0]:
                        principal1 = vonmiises.principal1(pmoment[i],pshear[i] )
                        principal2 = vonmiises.principal2(pmoment[i], pshear[i])
                        temp.append(math.sqrt((principal1*principal1)-(principal1*principal2)+(principal2*principal2)))
                        i=i+1
                    else:
                        temp.append(0)
            self.stress.append(temp)
    def principal1(moment,shear):
        return (moment/2)+math.sqrt(((moment/2)*(moment/2))+(shear*shear))
    def principal2 (moment,shear):
        return (moment/ 2) - math.sqrt(((moment/ 2) * (moment/ 2)) + (shear * shear))
