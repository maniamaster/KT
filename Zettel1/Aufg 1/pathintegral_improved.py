# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:16:29 2015

@author: eric.bertok
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import cmath

l=1 #length=1m, both source-slit , slit-screen
D=1.e-3 #slit width = 1*10^-3 m
nslit=1000. #  # of slit points
B=1/(nslit)
lamb=500.e-9 #wavelength
ndetector=1.e4
detectorwidth=1.e-4
photonenanz=ndetector*3600
print photonenanz

#compute 100 evenly spaced points in slit:
xslit=np.linspace(-D/2.,D/2.,nslit)

result=0
def A(screen):   
    global result
    for x in xslit:
        result=result+B*(np.cos(2*np.pi*(np.sqrt(1+x**2)+np.sqrt(1+(screen-x)**2))/lamb)  + 1j * np.sin(2*np.pi*(np.sqrt(1+x**2)+np.sqrt(1+(screen-x)**2))/lamb))
        #result=result+(B*exp(-1j*2*pi*(sqrt(1+x**2)+sqrt(1+(screen-x)**2))/lamb))   
    return result

#Schirm:
x=np.linspace(-ndetector*detectorwidth/2.,ndetector*detectorwidth/2.,ndetector+1)

#normierung:
norm=np.sum(abs(A(x))**2)
print norm

fig = plt.figure(figsize=(5,5))
plt.plot(x,np.abs(A(x))**2,'x')
plt.xlim(-0.5,0.5)
plt.show()
