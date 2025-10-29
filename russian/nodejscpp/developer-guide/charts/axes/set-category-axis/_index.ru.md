---
title: Как установить категориальную ось с помощью Node.js через C++
linktitle: Как настроить категориальную ось
description: Узнайте, как установить категориальную ось в Aspose.Cells for Node.js via C++. Наш гид поможет вам понять, как определить диапазон категориальной оси, настроить ее свойства и форматировать метки.
keywords: Aspose.Cells for Node.js via C++, категориальная ось, установка, диапазон, свойства, форматирование.
type: docs
weight: 205
url: /ru/nodejs-cpp/how-to-set-category-axis/
---

## **Возможные сценарии использования**
После создания диаграммы в листе, вы можете установить для нее категориальную ось. В этой статье мы покажем, как установить категориальную ось для диаграммы Excel с помощью Aspose.Cells, с примером кода.

## **Шаги в примерном коде**

1. Создайте новую книгу.

2. Создайте новую диаграмму на первом листе.

3. Добавьте некоторые значения в ячейки на первом листе.

4. Теперь вы можете установить категориальную ось; есть два способа: используя данные из ячейки или используя строки напрямую, оба показаны в примере кода.

5. Установите значение оси и сохраните рабочую книгу, чтобы просмотреть результат.

## **Образец кода**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const dataDir = ""; // Update with your path

// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CHART");

// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 8, 0, 20, 10);
const chart = worksheet.getCharts().get(chartIndex);

// Add some values to cells
worksheet.getCells().get("A1").putValue("Sales");
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(130);
worksheet.getCells().get("A5").putValue(160);
worksheet.getCells().get("A6").putValue(150);
worksheet.getCells().get("B1").putValue("Days");
worksheet.getCells().get("B2").putValue(1);
worksheet.getCells().get("B3").putValue(2);
worksheet.getCells().get("B4").putValue(3);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("B6").putValue(5);

// Some values in string
const Sales = "100,150,130,160,150";
const Days = "1,2,3,4,5";

// Set Category Axis Data with string
chart.getNSeries().setCategoryData(`{${Days}}`);
// Or you can set Category Axis Data with data in cells
// chart.getNSeries().setCategoryData("B2:B6");

// Add Series to the chart
chart.getNSeries().add("Demand1", true);
// Set value axis with string 
chart.getNSeries().get(0).setValues(`{${Sales}}`);
chart.getNSeries().add("Demand2", true);
// Set value axis with data in cells
chart.getNSeries().get(1).setValues("A2:A6");

// Set some Category Axis properties
chart.getCategoryAxis().getTickLabels().setRotationAngle(45);
chart.getCategoryAxis().getTickLabels().getFont().setSize(8);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

// Save the workbook to view the result file
workbook.save(path + "Output.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
