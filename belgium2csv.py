import numpy
import pandas as pd
import os

def transcode(filename):
    path1 = os.path.join('raw/belgium',filename+'.log')
    bds = []
    with open(path1,'r') as f1:
        lines = f1.readlines()
        for line in lines:
            bd = int(line.split()[4])
            bds.append(bd)
    print(bds)

    df2 = pd.DataFrame({'bandwidth':bds})
    path2 = os.path.join('clean_trace/belgium',filename+'.csv')
    df2.to_csv(path2,index='False')

if __name__=="__main__":
    import os
    rootdir = 'raw/belgium'
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            print(file)
            transcode(file.split('.')[0])