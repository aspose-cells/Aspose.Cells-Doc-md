---
title: Crear gráfico de acciones de apertura máximo mínimo cierre (OHLC) con Node.js vía C++
description: Aprende cómo crear un gráfico de acciones de apertura alto bajo cierre usando Aspose.Cells for Node.js via C++. Nuestra guía demostrará cómo trazar datos del mercado de valores, incluyendo los precios de apertura, alto, bajo y cierre, en un gráfico para un mejor análisis y visualización.
keywords: Aspose.Cells for Node.js via C++, Gráfico de acciones de Apertura Alto Bajo Cierre, Datos del mercado de valores, Análisis, Visualización.
type: docs
weight: 182
url: /es/nodejs-cpp/create-open-high-low-close-stock-chart/
---

## **Escenarios de uso posibles**
El gráfico de cotizaciones apertura-alta-baja-cierre (OHLC) utiliza cinco columnas de datos, en orden: categoría, apertura, alta, baja y cierre. El rango de precios en cada categoría nuevamente se indica con una línea vertical, mientras que el rango entre la apertura y el cierre se muestra con una barra flotante más ancha; si el precio aumenta en la categoría (el cierre es mayor que la apertura), la barra se llena de un color, mientras que si el precio disminuye, la barra se llena de otro. Este tipo de gráfico a menudo se llama gráfico de velas.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Mejoras de visibilidad en el gráfico**
A menudo usamos colores en lugar de blanco y negro para indicar precios en aumento y en disminución. En el primer conjunto de velas abajo, el rojo muestra precios en aumento y el verde en disminución.

![todo:image_alt_text](sample2.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de ejemplo](Open-High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().getCategoryData("A2:A9");
// Set the DownBars and UpBars with different color
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Red);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
