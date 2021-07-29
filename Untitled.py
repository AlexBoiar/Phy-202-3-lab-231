#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
a = np.genfromtxt("green1single.txt",skip_header=10,delimiter =",")

from numpy import sin, cos, pi


# In[6]:


x = a[:,0] - a[813,0]
Intensity = a[:,1]


# In[7]:


print(np.where(Intensity == np.max(Intensity)), len(x))


# In[8]:


fig = plt.figure()

ax = fig.add_subplot(111)

ax.plot(x,Intensity)

ax.plot()


# In[20]:


def diffract(theta, w, s, N, lmbda):
    k = (2 * pi) / lmbda
    v = 1/2 * k * s * sin(theta)
    u = 1/2 * k * w * sin(theta)
    y = (w ** 2) * (((sin(u) / u) * (sin(N * v) / sin(v))) ** 2)
    return y


# In[ ]:





# In[21]:


a[:,0]


# In[22]:


theta = np.arctan(x*5.474*10**-6)


# In[49]:


Theory = diffract(theta,4*650e-6,0.001,1,650e-9)


# In[50]:


plt.semilogy(sin(theta),Intensity)

plt.semilogy(sin(theta),Theory)


# In[ ]:





# In[ ]:





# In[ ]:




