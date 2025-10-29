---
title: Ось даты с помощью Node.js через C++
description: Узнайте, как управлять осью даты в Aspose.Cells for Node.js via C++. Наше руководство поможет вам понять, как работать с различными форматами даты, шкалами времени и частотами меток.
keywords: Aspose.Cells для Node.js, ось даты, управление, форматы даты, шкалы времени, частоты меток.
type: docs
weight: 200
url: /ru/nodejs-cpp/date-axis/
---

## **Возможные сценарии использования**
 Когда вы создаёте график на основе данных листа с использованием дат, и даты отображаются по горизонтальной (категорийной) оси в графике, Aspose.Cells for Node.js via C++ автоматически изменяет категориальную ось на ось даты (шкала времени).
Ось дат отображает даты в хронологическом порядке с определенными интервалами или базовыми единицами, такими как количество дней, месяцев или лет, даже если даты на листе не расположены последовательно или в тех же базовых единицах.
 По умолчанию Aspose.Cells определяет базовые единицы для оси даты на основе минимальной разницы между любыми двумя датами в данных листа. Например, если у вас есть данные о ценах акций, где минимальная разница между датами — семь дней, Excel устанавливает базовую единицу в дни, но вы можете изменить её на месяцы или годы, если хотите увидеть динамику акций за более длительный период.

## **Обработка оси дат, подобно Microsoft Excel**
Пожалуйста, посмотрите следующий пример кода, который создает новый Excel файл и помещает значения диаграммы в первый рабочий лист. 
Затем мы добавляем диаграмму и устанавливаем тип [**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/) 
на [**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--), а затем устанавливаем базовые единицы в Дни.

![todo:image_alt_text](excel.png)

## **Образец кода**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add the sample values to cells
worksheet.getCells().get("A1").putValue("Date");
// 14 means datetime format
const style = worksheet.getCells().getStyle();
style.setNumber(14);
// Put values to cells for creating chart
worksheet.getCells().get("A2").setStyle(style);
worksheet.getCells().get("A2").putValue(new Date(Date.UTC(2022, 5, 26)));
worksheet.getCells().get("A3").setStyle(style);
worksheet.getCells().get("A3").putValue(new Date(Date.UTC(2022, 4, 22)));
worksheet.getCells().get("A4").setStyle(style);
worksheet.getCells().get("A4").putValue(new Date(Date.UTC(2022, 7, 3)));
worksheet.getCells().get("B1").putValue("Price");
worksheet.getCells().get("B2").putValue(40);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(60);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 9, 6, 21, 13);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);         
// Set the Axis type to Date time
chart.getCategoryAxis().setCategoryType(AsposeCells.CategoryType.TimeScale);
// Set the base unit for CategoryAxis to days
chart.getCategoryAxis().setBaseUnitScale(AsposeCells.TimeUnit.Days);
// Set the direction for the axis text to be vertical
chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Vertical);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set max value of Y axis.
chart.getValueAxis().setMaxValue(70);
// Set major unit.
chart.getValueAxis().setMajorUnit(10);
// Save the file
workbook.save("DateAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
