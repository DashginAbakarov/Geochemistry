import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import ternary
import pandas as pd

df = pd.read_excel(r"C:\Users\dabakarov\Downloads\lakes\dashgin_thesis_phd\My_thesis\Pyhton\Hydrological_low_level_water.xlsx", header=2)

print(df)

print(df.columns)

df.columns = ['N', 'Name', 'Cl', 'SO4', 'HCO3', 'KNa', 'Mg', 'Ca',
       'TDS', 'total anionsl (g/Mol)', 'total  kations (g/Mol)',
       'Anions (g/l)', 'Total Ions', 'Kations (g/l)', 'Anion (mol/l)',
       'Kation (mol/l)', 'Cl mol/l', 'SO4 mol/l', 'HCO3 mol/l', 'KNa mol/l', 'Mg mol/l',
       'Ca mol/l', 'Cl g/l', 'SO4 g/l', 'HCO3 g/l', 'KNa g/l', 'Mg g/l',
       'Ca g/l']

low_water = pd.DataFrame()

# we start to add necessary columns to data frame
low_water['Sample'] = df['Name']

print(low_water)

#  we saw that names of lake contains spaces so we assing _ for space using str.replace
low_water['Sample'] = low_water['Sample'].str.replace(' ', '_')
print(low_water)

# now we create Label column with different names for different C values   
low_water['Label'] = 'C' + df['N'].map(str)
print(low_water)

# now we create color column
low_water['Color'] = ['#E6194B', '#3C78D8', '#3CB44B', '#FFE119', '#911EB4', 
          '#F58231', '#42D4F4', '#F032E6', '#BFEF45', '#9A6324']
print(low_water)

# next step is to make Marker, Size and Alpha  and ph values columns
low_water['Marker'] = 'o'
low_water['Size'] = 20
low_water['Alpha'] = 0.6
low_water['pH'] = 0

print(low_water)

low_water['Ca'] = df['Ca g/l']
low_water['Mg'] = df['Mg g/l']
low_water['Na'] = df['KNa g/l']
low_water['K'] = 0
low_water['HCO3'] = df['HCO3 g/l']
low_water['CO3'] = 0
low_water['Cl'] = df['Cl g/l']
low_water['SO4'] = df['SO4 g/l']
low_water['TDS'] = df['TDS']


print(low_water)

# Our values are g/l so we should convert to mg/l 
print(low_water.columns)
low_water[['pH', 'Ca', 'Mg',
       'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS']] = low_water[['pH', 'Ca', 'Mg',
       'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS']]*1000
print(low_water)

print(low_water)
# then we reset index to avoid unnecessary indexing issue
low_water.reset_index(inplace=True, drop=True)
print(low_water)

#  now we import WQchartpy
from wqchartpy import triangle_piper

# Draw the diagram
triangle_piper.plot(low_water, unit='mg/L', figname=r'C:\Users\dabakarov\Downloads\lakes\dashgin_thesis_phd\My_thesis\Pyhton\l water Piper diagram', figformat='jpg')