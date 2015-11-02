# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:37:51 2015

@author: eric.bertok
"""

import numpy as np
import matplotlib.pyplot as plt

c=299792458
h=6.62e-34

def lamb(Ekin,m):
    return h*c/np.sqrt(Ekin**2+2*Ekin*m*c**2)

Ekin=np.linspace(0,2.24e-7,10000)
fig = plt.figure(figsize=(5,5))
plt.loglog(Ekin,lamb(Ekin,1.673e-27),'b-')
plt.loglog(Ekin,lamb(Ekin,9.11e-31),'r-')
plt.loglog(Ekin,lamb(Ekin,0),'g-')
plt.show()