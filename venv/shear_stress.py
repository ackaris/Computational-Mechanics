#---------SHEAR CLASS------------
from body import body
from reactforce import reactforce
from force import force

class shear_stress:
    def __init__(self,body,reactforce,force):
        self.magnitude=[]
        self.avgstress=[]
        for x in body.y:
            cs=body.pcrossection(x)
            if x<body.l1:
                self.magnitude.append(reactforce.magnitude)
                self.avgstress.append((reactforce.magnitude)/cs)
            else:
                self.magnitude.append(reactforce.magnitude+force.magcalc(body,x))
                self.avgstress.append((reactforce.magnitude+force.magcalc(body,x))/cs)
    def stressarray(self,body,x):
        pyarray = body.pyarray(x)
        i = body.y.index(x)
        stressarray = []
        avgstress = self.avgstress[i]
        for a in pyarray:
            h=body.pcrossection(x)/body.thickness
            stress=((6*self.magnitude[i])/(body.thickness*h*h*h))*(((h*h)/4)-(a*a))
            stressarray.append(stress)
        return stressarray

            
            

