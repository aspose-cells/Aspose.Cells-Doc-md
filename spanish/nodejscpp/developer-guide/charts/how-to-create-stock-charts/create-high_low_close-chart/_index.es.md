---  
title: Crear gráfico de acciones de Máximo Mínimo Cierre (HLC) con Node.js vía C++  
linktitle: Crear Gráfico de Cotizaciones Altas Bajas Cierre (HLC)  
description: Aprende cómo crear un gráfico de acciones de máximo mínimo cierre usando Aspose.Cells for Node.js via C++. Nuestra guía paso a paso demostrará cómo representar datos del mercado bursátil, incluyendo los precios máximos, mínimos y de cierre, en un gráfico para mejor análisis y visualización.  
keywords: Aspose.Cells para Node.js, gráfico de acciones HLC, datos del mercado bursátil, análisis, visualización.  
type: docs  
weight: 181  
url: /es/nodejs-cpp/create-high-low-close-stock-chart/  
---  

## **Escenarios de uso posibles**  
El gráfico de acciones Máximo-Mínimo-Cierre (HLC) usa cuatro columnas de datos. La primera columna es una categoría, generalmente una fecha, aunque también pueden usarse nombres de acciones. Las siguientes tres columnas en orden son para precios máximos, mínimos y de cierre. El rango de precios para cada categoría se indica con una línea vertical de mínimo a máximo, y el precio de cierre se muestra con una marca en forma de tick extendiéndose a la derecha de esta línea.  

![todo:image_alt_text](sample.png)  
## **Mejoras de visibilidad en el gráfico**  
A veces, para que el gráfico luzca más intuitivo, podemos modificar la apariencia del marcador (cierre), o hacer que se muestre en el eje secundario.  

![todo:image_alt_text](sample2.png)  
## **Código de muestra**  
El siguiente código de ejemplo carga el [archivo de Excel de muestra](High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:D9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set the marker with the built-in data 
chart.getNSeries().get(2).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(2).getMarker().setMarkerSize(20);
chart.getNSeries().get(2).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(2).getMarker().getArea().setForegroundColor(AsposeCells.Color.Maroon);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

