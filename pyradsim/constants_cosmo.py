# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:46:57 2016

@author: wolfensb
"""
import scipy.special as spe
import pyradsim.constants as constants
import numpy as np

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# PSD Parameters

# Graupel PSD
N0_G=4*1E3 # mm-1 m-3
A_G=169.6/(1000**3.1) # m_g = am_g * D**3.1 (with m_g in kg and D in m)
B_G=3.1
ALPHA_G=442.0/(1000**0.89) # mm^0.89*s-1
BETA_G=0.89
MU_G=0.0
D_MIN_G=0.2
D_MAX_G=15

# Compute constant integration factors (saves time since evaluation 
# of gamma function is done only once)
LAMBDA_FACTOR_G=A_G*N0_G*spe.gamma(B_G+1)
VEL_FACTOR_G=spe.gamma(MU_G+BETA_G+1)
NTOT_FACTOR_G=spe.gamma(MU_G+1)

# Ice crystals PSD
N0_I=1.0E2 # mm-1 m-3

# Snow PSD
A_S=0.038/(1000**2)  # kg * mm^-2 
B_S=2 # power
ALPHA_S=4.9/np.sqrt(1000) # mm^0.5*s-1
BETA_S=0.5
MU_S=0.0
D_MIN_S=0.2
D_MAX_S=20

# Compute constant integration factors (saves time since evaluation 
# of gamma function is done only once)
LAMBDA_FACTOR_S=spe.gamma(B_S+1)
VEL_FACTOR_S=spe.gamma(MU_S+BETA_S+1)
NTOT_FACTOR_S=spe.gamma(MU_S+1)

# Rain DSD
RAIN_FACTOR=0.1
MU_R=0.5
N00_r=8E6/(1000**(1+MU_R))*(0.01)**(-MU_R) # m^(-3)*mm^(-1-mu)
N0_R=RAIN_FACTOR*N00_r*np.exp(3.2*MU_R)
A_R=np.pi/6.*constants.RHO_W
B_R=3.
ALPHA_R=130/np.sqrt(1000) # mm^0.5*s-1
BETA_R=0.5
D_MIN_R=0.2
D_MAX_R=8

# Compute constant integration factors (saves time since evaluation 
# of gamma function is done only once)
LAMBDA_FACTOR_R=A_R*N0_R*spe.gamma(1.+B_R+MU_R)
VEL_FACTOR_R=spe.gamma(MU_R+BETA_R+1)
NTOT_FACTOR_R=spe.gamma(MU_R+1)

# Vectorize the constant parameters (for rain, snow and graupel) in order to avoir recreating these arrays for every pixel
ALPHA_ALL=np.asarray([ALPHA_R, ALPHA_S, ALPHA_G],dtype='float32')
BETA_ALL=np.asarray([BETA_R, BETA_S, BETA_G],dtype='float32')
MU_ALL=np.asarray([MU_R, MU_S, MU_G],dtype='float32')

