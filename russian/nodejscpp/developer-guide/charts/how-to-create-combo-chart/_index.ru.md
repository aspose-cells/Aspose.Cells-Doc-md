---
title: Как создать комбинированный график с помощью Node.js через C++
linktitle: Как создать комбинированную диаграмму
description: Научитесь создавать комбинированный график с помощью Aspose.Cells for Node.js via C++. Наш комплексный гид покажет, как объединить разные типы графиков для более эффективной презентации данных.
keywords: Aspose.Cells for Node.js via C++, Комбинированный график, Объединение типов графиков, Представление данных, Эффективная визуализация.
type: docs
weight: 73
url: /ru/nodejs-cpp/create-combo-chart/
---

## **Возможные сценарии использования**
Комбинированные диаграммы в Excel позволяют вам воспользоваться этой опцией, потому что вы легко можете объединить два или более типа диаграмм, чтобы сделать понятными ваши данные. Комбинированные диаграммы полезны, когда в ваших данных содержится несколько видов значений, включая цену и объем. Кроме того, комбинированные диаграммы возможны, когда ваши числовые данные меняются широко от серии к серии.
Возьмем следующий набор данных в качестве примера, и мы можем увидеть, что эти данные довольно похожи на данные, упомянутые в [**VHCL**](https://docs.aspose.com/cells/nodejs-cpp/create-volume-high-low-close-stock-chart/). Если мы хотим визуализировать  series0, который соответствует "Общий доход", в виде линейной диаграммы, как нам следует поступить?

![todo:image_alt_text](sample.png)
## **Комбинированная диаграмма**
После выполнения нижеприведенного кода вы увидите комбинированную диаграмму, показанную ниже.

![todo:image_alt_text](result.png)
## **Образец кода**
В приведенном ниже образце кода загружается [образец файла Excel](combo.xlsx) и создается [выходной файл Excel](out.xlsx).

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
{{< app/cells/assistant language="nodejs-cpp" >}}
