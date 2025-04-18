# 🚕 Sprint 8 – Recopilación y Análisis de Datos de Viajes en Chicago (SQL + Python)

## 📌 Descripción del Proyecto

Este proyecto integra conocimientos de SQL y Python para recopilar, procesar y analizar datos reales de viajes en taxi en la ciudad de **Chicago**. A partir de consultas realizadas en una base de datos, se descargaron datasets que contienen información sobre compañías de taxis, barrios de destino y condiciones climáticas durante los viajes.

El objetivo es responder preguntas de negocio clave mediante análisis exploratorios y pruebas de hipótesis.

## 🎯 Propósito

- Identificar qué compañías de taxi realizaron más viajes.
- Determinar los 10 barrios con más viajes finalizados.
- Investigar si la duración de los viajes desde el centro de Chicago hasta el aeropuerto se ve afectada por las condiciones climáticas los días sábados lluviosos.

## 📁 Datasets utilizados

- `project_sql_result_01.csv`: Número de viajes por empresa (15-16 nov 2017).
- `project_sql_result_04.csv`: Promedio de viajes terminados por barrio en nov 2017.
- `project_sql_result_07.csv`: Viajes desde el Loop hasta el aeropuerto O'Hare, con duración y clima.

## 🧰 Funcionalidades del Proyecto

### 🔍 Análisis exploratorio

- Inspección de tipos de datos y limpieza.
- Agrupación de viajes por empresa y barrio.
- Visualización de:
  - Top 10 empresas de taxi por número de viajes.
  - Top 10 barrios con más viajes finalizados.

### 🧪 Prueba de hipótesis

**Hipótesis**:  
> La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos.

- Definición de hipótesis nula y alternativa.
- Aplicación de prueba estadística (por ejemplo, `ttest_ind`) para evaluar la diferencia.
- Interpretación de resultados y decisión sobre la hipótesis.

## 📊 Herramientas utilizadas

- Python  
- pandas  
- matplotlib / seaborn  
- scipy.stats  
- SQL (para obtener los datos)

---

📌 Proyecto desarrollado como parte del Sprint 8 del programa de Ciencia de Datos en **TripleTen**.
