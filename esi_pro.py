import os
import pandas as pd
import numpy as np

df_path = "data/"+os.listdir("data")[0]


df = pd.read_csv(df_path, quotechar="\"")

print(df)



















