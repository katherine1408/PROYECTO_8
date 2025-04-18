 # Zuber 

# Una nueva empresa de viajes compartidos que se está lanzando en Chicago. Tu tarea es encontrar patrones en la información disponible. Quieres comprender las preferencias de los pasajeros y el impacto de los factores externos en los viajes.
# Al trabajar con una base de datos, analizarás los datos de los competidores y probarás una hipótesis sobre el impacto del clima en la frecuencia de los viajes.
# 

# ## Análisis exploratorio de datos (Python):

# ### Inicialización:

# In[1]:


# Importar librerías:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
sns.set(style="whitegrid")


# ### Cargar Datos:

# In[2]:


# Importar archivos CSV:

file1 = r'd:\TRIPLETEN\SPRINT 8\PROYECTO_8\moved_project_sql_result_01.csv'
file2 = r'd:\TRIPLETEN\SPRINT 8\PROYECTO_8\moved_project_sql_result_04.csv'

df_taxis = pd.read_csv(file1)
df_barrios = pd.read_csv(file2)




# ### Visualización de datos:

# In[3]:


# Visualizar los primeros datos:

df_taxis.head()


# In[4]:


# Visualizar los primeros datos:
df_barrios.head()


# ### Estudiar los datos que contienen:

# In[5]:


# Verificar la información general de los DataFrames
df_taxis.info()


# In[6]:


# Verificar la información general de los DataFrames
df_barrios.info()


# In[7]:


# Resumen estadístico:

df_taxis.describe()


# In[8]:


# Resumen estadístico:
df_barrios.describe()


# ## Preparar los datos:

# ### Correción de datos: 
# Verifica que los tipos de datos sean correctos para que sean más fáciles de manejar.  
# 
# De la revisión de datos tenemos que no hay valores ausentes.

# In[9]:


df_taxis['trips_amount'] = df_taxis['trips_amount'].astype(int)
df_taxis.info()


# In[10]:


df_barrios['average_trips'] = df_barrios['average_trips'].astype(float)
df_barrios.info()


# ### Revisión de datos nulos:

# In[11]:


df_taxis.isna().sum()


# In[12]:


df_barrios.isna().sum()


# ### Revisión de datos duplicados:

# In[13]:


df_taxis.duplicated().sum()


# In[14]:


df_barrios.duplicated().sum()



# ## Analisis de Datos:

# ### Identificar los 10 principales barrios por número de finalización de recorridos:

# In[15]:


top_10_barrios = df_barrios.sort_values(by='average_trips', ascending=False).head(10)
top_10_barrios


# In[16]:


# Crear la gráfica
plt.figure(figsize=(10, 6))
sns.barplot(x='average_trips', y='dropoff_location_name', data=top_10_barrios, palette='viridis')

# Añadir un título a la gráfica
plt.title('Top 10 Barrios por Número Promedio de Finalización de Viajes en Noviembre 2017', fontsize=14)

# Añadir etiquetas a los ejes
plt.xlabel('Promedio de Viajes Finalizados', fontsize=12)
plt.ylabel('Nombre del Barrio', fontsize=12)

# Mostrar la gráfica
plt.tight_layout()
plt.show()




# ### Gráficos:

# In[17]:


# Gráfico de barras para empresas de taxis y número de viajes:

plt.figure(figsize=(10, 6))
sns.barplot(x='company_name', y='trips_amount', data=df_taxis)
plt.xticks(rotation=90)
plt.title('Número de viajes por compañía de taxis')
plt.show()


# * Conclusiones:
# *Empresas de taxis: Al observar el gráfico de las empresas de taxis, se puedes concluir qué compañías tienen más viajes y cómo varía la actividad entre ellas.

# In[18]:


#Los 10 barrios principales por número de finalizaciones:

# Gráfico de barras para los 10 barrios principales
plt.figure(figsize=(10, 6))
sns.barplot(x='dropoff_location_name', y='average_trips', data=top_10_barrios)
plt.xticks(rotation=90)
plt.title('Top 10 Barrios con más finalizaciones de viajes')
plt.show()


# * Conclusiones:
# 
# Barrios: El gráfico de los 10 barrios principales muestra en qué áreas de la ciudad terminan la mayoría de los viajes. Esto puede estar relacionado con la densidad de población o zonas comerciales.



# ## Hipotesis:

# ### Prueba de hipótesis (Python):

# In[19]:


# El resultado de la última consulta. Contiene datos sobre viajes desde el Loop hasta el Aeropuerto Internacional O'Hare
# Adicionamos la información de datos sobre viajes desde el LOOP:
#Importar los datos de la consulta:
df_viajes = pd.read_csv(r'd:\TRIPLETEN\SPRINT 8\PROYECTO_8\moved_project_sql_result_07.csv')
df_viajes.info()




# In[20]:


# Convertir la columna de fecha y hora en datetime:

df_viajes['start_ts'] = pd.to_datetime(df_viajes['start_ts'])
df_viajes.head()


# Establecer el Valor de Umbral Alfa (α)
# 
# Elegimos un nivel de significancia comúnmente utilizado, α = 0.05. Esto significa que estamos dispuestos a aceptar un 5% de probabilidad de rechazar la hipótesis nula cuando en realidad es cierta

# Criterio de Prueba y Justificación:
# 
# Utilizaremos la prueba t de dos muestras independientes (Student's t-test) para comparar las medias de dos grupos independientes en ambas hipótesis.
# 

# ###  Hipótesis sobre la duración promedio de los viajes desde Loop hasta el Aeropuerto:

# * Plantear las hipótesis:
# 
# Hipótesis nula (H₀): La duración promedio de los viajes desde el Loop hasta el Aeropuerto O'Hare es igual los sábados lluviosos que en otros sábados.
# 
# Hipótesis alternativa (H₁): La duración promedio de los viajes desde el Loop hasta el Aeropuerto O'Hare es diferente los sábados lluviosos en comparación con otros sábados.

# Revisión del Criterio para la Prueba de Hipótesis:
# Para la prueba de hipótesis, usamos una prueba t de Student para comparar las medias entre dos grupos (sábados lluviosos y sábados sin lluvia). Esta prueba es apropiada porque queremos ver si las diferencias observadas entre ambos grupos son significativas. El nivel de significancia (alfa 0.05) que escogemos define la probabilidad de rechazar incorrectamente la hipótesis nula cuando en realidad es verdadera.

# Conclusión basada en el valor p:
# Si el valor p es menor que el nivel de significancia (alfa 0.05), se rechaza la hipótesis nula, lo que indica que existen diferencias significativas en la duración de los viajes entre los sábados lluviosos y los sábados sin lluvia.

# In[21]:


# Filtrar los datos por sábados y condiciones climáticas:
# Crear una columna para identificar los sábados:

df_viajes['day_of_week'] = df_viajes['start_ts'].dt.day_name()
saturdays = df_viajes[df_viajes['day_of_week'] == 'Saturday']
saturdays


# In[22]:


# Filtrar los viajes con condiciones climáticas lluviosas
rainy_saturdays = saturdays[saturdays['weather_conditions'].str.contains('Bad')]
rainy_saturdays


# ### Probar las hipótesis:

# In[23]:


# Calcular la duración promedio de todos los sábados y los sábados lluviosos:
all_saturdays_mean = saturdays['duration_seconds'].mean()
all_saturdays_mean


# In[24]:


rainy_saturdays_mean = rainy_saturdays['duration_seconds'].mean()
rainy_saturdays_mean


# In[25]:


# Prueba de hipótesis con t-test:

t_stat_time = stats.ttest_ind(saturdays['duration_seconds'], rainy_saturdays['duration_seconds'], equal_var=False)

# Nivel de significancia (alpha)
alpha = 0.05

print(f'p-value:{t_stat_time.pvalue}')
if t_stat_time.pvalue < alpha:
    print("Podemos rechazar la hipótesis nula")
else:
    print("No podemos rechazar la hipotesis nula")


# 
# 
# ### **Conclusión General del Proyecto**
# 
# Este proyecto nos permitió realizar un análisis exploratorio de datos y una prueba de hipótesis utilizando información relacionada con los viajes en taxi en Chicago durante noviembre de 2017. A lo largo de las etapas del proyecto, se trabajó con tres conjuntos de datos que proporcionaron una visión completa del comportamiento de las compañías de taxis y la distribución de los viajes en la ciudad, así como el impacto de las condiciones climáticas en la duración de los trayectos entre puntos clave.
# 
# #### **Análisis Exploratorio de Datos:**
# 1. **Empresas de taxis**: Se analizaron las empresas de taxis más activas en términos de número de viajes los días 15 y 16 de noviembre de 2017. Los gráficos revelaron una clara diferencia entre las compañías, con algunas operando un volumen de viajes significativamente mayor que otras. Este hallazgo podría estar relacionado con la cantidad de vehículos disponibles, la popularidad de las empresas o la ubicación de sus operaciones.
# 
# 2. **Finalización de viajes por barrio**: El análisis mostró los 10 principales barrios de Chicago donde finalizaron más viajes en noviembre de 2017. Los resultados indican que ciertos barrios, probablemente áreas más urbanizadas o turísticas, atraen una mayor cantidad de trayectos. Este análisis puede ser útil para planificar la distribución de taxis y mejorar la cobertura de servicios en áreas con mayor demanda.
# 
# #### **Prueba de Hipótesis:**
# Se planteó y evaluó la hipótesis de que "la duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos". La prueba estadística realizada (prueba t de Student) comparó la duración promedio de los viajes entre todos los sábados y aquellos con condiciones de lluvia.
# 
# - Los resultados no mostraron una diferencia significativa en la duración de los viajes los sábados lluviosos, lo que llevó a  rechazar la hipótesis nula. Dado que el valor p es menor que 0.05, podemos rechazar la hipótesis nula y concluir que existen diferencias significativas en la duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare los sábados lluviosos en comparación con otros sábados. Esto sugiere que la lluvia tiene un impacto significativo en la duración de los viajes.
# 
# #### **Conclusiones finales:**
# El análisis de los datos permitió entender mejor el comportamiento del servicio de taxis en Chicago, identificando tanto las empresas más activas como los barrios con más finalizaciones de trayectos. Por otro lado, la prueba de hipótesis mostró que las condiciones climáticas lluviosas  parecen afectar significativamente la duración de los viajes hacia el Aeropuerto Internacional O'Hare, al menos en los sábados analizados. Estos hallazgos podrían ser útiles para mejorar la planificación de rutas y la asignación de recursos por parte de las compañías de taxis, así como para evaluar las dinámicas urbanas de transporte.
# 


