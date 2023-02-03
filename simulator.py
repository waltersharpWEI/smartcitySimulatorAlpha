import pandas as pd
import numpy as np
from config import Config
import logging

log = logging.getLogger('sim')

class Simulator():
    def __init__(self, cfg):
        self.df_bd = pd.read_csv(cfg['bandwidth_path'])
        self.df_t = pd.read_json(cfg['table_path'])
        self.fps = cfg['fps_target']

    def opt_acc(self,bd):
        max_acc = 0
        for index,row in self.df_t.iterrows():
            if row['size'] * self.fps < bd and row['1st_acc'] > max_acc:
                max_acc = row['1st_acc']
        return max_acc

    def opt_acc_latency_server_only(self, bd):
        max_acc = 0
        latency_bound = 1000 / self.fps
        for index, row in self.df_t.iterrows():
            total_latency = row['size'] / bd * 1000 + row['1st_inf'] \
                            + row['encoding_latency'] + row['decoding_latency']
            if  total_latency<latency_bound and row['1st_acc'] > max_acc:
                max_acc = row['1st_acc']
        return max_acc

    def sim_acc(self):
        results = []
        bds = self.df_bd['bandwidth']
        for bd in bds:
            acc = self.opt_acc_latency_server_only(bd)
            log.info("bandwidth: "+str(bd))
            log.info("accuracy: "+str(acc))
            results.append(acc)
        return np.array(results)