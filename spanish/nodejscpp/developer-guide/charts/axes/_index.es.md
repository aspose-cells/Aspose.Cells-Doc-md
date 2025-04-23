---  
title: Gestionar ejes de gráficos de Excel con Node.js a través de C++  
description: Aprende cómo configurar los ejes del gráfico en Aspose.Cells for Node.js via C++. Nuestra guía te mostrará cómo ajustar los ejes primario y secundario, establecer sus rangos y modificar sus propiedades para mejorar tus gráficos.  
keywords: Aspose.Cells for Node.js via C++, ejes del gráfico, configuración, ejes primarios, ejes secundarios, rango, propiedades.  
linktitle: Ejes  
type: docs  
weight: 50  
url: /es/nodejs-cpp/chart-axes/  
---  

{{% alert color="primary" %}}  

En los gráficos de Excel, hay 3 tipos de ejes:  
1. Eje Horizontal (Categoría): Eje X  
1. Eje Vertical (Valor): Eje Y  
1. Eje de Profundidad (Serie): Eje Z  

{{% /alert %}}  

## **Opciones del Eje**  
Aspose.Cells for Node.js via C++ también le permite gestionar los ejes del gráfico en tiempo de ejecución. Con el objeto [Axis](https://reference.aspose.com/cells/nodejs-cpp/axis/), puede cambiar todas las opciones del Eje como se hace en Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **Administrar Ejes X e Y**  
En los gráficos de Excel, los ejes horizontal y vertical son los dos ejes más populares para usar.  

El siguiente fragmento de código demuestra cómo establecer las opciones de los ejes X e Y.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart_axes.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue("Series1");
worksheet.getCells().get("A2").putValue(50);
worksheet.getCells().get("A3").putValue(100);
worksheet.getCells().get("A4").putValue(150);
worksheet.getCells().get("B1").putValue("Series2");
worksheet.getCells().get("B2").putValue(60);
worksheet.getCells().get("B3").putValue(32);
worksheet.getCells().get("B4").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);

// Hiding X axis
chart.getCategoryAxis().setIsVisible(false);

// Setting max value of Y axis
chart.getValueAxis().setMaxValue(200);
// Setting major unit
chart.getValueAxis().setMajorUnit(50);

// Save the file
workbook.save(filePath);
```  

## **Temas avanzados**  
- [Cambiar la dirección de la etiqueta del eje](/cells/es/nodejs-cpp/change-tick-label-direction/)  
- [Determinar qué Eje existe en el Gráfico](/cells/es/nodejs-cpp/determine-which-axis-exists-in-the-chart/)  
- [Manejar Unidades Automáticas del Eje del Gráfico como Microsoft Excel](/cells/es/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Leer etiquetas del eje después de calcular el gráfico](/cells/es/nodejs-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Cómo establecer el Eje de Categoría en el Gráfico de Excel](/cells/es/nodejs-cpp/how-to-set-category-axis/)  

