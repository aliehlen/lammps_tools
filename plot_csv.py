#!/usr/bin/env python

# usage: $ plot_csv.py log_csv.csv
# this is most useful after running the lammps log2txt.py tool 
# (which is in lammps/tools/python/log2txt.py, used like 
# log2txt.py log.lammps log.csv). That makes the csv which this script plots

import pandas as pd
import sys
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    logfile = sys.argv[1]
    df = pd.read_csv(logfile, sep="(?<!#)\s+", engine="python")
    
    # workaround for extra # at beginning of colnames
    df.columns = pd.Series(df.columns.str.replace("#\s", "", regex=True))

    colnames = df.columns.values
    
    df.plot(subplots=True, x=colnames[0], marker='o', ms=1.5, linewidth=0.25)
    plt.show()
    
