#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
from math import *
from scipy import special

#dimensionless time (tD)
tD = 6.33*k*t/(phi*mu*cwt*r**2)

#tcross (if tD < tcross, then aquifer is infinte else it is finite)
b0 = -1.767
b1 = -0.606
b2 = 0.12368
b3 = 3.02
b4 = 2.25
b5 = 0.5
tcross = b0+b1(rD)+b2((rD)**b4)+b3(loge(rD))**b5


#dimensionless aquifer size (rD)
rD = ra/r

##############################################################################
#Constant Terminal Pressure for finite aquifers(tD > tcross)
##############################################################################
csch(rD) = 2/((e**rD)-(e**-rD))
#for alpha 1
b0 = -0.00222107
b1 = -0.627638
b2 = 6.277915
b3 = -2.734405
b4 = 1.2708
b5 = -1.100417
a1 = b0+b1*(csch(rD))+b2*(rD**b3)+b4*(rD**b5)

#for alpha 2
b0 = -0.00796608
b1 = -1.85408
b2 = 18.71169
b3 = -2.758326
b4 = 4.829162
b5 = -1.009021
a2 = b0+b1*(csch(rD))+b2*(rD**b3)+b4*(rD**b5)

#Calculate qD
bj_0_1 = special.j0(a1)
bj_1_1 = special.j1(a1*rD)
bj_0_2 = special.j0(a2)
bj_1_2 = special.j1(a2*rD)
qD1 = ((rD**2)-1)/2
qD2 = (2e**((-a1**2)*tD)*bj_1_1**2)/((a1**2)*bj_0_1**2 - bj_1_1**2)
qD3 = (2*e**((-a2**2)*tD)*(bj_1_2)**2)/((a1**2)*(bj_0_1**2)- bj_1_1**2
qD = qD1 - qD2 - qD3
                    









'''#for tD < 0.01
qD = (2/SQRT(pi))(SQRT(tD))

#for 0.01-< tD <200

b0 = 1.129552
b1 = 1.160436
b2 = 0.2642821
b3 = 0.01131791
b4 = 0.5900113
b5 = 0.04589742
b6 = 1.00
b7 = 0.5002034
b8 = 1.500
b9 = 1.979139

qD = (b0(tD**b7)+b1(tD)+b2(tD**b8)+b3(tD**b9))/(b4(tD**b7)+b5(tD)+b6)

#for 200-<tD<2.0*10^12
b0 = 4.39880
b1 = 0.43693
b2 = -4.16078
b3 = 0.090
qD = 10**(b0+b1*loge(tD)+b2((loge(tD))**b3)'''
          
#################################################################################
#Aquifer parameters
#################################################################################
          




          
          

          


# In[5]:





# In[6]:


import scipy


# In[8]:


a = scipy.__dir__()


# In[9]:


import sympy


# In[11]:


scipy.special.jv(1,1) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




