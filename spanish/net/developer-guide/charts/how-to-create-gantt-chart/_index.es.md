---
title: Cómo crear un diagrama de Gantt
linktitle: Cómo crear un diagrama de Gantt
type: docs
weight: 72
url: /es/net/how-to-create-gantt-chart/
description: Aprenda cómo crear un diagrama de Gantt con la API Aspose.Cells for .NET.
keywords: C# crear un diagrama de Gantt, agregar un diagrama de Gantt, insertar un diagrama de Gantt
---

## **¿Qué es un diagrama de Gantt?**

Un diagrama de Gantt es un tipo de gráfico de barras que ilustra un cronograma de proyecto. Muestra las fechas de inicio y finalización de los diversos elementos de un proyecto. Cada tarea o actividad está representada por una barra, cuya longitud corresponde a su duración. Los diagramas de Gantt también indican las dependencias entre tareas, lo que permite a los gerentes de proyecto visualizar la secuencia en la que las tareas deben completarse. Se utilizan ampliamente en la gestión de proyectos para planificar, programar y rastrear proyectos de manera efectiva.

## **Cómo crear un diagrama de Gantt en Excel**

Puede crear un diagrama de Gantt en Excel siguiendo estos pasos:
1. Agregar algunos datos para el diagrama de Gantt. 
<br>
<img src="00.png" width=50% />
1. Seleccione los datos e vaya a Insertar --> Gráficos --> Insertar gráfico de barras o columnas --> Gráfico de barras apiladas. En nuestro ejemplo, sería B1:B7, y luego inserte un **gráfico de barras apiladas**.
<br>
<img src="1.png" width=50% />

1. Seleccione el gráfico, **Seleccionar datos**->**Agregar**, configure el **Nombre de la serie** y **Valores de la serie** como se indica a continuación.
<br>
<img src="2.png" width=50% />

1. Seleccione el gráfico, edite las **Etiquetas del eje horizontal (categoría)**.
<br>
<img src="3.png" width=50% />

1. **Formato del eje** Y, seleccione **Categorías en orden inverso**.
1. Seleccione la **Serie azul** y configure **Relleno-> Sin relleno**.
1. **Formato del eje** X, configure el **Mínimo y Máximo**(1/5/2019:43470,1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Agregar etiquetas de datos** para el gráfico, ahora obtendrá un diagrama de Gantt.
<br>
<img src="0.png" width=50% />


## **Cómo agregar un diagrama de Gantt en Aspose.Cells**
Consulte el siguiente código de ejemplo. Carga el [archivo de Excel de ejemplo](sample.xlsx) que contiene algunos datos de ejemplo. Luego crea el gráfico de barras apiladas basado en los datos iniciales y configura propiedades relevantes. Finalmente, guarda el libro de trabajo en [formato XLSX de salida](result.xlsx). La siguiente captura de pantalla muestra el diagrama de Gantt creado por Aspose.Cells en el archivo de Excel de salida.
<br>
<img src="5.png" width=60% />

### **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

