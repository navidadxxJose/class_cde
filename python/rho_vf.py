import matplotlib.pyplot as plt
from classy import Class
import pandas as pd 
from pylab import *
import numpy as np
MyClass = Class()
params = {'output':'',
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
	      }
MyClass.set(params)
MyClass.compute()
Bck_Quantity = MyClass.get_background()

plt.loglog(Bck_Quantity['z'],Bck_Quantity['(.)rho_vf'])

plt.show()
