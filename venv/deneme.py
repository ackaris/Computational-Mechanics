import matplotlib.pyplot as plt
import numpy as np
x=[1,10,20,30,40]
y=[1.5,2.5,3.5]

xx,yy=np.meshgrid(x,y)
def z(xx,yy):
   return xx*yy
z=z(xx,yy)
print(z)
plt.contour(x,y,z)
plt.show()