---  
title: Преобразование диаграммы в изображение с помощью Node.js через C++  
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для преобразования диаграммы в изображение, например JPEG или PNG. Наш гид покажет, как экспортировать диаграмму из Microsoft Excel и сохранить её как отдельное изображение для дальнейшего использования и редактирования.  
keywords: Aspose.Cells for Node.js via C++, Диаграмма в изображение, Microsoft Excel, Конвертация изображений, Экспорт, Отдельное изображение.  
linktitle: Диаграмма в изображение  
type: docs  
weight: 46  
url: /ru/nodejs-cpp/chart-to-image/  
---  

## **Диаграммы отображения**

API Aspose.Cells поддерживают преобразование диаграмм Excel в форматы изображений без необходимости использования дополнительных инструментов или приложений. Чтобы обеспечить поддержку отображения, класс [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart) предоставляет методы [**toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) с разными перегрузками, чтобы лучше соответствовать требованиям приложения.

### **Отображение диаграмм в изображения**

Метод [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-) имеет различные перегрузки для поддержки простого и расширенного рендеринга. Если задача — отобразить диаграмму в её стандартных размерах, рекомендуем использовать метод [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-), как показано ниже.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Converting chart to image
chart.toImage(path.join(dataDir, "chartEMF_out.emf"), AsposeCells.ImageType.Emf);

// Converting chart to Bitmap
chart.toImage(path.join(dataDir, "chartBMP_out.bmp"), AsposeCells.ImageType.Bmp);
```

Также возможно рендерить диаграммы в изображения с расширенными настройками. API Aspose.Cells включает перегруженную версию метода [**Chart.toImage(string)**](https://reference.aspose.com/cells/nodejs-cpp/chart/#toImage-string-), которая принимает экземпляр [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions), а также позволяет задавать параметры, такие как разрешение, режим сглаживания, формат изображения и так далее.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Adding a new worksheet to the Workbook
const sheetIndex = workbook.getWorksheets().add();
// Obtaining the reference of the newly added worksheet by passing its index to WorksheetCollection
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);
// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Create an instance of ImageOrPrintOptions and set a few properties
const options = new AsposeCells.ImageOrPrintOptions();
options.setVerticalResolution(300);
options.setHorizontalResolution(300);

// Convert chart to image with additional settings
chart.toImage(path.join(dataDir, "chartPNG_out.png"), options);
```

## **Поддерживаемые типы диаграмм для отображения**

Существует несколько видов диаграмм, которые в настоящее время не поддерживаются для рендеринга. Такие виды диаграмм содержат **N** в столбце **Поддерживаемые** в таблице ниже.

|Тип диаграммы|Подтип диаграммы|Поддерживается|  
| :- | :- | :- |  
|**Column**|Column|**Y**|  
| |ColumnStacked|**Y**|  
| |Column100PercentStacked|**Y**|  
| |Column3DClustered|**Y**|  
| |Column3DStacked|**Y**|  
| |Column3D100PercentStacked|**Y**|  
| |Column3D|**Y**|  
|**Bar**|Bar|**Y**|  
| |BarStacked|**Y**|  
| |Bar100PercentStacked|**Y**|  
| |Bar3DClustered|**Y**|  
| |Bar3DStacked|**Y**|  
| |Bar3D100PercentStacked|**Y**|  
|**Line**|Line|**Y**|  
| |LineStacked|**Y**|  
| |Line100PercentStacked|**Y**|  
| |LineWithDataMarkers|**Y**|  
| |LineStackedWithDataMarkers|**Y**|  
| |Line100PercentStackedWithDataMarkers|**Y**|  
| |Line3D|**Y**|  
|**Pie**|Pie|**Y**|  
| |Pie3D|**Y**|  
| |PiePie|**Y**|  
| |PieExploded|**Y**|  
| |Pie3DExploded|**Y**|  
| |PieBar|**Y**|  
|**Scatter**|Scatter|**Y**|  
| |ScatterConnectedByCurvesWithDataMarker|**Y**|  
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|  
| |ScatterConnectedByLinesWithDataMarker|**Y**|  
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|  
|**Area**|Area|**Y**|  
| |AreaStacked|**Y**|  
| |Area100PercentStacked|**Y**|  
| |Area3D|**Y**|  
| |Area3DStacked|**Y**|  
| |Area3D100PercentStacked|**Y**|  
|**Doughnut**|Doughnut|**Y**|  
| |DoughnutExploded|**Y**|  
|**Radar**|Radar|**Y**|  
| |RadarWithDataMarkers|**Y**|  
| |RadarFilled|**Y**|  
|**Surface**|Surface3D|N|  
| |SurfaceWireframe3D|N|  
| |SurfaceContour|N|  
| |SurfaceContourWireframe|N|  
|**Bubble**|Bubble|**Y**|  
| |Bubble3D|N|  
|**Stock**|StockHighLowClose|**Y**|  
| |StockOpenHighLowClose|**Y**|  
| |StockVolumeHighLowClose|**Y**|  
| |StockVolumeOpenHighLowClose|**Y**|  
|**Cylinder**|Cylinder|**Y**|  
| |CylinderStacked|**Y**|  
| |Cylinder100PercentStacked|**Y**|  
| |CylindricalBar|**Y**|  
| |CylindricalBarStacked|**Y**|  
| |CylindricalBar100PercentStacked|**Y**|  
| |CylindricalColumn3D|**Y**|  
|**Cone**|Cone|**Y**|  
| |ConeStacked|**Y**|  
| |Cone100PercentStacked|**Y**|  
| |ConicalBar|**Y**|  
| |ConicalBarStacked|**Y**|  
| |ConicalBar100PercentStacked|**Y**|  
| |ConicalColumn3D|**Y**|  
|**Pyramid**|Pyramid|**Y**|  
| |PyramidStacked|**Y**|  
| |Pyramid100PercentStacked|**Y**|  
| |PyramidBar|**Y**|  
| |PyramidBarStacked|**Y**|  
| |PyramidBar100PercentStacked|**Y**|  
| |PyramidColumn3D|**Y**|  
|**BoxWhisker**|BoxWhisker|Y|  
|**Funnel**|Funnel|**Y**|  
|**ParetoLine**|ParetoLine|**Y**|  
|**Sunburst**|Sunburst|**Y**|  
|**Treemap**|Treemap|**Y**|  
|**Waterfall**|Waterfall|**Y**|  
|**Histogram**|Histogram|Y|  
|**Map**|Map|**N**|  

{{% alert color="primary" %}}  
В случае попытки отобразить не поддерживаемые типы диаграмм в изображения или PDF, можно получить изображения нулевого размера или пустой PDF.  
{{% /alert %}}  

## **Продвинутые темы**  
- [Преобразовать диаграмму в PDF](/cells/ru/nodejs-cpp/chart-to-pdf/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
