---  
title: Настройка графиков с Node.js через C++  
linktitle: Настройка диаграмм  
description: Узнайте, как настраивать графики в Aspose.Cells for Node.js via C++. Наше руководство покажет, как изменять макеты графиков, добавлять и форматировать серии данных, настраивать оси и применять различные параметры форматирования для улучшения внешнего вида и удобства использования ваших графиков.  
keywords: Aspose.Cells for Node.js via C++, построение графиков, настройка, макеты, серии данных, оси, форматирование, внешний вид, удобство использования.  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/customizing-charts/  
---  

{{% alert color="primary" %}}  

## **Создание настраиваемых диаграмм**  

До настоящего времени, когда мы говорили о графиках, мы рассматривали стандартные графики с их стандартными настройками форматирования. Мы просто задаём источник данных, устанавливаем несколько свойств, и график создаётся с настройками по умолчанию. Но API Aspose.Cells поддерживает также создание пользовательских графиков, позволяющих разработчикам создавать графики с собственными настройками форматирования.  

Разработчики могут создавать пользовательские графики во время выполнения с использованием Aspose.Cells.  

График состоит из серии данных. Каждая серия данных в Aspose.Cells представлена объектом [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series), тогда как объект [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) служит коллекцией [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series) объектов. При создании пользовательского графика разработчики имеют возможность использовать разные типы графиков для разных серий данных (собранных в объекте [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection)).  

Приведенный ниже пример кода демонстрирует, как создать пользовательские графики. В этом примере мы собираемся использовать столбчатую диаграмму для первой серии данных и линейную диаграмму для второй серии. Результатом будет добавление столбчатой диаграммы, объединенной с линейной диаграммой, на лист.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(110);
worksheet.getCells().get("B1").putValue(260);
worksheet.getCells().get("B2").putValue(12);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(100);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the chart type of 2nd NSeries to display as line chart
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  

В настоящее время Aspose.Cells поддерживает только пользовательские графики, сочетающие диаграммы типа pie, line, column и column stack, однако в будущих версиях будет поддержано больше типов графиков.  

{{% /alert %}}  

