

import numpy as np
import matplotlib.pyplot as plt

test=np.round(np.random.randn(2, 2),2)
print('test=', test)
nd=np.random.randn(10)
print('nd=', nd)
print('mean=', nd.mean())
print('var=', nd.var())

ud=np.round(np.random.uniform(10, -10, size=[3, 3]),2)
print('ud=', ud)


mu=0; sigma=1
x1=np.round(mu+sigma*np.random.randn(100),2)

plt.figure(1)
plt.plot(x1, 'ro')
plt.grid()
plt.show()

print('x1 max =', x1.max())
print('x1 min =', x1.min())

mu=0; sigma2=2
x2=np.round(mu+sigma2*np.random.randn(100), 2)

plt.figure(2)
plt.plot(x2, 'b*')
plt.grid()
plt.show()


print('x2 max =', x2.max())
print('x2 min =', x2.min())

plt.figure(3)
plt.plot(x1,'ro', x2, 'b*')
plt.show()


NormalDistribution = np.round(np.random.randn(9, 12), 2)
mu = 0
SD = 6
LogNormal=mu+SD*NormalDistribution

print('NormalDistribution.min() =', NormalDistribution.min())
# -2.612972135276542
print('NormalDistribution.max() =', NormalDistribution.max())
# 2.0124483828718933
print('LogNormal.min() =', np.round(LogNormal.min(), 2))
#-15.677832811659252
print('LogNormal.max() =', np.round(LogNormal.max(), 2))
# 12.07469029723136

plt.figure(4)
plt.plot(NormalDistribution)
plt.show()

plt.figure(5)
plt.plot(LogNormal)
plt.show()

plt.figure(6)
plt.hist(NormalDistribution[0,:], bins=3, density=True, color='c', alpha=0.75)
plt.show()

# normed=True --> density=True
plt.figure(7)
plt.hist(NormalDistribution[0,:], bins=5, density=True, color='c', alpha=0.75)
plt.show()


np.round(NormalDistribution[0,:].min(),2)
#-1.2928843651360855
np.round(NormalDistribution[0,:].max(), 2)
#2.039330203724115
width=np.round((NormalDistribution[0,:].max()-NormalDistribution[0,:].min())/3,2)
#1.1107381896200668
np.round(NormalDistribution[0,:].min()+width,2)
#-0.18214617551601875NormalDistribution[0,:].min()+width*2
# 0.928592014104048
np.round(NormalDistribution[0,:].min()+width*3,2)
#2.0393302037241146
np.round(NormalDistribution[0,:].max(),2)
#2.039330203724115



NormalDistribution=np.random.randn(100)
NormalDistribution= np.round(NormalDistribution,2)

mu=0; sd1=1; sd6=6
SD1=mu+sd1*NormalDistribution
SD6=mu+sd6*NormalDistribution

mu1=5
MU1=mu+sd1*NormalDistribution
MU5=mu1+sd1*NormalDistribution

plt.figure(8)
plt.hist(MU1, bins=3, density=True, color='r', alpha=0.75)
plt.grid()
plt.show()

plt.figure(9)
#plt.hold(True)
plt.hist(MU5, bins=3, density=True, color='m', alpha=0.75)
plt.grid()
plt.show()


NormalDistribution = np.random.randn(9, 12)
NormalDistribution=np.round(NormalDistribution, 2)

move=3+NormalDistribution[0,:]
plt.figure(10)
plt.hist(move, bins=3, density=True, color='m', alpha=0.75)
plt.hist(NormalDistribution[0,:], bins=3, density=True, color='c', alpha=0.75)
plt.show()

plt.figure(11)
plt.hist(SD1, bins=3, density=True, color='r', alpha=0.75)
plt.grid()
plt.show()
plt.hist(SD6, bins=3, density=True, color='m', alpha=0.75)
plt.grid()
plt.show()




nd=np.random.randn(10000)
nd=np.round(nd,2)
plt.figure(100)
plt.hist(nd, bins=50, color='g')
plt.grid()
plt.show()

nd.mean() #-0.008050713102905626
nd.var() # 1.0059086547373635

a=nd.min()  # -3.5581370865725797
b=nd.max()  # 3.6194637168219708
aw=(b-a)/10  # 0.71776008033945504 width of each bin

nd=np.random.randn(10000)
nd=np.round(nd,2)
plt.figure(101)
n, bins, patches = plt.hist(nd, 50, density=True, facecolor='g', alpha=0.75)
plt.grid()
plt.show()

np.round(nd.mean(),2) #-0.008050713102905626
np.round(nd.var(),2) # 1.0059086547373635
a=np.round(nd.min(),2) # -3.5581370865725797
b=np.round(nd.max(),2)  # 3.619463716821970
aw=np.round((b-a)/10,2)  # 0.71776008033945504 width of each bin
