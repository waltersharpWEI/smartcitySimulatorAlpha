import numpy
import pandas as pd
import os

filename = 'c1'
path1 = os.path.join('raw',filename+'.csv')
df1 = pd.read_csv(path1)
bds = df1['bandwith.googAvailableSendBandwidth']

df2 = pd.DataFrame({'bandwidth':bds})
path2 = os.path.join('clean_trace',filename+'.csv')
df2.to_csv(path2,index='False')
