
import numpy as np
import matplotlib.pyplot as plt

SubX=np.random.uniform(2000, -2000, size=[9, 12])
SubY=np.random.uniform(2000, -2000, size=[9, 12])

plt.plot(SubX[8,:]-12000, SubY[8, :]+12000, '*')
plt.plot(SubX[8,:]-12000, SubY[8, :]+12000, '5')
plt.plot(SubX[7,:]-12000, SubY[7, :], '4')
plt.xlim(-14000, 14000)
plt.plot(SubX[6,:]-12000, SubY[6, :]-12000, '3')
plt.plot(SubX[5,:], SubY[5, :]-12000, '2')
plt.ylim(-14000, 14000)
plt.plot(SubX[4,:]+12000, SubY[4, :]-12000, '1')
plt.plot(SubX[3,:]+12000, SubY[3, :], 'p')
plt.xlim(-2000, 14000)
plt.plot(SubX[2,:]+12000, SubY[2, :]+12000, 'o')
plt.plot(SubX[0,:], SubY[0, :], 'o')
plt.ylim(-2000, 14000)
plt.xlim(-2000, 2000)
plt.plot(SubX[1,:], SubY[1,:]+12000, 'x')
plt.figure(2)
SubX[1,:]
plt.ylim(-2000, 2000)
plt.figure(1)

PlusShift=12000;
MinusShift=-12000;

Cell_x0=SubX[0,:];
Cell_y0=SubY[0,:];
Cell_x1=SubX[1,:];
Cell_y1=SubY[1,:]+PlusShift;
Cell_x2=SubX[2,:]+PlusShift;
Cell_y2=SubY[2,:]+PlusShift;
Cell_x3=SubX[3,:]+PlusShift;
Cell_y3=SubY[3,:];
Cell_x4=SubX[4,:]+PlusShift;
Cell_y4=SubY[4,:]+MinusShift;
Cell_x5=SubX[5,:];
Cell_y5=SubY[5,:]+MinusShift;
Cell_x6=SubX[6,:]+MinusShift;
Cell_y6=SubY[6,:]+MinusShift;
Cell_x7=SubX[7,:]+MinusShift;
Cell_y7=SubY[7,:];
Cell_x8=SubX[8,:]+MinusShift;
Cell_y8=SubY[8,:]+PlusShift;




ShiftX=np.array([Cell_x0, Cell_x1, Cell_x2, Cell_x3, Cell_x4, Cell_x5, Cell_x6, Cell_x7, Cell_x8])
ShiftY=np.array([Cell_y0, Cell_y1, Cell_y2, Cell_y3, Cell_y4, Cell_y5, Cell_y6, Cell_y7, Cell_y8])


Dist=np.sqrt(ShiftX**2+ShiftY**2)
Dist[0,0]
np.sqrt(ShiftX[0,0]**2+ShiftY[0,0]**2)
ShiftY[0,0]
ShiftX[0,0]
np.shape(ShiftX)
Dist


plt.plot(ShiftX, ShiftY, 'bo')
plt.figure(10)

np.size(ShiftX)
np.size(Cell_x0)
ShiftY
ShiftX




