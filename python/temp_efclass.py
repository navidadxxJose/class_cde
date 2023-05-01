from classy import Class
from pylab import *
import numpy as np


# Define your cosmology (what is not specified will be set to CLASS default parameters)
params = {
    'lensing' : 'yes',
    'accurate_lensing':0,
    'l_switch_limber':5.,
    'modes' : 's',
    'k_pivot' : 0.05,
    'omega_b' : 0.02237,
    'omega_cdm' : 0.1200,
    'ln10^{10}A_s' : 3.044, 
    'n_s': 0.9649, 
    'h' : 0.67,
    'tau_reio' : 0.0544,
    'm_ncdm' : 0.06,
    'N_ur' : 2.0328,
    'N_ncdm' : 1.,
    'deg_ncdm' : 1.,
    'T_ncdm':0.71611,
    'Omega_k' : 0.,
    'Omega_dcdmdr' : 0.0,
    'Omega_fld' : 0.0,
    'Omega_scf' : 0.0,
    'Omega_vf' : -1.0,
    'Omega_Lambda' : 0.,
    'output' : 'tCl,pCl,lCl,mPk,dTk,vTk',
    'k_output_values' : 1.0e-4,
    'gauge' : 'newtonian',
    'vf_parameters_1': 1.0,  
    'vf_parameters_2': 1.0,    
    'vf_parameters_3': 0.0,
    'vf_parameters_4': 0.0,
    'vf_parameters_5': 1.0,    
    'vf_parameters': '0.0, 0.0, 10.0',
    'vf_tuning_index' : 2,
    'num_sol_cdm_vf' : 'no',
    'l_max_scalars' : 2500,
    'format' : 'class'}

# Create an instance of the CLASS wrapper
cosmo = Class()

# Set the parameters to the cosmological code
cosmo.set(params)

# Run the whole code. Depending on your output, it will call the
# CLASS modules more or less fast. For instance, without any
# output asked, CLASS will only compute background quantities,
# thus running almost instantaneously.
# This is equivalent to the beginning of the `main` routine of CLASS,
# with all the struct_init() methods called.
cosmo.compute()

# Access the lensed cl until l=2000
cls = cosmo.lensed_cl(2000)

# Print on screen to see the output
print(cls['ell'])
data=np.loadtxt('Cl_vf__cl_lensed.dat.txt',unpack=True)
print(data[0])

# plot something with matplotlib...

#ell=arange(0,len(cls[0]),1)
#plot(ell,ell*(ell+1.)/2/pi*cls[0])
plot(cls['ell'],cls['ell']*(cls['ell']+1.)/2/pi*cls['tt'])
plot(data[0],data[1])
show()

#with open("../output/test_cl.dat") as f:
#    data = f.read()
#plot(data)
#show()


# Clean CLASS (the equivalent of the struct_free() in the `main`
# of CLASS. This step is primordial when running in a loop over different
# cosmologies, as you will saturate your memory very fast if you ommit
# it.
cosmo.struct_cleanup()

# If you want to change completely the cosmology, you should also
# clean the arguments, otherwise, if you are simply running on a loop
# of different values for the same parameters, this step is not needed
cosmo.empty()
