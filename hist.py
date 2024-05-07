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

plt.figure(20)
hist, bin_left, patch=plt.hist(s, bins=4)
plt.grid()


pdf=hist/np.size(s)
plt.figure(21)
plt.plot(bin_left[:-1], pdf, 'ro-', lw=2)


cdf=np.cumsum(pdf)
plt.figure(22)
plt.semilogy(bin_left[:-1], cdf, color='c', lw=2)
#plt.axis([0, 100, 10**-5, 10**0])
plt.xlabel('s')
plt.ylabel('Probability of s (s < x)')
plt.title('Cumulative Density Function of s')
#plt.text(20, 1e-3, r'Frequency Reuse Factor=9')
#plt.axis([-5, 50, 1e-4, 1])
plt.grid(True)
plt.show()
