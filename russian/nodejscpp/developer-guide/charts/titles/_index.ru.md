---
title: Управление названиями графиков Excel с помощью Node.js через C++
description: Узнайте, как использовать Aspose.Cells for Node.js via C++ для добавления и форматирования названий графиков и осей в Microsoft Excel. Наш гид покажет, как задавать различные типы названий, корректировать их внешний вид и изменять названия осей для лучшего отображения данных и ясности.
keywords: Aspose.Cells for Node.js via C++, Названия графиков, Названия осей, Microsoft Excel, Представление данных, Внешний вид.
linktitle: Заголовки
type: docs
weight: 50
url: /ru/nodejs-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

В диаграммах Excel существует 2 вида заголовков:
1. Заголовок диаграммы 
1. Заголовки осей

{{% /alert %}}

## **Параметры заголовка**
Aspose.Cells for Node.js via C++ также позволяет управлять названиями диаграмм во время выполнения. С помощью объекта [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) вы можете изменять текст, шрифт и заливку заголовков.

|![todo:image_alt_text](chart_title.png)|

## **Настройка заголовков диаграмм или осей**
Вы можете использовать Microsoft Excel для установки названий диаграмм и их осей в визуальной среде WYSIWYG. Aspose.Cells for Node.js via C++ также позволяет разработчикам задавать названия диаграмм и осей во время выполнения. Все диаграммы и их оси содержат свойство [Title](https://reference.aspose.com/cells/nodejs-cpp/title/), которое можно использовать для установки их названий, как показано в примере ниже.

 Следующий фрагмент кода демонстрирует, как задавать названия диаграмм и осей.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Продвинутые темы**
- [Чтение подзаголовка диаграммы из файла ODS](/cells/ru/nodejs-cpp/read-chart-subtitle-from-ods-file/)
{{< app/cells/assistant language="nodejs-cpp" >}}
