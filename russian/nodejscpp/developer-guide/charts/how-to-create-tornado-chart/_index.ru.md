---
title: Как создать торнадо график с Node.js через C++
linktitle: Как создать диаграмму торнадо
type: docs
weight: 73
url: /ru/nodejs-cpp/create-tornado-chart/
description: Узнайте, как создавать торнадо график с API Aspose.Cells for Node.js via C++.
keywords: Node.js создайте смерчевую диаграмму, добавьте смерчевую диаграмму, вставьте смерчевую диаграмму
---

## **Введение**
Гистограмма торнадо, также известная как диаграмма торнадо или торнадо-график, является видом визуализации данных, который часто используется для анализа чувствительности в Excel. Она помогает понять влияние изменения переменных на конкретный результат или результат.

## **Как создать гистограмму торнадо в Excel**
Вы можете создать гистограмму торнадо в Excel, следуя этим шагам:
1. Выберите данные и перейдите во вкладку Вставка --> Диаграммы --> Вставить столбцовую или гистограмму --> Столбчатая гистограмма. Нажмите на неё.
<br>
<img src="1.png" width=70% />
2. Измените ось Y: Щелкните правой кнопкой мыши по оси Y. Нажмите на формат оси. В метках нажмите на выпадающий список позиции метки и выберите Положение Лоу.
<br>
<img src="2.png" width=70% />
3. Выберите любой столбец и перейдите к форматированию. установите соответствующую ширину промежутка.
<br>
<img src="3.png" width=70% />
4. Удалим знак минус(-) с гистограммы торнадо. Выберите ось X. Перейдите к форматированию. В параметрах оси нажмите на номер. В категории выберите пользовательское. В поле формата напишите ###0,###0. Нажмите добавить.
<br>
<img src="4.png" width=70% />
5. нажмите на ось Y и перейдите к параметрам оси. В параметрах оси отметьте Категории в обратном порядке.
<br>
<img src="5.png" width=70% />

## **Как добавить смерчевую диаграмму в Aspose.Cells for Node.js via C++**
Пожалуйста, ознакомьтесь с следующим образцом кода. Он загружает [образец электронной таблицы](sample.xlsx), который содержит некоторые тестовые данные. Затем он создает столбчатую диаграмму на основе исходных данных и настраивает соответствующие свойства. Наконец, он сохраняет книгу в [формате XLSX](out.xlsx). На следующем скриншоте показана гистограмма торнадо, созданная Aspose.Cells в выходном файле Excel.
<br>
<img src="6.png" width=70% />

### **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);
const charts = sheet.getCharts();
// Add bar chart
const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
const chart = charts.get(index);

// Set data for bar chart
chart.setChartDataRange("A1:C7", true);

// Set properties for bar chart
chart.getTitle().setText("Tornado chart");
chart.setStyle(2);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getPlotArea().getBorder().setColor(AsposeCells.Color.White);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

chart.getCategoryAxis().setTickLabelPosition(AsposeCells.TickLabelPositionType.Low);
chart.getCategoryAxis().setIsPlotOrderReversed(true);

chart.setGapWidth(10);

const valueAxis = chart.getValueAxis();
valueAxis.getTickLabels().setNumberFormat("#,##0;#,##0");

workbook.save("out.xlsx");
```
