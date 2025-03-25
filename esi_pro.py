import os
import pandas as pd
import numpy as np
import regex as re

df_path = "data/"+os.listdir("data")[0]

arrayfile = []
with open(df_path) as csvfile:
    for l in csvfile:
        a = l.replace("c(", "\"").replace(")", "\"")
        a0 = a.split("\"")[-1]
        a1 = a.split(",")[:-1]
        arrayfile.append([b.replace("\"", "").replace("\n", "") for b in a1]+[a0])
        print(arrayfile[-1])


df = pd.DataFrame(arrayfile[1:], columns=arrayfile[0])

print(df)



















