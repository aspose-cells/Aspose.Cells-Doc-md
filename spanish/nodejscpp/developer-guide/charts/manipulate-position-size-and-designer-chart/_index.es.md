---
title: Manipular posición, tamaño y diseñar gráficos con Node.js a través de C++
linktitle: Manipular la Posición, Tamaño y Diseño del Gráfico
description: Aprende cómo usar Aspose.Cells for Node.js via C++ para manipular eficazmente la posición, tamaño y diseño del gráfico en Microsoft Excel. Nuestra guía demostrará cómo ajustar estas propiedades para mejorar el diseño y la visualización.
keywords: Aspose.Cells for Node.js via C++, Posición, Tamaño, Diseño del gráfico, Microsoft Excel, Diseño, Visualización.
type: docs
weight: 45
url: /es/nodejs-cpp/manipulate-position-size-and-designer-chart/
---

## **Posición y Tamaño del Gráfico**
A veces, deseas cambiar la posición o tamaño del gráfico nuevo o existente dentro de la hoja de cálculo. Aspose.Cells proporciona la propiedad [Chart.getChartObject()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getChartObject--) para lograr esto. Puedes usar sus subpropiedades para redimensionar el gráfico con una **altura** y **anchura** nuevas o reposicionarlo con nuevas coordenadas **X** y **Y**.

### **Controlar la Posición y Tamaño del Gráfico**
Para cambiar la posición (coordenadas X, Y) o el tamaño (altura, ancho) del gráfico, use estas propiedades:

1. [Shape.getX()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getX--)
1. [Shape.getY()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getY--)
1. [Shape.getHeight()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getHeight--)
1. [Shape.getWidth()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getWidth--)

El siguiente ejemplo explica el uso de las APIs anteriores; carga el libro de trabajo existente que contiene un gráfico en su primera hoja. Luego redimensiona y vuelve a ubicar el gráfico usando Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart.xls");

// Loads the workbook which contains the chart
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(1);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

// Resize the chart
chart.getChartObject().setWidth(400);
chart.getChartObject().setHeight(300);

// Reposition the chart
chart.getChartObject().setX(250);
chart.getChartObject().setY(150);

// Output the file
workbook.save(path.join(dataDir, "chart.out.xls"));
```

## **Manipulación de gráficos de diseñador**
Hay ocasiones en las que necesitas manipular o modificar gráficos en archivos de plantilla de diseño. Aspose.Cells soporta totalmente la manipulación de contenidos y elementos de gráficos de diseño. Los datos, contenidos del gráfico, imagen de fondo y formato pueden ser conservados con precisión.

### **Manipulación de gráficos de diseñador en archivos de plantillas**
Para manipular gráficos de diseñadores en archivos de plantilla, utiliza la API relacionada con gráficos. Por ejemplo, puedes usar la propiedad Worksheet.charts para obtener la colección de gráficos existentes en el archivo de plantilla.

#### **Creación de un gráfico**
El siguiente ejemplo muestra cómo crear un gráfico de pirámide. Más adelante manipularemos este gráfico.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

#### **Manipulación del gráfico**
El siguiente ejemplo muestra cómo manipular el gráfico existente. En este ejemplo, modificamos el gráfico creado anteriormente. En la salida generada, se observa que la etiqueta de fecha de un punto de datos se ha establecido en 'Reino Unido, 30K'.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "piechart.xls");

// Loads the existing file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the designer chart in the second sheet.
const sheet = workbook.getWorksheets().get(1);
const chart = sheet.getCharts().get(0);

// Get the data labels in the data series of the third data point.
const dataLabels = chart.getNSeries().get(0).getPoints().get(2).getDataLabels();

// Change the text of the label.
dataLabels.setText("Unided Kingdom, 400K ");

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Manipulación de un gráfico de líneas en la plantilla de diseñador**
En este ejemplo, manipularemos un gráfico de líneas. Agregaremos algunas series de datos al gráfico existente y cambiaremos sus colores de línea.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Get the designer chart in the first worksheet.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Add the third data series to it.
chart.getNSeries().add("{60, 80, 10}", true);

// Add another data series (fourth) to it.
chart.getNSeries().add("{0.3, 0.7, 1.2}", true);

// Plot the fourth data series on the second axis.
chart.getNSeries().get(3).setPlotOnSecondAxis(true);

// Change the Border color of the second data series.
chart.getNSeries().get(1).getBorder().setColor(AsposeCells.Color.Green);

// Change the Border color of the third data series.
chart.getNSeries().get(2).getBorder().setColor(AsposeCells.Color.Red);

// Make the second value axis visible.
chart.getSecondValueAxis().setIsVisible(true);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

