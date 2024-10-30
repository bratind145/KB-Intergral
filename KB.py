import os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy.integrate import quad
#import mathNa30OW-OW-AroundARG.dat
A = np.loadtxt(os.path.join(os.path.expanduser('~'),'Desktop','1MMg2rmw','PBC','1Mrdfprotein-water.dat'))
B = open('1MMgProtein-waterKB.dat','w')

r = A[:,0]
g = A[:,1]
#c=[0]
z=len(r)
ans=0
result=[]
#n=g[z-1.0]
#n=g[z-1.0]
integrand = 4*np.pi*((g-1.00))*(r)*2
#print(integrand[5])
#print(len(g))
#print(len(integrand))

for i in range(z):
	ans = np.trapz(integrand[0:i],r[0:i])
	result = np.append(result,ans)
	B.write (str(r[i])+'\t'+str(result[i])+'\n')
	#print str(result[i])
	#print(result)	
	#print(len(result))	
plt.subplot(211),plt.plot(r[:-1],g[:-1],label='g(r)')
plt.legend()
plt.xlabel('r')
plt.ylabel ('g(r)')
plt.subplot(212),plt.plot(r[:-1],result[:-1],label='integrand(r)')
plt.xlabel('d')
plt.ylabel ('S')
plt.legend()
plt.show()	
