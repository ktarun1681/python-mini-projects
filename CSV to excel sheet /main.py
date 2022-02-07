import pandas as pd
import numpy as np

df_new = pd.read_csv('Sample.csv')

GFG = pd.ExcelWriter('names.xlsx')
df_new.to_excel(GFG, index= False)

GFG.save