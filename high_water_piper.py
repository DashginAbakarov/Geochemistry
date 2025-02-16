import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import ternary
import pandas as pd

df = pd.read_excel(r"C:\Users\dabakarov\Downloads\lakes\dashgin_thesis_phd\My_thesis\Pyhton\Hydrological_high_level_water.xlsx", header=2)

print(df)

print(df.columns)

df.columns = ['N', 'Name', 'Cl', 'SO4', 'HCO3', 'KNa', 'Mg', 'Ca',
       'TDS', 'total anionsl (g/Mol)', 'total  kations (g/Mol)',
       'Anions (g/l)', 'Total Ions', 'Kations (g/l)', 'Anion (mol/l)',
       'Kation (mol/l)', 'Cl mol/l', 'SO4 mol/l', 'HCO3 mol/l', 'KNa mol/l', 'Mg mol/l',
       'Ca mol/l', 'Cl g/l', 'SO4 g/l', 'HCO3 g/l', 'KNa g/l', 'Mg g/l',
       'Ca g/l']

high_water = pd.DataFrame()

# we start to add necessary columns to data frame
high_water['Sample'] = df['Name']

print(high_water)

#  we saw that names of lake contains spaces so we assing _ for space using str.replace
high_water['Sample'] = high_water['Sample'].str.replace(' ', '_')
print(high_water)

# now we create Label column with different names for different C values   
high_water['Label'] = 'C' + df['N'].map(str)
print(high_water)

# now we create color column
high_water['Color'] = ['#E6194B', '#3C78D8', '#3CB44B', '#FFE119', '#911EB4', 
          '#F58231', '#42D4F4', '#F032E6', '#BFEF45', '#9A6324']
print(high_water)

# next step is to make Marker, Size and Alpha  and ph values columns
high_water['Marker'] = 'o'
high_water['Size'] = 20
high_water['Alpha'] = 0.6
high_water['pH'] = 0

print(high_water)

high_water['Ca'] = df['Ca g/l']
high_water['Mg'] = df['Mg g/l']
high_water['Na'] = df['KNa g/l']
high_water['K'] = 0
high_water['HCO3'] = df['HCO3 g/l']
high_water['CO3'] = 0
high_water['Cl'] = df['Cl g/l']
high_water['SO4'] = df['SO4 g/l']
high_water['TDS'] = df['TDS']


print(high_water)

# Our values are g/l so we should convert to mg/l 
print(high_water.columns)
high_water[['pH', 'Ca', 'Mg',
       'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS']] = high_water[['pH', 'Ca', 'Mg',
       'Na', 'K', 'HCO3', 'CO3', 'Cl', 'SO4', 'TDS']]*1000
print(high_water)

print(high_water)
# then we reset index to avoid unnecessary indexing issue
high_water.reset_index(inplace=True, drop=True)
print(high_water)

#  now we import WQchartpy
from wqchartpy import triangle_piper

# Draw the diagram
# triangle_piper.plot(high_water, unit='mg/L', figname=r'C:\Users\dabakarov\Downloads\lakes\dashgin_thesis_phd\My_thesis\Pyhton\High water Piper diagram', figformat='jpg')