---  
title: Configurar la fuente de datos para el gráfico con Node.js mediante C++  
description: Aprende sobre las diferentes fuentes de datos soportadas por Aspose.Cells for Node.js via C++. Nuestra guía te mostrará los distintos tipos de fuentes de datos disponibles y cómo conectarte y recuperar datos de ellas para llenar tus hojas de cálculo.  
keywords: Aspose.Cells for Node.js via C++, graficación, formateo de datos, etiquetas, colores, fuentes, apariencia, usabilidad.  
linktitle: Fuente de datos  
type: docs  
weight: 10  
url: /es/nodejs-cpp/data-formatting-in-charts/  
---  

En nuestros temas anteriores, ya hemos proporcionado muchos ejemplos para demostrar cómo puedes configurar una fuente de datos para tu gráfico, pero en este tema, proporcionaremos más detalles sobre los tipos de datos que se pueden establecer para un gráfico.

## **Establecer Datos del Gráfico**

Hay dos tipos de datos con los que trabajar al utilizar gráficos con Aspose.Cells como se muestra a continuación:

- Datos del gráfico.
- Datos de categoría.

### **Datos del Gráfico**

Los datos del gráfico son los datos que usamos como fuente para construir nuestros gráficos. Podemos añadir un rango de celdas (que contienen datos del gráfico) llamando al método [**add(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#add-string-boolean-) del objeto [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection).

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
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(300);
worksheet.getCells().get("B1").putValue(160);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Datos de Categoría**

Los datos de categoría se utilizan para etiquetar los datos del gráfico y se pueden agregar a [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) usando su propiedad [**getCategoryData()**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#getCategoryData--). A continuación se presenta un ejemplo completo para demostrar el uso de datos de gráfico y categoría. Después de ejecutar el código de ejemplo anterior, se añadirá un gráfico de columnas a la hoja de cálculo como se muestra abajo.

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
worksheet.getCells().get("A1").putValue(10);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(200);
worksheet.getCells().get("B1").putValue(120);
worksheet.getCells().get("B2").putValue(320);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the data source for the category data of SeriesCollection
chart.getNSeries().setCategoryData("C1:C4");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Temas avanzados**  
- [Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango](/cells/es/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [Crear Gráficos Dinámicos](/cells/es/nodejs-cpp/create-dynamic-charts/)  
- [Forma fácil para la configuración de gráficos utilizando el método Chart.SetChartDataRange](/cells/es/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico](/cells/es/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)  
