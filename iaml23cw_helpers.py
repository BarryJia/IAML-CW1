#
#  Helper functions for IAML 2022/23 S2 cw
#   by Hiroshi Shimodaira (h.shimodaira@ed.ac.uk)
#
import os
import gzip
import numpy as np
import scipy
from scipy.io import loadmat
import pandas as pd

def print_versions():
    import platform
    import scipy
    import numpy
    import sklearn
    import matplotlib
    import seaborn
    import pandas

    tabs = [ ['Python', platform.python_version(), '3.9.12'],
             ['Scipy', scipy.__version__, '1.7.3'],
             ['Numpy', numpy.__version__, '1.21.6'],
             ['Sklearn', sklearn.__version__, '1.1.1'],
             ['Pandas', pandas.__version__, '1.4.2'],
             ['Matplotlib', matplotlib.__version__, '3.5.2'],
             ['Seaborn', seaborn.__version__, '0.11.2']
            ]
    for p in tabs:
        print('%s\t%s ' % (p[0], p[1]), end='')
        if p[1] == p[2]:
            print(': Ok')
        else:
            print('<=> %s' % p[2])

def load_q2_dataset(fname="dset_q2.npz"):
    t = np.load(fname)
    Xtrn = t["Xtrn"]; Ytrn = t["Ytrn"]
    Xtst = t["Xtst"]; Ytst = t["Ytst"]
    return(Xtrn.astype(np.float64), Ytrn.astype(np.int_), Xtst.astype(np.float64), Ytst.astype(np.int_))
