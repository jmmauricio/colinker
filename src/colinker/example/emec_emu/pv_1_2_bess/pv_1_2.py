import numpy as np
import scipy.sparse as sspa
import cffi
import solver_ini,solver_run

dae_file_mode = 'local'

ffi = cffi.FFI()

sparse = False


if sparse:
    sp_jac_ini_xy_eval = jacs.lib.sp_jac_ini_xy_eval
    sp_jac_ini_up_eval = jacs.lib.sp_jac_ini_up_eval
    sp_jac_ini_num_eval = jacs.lib.sp_jac_ini_num_eval


if sparse:
    sp_jac_run_xy_eval = jacs.lib.sp_jac_run_xy_eval
    sp_jac_run_up_eval = jacs.lib.sp_jac_run_up_eval
    sp_jac_run_num_eval = jacs.lib.sp_jac_run_num_eval


if sparse:
    sp_jac_trap_xy_eval= jacs.lib.sp_jac_trap_xy_eval            
    sp_jac_trap_up_eval= jacs.lib.sp_jac_trap_up_eval        
    sp_jac_trap_num_eval= jacs.lib.sp_jac_trap_num_eval





import json

sin = np.sin
cos = np.cos
atan2 = np.arctan2
sqrt = np.sqrt 
sign = np.sign 
exp = np.exp


class model: 

    def __init__(self): 
        
        self.matrices_folder = 'build'
        self.sparse = True
        self.dae_file_mode = 'local'
        self.t_end = 10.000000 
        self.Dt = 0.0010000 
        self.decimation = 10.000000 
        self.itol = 1e-6 
        self.Dt_max = 0.001000 
        self.Dt_min = 0.001000 
        self.solvern = 5 
        self.imax = 100 
        self.N_x = 14
        self.N_y = 42 
        self.N_z = 37 
        self.N_store = 100000 
        self.params_list = ['S_base', 'g_POI_GRID', 'b_POI_GRID', 'bs_POI_GRID', 'g_BESS_POI_MV', 'b_BESS_POI_MV', 'bs_BESS_POI_MV', 'g_PV_POI_MV', 'b_PV_POI_MV', 'bs_PV_POI_MV', 'g_LV0101_MV0101', 'b_LV0101_MV0101', 'bs_LV0101_MV0101', 'g_MV0101_PV', 'b_MV0101_PV', 'bs_MV0101_PV', 'g_LV0102_MV0102', 'b_LV0102_MV0102', 'bs_LV0102_MV0102', 'g_MV0102_MV0101', 'b_MV0102_MV0101', 'bs_MV0102_MV0101', 'g_cc_POI_MV_POI', 'b_cc_POI_MV_POI', 'tap_POI_MV_POI', 'ang_POI_MV_POI', 'U_POI_MV_n', 'U_PV_n', 'U_POI_n', 'U_GRID_n', 'U_BESS_n', 'U_LV0101_n', 'U_MV0101_n', 'U_LV0102_n', 'U_MV0102_n', 'K_p_BESS', 'K_i_BESS', 'soc_min_BESS', 'soc_max_BESS', 'S_n_BESS', 'E_kWh_BESS', 'A_loss_BESS', 'B_loss_BESS', 'C_loss_BESS', 'R_bat_BESS', 'S_n_GRID', 'F_n_GRID', 'X_v_GRID', 'R_v_GRID', 'K_delta_GRID', 'K_alpha_GRID', 'K_rocov_GRID', 'I_sc_LV0101', 'I_mp_LV0101', 'V_mp_LV0101', 'V_oc_LV0101', 'N_pv_s_LV0101', 'N_pv_p_LV0101', 'K_vt_LV0101', 'K_it_LV0101', 'v_lvrt_LV0101', 'T_lp1p_LV0101', 'T_lp2p_LV0101', 'T_lp1q_LV0101', 'T_lp2q_LV0101', 'PRampUp_LV0101', 'PRampDown_LV0101', 'QRampUp_LV0101', 'QRampDown_LV0101', 'S_n_LV0101', 'F_n_LV0101', 'U_n_LV0101', 'X_s_LV0101', 'R_s_LV0101', 'I_sc_LV0102', 'I_mp_LV0102', 'V_mp_LV0102', 'V_oc_LV0102', 'N_pv_s_LV0102', 'N_pv_p_LV0102', 'K_vt_LV0102', 'K_it_LV0102', 'v_lvrt_LV0102', 'T_lp1p_LV0102', 'T_lp2p_LV0102', 'T_lp1q_LV0102', 'T_lp2q_LV0102', 'PRampUp_LV0102', 'PRampDown_LV0102', 'QRampUp_LV0102', 'QRampDown_LV0102', 'S_n_LV0102', 'F_n_LV0102', 'U_n_LV0102', 'X_s_LV0102', 'R_s_LV0102', 'K_p_agc', 'K_i_agc', 'K_xif'] 
        self.params_values_list  = [100000000.0, 0.0, -0.32, 0.0, 0.0, -0.23999999999999996, 0.0, 0.0, -0.4, 0.0, 0.04615384615384615, -0.23076923076923075, 0.0, 1.2, -1.2, 0.0, 0.04615384615384615, -0.23076923076923075, 0.0, 0.6, -0.6, 0.0, 0.0, -0.4, 1.0, 0.0, 20000.0, 20000.0, 132000, 132000, 690.0, 400.0, 20000.0, 400.0, 20000.0, 1e-06, 1e-06, 0.0, 1.0, 1000000.0, 250, 0.0001, 0.0, 0.0001, 0.0, 1000000000.0, 50.0, 0.001, 0.0, 0.001, 1e-06, 1e-06, 8, 3.56, 33.7, 42.1, 25, 250, -0.16, 0.065, 0.8, 0.1, 0.1, 0.1, 0.1, 2.5, -2.5, 2.5, -2.5, 1000000.0, 50.0, 400.0, 0.1, 0.0001, 8, 3.56, 33.7, 42.1, 25, 250, -0.16, 0.065, 0.8, 0.1, 0.1, 0.1, 0.1, 2.5, -2.5, 2.5, -2.5, 1000000.0, 50.0, 400.0, 0.1, 0.0001, 0.0, 0.0, 0.01] 
        self.inputs_ini_list = ['P_POI_MV', 'Q_POI_MV', 'P_PV', 'Q_PV', 'P_POI', 'Q_POI', 'P_GRID', 'Q_GRID', 'P_BESS', 'Q_BESS', 'P_LV0101', 'Q_LV0101', 'P_MV0101', 'Q_MV0101', 'P_LV0102', 'Q_LV0102', 'P_MV0102', 'Q_MV0102', 'p_s_ref_BESS', 'q_s_ref_BESS', 'soc_ref_BESS', 'alpha_GRID', 'v_ref_GRID', 'omega_ref_GRID', 'delta_ref_GRID', 'phi_GRID', 'rocov_GRID', 'irrad_LV0101', 'temp_deg_LV0101', 'lvrt_ext_LV0101', 'ramp_enable_LV0101', 'p_s_ppc_LV0101', 'q_s_ppc_LV0101', 'i_sa_ref_LV0101', 'i_sr_ref_LV0101', 'irrad_LV0102', 'temp_deg_LV0102', 'lvrt_ext_LV0102', 'ramp_enable_LV0102', 'p_s_ppc_LV0102', 'q_s_ppc_LV0102', 'i_sa_ref_LV0102', 'i_sr_ref_LV0102'] 
        self.inputs_ini_values_list  = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0, 1.0, 1.0, 0.0, 0.0, 0.0, 1000.0, 25.0, 0.0, 1e-05, 1.5, 0.0, 0.0, 0.0, 1000.0, 25.0, 0.0, 1e-05, 1.5, 0.0, 0.0, 0.0] 
        self.inputs_run_list = ['P_POI_MV', 'Q_POI_MV', 'P_PV', 'Q_PV', 'P_POI', 'Q_POI', 'P_GRID', 'Q_GRID', 'P_BESS', 'Q_BESS', 'P_LV0101', 'Q_LV0101', 'P_MV0101', 'Q_MV0101', 'P_LV0102', 'Q_LV0102', 'P_MV0102', 'Q_MV0102', 'p_s_ref_BESS', 'q_s_ref_BESS', 'soc_ref_BESS', 'alpha_GRID', 'v_ref_GRID', 'omega_ref_GRID', 'delta_ref_GRID', 'phi_GRID', 'rocov_GRID', 'irrad_LV0101', 'temp_deg_LV0101', 'lvrt_ext_LV0101', 'ramp_enable_LV0101', 'p_s_ppc_LV0101', 'q_s_ppc_LV0101', 'i_sa_ref_LV0101', 'i_sr_ref_LV0101', 'irrad_LV0102', 'temp_deg_LV0102', 'lvrt_ext_LV0102', 'ramp_enable_LV0102', 'p_s_ppc_LV0102', 'q_s_ppc_LV0102', 'i_sa_ref_LV0102', 'i_sr_ref_LV0102'] 
        self.inputs_run_values_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0, 1.0, 1.0, 0.0, 0.0, 0.0, 1000.0, 25.0, 0.0, 1.0, 1.5, 0.0, 0.0, 0.0, 1000.0, 25.0, 0.0, 1.0, 1.5, 0.0, 0.0, 0.0] 
        self.outputs_list = ['V_POI_MV', 'V_PV', 'V_POI', 'V_GRID', 'V_BESS', 'V_LV0101', 'V_MV0101', 'V_LV0102', 'V_MV0102', 'p_line_POI_GRID', 'q_line_POI_GRID', 'p_line_GRID_POI', 'q_line_GRID_POI', 'p_line_BESS_POI_MV', 'q_line_BESS_POI_MV', 'p_line_POI_MV_BESS', 'q_line_POI_MV_BESS', 'p_line_PV_POI_MV', 'q_line_PV_POI_MV', 'p_line_POI_MV_PV', 'q_line_POI_MV_PV', 'p_loss_BESS', 'i_s_BESS', 'e_BESS', 'i_dc_BESS', 'p_s_BESS', 'q_s_BESS', 'alpha_GRID', 'Dv_GRID', 'm_ref_LV0101', 'v_sd_LV0101', 'v_sq_LV0101', 'lvrt_LV0101', 'm_ref_LV0102', 'v_sd_LV0102', 'v_sq_LV0102', 'lvrt_LV0102'] 
        self.x_list = ['soc_BESS', 'xi_soc_BESS', 'delta_GRID', 'Domega_GRID', 'Dv_GRID', 'x_p_lp1_LV0101', 'x_p_lp2_LV0101', 'x_q_lp1_LV0101', 'x_q_lp2_LV0101', 'x_p_lp1_LV0102', 'x_p_lp2_LV0102', 'x_q_lp1_LV0102', 'x_q_lp2_LV0102', 'xi_freq'] 
        self.y_run_list = ['V_POI_MV', 'theta_POI_MV', 'V_PV', 'theta_PV', 'V_POI', 'theta_POI', 'V_GRID', 'theta_GRID', 'V_BESS', 'theta_BESS', 'V_LV0101', 'theta_LV0101', 'V_MV0101', 'theta_MV0101', 'V_LV0102', 'theta_LV0102', 'V_MV0102', 'theta_MV0102', 'p_dc_BESS', 'i_dc_BESS', 'v_dc_BESS', 'omega_GRID', 'i_d_GRID', 'i_q_GRID', 'p_s_GRID', 'q_s_GRID', 'v_dc_LV0101', 'i_sq_ref_LV0101', 'i_sd_ref_LV0101', 'i_sr_LV0101', 'i_si_LV0101', 'p_s_LV0101', 'q_s_LV0101', 'v_dc_LV0102', 'i_sq_ref_LV0102', 'i_sd_ref_LV0102', 'i_sr_LV0102', 'i_si_LV0102', 'p_s_LV0102', 'q_s_LV0102', 'omega_coi', 'p_agc'] 
        self.xy_list = self.x_list + self.y_run_list 
        self.y_ini_list = ['V_POI_MV', 'theta_POI_MV', 'V_PV', 'theta_PV', 'V_POI', 'theta_POI', 'V_GRID', 'theta_GRID', 'V_BESS', 'theta_BESS', 'V_LV0101', 'theta_LV0101', 'V_MV0101', 'theta_MV0101', 'V_LV0102', 'theta_LV0102', 'V_MV0102', 'theta_MV0102', 'p_dc_BESS', 'i_dc_BESS', 'v_dc_BESS', 'omega_GRID', 'i_d_GRID', 'i_q_GRID', 'p_s_GRID', 'q_s_GRID', 'v_dc_LV0101', 'i_sq_ref_LV0101', 'i_sd_ref_LV0101', 'i_sr_LV0101', 'i_si_LV0101', 'p_s_LV0101', 'q_s_LV0101', 'v_dc_LV0102', 'i_sq_ref_LV0102', 'i_sd_ref_LV0102', 'i_sr_LV0102', 'i_si_LV0102', 'p_s_LV0102', 'q_s_LV0102', 'omega_coi', 'p_agc'] 
        self.xy_ini_list = self.x_list + self.y_ini_list 
        self.t = 0.0
        self.it = 0
        self.it_store = 0
        self.xy_prev = np.zeros((self.N_x+self.N_y,1))
        self.initialization_tol = 1e-6
        self.N_u = len(self.inputs_run_list) 
        self.sopt_root_method='hybr'
        self.sopt_root_jac=True
        self.u_ini_list = self.inputs_ini_list
        self.u_ini_values_list = self.inputs_ini_values_list
        self.u_run_list = self.inputs_run_list
        self.u_run_values_list = self.inputs_run_values_list
        self.N_u = len(self.u_run_list)
        self.u_ini = np.array(self.inputs_ini_values_list, dtype=np.float64)
        self.p = np.array(self.params_values_list, dtype=np.float64)
        self.xy_0 = np.zeros((self.N_x+self.N_y,),dtype=np.float64)
        self.xy = np.zeros((self.N_x+self.N_y,),dtype=np.float64)
        self.z = np.zeros((self.N_z,),dtype=np.float64)
        
        # numerical elements of jacobians computing:
        x = self.xy[:self.N_x]
        y = self.xy[self.N_x:]
        
        self.yini2urun = list(set(self.u_run_list).intersection(set(self.y_ini_list)))
        self.uini2yrun = list(set(self.y_run_list).intersection(set(self.u_ini_list)))
        self.Time = np.zeros(self.N_store)
        self.X = np.zeros((self.N_store,self.N_x))
        self.Y = np.zeros((self.N_store,self.N_y))
        self.Z = np.zeros((self.N_store,self.N_z))
        self.iters = np.zeros(self.N_store) 
        self.u_run = np.array(self.u_run_values_list,dtype=np.float64)
 
        ## jac_ini
        if self.sparse:
            self.sp_jac_ini_indices, self.sp_jac_ini_indptr, self.sp_jac_ini_nia, self.sp_jac_ini_nja = sp_jac_ini_vectors()
            self.sp_jac_ini_indices = np.array(self.sp_jac_ini_indices,dtype=np.int32)    
            self.sp_jac_ini_indptr = np.array(self.sp_jac_ini_indptr,dtype=np.int32)    
            self.sp_jac_ini_data = np.array(self.sp_jac_ini_indices,dtype=np.float64)            

        ## jac_run
        if self.sparse:
            self.sp_jac_run_indices, self.sp_jac_run_indptr, self.sp_jac_run_nia, self.sp_jac_run_nja = sp_jac_run_vectors()
            self.sp_jac_run_indices = np.array(self.sp_jac_run_indices,dtype=np.int32)    
            self.sp_jac_run_indptr = np.array(self.sp_jac_run_indptr,dtype=np.int32)    
            self.sp_jac_run_data = np.array(self.sp_jac_run_indices,dtype=np.float64)

        ## jac_trap
        if self.sparse:
            self.sp_jac_trap_indices, self.sp_jac_trap_indptr, self.sp_jac_trap_nia, self.sp_jac_trap_nja = sp_jac_trap_vectors()
            self.sp_jac_trap_indices = np.array(self.sp_jac_trap_indices,dtype=np.int32)    
            self.sp_jac_trap_indptr = np.array(self.sp_jac_trap_indptr,dtype=np.int32)    
            self.sp_jac_trap_data = np.array(self.sp_jac_trap_indices,dtype=np.float64)
        
        self.max_it,self.itol,self.store = 50,1e-8,1 
        self.lmax_it,self.ltol,self.ldamp= 50,1e-8,1.0
        self.mode = 0 

        self.lmax_it_ini,self.ltol_ini,self.ldamp_ini=50,1e-8,1.0

        #self.sp_Fu_run = sspa.load_npz(f'./{self.matrices_folder}/pv_1_2_Fu_run_num.npz')
        #self.sp_Gu_run = sspa.load_npz(f'./{self.matrices_folder}/pv_1_2_Gu_run_num.npz')
        #self.sp_Hx_run = sspa.load_npz(f'./{self.matrices_folder}/pv_1_2_Hx_run_num.npz')
        #self.sp_Hy_run = sspa.load_npz(f'./{self.matrices_folder}/pv_1_2_Hy_run_num.npz')
        #self.sp_Hu_run = sspa.load_npz(f'./{self.matrices_folder}/pv_1_2_Hu_run_num.npz')        
        
        self.ss_solver = 2
        self.lsolver = 2

        # ini initialization
        self.inidblparams = np.zeros(10,dtype=np.float64)
        self.iniintparams = np.zeros(10,dtype=np.int32)

        # run initialization
        self.rundblparams = np.zeros(10,dtype=np.float64)
        self.runintparams = np.zeros(10,dtype=np.int32)

        self.xy = self.xy_0
        self.pt_ini = np.zeros(64,dtype=np.int32)
        xy = self.xy
        x = xy[:self.N_x]
        y_ini = xy[self.N_x:]
        Dxy = np.zeros((self.N_x+self.N_y),dtype=np.float64)
        
        self.f = np.zeros((self.N_x),dtype=np.float64)
        self.g = np.zeros((self.N_y),dtype=np.float64)
        self.fg = np.zeros((self.N_x+self.N_y),dtype=np.float64)


        self.p_pt_ini =solver_ini.ffi.cast('int *', self.pt_ini.ctypes.data)
        self.p_sp_jac_ini = solver_ini.ffi.cast('double *', self.sp_jac_ini_data.ctypes.data)
        self.p_indptr = solver_ini.ffi.cast('int *', self.sp_jac_ini_indptr.ctypes.data)
        self.p_indices = solver_ini.ffi.cast('int *', self.sp_jac_ini_indices.ctypes.data)
        self.p_x = solver_ini.ffi.cast('double *', x.ctypes.data)
        self.p_y_ini = solver_ini.ffi.cast('double *', y_ini.ctypes.data)
        self.p_xy = solver_ini.ffi.cast('double *', self.xy.ctypes.data)
        self.p_Dxy = solver_ini.ffi.cast('double *', Dxy.ctypes.data)
        self.p_u_ini = solver_ini.ffi.cast('double *', self.u_ini.ctypes.data)
        self.p_p = solver_ini.ffi.cast('double *', self.p.ctypes.data)
        self.p_z = solver_ini.ffi.cast('double *', self.z.ctypes.data)
        self.p_inidblparams = solver_ini.ffi.cast('double *', self.inidblparams.ctypes.data)
        self.p_iniintparams = solver_ini.ffi.cast('int *', self.iniintparams.ctypes.data)
        self.p_f = solver_ini.ffi.cast('double *', self.f.ctypes.data)
        self.p_g = solver_ini.ffi.cast('double *', self.g.ctypes.data)
        self.p_fg = solver_ini.ffi.cast('double *', self.fg.ctypes.data)

        self.pt_run = np.zeros(64,dtype=np.int32)

        self.p_pt_run =solver_ini.ffi.cast('int *', self.pt_run.ctypes.data)

        self.X = np.zeros((100_000*self.N_x))
        self.Y = np.zeros((100_000*self.N_y))
        self.Z = np.zeros((100_000*self.N_z))
        self.Time = np.zeros((100_000))
        self.its = np.array([0],dtype=np.int32)

    # def update(self):

    #     self.Time = np.zeros(self.N_store)
    #     self.X = np.zeros((self.N_store,self.N_x))
    #     self.Y = np.zeros((self.N_store,self.N_y))
    #     self.Z = np.zeros((self.N_store,self.N_z))
    #     self.iters = np.zeros(self.N_store)
    
    def jac_run_eval(self):
        de_jac_run_eval(self.jac_run,self.x,self.y_run,self.u_run,self.p,self.Dt)
      
    def post_run_checker(self):

        self.N_iters = self.runintparams[2]  # number of iterations done
        self.N_mkl_factorizations = self.runintparams[3]
        self.N_mkl_resets = self.runintparams[4]
        self.pt_run_sum = np.sum(self.pt_run) # this variable should be 0

    def run(self,t_end,up_dict):

        for item in up_dict:
            self.set_value(item,up_dict[item])
            
        t = self.t
        it = self.it
        it_store = self.it_store
        xy = self.xy
        u = self.u_run
        z = self.z

        pt = np.zeros(64,dtype=np.int32)
        xy = self.xy
        x = xy[:self.N_x]
        y_run = xy[self.N_x:]

        p_sp_jac_trap = solver_run.ffi.cast('double *', self.sp_jac_trap_data.ctypes.data)
        p_indptr = solver_run.ffi.cast('int *', self.sp_jac_trap_indptr.ctypes.data)
        p_indices = solver_run.ffi.cast('int *', self.sp_jac_trap_indices.ctypes.data)
        p_x = solver_run.ffi.cast('double *', x.ctypes.data)
        p_y_run = solver_run.ffi.cast('double *', y_run.ctypes.data)
        p_xy = solver_run.ffi.cast('double *', self.xy.ctypes.data)
        p_u_run = solver_run.ffi.cast('double *', self.u_run.ctypes.data)
        p_z = solver_run.ffi.cast('double *', self.z.ctypes.data)
        p_dblparams = solver_run.ffi.cast('double *', self.rundblparams.ctypes.data)
        p_intparams = solver_run.ffi.cast('int *', self.runintparams.ctypes.data)
        p_x = solver_run.ffi.cast('double *', x.ctypes.data)
        p_X = solver_run.ffi.cast('double *', self.X.ctypes.data)
        p_Y = solver_run.ffi.cast('double *', self.Y.ctypes.data)
        p_Z = solver_run.ffi.cast('double *', self.Z.ctypes.data)
        p_Time = solver_run.ffi.cast('double *', self.Time.ctypes.data)
        p_its = solver_run.ffi.cast('int *', self.its.ctypes.data)
        p_p = solver_run.ffi.cast('double *', self.p.ctypes.data)
        N_x = self.N_x
        N_y = self.N_y
        max_it = self.max_it
        itol = self.itol
        max_it = 5
        itol = 1e-8

        solver_run.lib.run(self.p_pt_run, t, t_end,p_sp_jac_trap, p_indptr,p_indices,p_x,p_y_run,p_xy,p_u_run,p_p,N_x,N_y, max_it, itol, p_its, self.Dt, p_z,p_dblparams, p_intparams, p_Time, p_X, p_Y, p_Z, self.N_z, self.N_store)


        self.t = self.rundblparams[0]
        self.it = it
        self.it_store = self.its[0]
        self.xy = xy
        self.z = z

    def step(self,t_end,up_dict):

        for item in up_dict:
            self.set_value(item,up_dict[item])
            
        t = self.t
        it = self.it
        it_store = self.it_store
        xy = self.xy
        u = self.u_run
        z = self.z

        pt = np.zeros(64,dtype=np.int32)
        xy = self.xy
        x = xy[:self.N_x]
        y_run = xy[self.N_x:]

        p_sp_jac_trap = solver_run.ffi.cast('double *', self.sp_jac_trap_data.ctypes.data)
        p_indptr = solver_run.ffi.cast('int *', self.sp_jac_trap_indptr.ctypes.data)
        p_indices = solver_run.ffi.cast('int *', self.sp_jac_trap_indices.ctypes.data)
        p_x = solver_run.ffi.cast('double *', x.ctypes.data)
        p_y_run = solver_run.ffi.cast('double *', y_run.ctypes.data)
        p_xy = solver_run.ffi.cast('double *', self.xy.ctypes.data)
        p_u_run = solver_run.ffi.cast('double *', self.u_run.ctypes.data)
        p_z = solver_run.ffi.cast('double *', self.z.ctypes.data)
        p_dblparams = solver_run.ffi.cast('double *', self.rundblparams.ctypes.data)
        p_intparams = solver_run.ffi.cast('int *', self.runintparams.ctypes.data)
        p_x = solver_run.ffi.cast('double *', x.ctypes.data)
        p_X = solver_run.ffi.cast('double *', self.X.ctypes.data)
        p_Y = solver_run.ffi.cast('double *', self.Y.ctypes.data)
        p_Z = solver_run.ffi.cast('double *', self.Z.ctypes.data)
        p_Time = solver_run.ffi.cast('double *', self.Time.ctypes.data)
        p_its = solver_run.ffi.cast('int *', self.its.ctypes.data)
        p_p = solver_run.ffi.cast('double *', self.p.ctypes.data)
        N_x = self.N_x
        N_y = self.N_y
        max_it = self.max_it
        itol = self.itol
        itol = 1e-8

        solver_run.lib.step3(self.p_pt_run, t, t_end,p_sp_jac_trap, p_indptr,p_indices,p_x,p_y_run,p_xy,p_u_run,p_p,N_x,N_y, max_it, itol, p_its, self.Dt, p_z,p_dblparams, p_intparams, p_Time, p_X, p_Y, p_Z, self.N_z, self.N_store)

        self.t = self.rundblparams[0]
        self.it = it
        self.it_store = self.its[0]
        self.xy = xy
        self.z = z
        self.it_max = self.runintparams[5]
        
    def post(self):
        
        self.Time = self.Time[:self.its[0]].reshape(self.its[0],1)
        self.X = self.X[:self.its[0]*self.N_x].reshape(self.its[0],self.N_x)
        self.Y = self.Y[:self.its[0]*self.N_y].reshape(self.its[0],self.N_y)
        self.Z = self.Z[:self.its[0]*self.N_z].reshape(self.its[0],self.N_z)

        
    def ini2run(self):
        
        ## y_ini to y_run
        self.y_ini = self.xy_ini[self.N_x:]
        self.y_run = np.copy(self.y_ini)
        
        ## y_ini to u_run
        for item in self.yini2urun:
            self.u_run[self.u_run_list.index(item)] = self.y_ini[self.y_ini_list.index(item)]
                
        ## u_ini to y_run
        for item in self.uini2yrun:
            self.y_run[self.y_run_list.index(item)] = self.u_ini[self.u_ini_list.index(item)]
            
        
        self.x = self.xy_ini[:self.N_x]
        self.xy[:self.N_x] = self.x
        self.xy[self.N_x:] = self.y_run        

    def get_value(self,name):
        
        if name in self.inputs_run_list:
            value = self.u_run[self.inputs_run_list.index(name)]
            return value
            
        if name in self.x_list:
            idx = self.x_list.index(name)
            value = self.xy[idx]
            return value
            
        if name in self.y_run_list:
            idy = self.y_run_list.index(name)
            value = self.xy[self.N_x+idy]
            return value
        
        if name in self.params_list:
            idp = self.params_list.index(name)
            value = self.p[idp]
            return value
            
        if name in self.outputs_list:
            idz = self.outputs_list.index(name)
            value = self.z[idz]
            return value

    def get_values(self,name):
        if name in self.x_list:
            values = self.X[:,self.x_list.index(name)]
        if name in self.y_run_list:
            values = self.Y[:,self.y_run_list.index(name)]
        if name in self.outputs_list:
            values = self.Z[:,self.outputs_list.index(name)]
                        
        return values

    def get_mvalue(self,names):
        '''

        Parameters
        ----------
        names : list
            list of variables names to return each value.

        Returns
        -------
        mvalue : TYPE
            list of value of each variable.

        '''
        mvalue = []
        for name in names:
            mvalue += [self.get_value(name)]
                        
        return mvalue
    
    def set_value(self,name_,value):
        if name_ in self.inputs_ini_list or name_ in self.inputs_run_list:
            if name_ in self.inputs_ini_list:
                self.u_ini[self.inputs_ini_list.index(name_)] = value
            if name_ in self.inputs_run_list:
                self.u_run[self.inputs_run_list.index(name_)] = value
            return
        elif name_ in self.params_list:
            self.p[self.params_list.index(name_)] = value
            return
        else:
            print(f'Input or parameter {name_} not found.')
 
    def report_x(self,value_format='5.2f'):
        for item in self.x_list:
            print(f'{item:5s} = {self.get_value(item):{value_format}}')

    def report_y(self,value_format='5.2f'):
        for item in self.y_run_list:
            print(f'{item:5s} = {self.get_value(item):{value_format}}')
            
    def report_u(self,value_format='5.2f'):
        for item in self.inputs_run_list:
            print(f'{item:5s} ={self.get_value(item):{value_format}}')

    def report_z(self,value_format='5.2f'):
        for item in self.outputs_list:
            print(f'{item:5s} = {self.get_value(item):{value_format}}')

    def report_params(self,value_format='5.2f'):
        for item in self.params_list:
            print(f'{item:5s} ={self.get_value(item):{value_format}}')


    def post_ini_checker(self):

        self.N_iters = self.iniintparams[2]  # number of iterations done
        self.N_mkl_factorizations = self.iniintparams[3]
        self.N_mkl_resets = self.iniintparams[4]
        self.pt_ini_sum = np.sum(self.pt_ini) # this variable should be 0


    def ini(self,up_dict,xy_0={}):
        '''
        Find the steady state of the initialization problem:
            
               0 = f(x,y,u,p) 
               0 = g(x,y,u,p) 

        Parameters
        ----------
        up_dict : dict
            dictionary with all the parameters p and inputs u new values.
        xy_0: if scalar, all the x and y values initial guess are set to the scalar.
              if dict, the initial guesses are applied for the x and y that are in the dictionary
              if string, the initial guess considers a json file with the x and y names and their initial values

        Returns
        -------
        mvalue : TYPE
            list of value of each variable.

        '''
        
        self.it = 0
        self.it_store = 0
        self.t = 0.0
    
        for item in up_dict:
            self.set_value(item,up_dict[item])
            
        if type(xy_0) == dict:
            xy_0_dict = xy_0
            self.dict2xy0(xy_0_dict)
            
        if type(xy_0) == str:
            if xy_0 == 'eval':
                N_x = self.N_x
                self.xy_0_new = np.copy(self.xy_0)*0
                xy0_eval(self.xy_0_new[:N_x],self.xy_0_new[N_x:],self.u_ini,self.p)
                self.xy_0_evaluated = np.copy(self.xy_0_new)
                self.xy_0 = np.copy(self.xy_0_new)
            else:
                self.load_xy_0(file_name = xy_0)
                
        if type(xy_0) == float or type(xy_0) == int:
            self.xy_0 = np.ones(self.N_x+self.N_y,dtype=np.float64)*xy_0

        self.f = np.zeros((self.N_x),dtype=np.float64)
        self.g = np.zeros((self.N_y),dtype=np.float64)
        self.fg = np.zeros((self.N_x+self.N_y),dtype=np.float64)

        xy = self.xy_0
        x = xy[:self.N_x]
        y_ini = xy[self.N_x:]
        Dxy = np.zeros((self.N_x+self.N_y),dtype=np.float64)
        self.p_pt_ini =solver_ini.ffi.cast('int *', self.pt_ini.ctypes.data)
        self.p_sp_jac_ini = solver_ini.ffi.cast('double *', self.sp_jac_ini_data.ctypes.data)
        self.p_indptr = solver_ini.ffi.cast('int *', self.sp_jac_ini_indptr.ctypes.data)
        self.p_indices = solver_ini.ffi.cast('int *', self.sp_jac_ini_indices.ctypes.data)
        self.p_x = solver_ini.ffi.cast('double *', x.ctypes.data)
        self.p_y_ini = solver_ini.ffi.cast('double *', y_ini.ctypes.data)
        self.p_xy = solver_ini.ffi.cast('double *', self.xy.ctypes.data)
        self.p_Dxy = solver_ini.ffi.cast('double *', Dxy.ctypes.data)
        self.p_u_ini = solver_ini.ffi.cast('double *', self.u_ini.ctypes.data)
        self.p_p = solver_ini.ffi.cast('double *', self.p.ctypes.data)
        self.p_z = solver_ini.ffi.cast('double *', self.z.ctypes.data)
        self.p_inidblparams = solver_ini.ffi.cast('double *', self.inidblparams.ctypes.data)
        self.p_iniintparams = solver_ini.ffi.cast('int *', self.iniintparams.ctypes.data)
        self.p_f = solver_ini.ffi.cast('double *', self.f.ctypes.data)
        self.p_g = solver_ini.ffi.cast('double *', self.g.ctypes.data)
        self.p_fg = solver_ini.ffi.cast('double *', self.fg.ctypes.data)


        solver_ini.lib.ini(self.p_pt_ini,
                            self.p_sp_jac_ini,
                            self.p_indptr,
                            self.p_indices,
                            self.p_x,
                            self.p_y_ini,
                            self.p_xy,
                            self.p_Dxy,
                            self.p_u_ini,
                            self.p_p,
                            self.N_x,
                            self.N_y,
                            self.max_it,
                            self.itol,
                            self.p_z,
                            self.p_inidblparams,
                            self.p_iniintparams,
                            self.p_f,
                            self.p_g,
                            self.p_fg)
        
        self.post_ini_checker()
        
        if self.iniintparams[2] < self.max_it-1:
            
            self.xy_ini = self.xy
            self.N_iters = self.iniintparams[2]

            self.ini2run()
            
            self.ini_convergence = True
            
        if self.iniintparams[2] >= self.max_it-1:
            print(f'Maximum number of iterations (max_it = {self.max_it}) reached without convergence.')
            self.ini_convergence = False
            
        return self.ini_convergence
            
        
    def dict2xy0(self,xy_0_dict):
    
        for item in xy_0_dict:
            if item in self.x_list:
                self.xy_0[self.x_list.index(item)] = xy_0_dict[item]
            if item in self.y_ini_list:
                self.xy_0[self.y_ini_list.index(item) + self.N_x] = xy_0_dict[item]
        
    
    def save_xy_0(self,file_name = 'xy_0.json'):
        xy_0_dict = {}
        for item in self.x_list:
            xy_0_dict.update({item:self.get_value(item)})
        for item in self.y_ini_list:
            xy_0_dict.update({item:self.get_value(item)})
    
        xy_0_str = json.dumps(xy_0_dict, indent=4)
        with open(file_name,'w') as fobj:
            fobj.write(xy_0_str)
    
    def load_xy_0(self,file_name = 'xy_0.json'):
        with open(file_name) as fobj:
            xy_0_str = fobj.read()
        xy_0_dict = json.loads(xy_0_str)
    
        for item in xy_0_dict:
            if item in self.x_list:
                self.xy_0[self.x_list.index(item)] = xy_0_dict[item]
            if item in self.y_ini_list:
                self.xy_0[self.y_ini_list.index(item)+self.N_x] = xy_0_dict[item]            

    def load_params(self,data_input):
    
        if type(data_input) == str:
            json_file = data_input
            self.json_file = json_file
            self.json_data = open(json_file).read().replace("'",'"')
            data = json.loads(self.json_data)
        elif type(data_input) == dict:
            data = data_input
    
        self.data = data
        for item in self.data:
            self.set_value(item, self.data[item])

    def save_params(self,file_name = 'parameters.json'):
        params_dict = {}
        for item in self.params_list:
            params_dict.update({item:self.get_value(item)})

        params_dict_str = json.dumps(params_dict, indent=4)
        with open(file_name,'w') as fobj:
            fobj.write(params_dict_str)

    def save_inputs_ini(self,file_name = 'inputs_ini.json'):
        inputs_ini_dict = {}
        for item in self.inputs_ini_list:
            inputs_ini_dict.update({item:self.get_value(item)})

        inputs_ini_dict_str = json.dumps(inputs_ini_dict, indent=4)
        with open(file_name,'w') as fobj:
            fobj.write(inputs_ini_dict_str)


    def eval_jac_u2z(self):

        '''

        0 =   J_run * xy + FG_u * u
        z = Hxy_run * xy + H_u * u

        xy = -1/J_run * FG_u * u
        z = -Hxy_run/J_run * FG_u * u + H_u * u
        z = (-Hxy_run/J_run * FG_u + H_u ) * u 
        '''
        
        sp_Fu_run_eval(self.sp_Fu_run.data,self.x,self.y_run,self.u_run,self.p,self.Dt)
        sp_Gu_run_eval(self.sp_Gu_run.data,self.x,self.y_run,self.u_run,self.p,self.Dt)
        sp_H_jacs_run_eval(self.sp_Hx_run.data,
                        self.sp_Hy_run.data,
                        self.sp_Hu_run.data,
                        self.x,self.y_run,self.u_run,self.p,self.Dt)
        sp_jac_run = self.sp_jac_run
        sp_jac_run_eval(sp_jac_run.data,
                        self.x,self.y_run,
                        self.u_run,self.p,
                        self.Dt)



        Hxy_run = sspa.bmat([[self.sp_Hx_run,self.sp_Hy_run]])
        FGu_run = sspa.bmat([[self.sp_Fu_run],[self.sp_Gu_run]])
        

        #((sspa.linalg.spsolve(s.sp_jac_ini,-Hxy_run)) @ FGu_run + sp_Hu_run )@s.u_ini

        self.jac_u2z = Hxy_run @ sspa.linalg.spsolve(self.sp_jac_run,-FGu_run) + self.sp_Hu_run  
        
        
    # def step(self,t_end,up_dict):
    #     for item in up_dict:
    #         self.set_value(item,up_dict[item])

    #     t = self.t
    #     p = self.p
    #     it = self.it
    #     it_store = self.it_store
    #     xy = self.xy
    #     u = self.u_run
    #     z = self.z

    #     pt = np.zeros(64,dtype=np.int32)
    #     xy = self.xy
    #     x = xy[:self.N_x]
    #     y_run = xy[self.N_x:]

    #     p_pt =solver_run.ffi.cast('int *', pt.ctypes.data)
    #     p_sp_jac_trap = solver_run.ffi.cast('double *', self.sp_jac_trap_data.ctypes.data)
    #     p_indptr = solver_run.ffi.cast('int *', self.sp_jac_trap_indptr.ctypes.data)
    #     p_indices = solver_run.ffi.cast('int *', self.sp_jac_trap_indices.ctypes.data)
    #     p_x = solver_run.ffi.cast('double *', x.ctypes.data)
    #     p_y_run = solver_run.ffi.cast('double *', y_run.ctypes.data)
    #     p_xy = solver_run.ffi.cast('double *', self.xy.ctypes.data)
    #     p_u_run = solver_run.ffi.cast('double *', self.u_run.ctypes.data)
    #     p_z = solver_run.ffi.cast('double *', self.z.ctypes.data)
    #     p_dblparams = solver_run.ffi.cast('double *', self.rundblparams.ctypes.data)
    #     p_intparams = solver_run.ffi.cast('int *', self.runintparams.ctypes.data)
    #     p_x = solver_run.ffi.cast('double *', x.ctypes.data)
    #     p_its = solver_run.ffi.cast('int *', self.its.ctypes.data)
    #     p_p = solver_run.ffi.cast('double *', self.p.ctypes.data)
    #     N_x = self.N_x
    #     N_y = self.N_y
    #     max_it = self.max_it
    #     itol = self.itol
    #     max_it = 5
    #     itol = 1e-8

    #     N_x = self.N_x
    #     N_y = self.N_y
    #     max_it = self.max_it
    #     itol = self.itol
    #     max_it = 5
    #     itol = 1e-8
    #     its = 0

    # #   solver_run.lib.run( self.p_pt_run, t, t_end,p_sp_jac_trap, p_indptr,p_indices,p_x,p_y_run,p_xy,p_u_run,p_p,N_x,N_y, max_it, itol, p_its, self.Dt, p_z,p_dblparams, p_intparams, p_Time, p_X, p_Y, p_Z, self.N_z, self.N_store)
    #     solver_run.lib.step(self.p_pt_run, t, t_end,p_sp_jac_trap, p_indptr,p_indices,p_x,p_y_run,p_xy,p_u_run,p_p,N_x,N_y, max_it, itol, p_its, self.Dt, p_z,p_dblparams, p_intparams)

    #     self.t = t
    #     self.it = it
    #     self.it_store = it_store
    #     self.xy = xy
    #     self.z = z
           
    def save_run(self, file_name = ''):

        np.savez_compressed(file_name, Time = self.Time,
                            X = self.X,
                            Y = self.Y,
                            Z = self.Z,
                            params = self.p,
                            u_run = self.u_run,
                            u_ini = self.u_ini)
        
        return None            

    def load_run(self, file_name = ''):

        results = np.load(file_name)
        self.Time = results['Time']
        self.X = results['X']
        self.Y = results['Y']
        self.Z = results['Z']
        self.p = results['params']
        self.u_ini = results['u_ini']
        self.u_run = results['u_run']

        self.t = self.Time[-1]
        self.xy[:self.N_x] = self.X[-1,:]
        self.xy[self.N_x:] = self.Y[-1,:]
        self.z = self.Z[-1,:]    
        return None
        
        
    def full_jacs_eval(self):
        N_x = self.N_x
        N_y = self.N_y
        N_xy = N_x + N_y
    
        sp_jac_run = self.sp_jac_run
        sp_Fu = self.sp_Fu_run
        sp_Gu = self.sp_Gu_run
        sp_Hx = self.sp_Hx_run
        sp_Hy = self.sp_Hy_run
        sp_Hu = self.sp_Hu_run
        
        x = self.xy[0:N_x]
        y = self.xy[N_x:]
        u = self.u_run
        p = self.p
        Dt = self.Dt
    
        sp_jac_run_eval(sp_jac_run.data,x,y,u,p,Dt)
        
        self.Fx = sp_jac_run[0:N_x,0:N_x]
        self.Fy = sp_jac_run[ 0:N_x,N_x:]
        self.Gx = sp_jac_run[ N_x:,0:N_x]
        self.Gy = sp_jac_run[ N_x:, N_x:]
        
        sp_Fu_run_eval(sp_Fu.data,x,y,u,p,Dt)
        sp_Gu_run_eval(sp_Gu.data,x,y,u,p,Dt)
        sp_H_jacs_run_eval(sp_Hx.data,sp_Hy.data,sp_Hu.data,x,y,u,p,Dt)
        
        self.Fu = sp_Fu
        self.Gu = sp_Gu
        self.Hx = sp_Hx
        self.Hy = sp_Hy
        self.Hu = sp_Hu




def sp_jac_ini_vectors():

    sp_jac_ini_ia = [0, 33, 0, 2, 35, 54, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 13, 54, 14, 15, 16, 17, 18, 19, 22, 23, 14, 15, 16, 17, 18, 19, 22, 23, 14, 15, 16, 17, 26, 27, 14, 15, 16, 17, 26, 27, 14, 15, 18, 19, 20, 21, 14, 15, 18, 19, 20, 21, 18, 19, 20, 21, 38, 18, 19, 20, 21, 39, 0, 1, 14, 15, 22, 23, 14, 15, 22, 23, 24, 25, 26, 27, 45, 24, 25, 26, 27, 46, 16, 17, 24, 25, 26, 27, 30, 31, 16, 17, 24, 25, 26, 27, 30, 31, 28, 29, 30, 31, 52, 28, 29, 30, 31, 53, 26, 27, 28, 29, 30, 31, 26, 27, 28, 29, 30, 31, 0, 1, 22, 32, 32, 33, 34, 0, 33, 34, 3, 35, 2, 20, 21, 36, 37, 2, 4, 20, 21, 36, 37, 2, 20, 21, 36, 37, 38, 2, 20, 21, 36, 37, 39, 40, 45, 8, 24, 42, 6, 24, 41, 24, 25, 41, 42, 43, 44, 24, 25, 41, 42, 43, 44, 24, 25, 43, 44, 45, 24, 25, 43, 44, 46, 47, 52, 12, 28, 49, 10, 28, 48, 28, 29, 48, 49, 50, 51, 28, 29, 48, 49, 50, 51, 28, 29, 50, 51, 52, 28, 29, 50, 51, 53, 35, 54, 13, 54, 55]
    sp_jac_ini_ja = [0, 2, 3, 6, 7, 8, 9, 11, 12, 14, 15, 17, 18, 20, 22, 30, 38, 44, 50, 56, 62, 67, 72, 78, 82, 87, 92, 100, 108, 113, 118, 124, 130, 134, 137, 140, 142, 147, 153, 159, 165, 167, 170, 173, 179, 185, 190, 195, 197, 200, 203, 209, 215, 220, 225, 227, 230]
    sp_jac_ini_nia = 56
    sp_jac_ini_nja = 56
    return sp_jac_ini_ia, sp_jac_ini_ja, sp_jac_ini_nia, sp_jac_ini_nja 

def sp_jac_run_vectors():

    sp_jac_run_ia = [0, 33, 0, 2, 35, 54, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 13, 54, 14, 15, 16, 17, 18, 19, 22, 23, 14, 15, 16, 17, 18, 19, 22, 23, 14, 15, 16, 17, 26, 27, 14, 15, 16, 17, 26, 27, 14, 15, 18, 19, 20, 21, 14, 15, 18, 19, 20, 21, 18, 19, 20, 21, 38, 18, 19, 20, 21, 39, 0, 1, 14, 15, 22, 23, 14, 15, 22, 23, 24, 25, 26, 27, 45, 24, 25, 26, 27, 46, 16, 17, 24, 25, 26, 27, 30, 31, 16, 17, 24, 25, 26, 27, 30, 31, 28, 29, 30, 31, 52, 28, 29, 30, 31, 53, 26, 27, 28, 29, 30, 31, 26, 27, 28, 29, 30, 31, 0, 1, 22, 32, 32, 33, 34, 0, 33, 34, 3, 35, 2, 20, 21, 36, 37, 2, 4, 20, 21, 36, 37, 2, 20, 21, 36, 37, 38, 2, 20, 21, 36, 37, 39, 40, 45, 8, 24, 42, 6, 24, 41, 24, 25, 41, 42, 43, 44, 24, 25, 41, 42, 43, 44, 24, 25, 43, 44, 45, 24, 25, 43, 44, 46, 47, 52, 12, 28, 49, 10, 28, 48, 28, 29, 48, 49, 50, 51, 28, 29, 48, 49, 50, 51, 28, 29, 50, 51, 52, 28, 29, 50, 51, 53, 35, 54, 13, 54, 55]
    sp_jac_run_ja = [0, 2, 3, 6, 7, 8, 9, 11, 12, 14, 15, 17, 18, 20, 22, 30, 38, 44, 50, 56, 62, 67, 72, 78, 82, 87, 92, 100, 108, 113, 118, 124, 130, 134, 137, 140, 142, 147, 153, 159, 165, 167, 170, 173, 179, 185, 190, 195, 197, 200, 203, 209, 215, 220, 225, 227, 230]
    sp_jac_run_nia = 56
    sp_jac_run_nja = 56
    return sp_jac_run_ia, sp_jac_run_ja, sp_jac_run_nia, sp_jac_run_nja 

def sp_jac_trap_vectors():

    sp_jac_trap_ia = [0, 33, 0, 1, 2, 35, 54, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 13, 54, 14, 15, 16, 17, 18, 19, 22, 23, 14, 15, 16, 17, 18, 19, 22, 23, 14, 15, 16, 17, 26, 27, 14, 15, 16, 17, 26, 27, 14, 15, 18, 19, 20, 21, 14, 15, 18, 19, 20, 21, 18, 19, 20, 21, 38, 18, 19, 20, 21, 39, 0, 1, 14, 15, 22, 23, 14, 15, 22, 23, 24, 25, 26, 27, 45, 24, 25, 26, 27, 46, 16, 17, 24, 25, 26, 27, 30, 31, 16, 17, 24, 25, 26, 27, 30, 31, 28, 29, 30, 31, 52, 28, 29, 30, 31, 53, 26, 27, 28, 29, 30, 31, 26, 27, 28, 29, 30, 31, 0, 1, 22, 32, 32, 33, 34, 0, 33, 34, 3, 35, 2, 20, 21, 36, 37, 2, 4, 20, 21, 36, 37, 2, 20, 21, 36, 37, 38, 2, 20, 21, 36, 37, 39, 40, 45, 8, 24, 42, 6, 24, 41, 24, 25, 41, 42, 43, 44, 24, 25, 41, 42, 43, 44, 24, 25, 43, 44, 45, 24, 25, 43, 44, 46, 47, 52, 12, 28, 49, 10, 28, 48, 28, 29, 48, 49, 50, 51, 28, 29, 48, 49, 50, 51, 28, 29, 50, 51, 52, 28, 29, 50, 51, 53, 35, 54, 13, 54, 55]
    sp_jac_trap_ja = [0, 2, 4, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 31, 39, 45, 51, 57, 63, 68, 73, 79, 83, 88, 93, 101, 109, 114, 119, 125, 131, 135, 138, 141, 143, 148, 154, 160, 166, 168, 171, 174, 180, 186, 191, 196, 198, 201, 204, 210, 216, 221, 226, 228, 231]
    sp_jac_trap_nia = 56
    sp_jac_trap_nja = 56
    return sp_jac_trap_ia, sp_jac_trap_ja, sp_jac_trap_nia, sp_jac_trap_nja 
