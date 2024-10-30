import os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
#from scipy.integrate import quad
import math
A = np.loadtxt(os.path.join(os.path.expanduser('~'),'Desktop','1MMg2rmw','PBC','1MMg-ClKB.dat'))
B = np.loadtxt(os.path.join(os.path.expanduser('~'),'Desktop','1MMg2rmw','PBC','1MMg-OwKB.dat'))
C = open('Mg-Cl-PBC.dat','w')

r = A[:,0]
r1 = B[:,0]
g = A[:,1]
g1 = B[:,1]
z=len(r)
ans=0
result=[]
result= 3.2*(g-g1)
#print str(ans)
for i in range(len(r)):
	ans = (result [0:i],r[0:i])
		#print (ans)
	#result = np.append(result,ans)
	C.write (str(r[i])+'\t'+ str(result[i])+'\n')
	#print (str(r[i])+'\t'+str(result[i])+'\n')
#result = np.append(result,ans)
#	c.write (str(r[i])+'\t'+str(result[i])+'\n')
	#print str(ans[i])

plt.subplot(211),plt.plot(r[:-1],g[:-1],label='g(r)')
plt.legend()
plt.xlabel('r')
plt.ylabel ('g(r)')
plt.subplot(212),plt.plot(r[:-1],result[:-1],label='diff(ga)')
plt.xlabel('d')
plt.ylabel ('S')
plt.legend()
plt.show()	
