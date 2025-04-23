---
title: Establecer el tipo de forma de las etiquetas de datos del gráfico con Node.js a través de C++
linktitle: Establecer el tipo de forma de las etiquetas de datos del gráfico
description: Aprende cómo establecer el tipo de forma de las etiquetas de datos en los gráficos usando Aspose.Cells for Node.js via C++. Esta guía explicará los diferentes tipos de formas disponibles y te mostrará cómo elegir la forma adecuada para tus etiquetas de datos para mejorar la presentación y usabilidad.
keywords: Aspose.Cells for Node.js via C++, creación de gráficos, etiquetas de datos, tipos de forma, presentación, usabilidad.
type: docs
weight: 110
url: /es/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Escenarios de uso posibles**
Puedes cambiar el tipo de forma de las etiquetas de datos del gráfico usando la propiedad `DataLabels.shapeType`. Toma el valor del enumerado `DataLabelShapeType` y cambia el tipo de forma de las etiquetas de datos en consecuencia. Algunos de sus valores son

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **Establecer el tipo de forma de las etiquetas de datos del gráfico**
El siguiente ejemplo cambia el tipo de forma de las etiquetas de datos del gráfico a `DataLabelShapeType.WedgeEllipseCallout`. Por favor, revisa el archivo de Excel de ejemplo ([60489778.xlsx](60489778.xlsx)) usado en este código y el archivo de Excel de salida ([60489779.xlsx](60489779.xlsx)) generado por él. La captura de pantalla muestra el efecto del código en el archivo de ejemplo.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Código de muestra**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
