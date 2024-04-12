#%%
from src import soporte as sp
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# %%

# ✅ Apertura fichero brecha salariar (paises UE 2002-2022 dato %)
df_brecha = pd.read_excel("files/brecha_salarial_UE.xlsx")
df_brecha
df_brecha.to_csv('doc_graficar/brecha_genero.csv')


# %%
# ✅ Apertura archivo educacion (2016 a 2022 - Division por genero y tipo educacion)
df_formacion = pd.read_excel("files/Nivel_formacion_por_genero_sector_2016_2022.xlsx")
df_formacion.name = "Formacion"
sp.cambio_nombre_columnas_df(df_formacion)

df_formacion["sector_del_nivel_de_formación_alcanzado"] = df_formacion["sector_del_nivel_de_formación_alcanzado"].apply(sp.separar_columna)

df_formacion.to_csv('doc_graficar/formacion.csv')


#✅ Apertura archivo ocupacion por CNAE (2016 a 2022 - Division por genero)

df_ocupados = pd.read_csv("files/files sin modificacion/Ocupados_por_actividad_genero_CCAA_2016_2023.csv", sep=";")
df_ocupados.name = "Ocupacion"
sp.cambio_nombre_columnas_df(df_ocupados)

df_ocupados["comunidades_y_ciudades_autónomas"] = df_ocupados["comunidades_y_ciudades_autónomas"].apply(sp.separar_columna)
df_ocupados["comunidades_y_ciudades_autónomas"] = df_ocupados["comunidades_y_ciudades_autónomas"].apply(sp.separar_columna_coma)
df_ocupados["rama_de_actividad_-_cnae_2009"] = df_ocupados["rama_de_actividad_-_cnae_2009"].apply(sp.categorizar_cnae)
df_ocupados["total"] = df_ocupados["total"].str.replace(".","").str.replace(",",".")

df_ocupados.to_csv('doc_graficar/ocupacion.csv')


# %%
df_salario_jornada = pd.read_excel("files/salario_medio_jornada_completa_2016_2022.xlsx")
df_salario_jornada


df_salario_sector = pd.read_excel("files/salario_medio_por_sector_genero_2016__2021.xlsx")
df_salario_sector

# %%
excedencia = pd.read_excel("files/excedendia_por_cuidado_hijos.xlsx")
excedencia


tasa_actividad = pd.read_excel("files/tasa_actividad_UE.xlsx")
tasa_actividad


tasa_paro = pd.read_excel("files/tasa_paro.xlsx")
tasa_paro

horas_cuidado_hogar = pd.read_excel("files/horas_semanales_cuidados_hogar_2016.xlsx")
horas_cuidado_hogar


# %%
