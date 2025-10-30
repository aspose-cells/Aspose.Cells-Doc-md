---
title: Crear gráfico de acciones de Volumen Apertura Alto Bajo Cierre (VOHLC) con Node.js mediante C++
description: Aprende cómo crear un gráfico de acciones de volumen apertura alto bajo cierre usando Aspose.Cells for Node.js via C++. Nuestra guía demostrará cómo trazar datos del mercado de valores, incluyendo volumen, apertura, alto, bajo y precios de cierre, en un gráfico para un mejor análisis y visualización.
keywords: Aspose.Cells for Node.js via C++, Gráfico de acciones de Volumen Apertura Alto Bajo Cierre, Datos del mercado de valores, Análisis, Visualización.
type: docs
weight: 184
url: /es/nodejs-cpp/create-volume-open-high-low-close-stock-chart/
---

## **Escenarios de uso posibles**
El cuarto gráfico de acciones que veremos es el gráfico de volumen apertura-alto-bajo-cierre. Es importante repetir que los datos deben estar en el orden correcto. Si necesita reorganizar su tabla de datos, háganlo antes de configurar su gráfico. Este gráfico incluye una columna para volumen justo después de la primera columna (categoría), y los gráficos incluyen un gráfico de columnas en el eje primario que muestra este volumen, mientras que los precios se mueven al eje secundario.

![todo:image_alt_text](data.png)
## **Gráfico de valores-apertura-altos-bajos-cierre (VOHLC) de acciones**

![todo:image_alt_text](sample.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](Volume-Open-High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:F9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series (Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
