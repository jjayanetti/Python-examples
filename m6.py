# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:58:59 2024

@author: JJayanetti
"""

import numpy as np
values=np.array([6,0,0,3,2,5,6])
print(np.in1d(values,[2,3,5]))

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[6,23],[-1,7],[8,9]])

print(x.dot(y))

from numpy.linalg import inv, qr
X=np.random.standard_normal((5,5))
mat=X.T@X
print(inv(mat))
