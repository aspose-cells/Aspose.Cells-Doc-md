---
title: Cómo crear un gráfico combinado con Node.js mediante C++
linktitle: Cómo crear un gráfico combinado
description: Aprende cómo crear un gráfico combinado usando Aspose.Cells for Node.js via C++. Nuestra guía completa demostrará cómo combinar diferentes tipos de gráficos en un solo gráfico combinado para una presentación de datos más efectiva.
keywords: Aspose.Cells for Node.js via C++, gráfico combinado, combinación de tipos de gráficos, presentación de datos, visualización efectiva.
type: docs
weight: 73
url: /es/nodejs-cpp/create-combo-chart/
---

## **Escenarios de uso posibles**
Los gráficos combo en Excel te permiten aprovechar esta opción porque puedes combinar fácilmente dos o más tipos de gráficos para hacer que tus datos sean comprensibles. Los gráficos combo son útiles cuando tus datos contienen múltiples tipos de valores, incluidos precio y volumen. Además, los gráficos combo son factibles cuando los números de tus datos varían ampliamente de serie a serie.
Tomando el siguiente conjunto de datos como ejemplo, podemos observar que estos datos son bastante similares a los datos mencionados en [**VHCL**](https://docs.aspose.com/cells/nodejs-cpp/create-volume-high-low-close-stock-chart/). Si queremos visualizar la serie0, que corresponde a "Ingresos totales," como un gráfico de líneas, ¿cómo deberíamos proceder?

![todo:image_alt_text](sample.png)
## **Gráfico combo**
Después de ejecutar el código a continuación, verás el gráfico combo como se muestra a continuación.

![todo:image_alt_text](result.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](combo.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "combo.xlsx");

// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a stock volume (VHLC)
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 15, 0, 34, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Combo Chart");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E12", true);
// Set category data 
chart.getNSeries().get(0).setXValues("A2:A12");  // Corrected method

// Set the Series[1] Series[2] and Series[3] to different Marker Style
for (let j = 0; j < chart.getNSeries().getCount(); j++) {
switch (j) {
case 1:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Circle);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Pink);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 2:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Orange);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 3:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Square);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.LightBlue);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
}
}
// Set the chart type for Series[0] 
chart.getNSeries().get(0).setType(AsposeCells.ChartType.Line);
// Set style for the border of first series
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Solid);
// Set Color for the first series
chart.getNSeries().get(0).getBorder().setColor(AsposeCells.Color.DarkBlue);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
