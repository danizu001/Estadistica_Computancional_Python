import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5,6,7,8,9]
y=[1,2,3,5,4,6,8,7,9]
coef=np.polyfit(x,y,1)
print(coef)
m=coef[0]
b=coef[1]
est_y=(m*np.array(x))+b
plt.plot(x,y)
plt.plot(x,est_y)
plt.scatter(x,y)