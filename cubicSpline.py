import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

A = np.array([[1,1,1,0,0,0],
              [3,2,1,0,0,-1],
              [6,2,0,0,-2,0],
              [0,0,0,1,1,1],
              [0,2,0,0,0,0],
              [0,0,0,6,2,0]])

y = np.array([1,0,0,-1,0,0]).reshape(6,1)

c = la.solve(A,y)   # Directly solving System

np.linalg.cond(A)    # Gives us condition number of Matrix

t1 = [0,1,2]
y1 = [0,1,0]
cs1 = CubicSpline(t1,y1,bc_type='natural')
T1 = np.linspace(0,2,200)
Y1 = cs1(T1)
plt.plot(T1,Y1,t1,y1,'r.',markersize=12)
plt.show()