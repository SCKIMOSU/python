
import numpy as np
import matplotlib.pyplot as plt

test=np.random.randn(2, 2)
print('test=', test)
nd=np.random.randn(10)
print('nd=', nd)
print('mean=', nd.mean())
print('var=', nd.var())

ud=np.random.uniform(10, -10, size=[3, 3])
print('ud=', ud)


mu=0; sigma=1
x1=mu+sigma*np.random.randn(100)
plt.figure(1)
plt.plot(x1, 'ro')
plt.grid()
plt.show()

print('x1 max =', x1.max())
print('x1 min =', x1.min())

mu=0; sigma2=2
x2=mu+sigma2*np.random.randn(100)
plt.figure(2)
plt.plot(x2, 'b*')
plt.grid()

print('x2 max =', x2.max())
print('x2 min =', x2.min())

plt.figure(3)
plt.plot(x1,'ro', x2, 'b*')



NormalDistribution = np.random.randn(9, 12)
mu = 0
SD = 6
LogNormal=mu+SD*NormalDistribution

print('NormalDistribution.min() =', NormalDistribution.min())
# -2.612972135276542
print('NormalDistribution.max() =', NormalDistribution.max())
# 2.0124483828718933
print('LogNormal.min() =', LogNormal.min())
#-15.677832811659252
print('LogNormal.max() =', LogNormal.max())
# 12.07469029723136
plt.figure(1)
plt.plot(NormalDistribution)
plt.figure(2)
plt.plot(LogNormal)


plt.figure(3)
plt.hist(NormalDistribution[0,:], bins=3, normed=True, color='c', alpha=0.75)

plt.figure(4)
plt.hist(NormalDistribution[0,:], bins=5, normed=True, color='c', alpha=0.75)


NormalDistribution[0,:].min()
#-1.2928843651360855
NormalDistribution[0,:].max()
#2.039330203724115
width=(NormalDistribution[0,:].max()-NormalDistribution[0,:].min())/3
#1.1107381896200668
NormalDistribution[0,:].min()+width
#-0.18214617551601875NormalDistribution[0,:].min()+width*2
0.928592014104048
NormalDistribution[0,:].min()+width*3
#2.0393302037241146
NormalDistribution[0,:].max()
#2.039330203724115



NormalDistribution=np.random.randn(100)
mu=0; sd1=1; sd6=6
SD1=mu+sd1*NormalDistribution
SD6=mu+sd6*NormalDistribution
mu1=5
MU1=mu+sd1*NormalDistribution
MU5=mu1+sd1*NormalDistribution
plt.figure(5)
plt.hist(MU1, bins=3, normed=True, color='r', alpha=0.75)
plt.grid()
plt.show()
plt.figure(5)
#plt.hold(True)
plt.hist(MU5, bins=3, normed=True, color='m', alpha=0.75)
plt.grid()
plt.show()


NormalDistribution = np.random.randn(9, 12)
move=3+NormalDistribution[0,:]
plt.figure(6)
plt.hist(move, bins=3, normed=True, color='m', alpha=0.75)
plt.hist(NormalDistribution[0,:], bins=3, normed=True, color='c', alpha=0.75)

plt.figure(7)
plt.hist(SD1, bins=3, normed=True, color='r', alpha=0.75)
plt.grid()
plt.show()
plt.hist(SD6, bins=3, normed=True, color='M', alpha=0.75)
plt.grid()
plt.show()

