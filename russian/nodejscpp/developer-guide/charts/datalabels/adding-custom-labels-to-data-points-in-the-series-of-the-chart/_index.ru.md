---  
title: Добавление пользовательских меток к точкам данных в серии диаграммы с помощью Node.js через C++  
linktitle: Добавление пользовательских меток к данным точек в серии диаграммы  
description: Узнайте, как добавлять пользовательские метки к точкам данных в серии диаграммы с помощью Aspose.Cells for Node.js via C++. Это руководство продемонстрирует, как изменять внешний вид, расположение и форматирование меток, при этом связывая их с вашим источником данных для точного отображения.  
keywords: Aspose.Cells для Node.js, построение диаграмм, пользовательские метки, точки данных, серия, внешний вид, позиция, форматирование, источник данных, отображение.  
type: docs  
weight: 100  
url: /ru/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

Вы можете добавлять пользовательские метки к точкам данных в серии диаграммы. Aspose.Cells предоставляет свойство [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--) для добавления этих пользовательских меток. В этой статье будет объяснено, как использовать это свойство для добавления пользовательских меток к точкам данных в серии диаграммы.

{{% /alert %}}  

Следующий код создает **Точечную диаграмму, соединенную линиями с маркерами данных** и добавляет **Пользовательские метки** к **точкам данных** в **серии** диаграммы. Каждая пользовательская метка показывает **название серии** и **название точки**. Вместо них можно использовать любой другой текст.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Put data
sheet.getCells().get(0, 0).putValue(1);
sheet.getCells().get(0, 1).putValue(2);
sheet.getCells().get(0, 2).putValue(3);

sheet.getCells().get(1, 0).putValue(4);
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(1, 2).putValue(6);

sheet.getCells().get(2, 0).putValue(7);
sheet.getCells().get(2, 1).putValue(8);
sheet.getCells().get(2, 2).putValue(9);

// Generate the chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
const chart = sheet.getCharts().get(chartIndex);

chart.getTitle().setText("Test");
chart.getCategoryAxis().getTitle().setText("X-Axis");
chart.getValueAxis().getTitle().setText("Y-Axis");

chart.getNSeries().setCategoryData("A1:C1");

// Insert series
chart.getNSeries().add("A2:C2", false);

let series = chart.getNSeries().get(0);

let pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 1" + "\n" + "Point " + i);
}

// Insert series
chart.getNSeries().add("A3:C3", false);

series = chart.getNSeries().get(1);

pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 2" + "\n" + "Point " + i);
}

workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

