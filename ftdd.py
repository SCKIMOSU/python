import numpy as np
import matplotlib.pyplot as plt

SubX=np.random.uniform(2000, -2000, size=[9, 12])
SubY=np.random.uniform(2000, -2000, size=[9, 12])
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

plt.figure(10)
plt.plot(ShiftX, ShiftY, 'bo')

Dist=np.sqrt(ShiftX**2+ShiftY**2)


