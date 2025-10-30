---
title: Cómo crear un diagrama de Gantt con Node.js vía C++
linktitle: Cómo crear un gráfico de Gantt
type: docs
weight: 72
url: /es/nodejs-cpp/how-to-create-gantt-chart/
description: Aprende cómo crear un diagrama de Gantt con la API Aspose.Cells for Node.js via C++.
keywords: Crear un diagrama de Gantt en Node.js, agregar un diagrama de Gantt, insertar un diagrama de Gantt
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

1. Selecciona el gráfico, **Seleccionar datos** -> **Agregar**, configura el **Nombre de la serie** y los **Valores de la serie** como sigue.
<br>
<img src="2.png" width=50% />

1. Selecciona el gráfico, edita las **Etiquetas del eje horizontal (categoría)**.
<br>
<img src="3.png" width=50% />

1. **Formatear eje** la Eje Y, selecciona **Categorías en orden inverso**.
1. Selecciona la **Serie Azul** y establece **Relleno -> Sin relleno**.
1. **Formatear eje** en el eje X, establece los **Mínimo y Máximo** (1/5/2019:43470, 1/30/2019:43494).
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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Create BarStacked Chart
const i = worksheet.getCharts().add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(i);
// Set the chart title name 
chart.getTitle().setText("Gantt Chart");
// Set the chart title is Visible
chart.getTitle().setIsVisible(true);
// Set data range
chart.setChartDataRange("B1:B6", true);
// Add series data range
chart.getNSeries().add("C2:C6", true);
// No fill for one serie
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set the Horizontal(Category) Axis
chart.getNSeries().setCategoryData("A2:A6");
// Reverse the Horizontal(Category) Axis
chart.getCategoryAxis().setIsPlotOrderReversed(true);
// Set the value axis's MinValue and MaxValue
const minValue = parseFloat(worksheet.getCells().get("B2").getValue());
const maxValue = parseFloat(worksheet.getCells().get("D6").getValue());
chart.getValueAxis().setMinValue(isNaN(minValue) ? 0 : minValue);
chart.getValueAxis().setMaxValue(isNaN(maxValue) ? 0 : maxValue);
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Show the DataLabels
chart.getNSeries().get(1).getDataLabels().setShowValue(true);
// Disable the Legend
chart.setShowLegend(false);
// Save the result
workbook.save("result.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
