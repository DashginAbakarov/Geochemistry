
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ternary
import random
import matplotlib.markers as markerss
import seaborn as sns
# we open excel file using pandas dataframe
df = pd.read_excel(r"C:\Users\dabakarov\Downloads\lakes\dashgin_thesis_phd\My_thesis\Pyhton\Hydrological_high_level_water.xlsx", header=2)
print(df)
# general information about what is inside datatype
df.info()

# # give first 5 rows
# print(df.head(5))

# display whole data
pd.options.display.max_columns = None
print(df)
#  there are uncessery columns which we will not use therefore first we look at the column names to see which ones should be removed
print(df.columns)



# we drop the list of column
df_dropped = df.drop(['Cl %', 'SO4 [-2] %', 'HCO3 %', '(K+Na) %', 'Mg [+2] %',
       'Ca [+2] %', 'Total (g/l)', 'total anionsl (g/Mol)',
       'total  kations (g/Mol)', 'Anions (g/l)', 'Total Ions', 'Kations (g/l)',
       'Anion (mol/l)', 'Kation (mol/l)','Cl .1', 'SO4 [-2].1', 'HCO3 .1',
       '(K+Na) .1', 'Mg [+2] .1', 'Ca [+2] .1'], axis=1)

print(df_dropped.head())

#  some of the column names are not appropirate so we change 
# print(df_dropped.columns)
df_dropped.columns = ['N','Name',
        'Cl ', 'SO4', 'HCO3 ', '(K+Na) ', 'Mg ',
       'Ca']

print(df_dropped)

# print(df_dropped.columns)

# # # we add color and markercolumn to our data frame
# # #  adding color column
# # #  we will generate random colors but to avoid each time when we run code again having different colors we use random.seed(42) function 
# # but it does not work as we wish so we create custom using color names below
# # #  we also set the range for total rows in our data frame using len
# # random.seed(42) 
# # df_dropped['Color'] = ["#{:06x}".format(random.randint(0, 0xFFFFFF)) for _ in range(len(df_dropped))]
# # # # df_dropped['Color'] = []

df_dropped['Color'] = ['#E6194B', '#3C78D8', '#3CB44B', '#FFE119', '#911EB4', 
          '#F58231', '#42D4F4', '#F032E6', '#BFEF45', '#9A6324']

# #  to generate markers first we need to look at what are the available markers in matplotlib to do so we run function but we can check website as well
# # available_markers = list(markerss.MarkerStyle.markers.keys())
# # print(available_markers)

# to make ternary diagram first we should normalize values to percentage using div and sum
#  to do so first we choose columns we need for diagram
#  for anions Cl, SO4 and HCO3
df_nor_anion = df_dropped.iloc[:, 2:5] = df_dropped.iloc[:, 2:5].div(df_dropped.iloc[:, 2:5].sum(axis=1), axis=0)*100
df_nor_cation = df_dropped.iloc[:, 5:8] = df_dropped.iloc[:, 5:8].div(df_dropped.iloc[:, 5:8].sum(axis=1), axis=0)*100
print(df_nor_anion)
print(df_nor_cation)
# # then we convert list of values to tuples for ternary plot
points_anion = list(df_nor_anion.itertuples(index=False, name=None))
points_cation = list(df_nor_cation.itertuples(index=False, name=None))

print(points_anion)
print(points_cation)

# #  now we ternary diagram
fig, axs = plt.subplots(1, 2, figsize=(16, 8))  # 1 row, 2 columns

#  for anions
tax_anions = ternary.TernaryAxesSubplot(ax=axs[0], scale=100)
tax_anions.boundary()
tax_anions.gridlines(multiple=10, color="gray", linestyle="dotted")

#  now we plot points and iterate through the names
# we used zip to combine name and corresponding values
# we use enumerate to add index to iterate on them and caunt but it is not necessary step we can remove.
# enumerate is good approach if we have dublicated names and not to remove them accidentaly iterate solely with names
for i, (point, N, name,color) in enumerate(zip(points_anion, df_dropped['N'],df_dropped['Name'], df_dropped['Color'])):
       tax_anions.scatter([point], marker='o', label=f"{i+1}: {name}", color=color, s=100, edgecolors="black", linewidth=1.0)
       tax_anions.annotate(str(N), point, fontsize=8, horizontalalignment='left', verticalalignment='center', color='Black')

# now we plot ternary diagram
## Label corners
tax_anions.set_title("Anions: Cl, SO₄²⁻, HCO₃⁻,Mol/l ", fontsize=14)
tax_anions.left_axis_label("%SO₄²⁻", fontsize=12, rotation=60)
tax_anions.right_axis_label("%Cl⁻", fontsize=12, rotation=-60)
tax_anions.bottom_axis_label("%HCO₃⁻ + CO₃²⁻", fontsize=12,offset = -0.1)
tax_anions.legend(fontsize=8)

# for cations
tax_cations = ternary.TernaryAxesSubplot(ax=axs[1], scale=100)
tax_cations.boundary()
tax_cations.gridlines(multiple=10, color="gray", linestyle="dotted")

#  now we plot points and iterate through the names
# we used zip to combine name and corresponding values
# we use enumerate to add index to iterate on them and caunt but it is not necessary step we can remove.
# enumerate is good approach if we have dublicated names and not to remove them accidentaly iterate solely with names
for i, (point, N, name,color) in enumerate(zip(points_cation, df_dropped['N'],df_dropped['Name'], df_dropped['Color'])):
       tax_cations.scatter([point], marker='o', label=f"{i+1}: {name}", color=color, s=100, edgecolors="black", linewidth=1.0)
       tax_cations.annotate(str(N), point, fontsize=8, horizontalalignment='left', verticalalignment='center', color='Black')

# now we plot ternary diagram
## Label corners
tax_cations.set_title("Cations: Ca, Mg, Na+K, Mol/l", fontsize=14)
tax_cations.left_axis_label("%Mg²⁺", fontsize=12, rotation=60)
tax_cations.right_axis_label("%Na⁺ + %K⁺", fontsize=12, rotation=-60)
tax_cations.bottom_axis_label("%Ca²⁺", fontsize=12, offset = -0.1)
tax_cations.legend(fontsize=8)


# plt.savefig(r'C:\Users\dabakarov\Downloads\lakes\dashgin_thesis_phd\My_thesis\Pyhton\Ternary High water.jpeg', format='jpeg', dpi=300)

# Show plot
plt.tight_layout()
plt.show()

# Draw the diagram



 


