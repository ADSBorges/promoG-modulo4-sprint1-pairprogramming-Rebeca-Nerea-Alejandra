#%%
from src import soporte as sp
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# ✅
df_brecha = pd.read_excel("files/brecha_salarial_UE.xlsx")
df_brecha

# ✅
df_formacion = pd.read_excel("files/Nivel_formacion_por_genero_sector_2016_2022.xlsx")
df_formacion

# ✅
df_ocupados = pd.read_excel("files/Ocupados_por_actividad_genero_CCAA_2016_2023.xlsx")
df_ocupados

# ✅
df_salario_jornada = pd.read_excel("files/salario_medio_jornada_completa_2016_2022.xlsx")
df_salario_jornada

# ✅
df_salario_sector = pd.read_excel("files/salario_medio_por_sector_genero_2016__2021.xlsx")
df_salario_sector

# ✅
excedencia = pd.read_excel("files/excedendia_por_cuidado_hijos.xlsx")
excedencia

# ✅
tasa_actividad = pd.read_excel("files/tasa_actividad_UE.xlsx")
tasa_actividad

# ✅
tasa_paro = pd.read_excel("files/tasa_paro.xlsx")
tasa_paro

# ✅
horas_cuidado_hogar = pd.read_excel("files/horas_semanales_cuidados_hogar_2016.xlsx")
horas_cuidado_hogar
# %%
