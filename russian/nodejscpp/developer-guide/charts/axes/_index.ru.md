---  
title: Управление осями графиков Excel с помощью Node.js через C++  
description: Узнайте, как настраивать оси графиков в Aspose.Cells for Node.js via C++. Наше руководство покажет вам, как изменить первичные и вторичные оси, установить их диапазоны и изменить их свойства для улучшения визуализации.  
keywords: Aspose.Cells for Node.js via C++, оси графиков, настройка, первичные оси, вторичные оси, диапазон, свойства.  
linktitle: Оси  
type: docs  
weight: 50  
url: /ru/nodejs-cpp/chart-axes/  
---  

{{% alert color="primary" %}}  

В диаграммах Excel существует 3 вида осей:  
1. Горизонтальная (Категориальная) ось: OX  
1. Вертикальная(значения) ось: ось Y  
1. Глубина(серии) ось: ось Z  

{{% /alert %}}  

## **Опции оси**  
Aspose.Cells for Node.js via C++ также позволяет управлять осями графика во время выполнения. С помощью объекта [Axis](https://reference.aspose.com/cells/nodejs-cpp/axis/) вы можете изменить все параметры оси так же, как в Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **Управление осью X и Y**  
В графике Excel горизонтальные и вертикальные оси — это две наиболее популярные оси.  

Следующий фрагмент кода демонстрирует, как установить параметры осей X и Y.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart_axes.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue("Series1");
worksheet.getCells().get("A2").putValue(50);
worksheet.getCells().get("A3").putValue(100);
worksheet.getCells().get("A4").putValue(150);
worksheet.getCells().get("B1").putValue("Series2");
worksheet.getCells().get("B2").putValue(60);
worksheet.getCells().get("B3").putValue(32);
worksheet.getCells().get("B4").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);

// Hiding X axis
chart.getCategoryAxis().setIsVisible(false);

// Setting max value of Y axis
chart.getValueAxis().setMaxValue(200);
// Setting major unit
chart.getValueAxis().setMajorUnit(50);

// Save the file
workbook.save(filePath);
```  

## **Продвинутые темы**  
- [Изменение направления меток делений](/cells/ru/nodejs-cpp/change-tick-label-direction/)  
- [Определение существующих осей на графике](/cells/ru/nodejs-cpp/determine-which-axis-exists-in-the-chart/)  
- [Обработка автоматических единиц оси диаграммы, как в Microsoft Excel](/cells/ru/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Чтение меток оси после вычисления диаграммы](/cells/ru/nodejs-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Как установить ось категорий в графике Excel](/cells/ru/nodejs-cpp/how-to-set-category-axis/)  

