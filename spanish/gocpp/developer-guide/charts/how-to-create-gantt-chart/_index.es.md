---
title: Cómo crear un gráfico de Gantt con Golang a través de C++
linktitle: Cómo crear un gráfico de Gantt
type: docs
weight: 72
url: /es/go-cpp/how-to-create-gantt-chart/
description: Aprende cómo crear un gráfico de Gantt con la API Aspose.Cells for C++.
keywords: Crear un gráfico de Gantt con C++, agregar un gráfico de Gantt, insertar un gráfico de Gantt
---

## **Qué es un gráfico de Gantt**

Un gráfico de Gantt es un tipo de gráfico de barras que ilustra un cronograma de proyecto. Muestra las fechas de inicio y fin de los diferentes elementos de un proyecto. Cada tarea o actividad está representada por una barra, cuya duración corresponde a su período. Los gráficos de Gantt también indican dependencias entre tareas, permitiendo a los gerentes de proyecto visualizar la secuencia en la que las tareas deben completarse. Son ampliamente utilizados en la gestión de proyectos para planificar, programar y rastrear proyectos de manera efectiva.

## **Cómo crear un gráfico de Gantt en Excel**

Puedes crear un gráfico de Gantt en Excel siguiendo estos pasos:
1. Agrega algunos datos para el gráfico de Gantt. 
<br>
<img src="00.png" width=50% />
1. Selecciona los datos y ve a Insertar --> Gráficos --> Insertar gráfico de columnas o barras --> Barra apilada. En nuestro ejemplo, eso es B1:B7, y luego Inserta un gráfico de **barra apilada**.
<br>
<img src="1.png" width=50% />

1. Selecciona el gráfico, **Seleccionar datos**->**Agregar**, configura el **nombre de la serie** y los **valores de la serie** de la siguiente manera.
<br>
<img src="2.png" width=50% />

1. Selecciona el gráfico, edita las **Etiquetas del eje horizontal (categoría)**.
<br>
<img src="3.png" width=50% />

1. **Formatear eje** la Eje Y, selecciona **Categorías en orden inverso**.
1. Selecciona la **Serie Azul** y configura el **Relleno -> Sin relleno**.
1. **Formatar eje** la Eje X, configura el **Mínimo y Máximo**(1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Agregar etiquetas de datos** para el gráfico, ahora obtendrás un gráfico de Gantt.
<br>
<img src="0.png" width=50% />


## **Cómo agregar un gráfico de Gantt en Aspose.Cells**
Por favor, vea el siguiente código de ejemplo. Carga el [archivo de Excel de ejemplo](sample.xlsx) que contiene algunos datos de muestra. Luego crea el gráfico de barras apiladas basado en los datos iniciales y establece las propiedades relevantes. Finalmente, guarda el libro de trabajo en [formato XLSX de salida](result.xlsx). La siguiente captura de pantalla muestra el gráfico de Gantt creado por Aspose.Cells en el archivo de Excel de salida.
<br>
<img src="5.png" width=60% />

### **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToCreateGanttChart.go" >}}
