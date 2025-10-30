---
title: Crear gráfico de acciones de Volumen Alto Bajo Cierre (VHLC) con Node.js mediante C++
linktitle: Crear Gráfico de la bolsa de valores con Volumen Alto Bajo Cierre (VHLC)
description: Aprende cómo crear un gráfico de acciones de volumen alto bajo cierre usando Aspose.Cells for Node.js via C++. Nuestra guía demostrará cómo trazar datos del mercado de valores, incluyendo volumen, alto, bajo y precios de cierre, en un gráfico para un mejor análisis y visualización.
keywords: Aspose.Cells for Node.js via C++, Gráfico de acciones de Volumen Alto Bajo Cierre, Datos del mercado de valores, Análisis, Visualización.
type: docs
weight: 183
url: /es/nodejs-cpp/create-volume-high-low-close-stock-chart/
---

## **Escenarios de uso posibles**
El tercer gráfico que analizaremos es el gráfico de volumen alto, bajo y cierre. Nuevamente, es importante repetir que los datos deben estar en el orden correcto. Si necesitas reorganizar tu tabla de datos, debes hacerlo antes de configurar tu gráfico.
Este gráfico incluye una columna para volumen justo después de la primera columna (categoría), y los gráficos incluyen un gráfico de columnas en el eje primario que muestra este volumen, mientras que los precios se trasladan al eje secundario.

![todo:image_alt_text](data.png)
## **Gráfico de bolsa de valores Volumen-Alto-Bajo-Cierre (VHLC)**

![todo:image_alt_text](sample.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo Excel de muestra](Volume-High-Low-Close.xlsx) y genera el [archivo Excel de salida](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series(Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
