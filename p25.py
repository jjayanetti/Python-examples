# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:49:40 2020

@author: JJayanetti
"""

#import torch
#### Generate some data
#torch.manual_seed(7) # Set the random seed so things are predictable
#
## Features are 3 random normal variables
#features = torch.randn((1, 5))
## True weights for our data, random normal variables again
#weights = torch.randn_like(features)
## and a true bias term
#bias = torch.randn((1, 1))
#
#print(features)

import numpy as np
a = np.random.rand(4,3)
print(a)
b=np.round(a*10)
print(b)