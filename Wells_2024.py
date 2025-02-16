import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import ternary
import pandas as pd

df = pd.read_excel(r"C:\Users\dabakarov\Downloads\lakes\dashgin_thesis_phd\My_thesis\Lab_Analyses\Wells.xlsx")

print(df)

print(df.columns)

df.columns = ['N', 'Name', 'Cl', 'SO4', 'HCO3', 'KNa', 'Mg', 'Ca']

well = pd.DataFrame()

# we start to add necessary columns to data frame
well['Sample'] = df['Name']

print(well)

#  we saw that names of lake contains spaces so we assing _ for space using str.replace
well['Sample'] = well['Sample'].str.replace(' ', '_')
print(well)

# now we create Label column with different names for different C values   
well['Label'] = 'C' + df['N'].map(str)
print(well)

# now we create color column
well['Color'] = ['#E6194B', '#3C78D8', '#3CB44B', '#FFE119', '#911EB4', 
          '#F58231', '#42D4F4', '#F032E6']
print(well)

# next step is to make Marker, Size and Alpha  and ph values columns
well['Marker'] = 'o'
well['Size'] = 20
well['Alpha'] = 0.6
well['pH'] = 0

print(well)

well['Ca'] = df['Ca']
well['Mg'] = df['Mg']
well['Na'] = df['KNa']
well['K'] = 0
well['HCO3'] = df['HCO3']
well['CO3'] = 0
well['Cl'] = df['Cl']
well['SO4'] = df['SO4']
well['TDS'] = df.iloc[:, 2:].sum(axis=1)


print(well)

# then we reset index to avoid unnecessary indexing issue
well.reset_index(inplace=True, drop=True)
print(well)

#  now we import WQchartpy
from wqchartpy import triangle_piper

# Draw the diagram
# triangle_piper.plot(well, unit='mg/L', figname=r'C:\Users\dabakarov\Downloads\lakes\dashgin_thesis_phd\My_thesis\Pyhton\wells', figformat='jpg')