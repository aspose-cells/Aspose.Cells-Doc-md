---
title: Cómo crear un gráfico de Gantt
linktitle: Cómo crear un gráfico de Gantt
type: docs
weight: 72
url: /es/net/how-to-create-gantt-chart/
description: Aprende cómo crear un gráfico Gantt con la API Aspose.Cells for .NET.
keywords: Crear un gráfico Gantt en C#, agregar un gráfico Gantt, insertar un gráfico Gantt
---

## **Qué es un gráfico de Gantt**

Un gráfico de Gantt es un tipo de gráfico de barras que ilustra un cronograma de proyecto. Muestra las fechas de inicio y fin de los diferentes elementos de un proyecto. Cada tarea o actividad está representada por una barra, cuya duración corresponde a su período. Los gráficos de Gantt también indican dependencias entre tareas, permitiendo a los gerentes de proyecto visualizar la secuencia en la que las tareas deben completarse. Son ampliamente utilizados en la gestión de proyectos para planificar, programar y rastrear proyectos de manera efectiva.

## **Cómo crear un gráfico de Gantt en Excel**

Puedes crear un gráfico de Gantt en Excel siguiendo estos pasos:
1. Agrega algunos datos para el gráfico de Gantt. 
<br>
<img src="00.png" width=50% />
1. Selecciona los datos y ve a Insertar --> Gráficos --> Insertar gráfico de columnas o barras --> Gráfico de barras apiladas. En nuestro ejemplo, es B1:B7, y luego Inserta un **Gráfico de barras apiladas**.
<br>
<img src="1.png" width=50% />

1. Selecciona el gráfico,**Seleccionar datos**->**Agregar**, configura el **Nombre de la serie** y los **Valores de la serie** de la siguiente manera.
<br>
<img src="2.png" width=50% />

1. Selecciona el gráfico, edita las **Etiquetas del eje horizontal (categoría)**.
<br>
<img src="3.png" width=50% />

1. **Formatear eje** la Eje Y, selecciona **Categorías en orden inverso**.
1. Selecciona la **Serie azul** y configura el **Relleno->Sin relleno**.
1. **Formatear eje** la Eje X, establece los **Mínimos y Máximos** (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Agregar etiquetas de datos** al gráfico, ahora tendrás un gráfico de Gantt.
<br>
<img src="0.png" width=50% />


## **Cómo agregar un gráfico de Gantt en Aspose.Cells**
Por favor, vea el siguiente código de ejemplo. Carga el [archivo de Excel de ejemplo](sample.xlsx) que contiene algunos datos de muestra. Luego crea el gráfico de barras apiladas basado en los datos iniciales y establece las propiedades relevantes. Finalmente, guarda el libro de trabajo en [formato XLSX de salida](result.xlsx). La siguiente captura de pantalla muestra el gráfico de Gantt creado por Aspose.Cells en el archivo de Excel de salida.
<br>
<img src="5.png" width=60% />

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
