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
plt.bar(bin_left, bin_height/np.size(s), bin_width-0.1)

plt.subplot(3,1,2)
plt.bar(bin_left, pdf, bin_width-0.1)

plt.subplot(3,1,3)
plt.bar(bin_left, cdf, bin_width-0.1)






