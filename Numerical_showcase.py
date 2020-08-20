# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:46:25 2020

@author: JCTron
"""
    
#%% Euler method
# solving a = -G*sin(phi)

import numpy
import matplotlib.pyplot as plt
import math

t = numpy.linspace(0,50,501)
n = numpy.arange(0,len(t)-1,1)
print(len(t))
print(len(n))

x1 = numpy.zeros(len(t))
x1[0] = 1
x2 = numpy.zeros(len(t))
a = numpy.zeros(len(t))

G = 7.6

for i in n:
    ts = t[i+1] - t[i]
    a[i] = -G*math.sin(x1[i])
    x1[i+1] = x1[i] + x2[i]*ts + (1/2)*a[i]*ts**2
    x2[i+1] = x2[i] + a[i]*ts
        
plt.plot(t,x1)
plt.xlabel('time')
plt.ylabel('distance')

#%% improved Euler method on x2[i+1]
# solving a = -G*sin(x1)

import numpy
import matplotlib.pyplot as plt
import math

t = numpy.linspace(0,50,501)
n = numpy.arange(0,len(t)-1,1)
print(len(t))
print(len(n))

x1 = numpy.zeros(len(t))
x1[0] = 1
x2 = numpy.zeros(len(t))
x2[0] = 0
x2r = numpy.zeros(len(t))
x2r[0] = 0
k1 = numpy.zeros(len(t))
k2 = numpy.zeros(len(t))
a = numpy.zeros(len(t))
v = numpy.zeros(len(t))

G = 7.6

for i in n:
    ts = t[i+1] - t[i]
    k1[i] = -G*math.sin(x1[i])
    x2r[i+1] = x2[i] + k1[i]*ts
    k2[i] = -G*math.sin(x1[i]+x2r[i]*ts)
    a[i] = (1/2)*(k1[i]+k2[i])
    x2[i+1] = x2[i] + a[i]*ts
    x1[i+1] = x1[i] + x2[i]*ts + (1/2)*a[i]*ts**2

plt.plot(t,x1)
print(len(x1))

#%% improved Euler method on x[i+1]
# a = -G*sin(phi)

import numpy
import matplotlib.pyplot as plt
import math

t = numpy.linspace(0,50,501)
n = numpy.arange(0,len(t)-1,1)

x1 = numpy.zeros(len(t))
x1[0] = 1
x2 = numpy.zeros(len(t))
x2[0] = 0
a = numpy.zeros(len(t))
v = numpy.zeros(len(t))

G = 7.6

for i in n:
    ts = t[i+1] - t[i]
    a[i] = -G*math.sin(x1[i])
    x2[i+1] = x2[i] + a[i]*ts
    v[i] = (1/2)*(x2[i]+x2[i+1])
    x1[i+1] = x1[i] + v[i]*ts + (1/2)*a[i]*ts**2
    
plt.plot(t,x1)

#%% Runge-Kutta method on v[i+1]
# a = -G*sin(phi)

import numpy
import matplotlib.pyplot as plt
import math

t = numpy.linspace(0,50,501)
n = numpy.arange(0,len(t)-1,1)
print(len(t))
print(len(n))

x = numpy.zeros(len(t))
x[0] = 1
k1 = numpy.zeros(len(t))
k2= numpy.zeros(len(t))
k3 = numpy.zeros(len(t))
k4 = numpy.zeros(len(t))
v = numpy.zeros(len(t))

G = 7.6

for i in n:
    ts = t[i+1] - t[i]
    k1[i] = -G*math.sin(x[i])
    k2[i] = -G*math.sin(x[i]+(v[i]+k1[i]*(1/2)*ts)*(1/2)*ts)
    k3[i] = -G*math.sin(x[i]+(v[i]+k2[i]*(1/2)*ts)*(1/2)*ts)
    k4[i] = -G*math.sin(x[i]+(v[i]+k3[i]*ts)*ts)
    v[i+1] = v[i] + (1/6)*(k1[i]+2*k2[i]+2*k3[i]+k4[i])*ts
    x[i+1] = x[i] + v[i]*ts + (1/2)*(1/6)*(k1[i]+2*k2[i]+2*k3[i]+k4[i])*ts**2
    
plt.plot(t,x)
print(len(x))

#%% Runge-Kutta method on x[i+1]
# a = -G*sin(phi)

import numpy
import matplotlib.pyplot as plt
import math

t = numpy.linspace(0,50,501)
n = numpy.arange(0,len(t)-1,1)

x = numpy.zeros(len(t))
x[0] = 1
k1 = numpy.zeros(len(t))
k2= numpy.zeros(len(t))
k3 = numpy.zeros(len(t))
k4 = numpy.zeros(len(t))
v = numpy.zeros(len(t))

G = 7.6

for i in n:
    ts = t[i+1] - t[i]
    k1[i] = v[i]
    k2[i] = v[i] + -G*math.sin(x[i]+k1[i]*(1/2)*ts)*(1/2)*ts
    k3[i] = v[i] + -G*math.sin(x[i]+k2[i]*(1/2)*ts)*(1/2)*ts
    k4[i] = v[i] + -G*math.sin(x[i]+k3[i]*ts)*ts
    v[i+1] = k4[i]
    x[i+1] = x[i] + (1/6)*(k1[i]+2*k2[i]+2*k3[i]+k4[i])*ts
    
plt.plot(t,x)

#%% Collatz Runge-Kutta
# solving a = -G*sin(phi)

import numpy
import matplotlib.pyplot as plt
import math

t = numpy.linspace(0,50,501)
n = numpy.arange(0,len(t)-1,1)

x = numpy.zeros(len(t))
x[0] = 1
k0 = numpy.zeros(len(t))
k1 = numpy.zeros(len(t))
k2 = numpy.zeros(len(t))
v = numpy.zeros(len(t))
v[0] = 0

G = 7.6

for i in n:
    ts = t[i+1] - t[i]
    k0[i] = -G*math.sin(x[i])
    k1[i] = -G*math.sin(x[i]+(1/2)*ts*v[i]+(1/8)*k0[i]*ts**2)
    k2[i] = -G*math.sin(x[i]+ts*v[i]+(1/2)*k1[i]*ts**2)
    x[i+1] = x[i] + ts*v[i] + (1/6)*(k0[i]+2*k1[i])*ts**2
    v[i+1] = v[i] + (1/6)*(k0[i]+4*k1[i]+k2[i])*ts

plt.plot(t,x)
