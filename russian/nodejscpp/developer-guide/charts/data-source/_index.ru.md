---  
title: Установите источник данных для графика с помощью Node.js через C++  
description: Узнайте о различных источниках данных, поддерживаемых Aspose.Cells for Node.js via C++. Наш гид проведет вас по различным типам доступных источников данных и покажет, как подключаться и получать данные для заполнения ваших листов.  
keywords: Aspose.Cells for Node.js via C++, построение графиков, форматирование данных, метки, цвета, шрифты, внешний вид, удобство использования.  
linktitle: Источник данных  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/data-formatting-in-charts/  
---  

В наших предыдущих темах мы уже предоставили много примеров, демонстрирующих, как можно установить источник данных для вашего графика, но в этой теме мы расскажем подробнее о типах данных, которые можно установить для графика.

## **Установка данных графика**

При работе с графиками с использованием Aspose.Cells есть два типа данных, с которыми нужно работать, следующие:

- Данные графика.
- Данные категорий.

### **Данные графика**

Данные для графика — это данные, которые мы используем в качестве источника данных для построения графиков. Мы можем добавить диапазон ячеек (с содержащими данными для графика), вызвав метод [**add(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#add-string-boolean-) объекта [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(300);
worksheet.getCells().get("B1").putValue(160);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Данные категорий**

Категорийные данные используются для подписи данных графика и могут быть добавлены к [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection) с помощью его свойства [**getCategoryData()**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/#getCategoryData--). Ниже приведен полный пример, демонстрирующий использование данных графика и категорий. После выполнения приведенного выше кода будет добавлен столбчатый график на лист.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(10);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(170);
worksheet.getCells().get("A4").putValue(200);
worksheet.getCells().get("B1").putValue(120);
worksheet.getCells().get("B2").putValue(320);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(40);

// Adding sample values to cells as category data
worksheet.getCells().get("C1").putValue("Q1");
worksheet.getCells().get("C2").putValue("Q2");
worksheet.getCells().get("C3").putValue("Y1");
worksheet.getCells().get("C4").putValue("Y2");

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.getNSeries().add("A1:B4", true);

// Setting the data source for the category data of SeriesCollection
chart.getNSeries().setCategoryData("C1:C4");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Продвинутые темы**  
- [Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона](/cells/ru/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)  
- [Создание динамических диаграмм](/cells/ru/nodejs-cpp/create-dynamic-charts/)  
- [Простой способ настройки диаграммы с использованием метода Chart.SetChartDataRange](/cells/ru/nodejs-cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)  
- [Найдите тип значений X и Y точек в серии графика](/cells/ru/nodejs-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)  
{{< app/cells/assistant language="nodejs-cpp" >}}
