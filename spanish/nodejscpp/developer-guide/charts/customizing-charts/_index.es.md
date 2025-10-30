---  
title: Personalización de gráficos con Node.js mediante C++  
linktitle: Personalización de gráficos  
description: Aprende cómo personalizar gráficos en Aspose.Cells for Node.js via C++. Nuestra guía te mostrará cómo modificar los diseños del gráfico, agregar y formatear series de datos, ajustar los ejes y aplicar varias opciones de formato para mejorar la apariencia y usabilidad de tus gráficos.  
keywords: Aspose.Cells for Node.js via C++, gráficos, personalización, diseños, series de datos, ejes, formato, apariencia, usabilidad.  
type: docs  
weight: 40  
url: /es/nodejs-cpp/customizing-charts/  
---  


## **Creación de gráficos personalizados**  

Hasta ahora, cuando hemos discutido sobre gráficos, hemos visto gráficos estándar que tienen su configuración de formato estándar. Solo definimos la fuente de datos, configuramos algunas propiedades y el gráfico se crea con su configuración predeterminada. Pero las API de Aspose.Cells también soportan la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con sus propios ajustes de formato.  

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells.  

Un gráfico se compone de una serie de datos. Cada serie de datos en Aspose.Cells está representada por un objeto [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) mientras que el objeto [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) sirve como colección de objetos [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series). Al crear un gráfico personalizado, los desarrolladores tienen la libertad de usar diferentes tipos de gráficos para diferentes series de datos (recogidas en el objeto [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)).  

El código de ejemplo a continuación demuestra cómo crear gráficos personalizados. En este ejemplo, vamos a usar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de cálculo.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

Actualmente, Aspose.Cells solo soporta gráficos personalizados que combinan gráficos de pastel, línea, columna y apilados, pero en futuras versiones se soportarán más gráficos.  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
