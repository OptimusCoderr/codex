
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,1000)
y=np.sin(x)
#plt.plot(x,y)
plt.scatter(x[::10],y[::10],color='red')
plt.plot(x,y,color='b')
plt.plot(x,np.cos(x),color='g')
plt.plot(x,x+0,':r')
plt.plot(x,x+1,'--g')
plt.plot(x,x+2,'-.k')
plt.show()