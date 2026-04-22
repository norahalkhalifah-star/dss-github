# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Input_Data = dataiku.Folder("9dgAXSxw")
Input_Data_info = Input_Data.get_info()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

t_shirt_data_df = ... # Compute a Pandas dataframe to write into t_shirt_data


# Write recipe outputs
t_shirt_data = dataiku.Dataset("t_shirt_data")
t_shirt_data.write_with_schema(t_shirt_data_df)
