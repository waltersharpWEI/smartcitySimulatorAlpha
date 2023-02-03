#This is the main loop of the simulator

import os
import pandas as pd
import numpy as np
from config import Config
import logging
from simulator import Simulator



if __name__ == '__main__':
    #set up the logger
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger('sim')
    #read the config
    config_path = 'basic.cfg'
    with open(config_path,'r') as f:
        cfg = Config(f)
        log.info("Bandwith_log:"+str(cfg['bandwidth_path']))
        log.info("Table:"+str(cfg['table_path']))
        df_bd = pd.read_csv(cfg['bandwidth_path'])
        df_t = pd.read_csv(cfg['table_path'])
        log.info("Starting Simulator.")
        #start simulator according to config
        sim = Simulator(cfg)
        acc_list = sim.sim_acc()
        log.info("Simulator Stopped.")
        #print the average accuracy
        print('Average Accuracy:',acc_list.mean())

