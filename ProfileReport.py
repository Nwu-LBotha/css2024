# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:03:20 2024

@author: Louise
"""

import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])

profile = ProfileReport(df, title="Pandas Profiling Report")
# profile = ProfileReport(df,title='Profiling Report')
profile.to_file('your_report.html')

profile
