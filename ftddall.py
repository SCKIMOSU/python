
import numpy as np
import matplotlib.pyplot as plt

FreqReUse=9
NoUpLink=12
NtwSizeA=-2000
NtwSizeB=2000
PlusShift=12000
MinusShift=-12000
No_Iterations=1000


SIR=np.zeros((1,NoUpLink))

for Loop in range(0,No_Iterations):

    SubX = np.random.uniform(NtwSizeA, NtwSizeB, size=[FreqReUse, NoUpLink])
    SubY = np.random.uniform(NtwSizeA, NtwSizeB, size=[FreqReUse, NoUpLink])

    Cell_x0 = SubX[0, :]
    Cell_y0 = SubY[0, :]
    Cell_x1 = SubX[1, :]
    Cell_y1 = SubY[1, :] + PlusShift
    Cell_x2 = SubX[2, :] + PlusShift
    Cell_y2 = SubY[2, :] + PlusShift
    Cell_x3 = SubX[3, :] + PlusShift
    Cell_y3 = SubY[3, :]
    Cell_x4 = SubX[4, :] + PlusShift
    Cell_y4 = SubY[4, :] + MinusShift
    Cell_x5 = SubX[5, :]
    Cell_y5 = SubY[5, :] + MinusShift
    Cell_x6 = SubX[6, :] + MinusShift
    Cell_y6 = SubY[6, :] + MinusShift
    Cell_x7 = SubX[7, :] + MinusShift
    Cell_y7 = SubY[7, :]
    Cell_x8 = SubX[8, :] + MinusShift
    Cell_y8 = SubY[8, :] + PlusShift

    ShiftX = np.array([Cell_x0, Cell_x1, Cell_x2, Cell_x3, Cell_x4, Cell_x5,
                        Cell_x6, Cell_x7, Cell_x8])
    ShiftY = np.array([Cell_y0, Cell_y1, Cell_y2, Cell_y3, Cell_y4, Cell_y5,
                        Cell_y6, Cell_y7, Cell_y8])

    Dist = np.sqrt(ShiftX**2+ ShiftY**2)

    NormalDistribution = np.random.randn(FreqReUse, NoUpLink)
    mu = 0
    SD = 6
    LogNormal=mu+SD*NormalDistribution

    LogNormalP=10**(LogNormal/10)/(Dist**4)

    PS = LogNormalP[0, :]
    PI1 = LogNormalP[1, :]
    PI2 = LogNormalP[2, :]
    PI3 = LogNormalP[3, :]
    PI4 = LogNormalP[4, :]
    PI5 = LogNormalP[5, :]
    PI6 = LogNormalP[6, :]
    PI7 = LogNormalP[7, :]
    PI8 = LogNormalP[8, :]

    PI = PI1+PI2+PI3+PI4+PI5+PI6+PI7+PI8
    SIRn = PS/PI
    SIRdB = 10*np.log10(SIRn)

    SIR = np.vstack((SIR, SIRdB))

SIR=np.delete(SIR, 0,0)
SIR=SIR.flatten()


plt.figure(2)
hist, bin_left, patch=plt.hist(SIR, bins=100)
plt.grid()


pdf=hist/np.size(SIR)
plt.figure(3)
plt.plot(bin_left[:-1], pdf, 'ro-', lw=2)


cdf=np.cumsum(pdf)
plt.figure(4)
plt.semilogy(bin_left[:-1], cdf, color='c', lw=2)
#plt.axis([0, 100, 10**-5, 10**0])
plt.xlabel('Signal to Interference Ratio (SIR) [dB]')
plt.ylabel('Probability of SIR (SIR < x)')
plt.title('Cumulative Density Function of SIR')
plt.text(20, 1e-3, r'Frequency Reuse Factor=9')
plt.axis([-5, 50, 1e-4, 1])
plt.grid(True)
plt.show()











