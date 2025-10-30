---
title: Eje de fecha con Node.js vía C++
description: Aprende cómo gestionar el eje de fechas en Aspose.Cells for Node.js via C++. Nuestra guía te ayudará a entender cómo trabajar con varios formatos de fecha, escalas de tiempo y frecuencias de etiquetas de marcas.
keywords: Aspose.Cells para Node.js, eje de fecha, gestionar, formatos de fecha, escalas de tiempo, frecuencias de etiquetas de marcas.
type: docs
weight: 200
url: /es/nodejs-cpp/date-axis/
---

## **Escenarios de uso posibles**
Cuando creas un gráfico a partir de datos de hoja de cálculo que usan fechas, y las fechas se trazan a lo largo del eje horizontal (categoría) en el gráfico, Aspose.Cells for Node.js via C++ cambia automáticamente el eje de categoría a un eje de fecha (escala de tiempo).
Un eje de fecha muestra fechas en orden cronológico a intervalos específicos o unidades base, como el número de días, meses o años, incluso si las fechas en la hoja de cálculo no están en orden secuencial o en las mismas unidades base.
Por defecto, Aspose.Cells determina las unidades básicas para el eje de fecha en función de la menor diferencia entre dos fechas en los datos de la hoja de cálculo. Por ejemplo, si tienes datos de precios de acciones donde la menor diferencia entre fechas es de siete días, Excel establece la unidad base en días, pero puedes cambiar la unidad base a meses o años si deseas ver el rendimiento de la acción en un período de tiempo más largo.

## **Manejar el eje de fechas como en Microsoft Excel**
Por favor, vea el siguiente código de ejemplo que crea un nuevo archivo Excel y coloca los valores del gráfico en la primera hoja. 
Luego agregamos un gráfico y establecemos el tipo de [**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/) 
a [**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--) y luego establecemos las unidades base en Días.

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
// Add the sample values to cells
worksheet.getCells().get("A1").putValue("Date");
// 14 means datetime format
const style = worksheet.getCells().getStyle();
style.setNumber(14);
// Put values to cells for creating chart
worksheet.getCells().get("A2").setStyle(style);
worksheet.getCells().get("A2").putValue(new Date(Date.UTC(2022, 5, 26)));
worksheet.getCells().get("A3").setStyle(style);
worksheet.getCells().get("A3").putValue(new Date(Date.UTC(2022, 4, 22)));
worksheet.getCells().get("A4").setStyle(style);
worksheet.getCells().get("A4").putValue(new Date(Date.UTC(2022, 7, 3)));
worksheet.getCells().get("B1").putValue("Price");
worksheet.getCells().get("B2").putValue(40);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(60);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 9, 6, 21, 13);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);         
// Set the Axis type to Date time
chart.getCategoryAxis().setCategoryType(AsposeCells.CategoryType.TimeScale);
// Set the base unit for CategoryAxis to days
chart.getCategoryAxis().setBaseUnitScale(AsposeCells.TimeUnit.Days);
// Set the direction for the axis text to be vertical
chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Vertical);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set max value of Y axis.
chart.getValueAxis().setMaxValue(70);
// Set major unit.
chart.getValueAxis().setMajorUnit(10);
// Save the file
workbook.save("DateAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
