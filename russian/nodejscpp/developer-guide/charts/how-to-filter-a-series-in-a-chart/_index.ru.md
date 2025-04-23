---
title: Три метода фильтрации данных графика с помощью Node.js через C++
linktitle: Три метода фильтрации данных диаграммы
description: Узнайте, как фильтровать диаграммы в Excel, используя Aspose.Cells for Node.js via C++. Наш подробный гид покажет, как применять фильтры к диаграммам, настраивать элементы диаграммы и использовать инструменты анализа данных для получения лучших инсайтов и обоснованных решений.
keywords: Aspose.Cells for Node.js via C++, фильтрация диаграмм в Excel, анализ данных, принятие решений, визуализация.
type: docs
weight: 2210
url: /ru/nodejs-cpp/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Отфильтровать серии для отображения диаграммы**

### **Шаги по фильтрации серии с диаграммы в Excel**
В Excel мы можем фильтровать определённые серии на диаграмме, из-за чего эти фильтрованные серии не отображаются в диаграмме. Исходная диаграмма показана на **Рисунке 1**. Однако, когда мы фильтруем **Testseries2** и **Testseries4**, диаграмма будет выглядеть как на **Рисунке 2**.

В Aspose.Cells for Node.js via C++ мы можем выполнить аналогичную операцию. Для файла [пример](seriesFiltered.xlsx) такого типа, если мы хотим фильтровать **Testseries2** и **Testseries4**, мы можем выполнить следующий код. Кроме того, мы будем поддерживать два списка: один ([Chart.getNSeries()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getNSeries--)) для хранения всех выбранных серий.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Образец кода**
Приведенный ниже образец кода загружает [образец файла Excel](seriesFiltered.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "seriesFiltered.xlsx");
// Create an instance of existing Workbook
let workbook = new AsposeCells.Workbook(filePath);
// Get filtered series list
let nSeriesFiltered = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getFilteredNSeries();
// Get selected series list
let nSeries = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getNSeries();
// Should be 0
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 6
console.log("Visible Series count: " + nSeries.getCount());
// Process from the end to the beginning
nSeries.get(1).setIsFiltered(true);
nSeries.get(0).setIsFiltered(true);
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
workbook.save("seriesFiltered-out.xlsx");
workbook = new AsposeCells.Workbook("seriesFiltered-out.xlsx");
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
```

## **2. Отфильтруйте данные и дайте диаграмме измениться**

Фильтрация данных — отличный способ управлять фильтрами диаграмм с большим количеством данных. При фильтрации данные диаграммы изменяются. Одна из проблем — убедиться, что диаграмма остаётся на экране. Когда вы фильтруете, скрываются строки, и иногда диаграмма оказывается в скрытых строках.

![todo:image_alt_text](Figure3.png)

### **Шаги для использования фильтров данных для изменения диаграммы в Excel**

1. Щелкните внутри вашего диапазона данных.
2. Щелкните вкладку **Данные** и включите фильтры, щелкнув по кнопке Фильтры. Ваша строка заголовка будет иметь выпадающие стрелки.
3. Создайте диаграмму, перейдя на вкладку **Вставка** и выбрав столбчатую диаграмму.
4. Теперь отфильтруйте свои данные, используя выпадающие стрелки в данных. Не используйте фильтры диаграммы.

### **Образец кода**
Следующий пример кода показывает ту же функцию с использованием Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of Worksheet
const sheet = workbook.getWorksheets().get("Sheet1");
// Add data into details cells.
sheet.getCells().get(0, 0).putValue("Fruits Name");
sheet.getCells().get(0, 1).putValue("Fruits Price");
sheet.getCells().get(1, 0).putValue("Apples");
sheet.getCells().get(2, 0).putValue("Bananas");
sheet.getCells().get(3, 0).putValue("Grapes");
sheet.getCells().get(4, 0).putValue("Oranges");
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(2, 1).putValue(2);
sheet.getCells().get(3, 1).putValue(1);
sheet.getCells().get(4, 1).putValue(4);

// Add a chart to the worksheet
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
// Access the instance of the newly added chart
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B5", true);
// Set AutoFilter range
sheet.getAutoFilter().setRange("A1:B5");
// Add filters for a filter column.
sheet.getAutoFilter().addFilter(0, "Bananas");
sheet.getAutoFilter().addFilter(0, "Oranges");
// Apply the filters
sheet.getAutoFilter().refresh();
chart.toImage("Autofilter.png");
workbook.save("Autofilter.xlsx");
```

## **3. Отфильтруйте данные с помощью таблицы и дайте измениться диаграмме**

Использование таблицы похоже на Метод 2, используя диапазон, но у вас есть преимущества таблиц перед диапазонами. Когда вы изменяете свой диапазон на таблицу и добавляете данные, диаграмма автоматически обновляется. С диапазоном вам придется изменять источник данных.

### **Форматирование как таблица в Excel**

Щелкните внутри ваших данных и используйте **CTRL+T** или используйте вкладку **Главная**, **Форматировать как таблицу**

![todo:image_alt_text](Figure4.png)

### **Образец кода**
Следующий пример кода загружает [пример Excel](TableFilters.xlsx), показывая ту же функцию с помощью Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TableFilters.xlsx");
// Create a workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Access the instance of the newly added chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B7", true);
// Convert the chart to image
chart.toImage("TableFilters.before.png");
// Add a new List Object to the worksheet
const listObject = sheet.getListObjects().get(sheet.getListObjects().add("A1", "B7", true));
// Add default style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);
// Show Total
listObject.setShowTotals(false);
// Add filters for a filter column.
listObject.getAutoFilter().addFilter(0, "James");
// Apply the filters
listObject.getAutoFilter().refresh();
// After adding new value the chart will change
listObject.putCellValue(7, 0, "Me");
listObject.putCellValue(7, 1, 1000);
// Check the changed images
chart.toImage("TableFilters.after.png");
// Saving the Excel file
workbook.save("TableFilter.out.xlsx");
```
