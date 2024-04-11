#%%
from src import soporte as sp
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# ✅
df_brecha = pd.read_excel("files/brecha_salarial_UE.xlsx")
df_brecha

# %%
# ✅
df_formacion = pd.read_excel("files/Nivel_formacion_por_genero_sector_2016_2022.xlsx")
df_formacion

# %%
# ✅
df_ocupados = pd.read_excel("files/Ocupados_por_actividad_genero_CCAA_2016_2023.xlsx")
df_ocupados


# %%
# ✅
df_salario_jornada = pd.read_excel("files/salario_medio_jornada_completa_2016_2022.xlsx")

df_salario_jornada
# %%


df_salario_sector = pd.read_csv("files/salario_medio_por_sector_genero_2016__2021.csv",on_bad_lines='warn',index_col=False)

df_salario_sector

# %%
