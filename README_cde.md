CLASS: Cosmic Linear Anisotropy Solving System  {#mainpage}
==============================================


This is the code for the coupled vector dark energy model that includes both the background and the linear order perturbations.
----------------

The model has got nine parameters [s, b2, p2, beta ,Q,  q, Z_ini, Q_ini rho_vf_ini]. 

We have two options for beta: 1 or 0. 
beta=1 correspond to arXiv:1907.12216v2 while $beta = 0$ arXiv:2207.13682v1.
The .ini files for beta = 0 are missing.

We fix q in background.c if you want to change it, look for 'q_vf = 2p3_vf in background.c and perturbations.c and switch to
q_vf  =  pba->vf_parameters[5] .  

s, p2 and, Q are the parameters of the model.  

Q_ini and Z_ini are the initial condition for the dark energy perturbations.
----------------

To run an example with $Q = 0$, $p2 = 5$, and $s=0.2$  type 

./class ini_file_cde/s_02/Q_0/p_1.ini 

Taking into consideration that the parameter p is equal to p2/s 

Look at both ini_file_cde/s_02/ and ini_file_cde/s_1/  folders to see four different cases to execute the code with diverse values of Q (these correspond to 0, 0.2, -0.5, -1) and $s=0.2$ or $s=1$ respectively.

If you want to play with the values of p, you can see inside
cd  ini_file_cde/beta_1/s_02/Q_0/
cd  ini_file_cde/beta_1/s_02/Q_02/
cd  ini_file_cde/beta_1/s_02/Q_05/
cd  ini_file_cde/beta_1/s_02/Q_1/
cd  ini_file_cde/beta_1/s_1/Q_0/
cd  ini_file_cde/beta_1/s_1/Q_02/
cd  ini_file_cde/beta_1/s_1/Q_05/
cd  ini_file_cde/beta_1/s_1/Q_1/

Here, you will find .ini files with some of the following values of $p$: 5, 3, 2, 1.5, 1.1, 1.
The outputs will be saved in output_for_cde/


We have an option, in .ini files, to solve numerically a differential equation for dark matter:
''num_sol_cdm_vf = yes or no''

In ini_file_cde/beta_1/cdm_num you will find .ini files to execute Class solving numerically cdm. 
----------------

The file vector_field.ini can run the vector field model. In this, you can change freely the parameters of the model. 
----------------

If you want to run Class using dark energy as a vector field energy density, the gauge has to be 'Newtonian'
----------------


We modified the following files: input.h, background.h, perturbations.h, input.c, background.c, perturbations.c. All modifications are indexed by "_vf" 


-input.h 
 we added a new target in the variable 'target_names' and changed '_NUM_TARGETS_' from 6 to 7.  

-background.h 
we added all the vector field parameters in the structure background.

-perturbation.h 
we added all the dark energy perturbed sources and parameters in the structure perturbations.

-input.c
The following functions were modified to consider a new case ('Omega_vf') to make 'shooting': input_shooting, input_needs_shooting_for_target, input_find_root, input_get_guess, input_try_unknown_parameters.
Also, we wrote, in the function input_read_parameters_species, lines of code to permit Class to read the parameters related to the vector field. In the function input_default_params we added the default values for model's parameters.

-backgroun.c 
In background_functions we wrote the dark energy source. 
In background_indices we asigned a space in the background pointer (pba->) for the dark energy sources. 
In background_initial_conditions we fixed the initial conditions for the energy density of the vectot file. 
In background_derivs we solved the derivative of \rho_{DE} and \rho_{cdm}.
Some changes were made in the following functions as well, background_free_input, background_indices, background_solve, background_output_titles, background_output_budget

-perturbation.c 
In perturbations_output_data we selected the vector field sourses which will be in the output data.
In perturbations_output_titles we wrote the titles for the output of the vector field sources. 
In perturbations_indices were asigned a space for the new sources in the perturbations pointer (ptt->).
In perturbations_total_stress_energy we added the perturbed energy density and velocity for the vector field to 
In perturbations_sources again we included the vector field sources. 
In perturbations_print_variables we wrote the same as in the previous function.
In perturbations_derivs are writen the evolution equations for coupled vector dark energy.
Some changes were made in the following functions as well, perturbations_prepare_k_output, perturbations_vector_init, perturbations_initial_conditions