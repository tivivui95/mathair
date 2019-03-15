# Feb 27, 2019
# Nguyen Minh Van (Mr)
# MathAIR'19.01
# Practice of chapter 2
# Space of functions: representation and search
# Graph in Slide 4



import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
# create 2 theta array (a,b)
delta = 1
a = np.arange(-2, 3, delta)
b = np.arange(-2, 3, delta)
aa, bb = np.meshgrid(a,b)
y = aa + bb
# create first subplot for first graph
fig, ax = plt.subplots()
CS = ax.contour(aa, bb, y, 8,linewidths=2)

ax.clabel(CS, fontsize=15, inline=1, inline_spacing=1)
ax.set_title('Figure 1')
# create points
a1 = np.arange(-1,2, 0.125)
x = np.arange(-2, 3, 0.25)
b1 = 1-1*a1
y = a1+b1

plt.figure(1)
# draw points
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.xlabel('a')
plt.ylabel('b')
plt.plot(a1,b1,'ro')
# create another points 
b2 = np.arange(-2,2, 0.125)
a2 = 0.5*(b2**2) - 1
plt.plot(a2,b2,'ro', color='blue')
cc, ab = plt.subplots()
# plot all function 
for n in range(0,len(b1)):	
	plt.plot(x,a1[n]*x+b1[n], color='red')
	plt.plot(x,a2[n]*x+b2[n], color='blue')
ab.axhline(y=0, color='k')
ab.axvline(x=0, color='k')
ab.set_title('Figure 2')
plt.xlabel('x', multialignment='center')
plt.ylabel('y', multialignment='center')
plt.axis([-2,2,-2,2])
plt.show()
