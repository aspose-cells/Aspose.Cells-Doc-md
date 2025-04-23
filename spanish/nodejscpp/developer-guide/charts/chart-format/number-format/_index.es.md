---
title: Configurar el código de formato de valores de la serie del gráfico con Node.js mediante C++
description: Aprende cómo configurar el código de formato de valores de la serie del gráfico en Aspose.Cells for Node.js via C++. Esta guía te ayudará a entender cómo dar formato a los datos de la serie de tu gráfico usando el código de formato adecuado, permitiéndote presentar tus datos de forma precisa y profesional.
keywords: Aspose.Cells para Node.js, series de gráficos, código de formato de valores, formateo, presentación de datos, precisión, profesionalismo.
linktitle: Formato de número
type: docs
weight: 100
url: /es/nodejs-cpp/set-the-values-format-code-of-chart-series/
---

## **Escenarios de uso posibles**
Puedes establecer el código de formato de valores de la serie del gráfico usando la propiedad [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--). Esta propiedad no solo es útil para la serie basada en el rango dentro de la hoja, sino que también funciona bien para la serie creada con un arreglo de valores.

## **Establecer el código de formato de valores de la serie del gráfico**
El siguiente código de ejemplo agrega una serie en un gráfico vacío que no tenia series antes. Agrega la serie usando un arreglo de valores. Una vez que añade la serie, la formatea con el código $#,##0 usando la propiedad [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) y el número 10,000 se convierte en $10,000. La captura de pantalla muestra el efecto del código en el archivo de Excel de ejemplo (51740712.xlsx) y en el archivo Excel de salida (51740713.xlsx) después de la ejecución.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Código de muestra**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");

// Load the source Excel file 
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);

// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");

// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
