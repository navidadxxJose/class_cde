import matplotlib.pyplot as plt
from classy import Class
import pandas as pd 
from pylab import *
import numpy as np
MyClass = Class()
params = {'output':'tCl,pCl,lCl',
		  'T_cmb': 2.7255,
		  'omega_b': 0.02237,
		  'omega_cdm': 0.1200,
		  'N_ur':2.0328,
		  'Omega_fld':0.0,
		  'Omega_scf':0.0,
		  'Omega_Lambda':0.0,
		  'Omega_vf':-1.0,
		  'vf_parameters':'1.0, -1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 10.0',
		  'vf_tuning_index':8,
		  'num_sol_cdm_vf': 'no',		  
		  'h':0.67810, 
		  'n_s': 0.9649, 
		  'A_s':2.100549e-09, 
		  'modes':'s',
		  'ic': 'ad',
		  'gauge':'newtonian',
		  'lensing':'yes',
		  'l_max_scalars':2500,
#		  'P_k_max_h/Mpc':1.
	      }
MyClass.set(params)
MyClass.compute()
Bck_Quantity = MyClass.get_background()

#plt.loglog(Bck_Quantity['z'],Bck_Quantity['(.)rho_vf'])

######################
#Myclass.density_cl
'''dataQ0 = pd.read_csv('/Users/Cosmology/projects/repositores/class_cde_background/output/vector_field_00_background.dat', header = 3, delim_whitespace = True) #data obtained by run Class using gcc. You need to run Class vector_filed.ini
zQ0  = dataQ0.iloc[:,0] 
rhoDEQ0 = dataQ0.iloc[:,13]
HQ0 = dataQ0.iloc[:,3]
plt.loglog(Bck_Quantity['z'], Bck_Quantity['(.)rho_cdm'])
plt.loglog(Bck_Quantity['z'],Bck_Quantity['(.)rho_vf']-rhoDEQ0)
plt.loglog(Bck_Quantity['z'],Bck_Quantity['H [1/Mpc]']-HQ0) '''
######################################

'''dataclQ0 = pd.read_csv('/Users/Cosmology/projects/repositores/class_cde_background/output/copia_de_vector_field_00_cl_lensed.dat', delim_whitespace = True)
lQ0  = dataclQ0.iloc[:,0]
TTQ0 = dataclQ0.iloc[:,1]

#cls = MyClass.lensed_cl()
#ell=arange(0,len(cls['tt']),1)
#ell=arange(2,2501,1)
#plt.plot(ell,ell*(ell+1.)/2/pi*cls['tt'])
plt.plot(ell,cls['tt']-TTQ0). '''
#print(cls['tt'])
######################################
cls = MyClass.lensed_cl()
print(cls['tt'])
plt.show()
