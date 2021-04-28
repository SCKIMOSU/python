import numpy as np
import matplotlib.pyplot as plt


s=np.random.uniform(6, 7, 25)

smin=s.min()
smax=s.max()
bin_width=(s.max()-s.min())/4
first_left=smin
second_left=smin+bin_width
third_left=smin+bin_width*2
fourth_left=smin+bin_width*3
fifth_left=smin+bin_width*4

bins_left=np.array([first_left, second_left, third_left, fourth_left])

first_height=np.size(np.where( (s < second_left) & ( s>= first_left) ))
second_height=np.size(np.where( (s < third_left) & ( s>= second_left) ))
third_height=np.size(np.where( (s < fourth_left) & ( s>= third_left) ))
fourth_height=np.size(np.where( (s < fifth_left) & ( s>= fourth_left) ))

bins_height=np.array([first_height, second_height, third_height, fourth_height])

plt.figure(1)
plt.subplot(2,1,1)
plt.bar(bins_left, bins_height, width = bin_width)
plt.grid()

plt.subplot(2,1,2)
plt.bar(bins_left, bins_height, width = bin_width-0.05)
plt.grid()
plt.show()


pdf=bins_height/np.size(s)
#np.cumsum(bin_height/np.size(s))

cdf=np.cumsum(pdf)

plt.figure(12)
plt.subplot(3,1,1)
plt.bar(bins_left, bins_height/np.size(s), bin_width-0.1)

plt.subplot(3,1,2)
plt.bar(bins_left, pdf, bin_width-0.1)

plt.subplot(3,1,3)
plt.bar(bins_left, cdf, bin_width-0.1)




nd1=np.random.randn(10000)
ud1=np.random.uniform(-1, 1, 10000)

plt.figure(1)
plt.subplot(2, 1, 1)
plt.hist(nd1, 4)
plt.title('2 subplots')
plt.ylabel('Normal')
plt.grid()
plt.subplot(2, 1, 2)
plt.hist(ud1, 4)
plt.ylabel('Uniform')
plt.grid()
plt.show()


one_sigma=np.size(np.where((nd1>=-1) & (nd1<=1) ))
#Out[163]: 6768
ud_count=np.size(np.where((ud1>=-1) & (ud1<=1) ))
# 10000
two_sigma=np.size(np.where((nd1>=-2) & (nd1<=2) ))
# 9541
three_sigma=np.size(np.where((nd1>=-3) & (nd1<=3) ))


sd=6
nd_large=np.random.randn(10000)*sd
plt.figure(10)
plt.subplot(2, 1, 1)
plt.hist(nd1, 50)
#plt.plot(f, y1, 'ko-')
plt.title('2 subplots')
plt.ylabel('one_sigma')
#plt.axis([0, 5, -1, 3])
plt.grid()
plt.subplot(2, 1, 2)
plt.hist(nd_large, 50)
plt.ylabel('six_sigma')
#plt.axis([0, 5, -1, 3])
plt.grid()
plt.show()


one_sigma=np.size(np.where((nd1>=-1) & (nd1<=1) ))
# 6835
one_sigma1=np.size(np.where((nd_large>=-1) & (nd_large<=1) ))
# 1301

two_sigma=np.size(np.where((nd1>=-2) & (nd1<=2) ))
# 9541
two_sigma1=np.size(np.where((nd_large>=-2) & (nd_large<=2) ))
# 2556

three_sigma=np.size(np.where((nd1>=-3) & (nd1<=3) ))
# 9970
three_sigma1=np.size(np.where((nd_large>=-3) & (nd_large<=3) ))
#3805


plt.figure(11)
plt.subplot(2, 1, 1)
plt.hist(nd1, 50)
#plt.plot(f, y1, 'ko-')
plt.title('2 subplots')
plt.ylabel('one_sigma')
plt.axis([-20,20 , 0, 700])
plt.grid()
plt.subplot(2, 1, 2)
plt.hist(nd_large, 50)
plt.ylabel('six_sigma')
plt.axis([-20,20 , 0, 700])
plt.grid()
plt.show()



one_nd_large=np.size(np.where((nd_large>=-6) & (nd_large<=6) ))
# 6815
two_nd_large=np.size(np.where((nd_large>=-6*2) & (nd_large<=6*2) ))
# 9640



plt.figure(12)
plt.subplot(3, 1, 1)
plt.hist(ud1, 50)
plt.title('3 subplots')
plt.ylabel('uniform')
plt.axis([-20,20 , 0, 700])
plt.grid()
plt.subplot(3, 1, 2)
plt.hist(nd1, 50)
plt.ylabel('one_sigma')
plt.axis([-20,20 , 0, 700])
plt.grid()
plt.subplot(3, 1, 3)
plt.hist(nd_large, 50)
plt.ylabel('six_sigma')
plt.axis([-20,20 , 0, 700])
plt.grid()
plt.show()




