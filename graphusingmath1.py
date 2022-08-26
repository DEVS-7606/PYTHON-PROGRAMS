import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,2*np.pi,0.1)
x=t
y=np.sin(t)
plt.stem(x,y,'r')
plt.xlabel('t')
plt.ylabel('sint')
plt.title('sine wave')
plt.plot(x,y)
plt.show()