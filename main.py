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

# ✅ Apertura archivo poblacion España (2002 a 2023 - Division por genero)
df_poblacion_españa = pd.read_csv("files/poblacion_españa_2002_2023.csv", sep=";")
df_poblacion_españa.name = "Poblacion España"
sp.cambio_nombre_columnas_df(df_poblacion_españa)


def cambiar_punto(celda):
    return int(str(celda).replace(".", "").replace(",", ""))

def separar_celda_t(celda):
    try:
        celda = celda.split("T", maxsplit=1)
        return celda[0]
    
    except:
        return celda

df_poblacion_españa["total"] = df_poblacion_españa["total"].apply(cambiar_punto)
df_poblacion_españa["periodo"] = df_poblacion_españa["periodo"].apply(separar_celda_t)
df_poblacion_españa.drop(columns=["edad","unidad"],inplace=True)

#df_poblacion_españa.to_csv('doc_graficar/poblacion.csv')

# ✅ Apertura archivo salario por jornada España (2002 a 2023 - Division por genero)

df_salario_jornada = pd.read_excel("files/salario_medio_jornada_completa_2016_2022.xlsx")
df_salario_jornada.name = "Salario Jornada completa"

df_filtrado = df_salario_jornada[df_salario_jornada["Decil"] == "Total decil"]


display(df_filtrado)
#df_filtrado.to_csv('doc_graficar/salario_jornada.csv')

# ✅ Apertura archivo salario por CNAE España (2002 a 2023 - Division por genero)
#%%

df_salario_sector = pd.read_excel("files/salario_medio_por_sector_genero_2016__2021.xlsx")
df_salario_sector.name = "Salario por genero y CNAE"

df_salario_sector["Sectores de actividad económica"] = df_salario_sector["Sectores de actividad económica"].apply(sp.separar_columna)
df_salario_sector["Total"] = df_salario_sector["Total"].apply(abs)

#%%
#sp.exploracion_col_df(df_salario_sector)

# condicion1 = df_salario_sector["Sectores de actividad económica"] == "Información y comunicaciones"
# condicion2 = df_salario_sector["Periodo"] == 2020

# df_salario_sector[condicion1 & condicion2]


df_salario_sector.to_csv('doc_graficar/salario_sector.csv')

# ✅ Apertura archivo persoans que han pedido excedencia por cuidado de menores en España (2005 a 2023 - Division por genero)
excedencia = pd.read_excel("files/excedendia_por_cuidado_hijos.xlsx")
excedencia
excedencia.to_csv('doc_graficar/excedencia.csv')

# ✅ Apertura archivo horas semanales cuidado y labores hogar (UE y España)
#%%
horas_cuidado_familiar = pd.read_excel("files/horas_semanales_cuidados_hogar_2016.xlsx")
horas_cuidado_familiar
horas_cuidado_familiar.to_csv('doc_graficar/horas_cuidado_familiar.csv')

#%%
display(horas_cuidado_familiar)

# ✅ Apertura archivo Tasa actividad (UE)
tasa_actividad = pd.read_excel("files/tasa_actividad_UE.xlsx")
tasa_actividad
# tasa_actividad.to_csv('doc_graficar/tasa_actividad_ue.csv')
#%%
display(tasa_actividad)

#%%
# ✅ Apertura archivo Tasa paro (UE)
tasa_paro = pd.read_excel("files/tasa_paro.xlsx")
tasa_paro

tasa_paro.to_csv('doc_graficar/tasa_paro_ue.csv')




# %%
