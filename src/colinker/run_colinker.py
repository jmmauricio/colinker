from colinker import linker_run
from .example.emec_emu.pv_1_2_bess import Emulator
if __name__ == '__main__':

    name = 'LV0101'
    mode = 'lmah'
    cfg_dev = './example/emec_emu/pv_1_2_bess/config_devices.json' 
    cfg_ctrl = './example/emec_emu/pv_1_2_bess/config_controller.json'


    linker_run(name, mode, cfg_dev, cfg_ctrl)