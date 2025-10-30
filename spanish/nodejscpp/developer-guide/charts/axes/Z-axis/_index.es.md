---
title: Eje Z con Node.js mediante C++
description: Aprende cómo trabajar con el eje Z en Aspose.Cells for Node.js via C++. Nuestra guía te ayudará a entender cómo configurar y personalizar el eje Z, incluyendo su escala y etiquetas, para mejorar tus gráficos.
keywords: Aspose.Cells for Node.js via C++, eje Z, gráficos, configuración, personalización, escala, etiquetas.
type: docs
weight: 210
url: /es/nodejs-cpp/z-axis/
---

## **Escenarios de uso posibles**
Para algunos gráficos en 3D como columna 3D, cono 3D o pirámide 3D que tienen un eje de profundidad (serie), también conocido como eje Z, que puedes cambiar. Puedes especificar el intervalo entre marcas de graduación, etiquetas del eje y otras operaciones.

## **Manejar el eje primario y secundario como Microsoft Excel**
 Por favor, vea el siguiente código de ejemplo que crea un archivo Excel nuevo y coloca los valores del gráfico en la primera hoja. Luego, agregamos un gráfico y configuramos el tipo de gráfico a Column3D, y también puede ver el eje Z, también llamado Eje de Profundidad. 

![todo:image_alt_text](excel.png)

## **Código de muestra**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Put values to cells for creating chart
worksheet.getCells().get("A1").putValue("A");
worksheet.getCells().get("B1").putValue("B");
worksheet.getCells().get("C1").putValue("C");
worksheet.getCells().get("A2").putValue(2);
worksheet.getCells().get("A3").putValue(1);
worksheet.getCells().get("B2").putValue(2);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("C2").putValue(2);
worksheet.getCells().get("C3").putValue(3);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column3D, 9, 6, 25, 16);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Calculate the chart
chart.calculate();
// Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
chart.setChartDataRange("A2:C3", true);
// Hide the CategoryAxis axis
chart.getCategoryAxis().setIsVisible(false);
// Hide the ValueAxis axis
chart.getValueAxis().setIsVisible(false);
// Save the file
workbook.save("ZAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
