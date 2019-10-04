#-------------MAİN FİLE------------------
from force import force
from reactforce import reactforce
from shear_stress import shear_stress
from body import body
from moment import moment
from vonmises import vonmiises
import matplotlib.pyplot as plt
import numpy as np
from deflection import deflection
isim=input("File Name: ")
l1=int(input("l1: "))
l2=int(input("l2: "))
T=int(input("T: "))
f=int(input("F: "))
body=body(T,l1,l2) #body(thickness,l1,l2)
force=force(f,body) #force(magnitude,body)
rf=reactforce(force) #reactforcce(force)
print("magnitude of force:   "+str(force.magnitude))
print("magnitude of reaction force:   "+str(rf.magnitude))
print("Magnitude of moment raction:  "+str(rf.moment))
shear_stress=shear_stress(body,rf,force) #calculate shear stress
print("shear force:   "+str(shear_stress.magnitude))
moment = moment(body,rf,force) #calculate normal bending stress
print("bending moment: "+str(moment.magnitude))
print("shear stress: "+str(shear_stress.avgstress))
print("def stress: " + str(moment.defstress))
deflection=deflection(rf,body,moment)
print("deflection :  "+str(deflection.magnitude))
vonmiises = vonmiises(body,moment,shear_stress)
print("vonmises: "+str(vonmiises.stress))
print("slope: "+str(deflection.slope))
def write_file(b):
    if b==1:
        file=open(isim+".txt","a")
        file.write("Kahrolası X ekseni : \n\n"+str(body.y)+"\n\n\n"+"shear force:\n   "+str(shear_stress.magnitude)+"\n\n\n"+"bending moment:\n "+str(moment.magnitude)+"\n\n\n\n"+"shear stress:\n "+str(shear_stress.avgstress)+"\n\n\n\n"+"bending stress:\n " + str(moment.defstress)+"\n\n\n\n"+"deflection :\n  "+str(deflection.magnitude)+"\n\n\n\n"+"vonmises:\n "+str(vonmiises.stress)+"\n\n\n\n"+"slope:\n\n "+str(deflection.slope))
        file.close()
write_file(0)
#------------draw the plot-------------------

plt.subplot(211)
plt.plot(body.y,shear_stress.magnitude, 'r--')
plt.title("Kesme Kuvveti")
plt.ylabel("N")
plt.subplot(212)
plt.plot(body.y,moment.magnitude,'c--')
plt.title("Moment")
plt.ylabel("N.mm")
plt.show()
plt.subplot(211)
plt.plot(body.y,moment.defstress,'b--')
plt.title("def Normal Stres")
plt.ylabel("N/mm^2")
plt.subplot(212)
plt.plot(body.y,shear_stress.avgstress,'g--')
plt.title("avg Kayma Gerilmesi")
plt.ylabel("N/mm^2")
plt.show()
plt.subplot(211)
plt.plot(body.y,deflection.slope,'b--')
plt.title("Eğim")
plt.ylabel("mm")
plt.subplot(212)
plt.plot(body.y,deflection.magnitude,'r--')
plt.title("Yer Değiştirme")
plt.ylabel("mm")
plt.show()
plt.contourf(body.yy,body.y,vonmiises.stress,500,cmap=plt.cm.bone,)
plt.show()




